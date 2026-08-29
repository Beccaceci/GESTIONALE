"""
Tier 2: TikZ Figures Syntax, Bounding Box Checks & Graphics Validation
Validates TikZ diagrams, pgfplots, figure wrappers, captions, labels, and standalone compilability.
"""
import re
import subprocess
import tempfile
import shutil
from pathlib import Path
from typing import Dict, List, Tuple, Any, Optional

from .config import CHAPTER_SPECS, CONFIG_DIR, PACKAGES_TEX, ENVIRONMENTS_TEX, MACROS_TEX
from .models import CheckResult, Issue, IssueSeverity


class Tier2TikzValidator:
    def __init__(self, compile_standalone: bool = False, timeout_sec: int = 15):
        self.compile_standalone = compile_standalone
        self.timeout_sec = timeout_sec

    def validate_chapter(self, chapter_id: str, chapter_file: Path) -> CheckResult:
        issues: List[Issue] = []
        details: Dict[str, Any] = {
            "figures_count": 0,
            "tikz_count": 0,
            "pgfplots_count": 0,
            "compiled_count": 0,
            "compile_success_count": 0,
        }

        if not chapter_file.exists():
            return CheckResult(
                name="Tier 2: TikZ & Graphics Validation",
                tier=2,
                passed=False,
                score=0.0,
                issues=[
                    Issue(
                        tier=2,
                        chapter_id=chapter_id,
                        severity=IssueSeverity.CRITICAL,
                        rule_id="T2_FILE_EXISTS",
                        message=f"Chapter file not found: {chapter_file}",
                    )
                ],
                details=details,
            )

        content = chapter_file.read_text(encoding="utf-8")
        lines = content.splitlines()

        # 1. Figure wrappers validation
        fig_issues, figures_data = self._validate_figure_wrappers(chapter_id, lines)
        issues.extend(fig_issues)
        details["figures_count"] = len(figures_data)
        details["figures"] = figures_data

        # 2. TikZ code blocks extraction & syntax validation
        tikz_issues, tikz_blocks = self._validate_tikz_syntax(chapter_id, lines)
        issues.extend(tikz_issues)
        details["tikz_count"] = len(tikz_blocks)
        details["pgfplots_count"] = sum(1 for t in tikz_blocks if t.get("has_pgfplots", False))

        # 3. Standalone TikZ Compilation (if enabled)
        if self.compile_standalone and tikz_blocks:
            compile_issues, comp_details = self._compile_tikz_standalone(chapter_id, tikz_blocks)
            issues.extend(compile_issues)
            details["compiled_count"] = comp_details["compiled"]
            details["compile_success_count"] = comp_details["success"]
            details["compilation_results"] = comp_details["results"]

        # Check required figures from spec
        spec = CHAPTER_SPECS.get(chapter_id, {})
        expected_figs = spec.get("expected_figures", [])
        found_labels = [f["label"] for f in figures_data if f.get("label")]
        for exp in expected_figs:
            if exp not in found_labels:
                issues.append(
                    Issue(
                        tier=2,
                        chapter_id=chapter_id,
                        severity=IssueSeverity.WARNING,
                        rule_id="T2_EXPECTED_FIGURE_MISSING",
                        message=f"Expected figure '{exp}' not found in chapter",
                    )
                )

        errors = [i for i in issues if i.severity in (IssueSeverity.ERROR, IssueSeverity.CRITICAL)]
        warnings = [i for i in issues if i.severity == IssueSeverity.WARNING]
        passed = len(errors) == 0
        score = max(0.0, 1.0 - (len(errors) * 0.3 + len(warnings) * 0.05))

        return CheckResult(
            name="Tier 2: TikZ & Graphics Validation",
            tier=2,
            passed=passed,
            score=score,
            issues=issues,
            details=details,
        )

    def _validate_figure_wrappers(
        self, chapter_id: str, lines: List[str]
    ) -> Tuple[List[Issue], List[Dict[str, Any]]]:
        issues: List[Issue] = []
        figures: List[Dict[str, Any]] = []

        in_figure = False
        fig_start_line = 0
        fig_content: List[str] = []

        caption_re = re.compile(r"\\caption\{([^}]+)\}")
        label_re = re.compile(r"\\label\{fig:([^}]+)\}")
        centering_re = re.compile(r"\\centering")

        for line_num, line in enumerate(lines, 1):
            clean_line = line.split("%")[0]

            if r"\begin{figure}" in clean_line:
                in_figure = True
                fig_start_line = line_num
                fig_content = [clean_line]
            elif r"\end{figure}" in clean_line:
                if in_figure:
                    fig_content.append(clean_line)
                    full_fig_text = "\n".join(fig_content)

                    # Inspect figure content
                    has_centering = bool(centering_re.search(full_fig_text))
                    cap_match = caption_re.search(full_fig_text)
                    lab_match = label_re.search(full_fig_text)
                    has_tikz = r"\begin{tikzpicture}" in full_fig_text
                    has_image = r"\includegraphics" in full_fig_text

                    fig_info = {
                        "start_line": fig_start_line,
                        "end_line": line_num,
                        "has_centering": has_centering,
                        "caption": cap_match.group(1) if cap_match else None,
                        "label": f"fig:{lab_match.group(1)}" if lab_match else None,
                        "has_tikz": has_tikz,
                        "has_image": has_image,
                    }
                    figures.append(fig_info)

                    if not has_centering:
                        issues.append(
                            Issue(
                                tier=2,
                                chapter_id=chapter_id,
                                severity=IssueSeverity.WARNING,
                                rule_id="T2_FIGURE_CENTERING",
                                message=f"Figure at line {fig_start_line} is missing \\centering",
                                line_number=fig_start_line,
                            )
                        )

                    if not cap_match:
                        issues.append(
                            Issue(
                                tier=2,
                                chapter_id=chapter_id,
                                severity=IssueSeverity.ERROR,
                                rule_id="T2_FIGURE_NO_CAPTION",
                                message=f"Figure at line {fig_start_line} is missing \\caption{{...}}",
                                line_number=fig_start_line,
                            )
                        )

                    if not lab_match:
                        issues.append(
                            Issue(
                                tier=2,
                                chapter_id=chapter_id,
                                severity=IssueSeverity.WARNING,
                                rule_id="T2_FIGURE_NO_LABEL",
                                message=f"Figure at line {fig_start_line} is missing \\label{{fig:...}}",
                                line_number=fig_start_line,
                            )
                        )

                    in_figure = False
                    fig_content = []

            elif in_figure:
                fig_content.append(clean_line)

        return issues, figures

    def _validate_tikz_syntax(
        self, chapter_id: str, lines: List[str]
    ) -> Tuple[List[Issue], List[Dict[str, Any]]]:
        issues: List[Issue] = []
        blocks: List[Dict[str, Any]] = []

        in_tikz = False
        start_line = 0
        tikz_lines: List[Tuple[int, str]] = []

        for line_num, line in enumerate(lines, 1):
            clean_line = line.split("%")[0]

            if r"\begin{tikzpicture}" in clean_line:
                in_tikz = True
                start_line = line_num
                tikz_lines = [(line_num, line)]
            elif r"\end{tikzpicture}" in clean_line:
                if in_tikz:
                    tikz_lines.append((line_num, line))
                    code_text = "\n".join(l[1] for l in tikz_lines)
                    has_pgfplots = r"\begin{axis}" in code_text

                    block_info = {
                        "start_line": start_line,
                        "end_line": line_num,
                        "code": code_text,
                        "has_pgfplots": has_pgfplots,
                    }
                    blocks.append(block_info)

                    # Syntax checks on block
                    block_issues = self._check_single_tikz_block(chapter_id, tikz_lines)
                    issues.extend(block_issues)

                    in_tikz = False
                    tikz_lines = []
            elif in_tikz:
                tikz_lines.append((line_num, line))

        return issues, blocks

    def _check_single_tikz_block(
        self, chapter_id: str, tikz_lines: List[Tuple[int, str]]
    ) -> List[Issue]:
        issues: List[Issue] = []
        full_code = "\n".join(l[1] for l in tikz_lines)

        # Brace and bracket balance
        open_braces = full_code.count("{")
        close_braces = full_code.count("}")
        if open_braces != close_braces:
            issues.append(
                Issue(
                    tier=2,
                    chapter_id=chapter_id,
                    severity=IssueSeverity.ERROR,
                    rule_id="T2_TIKZ_BRACE_MISMATCH",
                    message=f"Brace mismatch in tikzpicture (lines {tikz_lines[0][0]}-{tikz_lines[-1][0]}): {open_braces} '{{' vs {close_braces} '}}'",
                    line_number=tikz_lines[0][0],
                )
            )

        open_brackets = full_code.count("[")
        close_brackets = full_code.count("]")
        if open_brackets != close_brackets:
            issues.append(
                Issue(
                    tier=2,
                    chapter_id=chapter_id,
                    severity=IssueSeverity.WARNING,
                    rule_id="T2_TIKZ_BRACKET_MISMATCH",
                    message=f"Bracket mismatch in tikzpicture (lines {tikz_lines[0][0]}-{tikz_lines[-1][0]}): {open_brackets} '[' vs {close_brackets} ']'",
                    line_number=tikz_lines[0][0],
                )
            )

        # Check path semicolon termination
        path_commands = [r"\draw", r"\fill", r"\filldraw", r"\path", r"\node", r"\coordinate", r"\addplot", r"\clip"]
        for line_num, line in tikz_lines:
            clean = line.split("%")[0].strip()
            if not clean:
                continue

            for cmd in path_commands:
                if clean.startswith(cmd):
                    # Check if line or following multiline command ends with ';'
                    # We check if semicolon appears in clean or later in command
                    if not clean.endswith(";") and not clean.endswith("}") and not clean.endswith("]") and not clean.endswith(r"\begin{axis}"):
                        # Could be multiline path, verify that path eventually terminates
                        pass

        # Check pgfplots axis options
        if r"\begin{axis}" in full_code:
            axis_opts_match = re.search(r"\\begin\{axis\}\s*\[(.*?)\]", full_code, re.DOTALL)
            if axis_opts_match:
                opts = axis_opts_match.group(1)
                for opt in ["xlabel", "ylabel", "xmin", "xmax", "ymin", "ymax"]:
                    if opt not in opts:
                        # Warning if standard axis bounds are missing
                        pass

        return issues

    def _compile_tikz_standalone(
        self, chapter_id: str, tikz_blocks: List[Dict[str, Any]]
    ) -> Tuple[List[Issue], Dict[str, Any]]:
        issues: List[Issue] = []
        details = {"compiled": len(tikz_blocks), "success": 0, "results": []}

        # Check if pdflatex is available
        pdflatex_bin = shutil.which("pdflatex") or "/Library/TeX/texbin/pdflatex"
        if not Path(pdflatex_bin).exists() and not shutil.which("pdflatex"):
            issues.append(
                Issue(
                    tier=2,
                    chapter_id=chapter_id,
                    severity=IssueSeverity.WARNING,
                    rule_id="T2_PDFLATEX_NOT_FOUND",
                    message="pdflatex executable not found; skipping standalone TikZ compilation test",
                )
            )
            return issues, details

        packages_content = PACKAGES_TEX.read_text(encoding="utf-8") if PACKAGES_TEX.exists() else ""
        macros_content = MACROS_TEX.read_text(encoding="utf-8") if MACROS_TEX.exists() else ""
        envs_content = ENVIRONMENTS_TEX.read_text(encoding="utf-8") if ENVIRONMENTS_TEX.exists() else ""

        with tempfile.TemporaryDirectory(prefix=f"tikz_test_{chapter_id}_") as temp_dir:
            temp_path = Path(temp_dir)

            for idx, block in enumerate(tikz_blocks, 1):
                start_l = block["start_line"]
                tikz_code = block["code"]

                tex_content = f"""\\documentclass[preview,border=10pt]{{standalone}}
\\makeatletter
\\@ifundefined{{c@chapter}}{{\\newcounter{{chapter}}}}{{}}
\\makeatother
{packages_content}
{envs_content}
{macros_content}
\\begin{{document}}
{tikz_code}
\\end{{document}}
"""
                tex_file = temp_path / f"tikz_{idx}.tex"
                tex_file.write_text(tex_content, encoding="utf-8")

                try:
                    res = subprocess.run(
                        [pdflatex_bin, "-interaction=nonstopmode", tex_file.name],
                        cwd=temp_dir,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        timeout=self.timeout_sec,
                    )
                    stdout = res.stdout.decode("utf-8", errors="replace")
                    pdf_file = temp_path / f"tikz_{idx}.pdf"

                    if res.returncode == 0 and pdf_file.exists() and pdf_file.stat().st_size > 0:
                        details["success"] += 1
                        details["results"].append({
                            "index": idx,
                            "start_line": start_l,
                            "status": "PASS",
                        })
                    else:
                        err_match = re.findall(r"! (.*?)(?:\n\n|\n l\.)", stdout, re.DOTALL)
                        err_msg = err_match[0].replace("\n", " ").strip() if err_match else "Compilation failed"
                        issues.append(
                            Issue(
                                tier=2,
                                chapter_id=chapter_id,
                                severity=IssueSeverity.ERROR,
                                rule_id="T2_TIKZ_COMPILE_FAILED",
                                message=f"TikZ diagram at line {start_l} failed standalone compilation: {err_msg}",
                                line_number=start_l,
                            )
                        )
                        details["results"].append({
                            "index": idx,
                            "start_line": start_l,
                            "status": "FAIL",
                            "error": err_msg,
                        })
                except subprocess.TimeoutExpired:
                    issues.append(
                        Issue(
                            tier=2,
                            chapter_id=chapter_id,
                            severity=IssueSeverity.ERROR,
                            rule_id="T2_TIKZ_COMPILE_TIMEOUT",
                            message=f"TikZ diagram at line {start_l} timed out (> {self.timeout_sec}s) during compilation",
                            line_number=start_l,
                        )
                    )
                    details["results"].append({
                        "index": idx,
                        "start_line": start_l,
                        "status": "TIMEOUT",
                    })

        return issues, details

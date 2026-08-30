"""
Tier 4: Global LaTeX Build & PDF Document Verification
Executes latexmk, parses compilation logs, and verifies the generated PDF document.
"""
import re
import subprocess
import shutil
import time
from pathlib import Path
from typing import Dict, List, Tuple, Any, Optional

from .config import PROJECT_ROOT, MAIN_TEX, MAIN_PDF, MAIN_LOG, MAIN_TOC, CHAPTER_SPECS
from .models import CheckResult, Issue, IssueSeverity

try:
    import fitz  # PyMuPDF
    HAVE_FITZ = True
except ImportError:
    HAVE_FITZ = False

try:
    import pypdf
    HAVE_PYPDF = True
except ImportError:
    HAVE_PYPDF = False


class Tier4BuildValidator:
    def __init__(self, timeout_sec: int = 120, max_overfull_warn: int = 20):
        self.timeout_sec = timeout_sec
        self.max_overfull_warn = max_overfull_warn

    def execute_and_validate(self, clean_first: bool = False) -> CheckResult:
        issues: List[Issue] = []
        details: Dict[str, Any] = {
            "build_command": "latexmk -pdf -g -interaction=nonstopmode main.tex",
            "exit_code": None,
            "duration_sec": 0.0,
            "pdf_exists": False,
            "pdf_pages": 0,
            "pdf_size_bytes": 0,
            "fatal_errors": [],
            "undefined_references": [],
            "undefined_citations": [],
            "overfull_hboxes": [],
            "underfull_hboxes_count": 0,
            "toc_chapters_found": 0,
        }

        if clean_first:
            self.clean_auxiliary_files()

        # Check latexmk executable
        latexmk_bin = shutil.which("latexmk") or "/Library/TeX/texbin/latexmk"
        if not Path(latexmk_bin).exists() and not shutil.which("latexmk"):
            issues.append(
                Issue(
                    tier=4,
                    chapter_id="global",
                    severity=IssueSeverity.CRITICAL,
                    rule_id="T4_LATEXMK_NOT_FOUND",
                    message="latexmk executable not found in PATH or standard TeX Live directories",
                )
            )
            return CheckResult(
                name="Tier 4: Global LaTeX Build",
                tier=4,
                passed=False,
                score=0.0,
                issues=issues,
                details=details,
            )

        # 1. Execute latexmk build
        start_time = time.time()
        try:
            res = subprocess.run(
                [latexmk_bin, "-pdf", "-g", "-interaction=nonstopmode", MAIN_TEX.name],
                cwd=str(PROJECT_ROOT),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=self.timeout_sec,
            )
            duration = time.time() - start_time
            details["duration_sec"] = round(duration, 2)
            details["exit_code"] = res.returncode
            stdout_text = res.stdout.decode("utf-8", errors="replace")

            if res.returncode != 0:
                issues.append(
                    Issue(
                        tier=4,
                        chapter_id="global",
                        severity=IssueSeverity.CRITICAL,
                        rule_id="T4_BUILD_EXIT_NON_ZERO",
                        message=f"latexmk failed with non-zero exit code: {res.returncode}",
                    )
                )
        except subprocess.TimeoutExpired:
            duration = time.time() - start_time
            details["duration_sec"] = round(duration, 2)
            issues.append(
                Issue(
                    tier=4,
                    chapter_id="global",
                    severity=IssueSeverity.CRITICAL,
                    rule_id="T4_BUILD_TIMEOUT",
                    message=f"latexmk compilation timed out after {self.timeout_sec} seconds",
                )
            )
            return CheckResult(
                name="Tier 4: Global LaTeX Build",
                tier=4,
                passed=False,
                score=0.0,
                issues=issues,
                details=details,
            )

        # 2. Deep Log File Parsing
        if MAIN_LOG.exists():
            log_issues, log_details = self._parse_log_file(MAIN_LOG)
            issues.extend(log_issues)
            details.update(log_details)
        else:
            issues.append(
                Issue(
                    tier=4,
                    chapter_id="global",
                    severity=IssueSeverity.ERROR,
                    rule_id="T4_NO_LOG_FILE",
                    message="Compilation log file main.log was not generated",
                )
            )

        # 3. PDF Document Verification
        if MAIN_PDF.exists():
            details["pdf_exists"] = True
            pdf_size = MAIN_PDF.stat().st_size
            details["pdf_size_bytes"] = pdf_size

            if pdf_size == 0:
                issues.append(
                    Issue(
                        tier=4,
                        chapter_id="global",
                        severity=IssueSeverity.CRITICAL,
                        rule_id="T4_EMPTY_PDF",
                        message="Generated PDF file main.pdf has 0 bytes",
                    )
                )
            else:
                pdf_issues, pdf_meta = self._verify_pdf_structure(MAIN_PDF)
                issues.extend(pdf_issues)
                details.update(pdf_meta)
        else:
            issues.append(
                Issue(
                    tier=4,
                    chapter_id="global",
                    severity=IssueSeverity.CRITICAL,
                    rule_id="T4_PDF_NOT_FOUND",
                    message="Generated PDF file main.pdf not found",
                )
            )

        # 4. Table of Contents Verification
        if MAIN_TOC.exists():
            toc_issues, toc_count = self._verify_toc(MAIN_TOC)
            issues.extend(toc_issues)
            details["toc_chapters_found"] = toc_count

        critical_and_errors = [i for i in issues if i.severity in (IssueSeverity.CRITICAL, IssueSeverity.ERROR)]
        warnings = [i for i in issues if i.severity == IssueSeverity.WARNING]
        passed = len(critical_and_errors) == 0
        score = max(0.0, 1.0 - (len(critical_and_errors) * 0.4 + len(warnings) * 0.05))

        return CheckResult(
            name="Tier 4: Global LaTeX Build",
            tier=4,
            passed=passed,
            score=score,
            issues=issues,
            details=details,
        )

    def _parse_log_file(self, log_path: Path) -> Tuple[List[Issue], Dict[str, Any]]:
        issues: List[Issue] = []
        details: Dict[str, Any] = {
            "fatal_errors": [],
            "undefined_references": [],
            "undefined_citations": [],
            "overfull_hboxes": [],
            "underfull_hboxes_count": 0,
        }

        log_content = log_path.read_text(encoding="utf-8", errors="replace")

        # 1. Fatal LaTeX Errors
        fatal_matches = re.findall(r"^!\s+(.+?)(?=\n\n|\n!\s|\n\s*l\.|\Z)", log_content, re.MULTILINE | re.DOTALL)
        for err in fatal_matches:
            clean_err = " ".join(err.strip().splitlines())
            details["fatal_errors"].append(clean_err)
            issues.append(
                Issue(
                    tier=4,
                    chapter_id="global",
                    severity=IssueSeverity.CRITICAL,
                    rule_id="T4_LATEX_FATAL_ERROR",
                    message=f"LaTeX Fatal Error: {clean_err}",
                )
            )

        # 2. Undefined references
        undef_refs = re.findall(r"LaTeX Warning:\s+Reference `([^']+)' on page \d+ undefined", log_content)
        details["undefined_references"] = list(set(undef_refs))
        for ref in set(undef_refs):
            issues.append(
                Issue(
                    tier=4,
                    chapter_id="global",
                    severity=IssueSeverity.ERROR,
                    rule_id="T4_UNDEFINED_REFERENCE",
                    message=f"Undefined LaTeX reference: `{ref}`",
                )
            )

        # 3. Undefined citations
        undef_cites = re.findall(r"LaTeX Warning:\s+Citation `([^']+)' on page \d+ undefined", log_content)
        details["undefined_citations"] = list(set(undef_cites))
        for cite in set(undef_cites):
            issues.append(
                Issue(
                    tier=4,
                    chapter_id="global",
                    severity=IssueSeverity.WARNING,
                    rule_id="T4_UNDEFINED_CITATION",
                    message=f"Undefined citation: `{cite}`",
                )
            )

        # 4. Overfull \hbox warnings
        overfulls = re.findall(r"Overfull \\hbox \(([0-9\.]+)pt too wide\) in paragraph at lines (\d+)--(\d+)", log_content)
        for width, l_start, l_end in overfulls:
            details["overfull_hboxes"].append({
                "overflow_pt": float(width),
                "line_start": int(l_start),
                "line_end": int(l_end),
            })
            if float(width) > 20.0:  # Major overflow > 20pt
                issues.append(
                    Issue(
                        tier=4,
                        chapter_id="global",
                        severity=IssueSeverity.WARNING,
                        rule_id="T4_MAJOR_OVERFULL_HBOX",
                        message=f"Significant Overfull \\hbox ({width}pt too wide) at lines {l_start}--{l_end}",
                        line_number=int(l_start),
                    )
                )

        # 5. Underfull \hbox & \vbox
        underfull_h = len(re.findall(r"Underfull \\hbox", log_content))
        underfull_v = len(re.findall(r"Underfull \\vbox", log_content))
        details["underfull_hboxes_count"] = underfull_h
        details["underfull_vboxes_count"] = underfull_v

        return issues, details

    def _verify_pdf_structure(self, pdf_path: Path) -> Tuple[List[Issue], Dict[str, Any]]:
        issues: List[Issue] = []
        meta: Dict[str, Any] = {"pdf_pages": 0, "title": "", "author": ""}

        page_count = 0
        if HAVE_FITZ:
            try:
                doc = fitz.open(str(pdf_path))
                page_count = len(doc)
                meta["pdf_pages"] = page_count
                meta["title"] = doc.metadata.get("title", "")
                meta["author"] = doc.metadata.get("author", "")
                doc.close()
            except Exception as e:
                issues.append(
                    Issue(
                        tier=4,
                        chapter_id="global",
                        severity=IssueSeverity.ERROR,
                        rule_id="T4_PDF_CORRUPT",
                        message=f"PyMuPDF failed to parse PDF: {e}",
                    )
                )
        elif HAVE_PYPDF:
            try:
                reader = pypdf.PdfReader(str(pdf_path))
                page_count = len(reader.pages)
                meta["pdf_pages"] = page_count
            except Exception as e:
                issues.append(
                    Issue(
                        tier=4,
                        chapter_id="global",
                        severity=IssueSeverity.ERROR,
                        rule_id="T4_PDF_CORRUPT",
                        message=f"pypdf failed to parse PDF: {e}",
                    )
                )

        if page_count < 50:
            issues.append(
                Issue(
                    tier=4,
                    chapter_id="global",
                    severity=IssueSeverity.WARNING,
                    rule_id="T4_LOW_PAGE_COUNT",
                    message=f"Generated PDF has only {page_count} pages (expected >= 50 for full text)",
                )
            )

        return issues, meta

    def _verify_toc(self, toc_path: Path) -> Tuple[List[Issue], int]:
        issues: List[Issue] = []
        toc_content = toc_path.read_text(encoding="utf-8", errors="replace")
        chapter_entries = re.findall(r"\\contentsline\s*\{chapter\}\{\\numberline\s*\{(\d+)\}", toc_content)
        found_nums = [int(n) for n in chapter_entries]

        expected_count = len(CHAPTER_SPECS)
        for num in range(1, expected_count + 1):
            if num not in found_nums:
                issues.append(
                    Issue(
                        tier=4,
                        chapter_id="global",
                        severity=IssueSeverity.WARNING,
                        rule_id="T4_TOC_MISSING_CHAPTER",
                        message=f"Chapter {num} is missing from Table of Contents (main.toc)",
                    )
                )

        return issues, len(found_nums)

    def clean_auxiliary_files(self) -> None:
        extensions = [".aux", ".log", ".fls", ".fdb_latexmk", ".out", ".toc", ".synctex.gz"]
        for ext in extensions:
            for f in PROJECT_ROOT.glob(f"*{ext}"):
                try:
                    f.unlink()
                except OSError:
                    pass
            for f in (PROJECT_ROOT / "chapters").glob(f"*/*{ext}"):
                try:
                    f.unlink()
                except OSError:
                    pass

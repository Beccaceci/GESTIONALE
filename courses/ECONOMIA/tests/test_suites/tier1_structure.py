"""
Tier 1: Feature and Structural Coverage Validation
Checks chapter files for structural correctness, environments, section hierarchy, and length.
"""
import re
from pathlib import Path
from typing import Dict, List, Tuple, Any

from .config import CHAPTER_SPECS, RECOGNIZED_TCOLORBOX_ENVS
from .models import CheckResult, Issue, IssueSeverity


class Tier1StructureValidator:
    def __init__(self, strict_mature: bool = False):
        self.strict_mature = strict_mature

    def validate_chapter(self, chapter_id: str, chapter_file: Path) -> CheckResult:
        issues: List[Issue] = []
        details: Dict[str, Any] = {}
        spec = CHAPTER_SPECS.get(chapter_id, {})

        if not chapter_file.exists():
            issues.append(
                Issue(
                    tier=1,
                    chapter_id=chapter_id,
                    severity=IssueSeverity.CRITICAL,
                    rule_id="T1_FILE_EXISTS",
                    message=f"Chapter file not found: {chapter_file}",
                )
            )
            return CheckResult(
                name="Tier 1: Structural Coverage",
                tier=1,
                passed=False,
                score=0.0,
                issues=issues,
                details={"file_exists": False},
            )

        content = chapter_file.read_text(encoding="utf-8")
        lines = content.splitlines()
        non_empty_lines = [l for l in lines if l.strip() and not l.strip().startswith("%")]
        words = re.findall(r"\b\w+\b", content)
        word_count = len(words)
        line_count = len(lines)

        details["line_count"] = line_count
        details["non_empty_line_count"] = len(non_empty_lines)
        details["word_count"] = word_count

        # 1. Prohibited root document commands
        prohibited = [
            (r"\\documentclass", "T1_NO_DOCUMENTCLASS", "Chapter file contains \\documentclass"),
            (r"\\begin\{document\}", "T1_NO_BEGIN_DOC", "Chapter file contains \\begin{document}"),
            (r"\\end\{document\}", "T1_NO_END_DOC", "Chapter file contains \\end{document}"),
        ]
        for pattern, rule_id, msg in prohibited:
            for idx, line in enumerate(lines, 1):
                if re.search(pattern, line):
                    issues.append(
                        Issue(
                            tier=1,
                            chapter_id=chapter_id,
                            severity=IssueSeverity.ERROR,
                            rule_id=rule_id,
                            message=msg,
                            line_number=idx,
                            snippet=line.strip(),
                        )
                    )

        # 2. Chapter header and label checks
        chap_match = re.search(r"\\chapter\{([^}]+)\}", content)
        if not chap_match:
            issues.append(
                Issue(
                    tier=1,
                    chapter_id=chapter_id,
                    severity=IssueSeverity.ERROR,
                    rule_id="T1_CHAPTER_TITLE",
                    message="Missing \\chapter{...} command",
                )
            )
            details["has_chapter_title"] = False
        else:
            details["has_chapter_title"] = True
            details["extracted_title"] = chap_match.group(1)

        label_match = re.search(r"\\label\{chap:([^}]+)\}", content)
        if not label_match:
            issues.append(
                Issue(
                    tier=1,
                    chapter_id=chapter_id,
                    severity=IssueSeverity.WARNING,
                    rule_id="T1_CHAPTER_LABEL",
                    message="Missing or non-standard \\label{chap:...} chapter label",
                )
            )
            details["has_chapter_label"] = False
        else:
            details["has_chapter_label"] = True
            details["extracted_label"] = label_match.group(1)

        # 3. Minimum length thresholds
        min_draft = spec.get("min_lines_draft", 40)
        min_mature = spec.get("min_lines_mature", 250)

        if line_count < min_draft:
            issues.append(
                Issue(
                    tier=1,
                    chapter_id=chapter_id,
                    severity=IssueSeverity.ERROR,
                    rule_id="T1_MIN_LENGTH_DRAFT",
                    message=f"Chapter line count ({line_count}) is below minimum threshold ({min_draft} lines)",
                )
            )
        elif self.strict_mature and line_count < min_mature:
            issues.append(
                Issue(
                    tier=1,
                    chapter_id=chapter_id,
                    severity=IssueSeverity.WARNING,
                    rule_id="T1_MIN_LENGTH_MATURE",
                    message=f"Chapter is in draft stage ({line_count} lines, target mature: {min_mature}+ lines)",
                )
            )

        # 4. Environment extraction and tag balancing
        env_issues, env_counts = self._check_environment_balance(chapter_id, lines)
        issues.extend(env_issues)
        details["env_counts"] = env_counts

        # Check for presence of tcolorbox environments
        tcb_counts = {k: v for k, v in env_counts.items() if k in RECOGNIZED_TCOLORBOX_ENVS}
        details["tcb_counts"] = tcb_counts
        total_tcb = sum(tcb_counts.values())
        details["total_tcb_environments"] = total_tcb

        if total_tcb == 0:
            issues.append(
                Issue(
                    tier=1,
                    chapter_id=chapter_id,
                    severity=IssueSeverity.ERROR,
                    rule_id="T1_NO_TCB_ENVS",
                    message="No didactic tcolorbox environments found in chapter",
                )
            )

        # Check required envs from specs
        required_envs = spec.get("required_envs", [])
        missing_envs = [env for env in required_envs if env_counts.get(env, 0) == 0]
        details["missing_required_envs"] = missing_envs
        if missing_envs:
            severity = IssueSeverity.WARNING if not self.strict_mature else IssueSeverity.ERROR
            issues.append(
                Issue(
                    tier=1,
                    chapter_id=chapter_id,
                    severity=severity,
                    rule_id="T1_MISSING_REQ_ENVS",
                    message=f"Missing recommended didactic environments: {', '.join(missing_envs)}",
                )
            )

        # 5. Section Hierarchy Validation
        sec_issues, sec_counts = self._check_section_hierarchy(chapter_id, lines)
        issues.extend(sec_issues)
        details["section_counts"] = sec_counts

        # 6. Table row separator validation
        tbl_issues = self._check_table_rows(chapter_id, lines)
        issues.extend(tbl_issues)

        # Score calculation
        errors = [i for i in issues if i.severity in (IssueSeverity.ERROR, IssueSeverity.CRITICAL)]
        warnings = [i for i in issues if i.severity == IssueSeverity.WARNING]
        passed = len(errors) == 0
        score = max(0.0, 1.0 - (len(errors) * 0.25 + len(warnings) * 0.05))

        return CheckResult(
            name="Tier 1: Structural Coverage",
            tier=1,
            passed=passed,
            score=score,
            issues=issues,
            details=details,
        )

    def _check_environment_balance(
        self, chapter_id: str, lines: List[str]
    ) -> Tuple[List[Issue], Dict[str, int]]:
        issues: List[Issue] = []
        stack: List[Tuple[str, int]] = []
        env_counts: Dict[str, int] = {}

        begin_re = re.compile(r"\\begin\{([a-zA-Z0-9_\*]+)\}")
        end_re = re.compile(r"\\end\{([a-zA-Z0-9_\*]+)\}")

        for line_num, line in enumerate(lines, 1):
            # Strip comments
            clean_line = line.split("%")[0]

            for match in begin_re.finditer(clean_line):
                env_name = match.group(1)
                stack.append((env_name, line_num))
                env_counts[env_name] = env_counts.get(env_name, 0) + 1

            for match in end_re.finditer(clean_line):
                env_name = match.group(1)
                if not stack:
                    issues.append(
                        Issue(
                            tier=1,
                            chapter_id=chapter_id,
                            severity=IssueSeverity.ERROR,
                            rule_id="T1_UNMATCHED_END_ENV",
                            message=f"Unmatched \\end{{{env_name}}} with no corresponding \\begin",
                            line_number=line_num,
                            snippet=line.strip(),
                        )
                    )
                else:
                    top_env, top_line = stack.pop()
                    if top_env != env_name:
                        issues.append(
                            Issue(
                                tier=1,
                                chapter_id=chapter_id,
                                severity=IssueSeverity.ERROR,
                                rule_id="T1_MISMATCHED_ENV",
                                message=f"Mismatched environment: \\begin{{{top_env}}} (line {top_line}) closed by \\end{{{env_name}}} (line {line_num})",
                                line_number=line_num,
                                snippet=line.strip(),
                            )
                        )

        while stack:
            unclosed_env, unclosed_line = stack.pop()
            issues.append(
                Issue(
                    tier=1,
                    chapter_id=chapter_id,
                    severity=IssueSeverity.ERROR,
                    rule_id="T1_UNCLOSED_ENV",
                    message=f"Unclosed \\begin{{{unclosed_env}}} from line {unclosed_line}",
                    line_number=unclosed_line,
                )
            )

        return issues, env_counts

    def _check_section_hierarchy(
        self, chapter_id: str, lines: List[str]
    ) -> Tuple[List[Issue], Dict[str, int]]:
        issues: List[Issue] = []
        counts = {"sections": 0, "subsections": 0, "subsubsections": 0}
        seen_section = False

        sec_re = re.compile(r"\\section\{")
        subsec_re = re.compile(r"\\subsection\{")
        subsubsec_re = re.compile(r"\\subsubsection\{")

        for line_num, line in enumerate(lines, 1):
            clean_line = line.split("%")[0]
            if sec_re.search(clean_line):
                counts["sections"] += 1
                seen_section = True
            elif subsec_re.search(clean_line):
                counts["subsections"] += 1
                if not seen_section:
                    issues.append(
                        Issue(
                            tier=1,
                            chapter_id=chapter_id,
                            severity=IssueSeverity.WARNING,
                            rule_id="T1_ORPHAN_SUBSECTION",
                            message="\\subsection used before first \\section",
                            line_number=line_num,
                            snippet=line.strip(),
                        )
                    )
            elif subsubsec_re.search(clean_line):
                counts["subsubsections"] += 1

        if counts["sections"] == 0:
            issues.append(
                Issue(
                    tier=1,
                    chapter_id=chapter_id,
                    severity=IssueSeverity.WARNING,
                    rule_id="T1_NO_SECTIONS",
                    message="No \\section divisions found in chapter",
                )
            )

        return issues, counts

    def _check_table_rows(self, chapter_id: str, lines: List[str]) -> List[Issue]:
        issues: List[Issue] = []
        in_table = False
        table_start_line = 0

        for line_num, line in enumerate(lines, 1):
            clean = line.split("%")[0].strip()
            if not clean:
                continue

            if r"\begin{tabular}" in clean or r"\begin{tabularx}" in clean or r"\begin{array}" in clean:
                in_table = True
                table_start_line = line_num
            elif r"\end{tabular}" in clean or r"\end{tabularx}" in clean or r"\end{array}" in clean:
                in_table = False
            elif in_table:
                # Check for single trailing backslash
                if clean.endswith(r"\ ") or (not clean.endswith(r"\\") and clean.endswith("\\")):
                    issues.append(
                        Issue(
                            tier=1,
                            chapter_id=chapter_id,
                            severity=IssueSeverity.ERROR,
                            rule_id="T1_TABLE_SINGLE_BACKSLASH",
                            message="Table row ends with single backslash '\\' instead of newline '\\\\'",
                            line_number=line_num,
                            snippet=clean,
                        )
                    )
        return issues

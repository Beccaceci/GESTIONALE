"""
Tier 3: Core Mathematical Notation & Formula Presence Validation
Checks LaTeX mathematical integrity, delimiters balance, macro usage, and required economic formulas.
"""
import re
from pathlib import Path
from typing import Dict, List, Tuple, Any

from .config import CHAPTER_SPECS, STANDARD_MACROS
from .models import CheckResult, Issue, IssueSeverity


class Tier3FormulasValidator:
    def __init__(self, strict_macro_usage: bool = False):
        self.strict_macro_usage = strict_macro_usage

    def validate_chapter(self, chapter_id: str, chapter_file: Path) -> CheckResult:
        issues: List[Issue] = []
        details: Dict[str, Any] = {
            "math_envs_count": 0,
            "equations_count": 0,
            "macro_usage": {},
            "key_formulas_found": [],
            "key_formulas_missing": [],
        }

        if not chapter_file.exists():
            return CheckResult(
                name="Tier 3: Mathematical & Formula Integrity",
                tier=3,
                passed=False,
                score=0.0,
                issues=[
                    Issue(
                        tier=3,
                        chapter_id=chapter_id,
                        severity=IssueSeverity.CRITICAL,
                        rule_id="T3_FILE_EXISTS",
                        message=f"Chapter file not found: {chapter_file}",
                    )
                ],
                details=details,
            )

        content = chapter_file.read_text(encoding="utf-8")
        lines = content.splitlines()

        # 1. Math syntax & delimiter balance checks
        math_issues, math_meta = self._check_math_syntax(chapter_id, lines)
        issues.extend(math_issues)
        details.update(math_meta)

        # 2. Standard Macros Usage Analysis
        macro_issues, macro_stats = self._check_macros_usage(chapter_id, content)
        issues.extend(macro_issues)
        details["macro_usage"] = macro_stats

        # 3. Chapter Key Formula Coverage from Specification
        formula_issues, formula_stats = self._check_key_formulas(chapter_id, content)
        issues.extend(formula_issues)
        details["key_formulas_found"] = formula_stats["found"]
        details["key_formulas_missing"] = formula_stats["missing"]

        errors = [i for i in issues if i.severity in (IssueSeverity.ERROR, IssueSeverity.CRITICAL)]
        warnings = [i for i in issues if i.severity == IssueSeverity.WARNING]
        passed = len(errors) == 0
        score = max(0.0, 1.0 - (len(errors) * 0.25 + len(warnings) * 0.05))

        return CheckResult(
            name="Tier 3: Mathematical & Formula Integrity",
            tier=3,
            passed=passed,
            score=score,
            issues=issues,
            details=details,
        )

    def _check_math_syntax(
        self, chapter_id: str, lines: List[str]
    ) -> Tuple[List[Issue], Dict[str, Any]]:
        issues: List[Issue] = []
        meta = {
            "math_envs_count": 0,
            "equations_count": 0,
            "inline_math_count": 0,
        }

        in_display_math = False
        display_math_env = None
        display_start_line = 0

        math_env_patterns = [
            "equation", "equation*", "align", "align*", "gather", "gather*",
            "multline", "multline*", "flalign", "flalign*", "alignat", "alignat*"
        ]

        left_right_stack: List[Tuple[str, int]] = []

        for line_num, line in enumerate(lines, 1):
            clean_line = line.split("%")[0].strip()
            if not clean_line:
                continue

            # Check double subscript error like x_a_b without braces
            double_sub = re.findall(r"(?<!\\)[a-zA-Z0-9]_([a-zA-Z0-9])_([a-zA-Z0-9])", clean_line)
            if double_sub:
                issues.append(
                    Issue(
                        tier=3,
                        chapter_id=chapter_id,
                        severity=IssueSeverity.ERROR,
                        rule_id="T3_DOUBLE_SUBSCRIPT",
                        message=f"Double subscript without braces detected: '{double_sub[0][0]}_{double_sub[0][1]}'",
                        line_number=line_num,
                        snippet=clean_line,
                    )
                )

            # Check broken \frac without second argument (e.g. \frac{a} followed by non-brace)
            broken_frac = re.findall(r"\\frac\{[^{}]+\}(?!\s*\{)", clean_line)
            if broken_frac:
                issues.append(
                    Issue(
                        tier=3,
                        chapter_id=chapter_id,
                        severity=IssueSeverity.ERROR,
                        rule_id="T3_BROKEN_FRAC",
                        message=f"Incomplete \\frac command (missing denominator): '{broken_frac[0]}'",
                        line_number=line_num,
                        snippet=clean_line,
                    )
                )

            # Check \begin{math_env}
            for env in math_env_patterns:
                if f"\\begin{{{env}}}" in clean_line:
                    in_display_math = True
                    display_math_env = env
                    display_start_line = line_num
                    meta["equations_count"] += 1
                    meta["math_envs_count"] += 1
                if f"\\end{{{env}}}" in clean_line:
                    in_display_math = False
                    display_math_env = None

            # Check \left and \right balance
            lefts = len(re.findall(r"\\left[\(\[\{\.\|]", clean_line))
            rights = len(re.findall(r"\\right[\)\]\}\.\|]", clean_line))
            if lefts != rights and not in_display_math:
                # If within a single inline line
                if "$" in clean_line:
                    issues.append(
                        Issue(
                            tier=3,
                            chapter_id=chapter_id,
                            severity=IssueSeverity.WARNING,
                            rule_id="T3_LEFT_RIGHT_MISMATCH",
                            message=f"Possible \\left and \\right mismatch ({lefts} \\left vs {rights} \\right)",
                            line_number=line_num,
                            snippet=clean_line,
                        )
                    )

            # Count inline math $...$
            dollar_count = clean_line.count("$") - clean_line.count(r"\$")
            if dollar_count > 0:
                meta["inline_math_count"] += dollar_count // 2
                if dollar_count % 2 != 0:
                    issues.append(
                        Issue(
                            tier=3,
                            chapter_id=chapter_id,
                            severity=IssueSeverity.WARNING,
                            rule_id="T3_UNMATCHED_DOLLAR",
                            message=f"Odd number of '$' math delimiters ({dollar_count}) on line",
                            line_number=line_num,
                            snippet=clean_line,
                        )
                    )

        return issues, meta

    def _check_macros_usage(
        self, chapter_id: str, content: str
    ) -> Tuple[List[Issue], Dict[str, int]]:
        issues: List[Issue] = []
        stats: Dict[str, int] = {}

        all_macros = (
            STANDARD_MACROS["differential"]
            + STANDARD_MACROS["logic"]
            + STANDARD_MACROS["micro"]
            + STANDARD_MACROS["macro"]
        )

        for macro in all_macros:
            # Escape for regex
            pattern = re.escape(macro) + r"(?![a-zA-Z])"
            count = len(re.findall(pattern, content))
            if count > 0:
                stats[macro] = count

        spec = CHAPTER_SPECS.get(chapter_id, {})
        expected_macros = spec.get("expected_macros", [])
        missing_expected = [m for m in expected_macros if stats.get(m, 0) == 0]

        if missing_expected and self.strict_macro_usage:
            issues.append(
                Issue(
                    tier=3,
                    chapter_id=chapter_id,
                    severity=IssueSeverity.WARNING,
                    rule_id="T3_MISSING_STANDARD_MACRO",
                    message=f"Standard macros not utilized: {', '.join(missing_expected)}",
                )
            )

        return issues, stats

    def _check_key_formulas(
        self, chapter_id: str, content: str
    ) -> Tuple[List[Issue], Dict[str, List[str]]]:
        issues: List[Issue] = []
        spec = CHAPTER_SPECS.get(chapter_id, {})
        patterns = spec.get("key_formula_patterns", [])

        found: List[str] = []
        missing: List[str] = []

        for pat in patterns:
            if re.search(pat, content):
                found.append(pat)
            else:
                missing.append(pat)

        if missing:
            issues.append(
                Issue(
                    tier=3,
                    chapter_id=chapter_id,
                    severity=IssueSeverity.WARNING,
                    rule_id="T3_KEY_FORMULA_MISSING",
                    message=f"Key theoretical formula / notation patterns missing: {', '.join(missing)}",
                )
            )

        return issues, {"found": found, "missing": missing}

#!/usr/bin/env python3
"""
E2E Test Runner for Istituzioni di Economia (Micro & Macro)
Comprehensive testing across:
- Tier 1: Feature and structural coverage (environments, length, sectioning, syntax balance)
- Tier 2: TikZ diagrams, bounding box checks, pgfplots, figure wrappers, standalone compilability
- Tier 3: Core mathematical notation & formula presence (micro/macro)
- Tier 4: Global LaTeX build (latexmk -pdf -g -interaction=nonstopmode main.tex, log parsing, PDF validation)
"""
import sys
import argparse
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Set, Any

# Ensure tests package is discoverable
TESTS_DIR = Path(__file__).resolve().parent
PROJECT_DIR = TESTS_DIR.parent
if str(TESTS_DIR) not in sys.path:
    sys.path.insert(0, str(TESTS_DIR))

from test_suites.config import CHAPTER_SPECS, CHAPTERS_DIR, PROJECT_ROOT
from test_suites.models import GlobalTestReport, ChapterTestReport, IssueSeverity, Issue
from test_suites.tier1_structure import Tier1StructureValidator
from test_suites.tier2_tikz import Tier2TikzValidator
from test_suites.tier3_formulas import Tier3FormulasValidator
from test_suites.tier4_build import Tier4BuildValidator
from test_suites.reporter import TestReporter


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Istituzioni di Economia — E2E Test Suite (Tiers 1-4)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 tests/run_e2e_tests.py                    # Run full E2E test suite (Tiers 1-4)
  python3 tests/run_e2e_tests.py --tier 1,2,3       # Run static analysis tiers only
  python3 tests/run_e2e_tests.py --chapter 01,02    # Run tests on specific chapters
  python3 tests/run_e2e_tests.py --fast             # Fast static mode (skip heavy compilation)
  python3 tests/run_e2e_tests.py --compile-tikz     # Verify standalone TikZ compilation
  python3 tests/run_e2e_tests.py --json             # Output structured JSON results
  python3 tests/run_e2e_tests.py --clean            # Clean auxiliary LaTeX files first
        """,
    )
    parser.add_argument(
        "-t", "--tier",
        type=str,
        default="all",
        help="Comma-separated tiers to run: 1, 2, 3, 4 or 'all' (default: all)",
    )
    parser.add_argument(
        "-c", "--chapter",
        type=str,
        default="all",
        help="Comma-separated chapter IDs/prefixes (e.g., '01', '02,03', 'all') (default: all)",
    )
    parser.add_argument(
        "--fast",
        action="store_true",
        help="Fast mode: skips standalone TikZ compilation and Tier 4 LaTeX build",
    )
    parser.add_argument(
        "--compile-tikz",
        action="store_true",
        help="Enable standalone compilation test for each TikZ picture",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Strict mode: treat all warnings as test failures",
    )
    parser.add_argument(
        "--strict-mature",
        action="store_true",
        help="Strict mature mode: require mature line counts (250+ lines) on all chapters",
    )
    parser.add_argument(
        "--clean",
        action="store_true",
        help="Clean LaTeX auxiliary files (.aux, .log, etc.) before compilation",
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose output including code snippets and detailed info",
    )
    parser.add_argument(
        "--no-color",
        action="store_true",
        help="Disable ANSI color output in terminal",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output raw JSON results to standard output",
    )
    parser.add_argument(
        "--json-report",
        type=str,
        default=None,
        help="Path to save the JSON test report",
    )
    parser.add_argument(
        "--md-report",
        type=str,
        default=None,
        help="Path to save the Markdown test report",
    )
    return parser.parse_args()


def resolve_chapters(chapter_arg: str) -> List[str]:
    all_chapters = sorted(list(CHAPTER_SPECS.keys()))
    if chapter_arg.lower() == "all":
        return all_chapters

    requested = [c.strip() for c in chapter_arg.split(",") if c.strip()]
    selected: List[str] = []

    for req in requested:
        matched = False
        for ch in all_chapters:
            if ch == req or ch.startswith(req) or f"{int(req):02d}" in ch:
                if ch not in selected:
                    selected.append(ch)
                    matched = True
        if not matched:
            print(f"[WARN] Chapter identifier '{req}' did not match any known chapter.", file=sys.stderr)

    return selected if selected else all_chapters


def resolve_tiers(tier_arg: str, fast: bool) -> Set[int]:
    if tier_arg.lower() == "all":
        tiers = {1, 2, 3, 4}
    else:
        tiers = set()
        for t in tier_arg.split(","):
            t = t.strip()
            if t.isdigit() and int(t) in {1, 2, 3, 4}:
                tiers.add(int(t))

    if fast:
        tiers.discard(4)

    return tiers if tiers else {1, 2, 3}


def main() -> int:
    args = parse_arguments()
    selected_chapters = resolve_chapters(args.chapter)
    active_tiers = resolve_tiers(args.tier, args.fast)
    compile_tikz = args.compile_tikz and not args.fast

    reporter = TestReporter(
        colorize=not args.no_color and not args.json,
        verbose=args.verbose,
    )

    if not args.json:
        reporter.print_header()

    # Instantiate validators
    t1_validator = Tier1StructureValidator(strict_mature=args.strict_mature)
    t2_validator = Tier2TikzValidator(compile_standalone=compile_tikz)
    t3_validator = Tier3FormulasValidator(strict_macro_usage=args.strict)
    t4_validator = Tier4BuildValidator()

    chapter_reports: Dict[str, ChapterTestReport] = {}
    all_issues: List[Issue] = []

    total_lines = 0
    total_words = 0
    total_envs = 0
    total_tikz = 0

    # Run Chapter-level Tiers (1, 2, 3)
    for chap_id in selected_chapters:
        spec = CHAPTER_SPECS[chap_id]
        chap_num = spec["num"]
        chap_title = spec["title"]
        chap_file = CHAPTERS_DIR / chap_id / "main.tex"

        chap_report = ChapterTestReport(
            chapter_id=chap_id,
            chapter_num=chap_num,
            title=chap_title,
            file_path=str(chap_file),
            passed=True,
        )

        # Tier 1
        if 1 in active_tiers:
            t1_res = t1_validator.validate_chapter(chap_id, chap_file)
            chap_report.tier1_result = t1_res
            chap_report.issues.extend(t1_res.issues)
            all_issues.extend(t1_res.issues)
            if not t1_res.passed:
                chap_report.passed = False
            chap_report.metrics.update(t1_res.details)
            total_lines += t1_res.details.get("line_count", 0)
            total_words += t1_res.details.get("word_count", 0)
            total_envs += t1_res.details.get("total_tcb_environments", 0)

        # Tier 2
        if 2 in active_tiers:
            t2_res = t2_validator.validate_chapter(chap_id, chap_file)
            chap_report.tier2_result = t2_res
            chap_report.issues.extend(t2_res.issues)
            all_issues.extend(t2_res.issues)
            if not t2_res.passed:
                chap_report.passed = False
            chap_report.metrics.update(t2_res.details)
            total_tikz += t2_res.details.get("tikz_count", 0)

        # Tier 3
        if 3 in active_tiers:
            t3_res = t3_validator.validate_chapter(chap_id, chap_file)
            chap_report.tier3_result = t3_res
            chap_report.issues.extend(t3_res.issues)
            all_issues.extend(t3_res.issues)
            if not t3_res.passed:
                chap_report.passed = False
            chap_report.metrics.update(t3_res.details)

        chapter_reports[chap_id] = chap_report

    # Run Tier 4 (Global Build) if requested
    tier4_result = None
    if 4 in active_tiers:
        if not args.json:
            print("  [Tier 4] Initiating Global LaTeX Build (latexmk -pdf)...")
        tier4_result = t4_validator.execute_and_validate(clean_first=args.clean)
        all_issues.extend(tier4_result.issues)

    # Compute overall status
    crit_count = sum(1 for i in all_issues if i.severity == IssueSeverity.CRITICAL)
    err_count = sum(1 for i in all_issues if i.severity == IssueSeverity.ERROR)
    warn_count = sum(1 for i in all_issues if i.severity == IssueSeverity.WARNING)

    tier1_passed = all(c.tier1_result.passed for c in chapter_reports.values() if c.tier1_result)
    tier2_passed = all(c.tier2_result.passed for c in chapter_reports.values() if c.tier2_result)
    tier3_passed = all(c.tier3_result.passed for c in chapter_reports.values() if c.tier3_result)
    tier4_passed = tier4_result.passed if tier4_result else True

    overall_passed = tier1_passed and tier2_passed and tier3_passed and tier4_passed
    if args.strict and warn_count > 0:
        overall_passed = False

    global_report = GlobalTestReport(
        timestamp=datetime.now().isoformat(),
        total_chapters=len(CHAPTER_SPECS),
        tested_chapters=len(selected_chapters),
        all_passed=overall_passed,
        tier1_passed=tier1_passed,
        tier2_passed=tier2_passed,
        tier3_passed=tier3_passed,
        tier4_passed=tier4_passed,
        tier4_result=tier4_result,
        chapter_reports=chapter_reports,
        summary_metrics={
            "total_lines": total_lines,
            "total_words": total_words,
            "total_environments": total_envs,
            "total_tikz_figures": total_tikz,
            "critical_issues": crit_count,
            "error_issues": err_count,
            "warning_issues": warn_count,
        },
        all_issues=all_issues,
    )

    # Output results
    if args.json:
        print(reporter.export_json(global_report))
    else:
        reporter.print_chapter_summary_table(global_report)
        reporter.print_global_summary(global_report)
        if all_issues:
            reporter.print_issues(global_report)

    if args.json_report:
        reporter.export_json(global_report, Path(args.json_report))

    if args.md_report:
        reporter.export_markdown(global_report, Path(args.md_report))

    return 0 if overall_passed else 1


if __name__ == "__main__":
    sys.exit(main())

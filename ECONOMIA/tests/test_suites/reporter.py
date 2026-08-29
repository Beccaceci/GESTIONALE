"""
E2E Test Reporter: ANSI Terminal Display, Markdown Generator & JSON Exporter
"""
import json
from pathlib import Path
from typing import Optional, Dict, Any

from .models import GlobalTestReport, ChapterTestReport, IssueSeverity, Issue


class ConsoleColors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    GRAY = "\033[90m"


class TestReporter:
    def __init__(self, colorize: bool = True, verbose: bool = False):
        self.colorize = colorize
        self.verbose = verbose

    def _c(self, text: str, color: str) -> str:
        if not self.colorize:
            return text
        return f"{color}{text}{ConsoleColors.ENDC}"

    def print_header(self, title: str = "ISTITUZIONI DI ECONOMIA — E2E TEST SUITE") -> None:
        border = "=" * 80
        print()
        print(self._c(border, ConsoleColors.OKBLUE))
        print(self._c(f"  {title}", ConsoleColors.BOLD + ConsoleColors.HEADER))
        print(self._c("  Tiers 1-4 Quality Gate & Validation Harness", ConsoleColors.OKCYAN))
        print(self._c(border, ConsoleColors.OKBLUE))
        print()

    def print_chapter_summary_table(self, report: GlobalTestReport) -> None:
        header = f"{'#':<3} | {'Chapter ID':<35} | {'Lines':<6} | {'Envs':<5} | {'TikZ':<5} | {'T1':<4} | {'T2':<4} | {'T3':<4} | {'Status':<6}"
        div = "-" * len(header)
        print(self._c(header, ConsoleColors.BOLD))
        print(div)

        for chap_id, chap in sorted(report.chapter_reports.items(), key=lambda x: x[1].chapter_num):
            t1_str = self._format_tier_status(chap.tier1_result)
            t2_str = self._format_tier_status(chap.tier2_result)
            t3_str = self._format_tier_status(chap.tier3_result)

            status_str = self._c(" PASS ", ConsoleColors.OKGREEN) if chap.passed else self._c(" FAIL ", ConsoleColors.FAIL)

            line_cnt = chap.metrics.get("line_count", 0)
            env_cnt = chap.metrics.get("total_tcb_environments", 0)
            tikz_cnt = chap.metrics.get("tikz_count", 0)

            print(f"{chap.chapter_num:02d}  | {chap_id:<35} | {line_cnt:<6} | {env_cnt:<5} | {tikz_cnt:<5} | {t1_str:<4} | {t2_str:<4} | {t3_str:<4} | {status_str}")

        print(div)
        print()

    def _format_tier_status(self, check_res) -> str:
        if check_res is None:
            return self._c("SKIP", ConsoleColors.GRAY)
        if check_res.passed:
            return self._c(" OK ", ConsoleColors.OKGREEN)
        return self._c("ERR ", ConsoleColors.FAIL)

    def print_global_summary(self, report: GlobalTestReport) -> None:
        print(self._c("--- GLOBAL VERIFICATION SUMMARY ---", ConsoleColors.BOLD + ConsoleColors.OKCYAN))
        print(f"  Total Chapters Defined:      {report.total_chapters}")
        print(f"  Tested Chapters:             {report.tested_chapters}")
        print(f"  Total Source Lines:          {report.summary_metrics.get('total_lines', 0):,}")
        print(f"  Total Word Count:            {report.summary_metrics.get('total_words', 0):,}")
        print(f"  Total Didactic Environments: {report.summary_metrics.get('total_environments', 0)}")
        print(f"  Total TikZ Diagrams:         {report.summary_metrics.get('total_tikz_figures', 0)}")

        if report.tier4_result:
            t4_pass = report.tier4_result.passed
            t4_str = self._c("PASS (Exit code 0)", ConsoleColors.OKGREEN) if t4_pass else self._c("FAIL", ConsoleColors.FAIL)
            print(f"  Tier 4 LaTeX Build:          {t4_str}")
            print(f"  Build Execution Time:        {report.tier4_result.details.get('duration_sec', 0)}s")
            print(f"  Generated PDF Pages:         {report.tier4_result.details.get('pdf_pages', 0)}")
            print(f"  Generated PDF Size:          {report.tier4_result.details.get('pdf_size_bytes', 0):,} bytes")
            print(f"  Undefined References:        {len(report.tier4_result.details.get('undefined_references', []))}")
            print(f"  Major Overfull \\hbox:       {len(report.tier4_result.details.get('overfull_hboxes', []))}")

        print()
        crit = report.summary_metrics.get("critical_issues", 0)
        errs = report.summary_metrics.get("error_issues", 0)
        warns = report.summary_metrics.get("warning_issues", 0)

        issues_summary = f"Issues: {crit} Critical | {errs} Errors | {warns} Warnings"
        if crit > 0 or errs > 0:
            print(self._c(f"  [RESULT: FAILED] {issues_summary}", ConsoleColors.BOLD + ConsoleColors.FAIL))
        elif warns > 0:
            print(self._c(f"  [RESULT: PASSED WITH WARNINGS] {issues_summary}", ConsoleColors.BOLD + ConsoleColors.WARNING))
        else:
            print(self._c(f"  [RESULT: PASSED (100% Clean)] {issues_summary}", ConsoleColors.BOLD + ConsoleColors.OKGREEN))
        print()

    def print_issues(self, report: GlobalTestReport) -> None:
        if not report.all_issues:
            print(self._c("  No issues found.", ConsoleColors.OKGREEN))
            return

        print(self._c("--- DIAGNOSTICS & ISSUES LIST ---", ConsoleColors.BOLD + ConsoleColors.WARNING))
        for issue in report.all_issues:
            if not self.verbose and issue.severity == IssueSeverity.INFO:
                continue

            sev_color = {
                IssueSeverity.CRITICAL: ConsoleColors.BOLD + ConsoleColors.FAIL,
                IssueSeverity.ERROR: ConsoleColors.FAIL,
                IssueSeverity.WARNING: ConsoleColors.WARNING,
                IssueSeverity.INFO: ConsoleColors.GRAY,
            }.get(issue.severity, ConsoleColors.ENDC)

            line_info = f":{issue.line_number}" if issue.line_number else ""
            print(f"  [{self._c(issue.severity.value, sev_color)}] [Tier {issue.tier}] [{issue.chapter_id}{line_info}] {issue.rule_id}: {issue.message}")
            if issue.snippet and self.verbose:
                print(self._c(f"    > {issue.snippet}", ConsoleColors.GRAY))
        print()

    def export_json(self, report: GlobalTestReport, output_file: Optional[Path] = None) -> str:
        data = report.to_dict()
        json_str = json.dumps(data, indent=2, ensure_ascii=False)
        if output_file:
            output_file.write_text(json_str, encoding="utf-8")
        return json_str

    def export_markdown(self, report: GlobalTestReport, output_file: Optional[Path] = None) -> str:
        lines = [
            "# E2E Test Suite Execution Report",
            f"**Timestamp**: `{report.timestamp}`  ",
            f"**Overall Status**: `{'PASSED' if report.all_passed else 'FAILED'}`  ",
            f"**Tested Chapters**: `{report.tested_chapters}/{report.total_chapters}`  ",
            "",
            "## Summary Metrics",
            f"- **Total Source Lines**: {report.summary_metrics.get('total_lines', 0):,}",
            f"- **Total Word Count**: {report.summary_metrics.get('total_words', 0):,}",
            f"- **Total Didactic Environments**: {report.summary_metrics.get('total_environments', 0)}",
            f"- **Total TikZ Figures**: {report.summary_metrics.get('total_tikz_figures', 0)}",
        ]

        if report.tier4_result:
            lines.extend([
                "",
                "## Tier 4 Global LaTeX Build",
                f"- **Status**: `{'SUCCESS' if report.tier4_result.passed else 'FAILED'}`",
                f"- **PDF Pages**: {report.tier4_result.details.get('pdf_pages', 0)}",
                f"- **PDF Size**: {report.tier4_result.details.get('pdf_size_bytes', 0):,} bytes",
                f"- **Build Duration**: {report.tier4_result.details.get('duration_sec', 0)}s",
                f"- **Undefined References**: {len(report.tier4_result.details.get('undefined_references', []))}",
            ])

        lines.extend([
            "",
            "## Chapter Breakdown",
            "| # | Chapter ID | Lines | Words | Envs | TikZ | Tier 1 | Tier 2 | Tier 3 | Status |",
            "|---|------------|-------|-------|------|------|--------|--------|--------|--------|",
        ])

        for chap_id, chap in sorted(report.chapter_reports.items(), key=lambda x: x[1].chapter_num):
            t1_s = "PASS" if chap.tier1_result and chap.tier1_result.passed else ("FAIL" if chap.tier1_result else "SKIP")
            t2_s = "PASS" if chap.tier2_result and chap.tier2_result.passed else ("FAIL" if chap.tier2_result else "SKIP")
            t3_s = "PASS" if chap.tier3_result and chap.tier3_result.passed else ("FAIL" if chap.tier3_result else "SKIP")
            st_s = "PASS" if chap.passed else "FAIL"

            line_cnt = chap.metrics.get("line_count", 0)
            word_cnt = chap.metrics.get("word_count", 0)
            env_cnt = chap.metrics.get("total_tcb_environments", 0)
            tikz_cnt = chap.metrics.get("tikz_count", 0)

            lines.append(f"| {chap.chapter_num:02d} | `{chap_id}` | {line_cnt} | {word_cnt} | {env_cnt} | {tikz_cnt} | {t1_s} | {t2_s} | {t3_s} | **{st_s}** |")

        if report.all_issues:
            lines.extend([
                "",
                "## Issues and Diagnostics",
                "| Severity | Tier | Chapter | Rule ID | Message |",
                "|----------|------|---------|---------|---------|",
            ])
            for iss in report.all_issues:
                line_str = f" (line {iss.line_number})" if iss.line_number else ""
                lines.append(f"| {iss.severity.value} | Tier {iss.tier} | `{iss.chapter_id}`{line_str} | `{iss.rule_id}` | {iss.message} |")

        md_content = "\n".join(lines) + "\n"
        if output_file:
            output_file.write_text(md_content, encoding="utf-8")
        return md_content

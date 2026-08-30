"""
E2E Test Harness Models and Data Structures
"""
from dataclasses import dataclass, field
from enum import Enum
from typing import List, Dict, Optional, Any


class IssueSeverity(Enum):
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


@dataclass
class Issue:
    tier: int
    chapter_id: str
    severity: IssueSeverity
    rule_id: str
    message: str
    line_number: Optional[int] = None
    snippet: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "tier": self.tier,
            "chapter_id": self.chapter_id,
            "severity": self.severity.value,
            "rule_id": self.rule_id,
            "message": self.message,
            "line_number": self.line_number,
            "snippet": self.snippet,
        }


@dataclass
class CheckResult:
    name: str
    tier: int
    passed: bool
    score: float = 1.0  # 0.0 to 1.0
    issues: List[Issue] = field(default_factory=list)
    details: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "tier": self.tier,
            "passed": self.passed,
            "score": self.score,
            "issues": [i.to_dict() for i in self.issues],
            "details": self.details,
        }


@dataclass
class ChapterTestReport:
    chapter_id: str
    chapter_num: int
    title: str
    file_path: str
    passed: bool = True
    tier1_result: Optional[CheckResult] = None
    tier2_result: Optional[CheckResult] = None
    tier3_result: Optional[CheckResult] = None
    issues: List[Issue] = field(default_factory=list)
    metrics: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "chapter_id": self.chapter_id,
            "chapter_num": self.chapter_num,
            "title": self.title,
            "file_path": self.file_path,
            "passed": self.passed,
            "tier1": self.tier1_result.to_dict() if self.tier1_result else None,
            "tier2": self.tier2_result.to_dict() if self.tier2_result else None,
            "tier3": self.tier3_result.to_dict() if self.tier3_result else None,
            "issues": [i.to_dict() for i in self.issues],
            "metrics": self.metrics,
        }


@dataclass
class GlobalTestReport:
    timestamp: str
    total_chapters: int
    tested_chapters: int
    all_passed: bool
    tier1_passed: bool
    tier2_passed: bool
    tier3_passed: bool
    tier4_passed: bool
    tier4_result: Optional[CheckResult] = None
    chapter_reports: Dict[str, ChapterTestReport] = field(default_factory=dict)
    summary_metrics: Dict[str, Any] = field(default_factory=dict)
    all_issues: List[Issue] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "timestamp": self.timestamp,
            "total_chapters": self.total_chapters,
            "tested_chapters": self.tested_chapters,
            "all_passed": self.all_passed,
            "tier1_passed": self.tier1_passed,
            "tier2_passed": self.tier2_passed,
            "tier3_passed": self.tier3_passed,
            "tier4_passed": self.tier4_passed,
            "tier4": self.tier4_result.to_dict() if self.tier4_result else None,
            "chapters": {k: v.to_dict() for k, v in self.chapter_reports.items()},
            "summary_metrics": self.summary_metrics,
            "issues_count": {
                "critical": sum(1 for i in self.all_issues if i.severity == IssueSeverity.CRITICAL),
                "error": sum(1 for i in self.all_issues if i.severity == IssueSeverity.ERROR),
                "warning": sum(1 for i in self.all_issues if i.severity == IssueSeverity.WARNING),
                "info": sum(1 for i in self.all_issues if i.severity == IssueSeverity.INFO),
            },
        }

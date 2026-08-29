"""
E2E Test Suite Package for Istituzioni di Economia
"""
from .config import CHAPTER_SPECS, PROJECT_ROOT, RECOGNIZED_TCOLORBOX_ENVS
from .models import Issue, IssueSeverity, CheckResult, ChapterTestReport, GlobalTestReport
from .tier1_structure import Tier1StructureValidator
from .tier2_tikz import Tier2TikzValidator
from .tier3_formulas import Tier3FormulasValidator
from .tier4_build import Tier4BuildValidator
from .reporter import TestReporter

__all__ = [
    "CHAPTER_SPECS",
    "PROJECT_ROOT",
    "RECOGNIZED_TCOLORBOX_ENVS",
    "Issue",
    "IssueSeverity",
    "CheckResult",
    "ChapterTestReport",
    "GlobalTestReport",
    "Tier1StructureValidator",
    "Tier2TikzValidator",
    "Tier3FormulasValidator",
    "Tier4BuildValidator",
    "TestReporter",
]

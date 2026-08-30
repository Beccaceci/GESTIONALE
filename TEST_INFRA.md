# E2E Test Infra: Analisi 1 Past Exams Archive

## Test Philosophy
- Opaque-box, requirement-driven verification of archive retrieval, document organization, session splitting, solution completeness, documentation integrity, and git deployment.
- Methodology: 4-tier verification (File Integrity + Page Accounting + Content/Solution Semantic Analysis + Visual/Link Consistency).

## Feature Inventory
| # | Feature | Source (requirement) | Tier 1 | Tier 2 | Tier 3 | Tier 4 |
|---|---------|---------------------|:------:|:------:|:------:|:------:|
| 1 | Academic Year Directory Coverage (12 years) | ORIGINAL_REQUEST §R1 | ✓ | ✓ | ✓ | ✓ |
| 2 | Master Compilation Integrity (12 PDFs) | ORIGINAL_REQUEST §R1, R2 | ✓ | ✓ | ✓ | ✓ |
| 3 | Date-Based Exam Session Splitting (99 PDFs) | ORIGINAL_REQUEST §R2 | ✓ | ✓ | ✓ | ✓ |
| 4 | ISO Filename Format (`YYYY-MM-DD_*.pdf`) | ORIGINAL_REQUEST §R2 | ✓ | ✓ | ✓ | ✓ |
| 5 | Complete Problem Statement Presence | ORIGINAL_REQUEST §R3 | ✓ | ✓ | ✓ | ✓ |
| 6 | Complete Official Solution Presence | ORIGINAL_REQUEST §R3 | ✓ | ✓ | ✓ | ✓ |
| 7 | Visual Renderability & Vector Font Integrity | ORIGINAL_REQUEST §R3 | ✓ | ✓ | ✓ | ✓ |
| 8 | Master README.md Index & Link Validity | ORIGINAL_REQUEST §R4 | ✓ | ✓ | ✓ | ✓ |
| 9 | Git Remote & Clean Status Verification | ORIGINAL_REQUEST §R4 | ✓ | ✓ | ✓ | ✓ |

## Test Architecture
- Test runner: `pytest tests/e2e/test_analisi1_exams.py` or standalone python test script `python3 scripts/analisi1_exams/verify_exams.py`
- Pass/Fail criteria: Exit code 0, 0 failures, 100% of PDFs pass all 4 tiers.

## Coverage Thresholds
- Tier 1: 100% of all generated PDFs (>110 files total) pass integrity, non-zero byte size, and valid %PDF header.
- Tier 2: 100% of sessions partitioned without dropped pages.
- Tier 3: 100% of session files contain both problem text markers and official solution markers.
- Tier 4: Master README.md contains links to all files, 0 broken links, and git status is clean after push.

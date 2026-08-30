# Project: Analisi 1 Past Exams Archive & Processing

## Architecture
This project retrieves, processes, organizes, validates, catalogs, and publishes the full archive of exam papers and official solutions from Prof. Giovanni Alberti's didactics website (Università di Pisa) into the GEST repository.

```
courses/first_year/ANALISI1/esami/
├── README.md                                 # Master Catalog & Comprehensive Index
├── 2024-25/
│   ├── esami_2024-25.pdf                     # Master Yearly Compilation PDF (59 pag.)
│   ├── 2025-02-10_primo_compitino.pdf        # Problems + Official Solutions
│   ├── 2025-05-30_secondo_compitino.pdf
│   ├── 2025-06-24_primo_appello.pdf
│   ├── 2025-07-21_secondo_appello.pdf
│   ├── 2025-09-18_terzo_appello.pdf
│   ├── 2026-01-22_quarto_appello.pdf
│   └── 2026-02-19_quinto_appello.pdf
├── 2023-24/ ... (8 sessions)
├── 2022-23/ ... (8 sessions)
├── 2021-22/ ... (8 sessions)
├── 2020-21/ ... (9 sessions)
├── 2017-18/ ... (8 sessions)
├── 2016-17/ ... (8 sessions)
├── 2015-16/ ... (8 sessions)
├── 2014-15/ ... (8 sessions)
├── 2013-14/ ... (9 sessions)
├── 2012-13/ ... (9 sessions)
└── 2011-12/ ... (9 sessions)
```

## Feature Inventory
| # | Feature | Description | Milestone | Source |
|---|---------|-------------|-----------|--------|
| F1 | Download a.a. 2024-25 | Fetch AM1_24-25 (59 pp) into `2024-25/esami_2024-25.pdf` | M1 | Survey |
| F2 | Download a.a. 2023-24 | Fetch AM1_23-24 (64 pp) into `2023-24/esami_2023-24.pdf` | M1 | Survey |
| F3 | Download a.a. 2022-23 | Fetch AM1_22-23 (75 pp) into `2022-23/esami_2022-23.pdf` | M1 | Survey |
| F4 | Download a.a. 2021-22 | Fetch AM1gest_21-22 (38 pp) into `2021-22/esami_2021-22.pdf` | M1 | Survey |
| F5 | Download a.a. 2020-21 | Fetch AM1gest_20-21 (47 pp) into `2020-21/esami_2020-21.pdf` | M1 | Survey |
| F6 | Download a.a. 2017-18 | Fetch AM1Gest_17-18 (98 pp) into `2017-18/esami_2017-18.pdf` | M1 | Survey |
| F7 | Download a.a. 2016-17 | Fetch AM1Gest_16-17 (82 pp) into `2016-17/esami_2016-17.pdf` | M1 | Survey |
| F8 | Download a.a. 2015-16 | Fetch AM1Gest_15-16 (92 pp) into `2015-16/esami_2015-16.pdf` | M1 | Survey |
| F9 | Download a.a. 2014-15 | Fetch AM1Gest_14-15 (89 pp) into `2014-15/esami_2014-15.pdf` | M1 | Survey |
| F10 | Download a.a. 2013-14 | Fetch AM1Gest_13-14 (76 pp) into `2013-14/esami_2013-14.pdf` | M1 | Survey |
| F11 | Download a.a. 2012-13 | Fetch AM1Gest_12-13 (69 pp) into `2012-13/esami_2012-13.pdf` | M1 | Survey |
| F12 | Download a.a. 2011-12 | Fetch MateGeo_11-12 (39 pp) into `2011-12/esami_2011-12.pdf` | M1 | Survey |
| F13 | Splitter Archetype A | Split & merge Testi + Soluzioni for 2011-12 to 2017-18 | M2 | Survey |
| F14 | Splitter Archetype B | Split integrated sessions for 2020-21 to 2024-25 | M2 | Survey |
| F15 | Naming & ISO normalization | Standardize filenames to `YYYY-MM-DD_<session_slug>.pdf` | M2 | Survey |
| F16 | Programmatic Problem-Solution Verification | Verify text markers for problems and solutions across all 99 PDFs | M3 | Survey |
| F17 | Visual & Rendering Verification | Verify page rendering, non-corruption, and page counts | M3 | Survey |
| F18 | Master README.md Index | Build comprehensive markdown catalog with tables, badges, links | M4 | Survey |
| F19 | Git Staging, Commit & Push | Stage all organized exam files, commit, and push to origin/main | M4 | Survey |
| F20 | E2E Regression & Adversarial Hardening | End-to-end multi-tier automated test suite verification | M5 | Survey |

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| M1 | Download & Directory Setup | Download all 12 yearly compilation PDFs into year subfolders | none | DONE |
| M2 | PDF Splitting & Organization | Split all yearly PDFs into 99 date-based single exam PDFs (problems + solutions) | M1 | DONE |
| M3 | Comprehensive Verification | Run 4-tier verification (file integrity, page accounting, problem/solution content, visual rendering) | M2 | DONE |
| M4 | Documentation & Git Deployment | Generate master `README.md` catalog, stage files, commit, and push to GitHub origin/main | M3 | DONE |
| M5 | E2E Testing & Final Gate | Run complete E2E test harness, verify 100% pass and clean git state | M4 | DONE |

## Interface Contracts
### Downloader (M1) ↔ Splitter (M2)
- Downloader outputs: `courses/first_year/ANALISI1/esami/<YYYY-YY>/esami_<YYYY-YY>.pdf`
- All files are valid PDF binaries with HTTP 200 verification.

### Splitter (M2) ↔ Verifier (M3)
- Splitter outputs: `courses/first_year/ANALISI1/esami/<YYYY-YY>/<YYYY-MM-DD>_<tipo_sessione>.pdf`
- Each session PDF contains problem statements followed by complete official solutions.

### Verifier (M3) ↔ Documenter & Git Publisher (M4)
- Verification report confirms 100% of PDFs are valid, non-empty, and contain solutions.
- README generator uses verified file metadata (dates, names, page counts) to populate catalog.

### Documenter & Git Publisher (M4) ↔ E2E Gate (M5)
- Git commit message: `feat(analisi1): add past exams archive (2011-12 to 2024-25) with solutions and date-based split` (commit `b78e934`)
- Git push to origin/main completed cleanly.

## Code Layout
- Target directory: `courses/first_year/ANALISI1/esami/`
- Tool scripts: `scripts/analisi1_exams/`
  - `download_archive.py`: Script to download all master compilations
  - `split_exams.py`: PyMuPDF engine to slice and concatenate sessions
  - `verify_exams.py`: Multi-tier verification suite
  - `generate_readme.py`: Catalog generator
- Test harness: `tests/e2e/test_analisi1_exams.py`

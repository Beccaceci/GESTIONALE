# E2E Test Suite & Testing Infrastructure Specification

**Project**: Istituzioni di Economia (Microeconomia & Macroeconomia)  
**Test Harness Location**: `ECONOMIA/tests/run_e2e_tests.py`  
**Test Suite Modules**: `ECONOMIA/tests/test_suites/`  
**Target Syllabus**: 18 Chapters (Microeconomia & Macroeconomia)  

---

## 1. Architecture Overview

The testing framework provides a rigorous, 4-tier quality assurance pipeline designed to validate LaTeX source code, didactic environments, TikZ diagrams, mathematical notation, and the global compilation output.

```
ECONOMIA/tests/
├── run_e2e_tests.py                 # Main CLI test runner
├── test_suites/
│   ├── __init__.py                  # Package exports
│   ├── config.py                    # Chapter catalog, thresholds & required formulas
│   ├── models.py                    # Data classes for reports, issues & severities
│   ├── tier1_structure.py           # Tier 1: Structure & Didactic Environments
│   ├── tier2_tikz.py                # Tier 2: TikZ & Graphics Validation
│   ├── tier3_formulas.py            # Tier 3: Mathematical Notation & Formulas
│   ├── tier4_build.py               # Tier 4: Global LaTeX Build & PDF Verification
│   └── reporter.py                  # ANSI Terminal, Markdown & JSON Exporters
```

---

## 2. The 4 Quality Tiers

### Tier 1: Feature & Structural Coverage
- **File & Header Contracts**: Every chapter must reside in `chapters/XX_.../main.tex`, start with `\chapter{...}`, and declare a valid `\label{chap:...}`.
- **Prohibited Root Constructs**: `\documentclass`, `\begin{document}`, and `\end{document}` are strictly prohibited inside chapter files.
- **Content Volume Metrics**: Line counts, word counts, and non-empty lines are measured. Evaluates draft thresholds (>= 40 lines) and mature textbook targets (>= 250 lines / 2,000 words).
- **Environment Completeness & Pairing**:
  - Full stack-based validation of tag matching (`\begin{env}` matching `\end{env}`).
  - Scans and counts all 11 standardized `tcolorbox` didactic environments from `config/environments.tex`:
    - `definizione` (blue, formal definitions)
    - `modello` (purple, economic models)
    - `legge` (teal, economic laws)
    - `teorema` (green, formal propositions)
    - `dimostrazione` (green vertical line, proofs)
    - `metodo` (amber, step-by-step algorithms)
    - `esame` (crimson, exam pitfalls & checklist)
    - `esempio` (purple, practical examples)
    - `esercizio` (amber, solved exercises)
    - `osservazione` (navy, economic intuition)
    - `empirico` (cyan, real-world empirical cases)
- **Table Structure**: Verifies `tabular`, `tabularx`, and `array` row termination (`\\` instead of broken `\`).

### Tier 2: TikZ & Graphic Validation
- **Figure Environment Compliance**: Verifies that every figure has `\centering`, non-empty `\caption{...}`, and `\label{fig:...}`.
- **TikZ / PGFPlots Syntax Checks**:
  - Validates bracket `[]` and brace `{}` pairing.
  - Verifies path command semicolon termination (`\draw`, `\node`, `\fill`, `\path`, `\coordinate`, `\addplot`).
  - Analyzes `axis` options (`xmin`, `xmax`, `ymin`, `ymax`, `xlabel`, `ylabel`, `domain`, `samples`).
- **Standalone Sandbox Compilation Engine**:
  - Extracts each `tikzpicture` block into a standalone preview document.
  - Compiles in a sandbox directory with `pdflatex` to guarantee zero TikZ compilation errors, clipping, or missing libraries.

### Tier 3: Mathematical Notation & Formula Integrity
- **Math Syntax Integrity**:
  - Validates delimiter pairing for `$$...$$`, `$...$`, `\begin{equation}`, `\begin{align}`, `\begin{gather}`, `\begin{cases}`.
  - Validates `\left` and `\right` matching.
  - Detects unescaped characters, double subscripts without braces (`a_b_c`), and incomplete `\frac{...}` statements.
- **Standardized Macro Coverage**:
  - Enforces adoption of macros from `config/macros.tex`:
    - Differential operators: `\dd`, `\dv`, `\dvtwo`, `\pdv`, `\pdvtwo`
    - Microeconomics: `\Qd`, `\Qs`, `\Qeq`, `\Peq`, `\epsp`, `\epsr`, `\epsxy`, `\SMS`, `\SMST`, `\U`, `\RT`, `\RMg`, `\RME`, `\CT`, `\CF`, `\CV`, `\CMg`, `\CME`, `\CMEF`, `\CMEV`, `\profit`, `\surplusC`, `\surplusP`, `\surplusT`, `\lossDW`
    - Macroeconomics: `\PIL`, `\PNL`, `\SA`, `\DA`, `\OA`, `\PMgC`, `\PMgS`, `\PMgM`, `\IS`, `\LM`, `\BP`, `\MD`, `\MS`, `\BM`, `\infl`, `\inflexp`, `\unemp`, `\unempnat`, `\cambionom`, `\cambioreal`
- **Theoretical Formula Syllabus Coverage**:
  - Verifies the presence of chapter-specific required equations (e.g. Slutsky equation in Cap 5, Amoroso-Robinson in Cap 4, Lerner Index and Cournot reaction curves in Cap 8, Keynesian multiplier in Cap 11, IS-LM equations in Cap 14, Phillips curve and NAIRU in Cap 16, Mundell-Fleming BP in Cap 18).

### Tier 4: Global LaTeX Build & PDF Verification
- **Automated Compilation**: Runs `latexmk -pdf -g -interaction=nonstopmode main.tex` in the project root.
- **Deep Log Parser (`main.log`)**:
  - Detects fatal LaTeX errors, missing packages, and emergency stops.
  - Detects undefined references (`LaTeX Warning: Reference '...' undefined`).
  - Detects undefined citations.
  - Extracts and flags major `Overfull \hbox` (> 20pt) with exact line numbers.
- **PDF Artifact Inspection**:
  - Validates `main.pdf` existence, size, and integrity.
  - Page count verification (via PyMuPDF `fitz` or `pypdf`).
  - Table of Contents (`main.toc`) inspection to ensure all 18 chapters are indexed.

---

## 3. CLI Usage & Flags

```bash
# Run complete test suite (Tiers 1-4)
python3 tests/run_e2e_tests.py

# Run static analysis tiers only (fast, sub-second execution)
python3 tests/run_e2e_tests.py --tier 1,2,3

# Filter specific chapters
python3 tests/run_e2e_tests.py --chapter 01,02,03

# Run fast mode (skips Tier 4 build and standalone TikZ compilation)
python3 tests/run_e2e_tests.py --fast

# Verify standalone compilation of every TikZ diagram
python3 tests/run_e2e_tests.py --compile-tikz

# Generate JSON and Markdown reports
python3 tests/run_e2e_tests.py --json-report tests/report.json --md-report tests/report.md

# Clean auxiliary LaTeX files before building
python3 tests/run_e2e_tests.py --clean

# Verbose diagnostic mode
python3 tests/run_e2e_tests.py -v
```

---

## 4. Diagnostics & Rule Catalog

| Rule ID | Severity | Description |
|---------|----------|-------------|
| `T1_FILE_EXISTS` | CRITICAL | Chapter `main.tex` file does not exist |
| `T1_NO_DOCUMENTCLASS` | ERROR | Chapter contains forbidden `\documentclass` |
| `T1_NO_BEGIN_DOC` | ERROR | Chapter contains forbidden `\begin{document}` |
| `T1_CHAPTER_TITLE` | ERROR | Missing `\chapter{...}` title |
| `T1_CHAPTER_LABEL` | WARNING | Missing `\label{chap:...}` |
| `T1_MIN_LENGTH_DRAFT` | ERROR | Chapter below minimum draft line count |
| `T1_UNMATCHED_END_ENV` | ERROR | Unmatched `\end{env}` without `\begin` |
| `T1_MISMATCHED_ENV` | ERROR | Mismatched environment nesting |
| `T1_UNCLOSED_ENV` | ERROR | Unclosed `\begin{env}` |
| `T1_NO_TCB_ENVS` | ERROR | No didactic tcolorbox environments found |
| `T1_TABLE_SINGLE_BACKSLASH` | ERROR | Table row ends with single `\` instead of `\\` |
| `T2_FIGURE_NO_CAPTION` | ERROR | Figure missing `\caption{...}` |
| `T2_FIGURE_NO_LABEL` | WARNING | Figure missing `\label{fig:...}` |
| `T2_FIGURE_CENTERING` | WARNING | Figure missing `\centering` |
| `T2_TIKZ_BRACE_MISMATCH` | ERROR | Unbalanced braces inside `tikzpicture` |
| `T2_TIKZ_COMPILE_FAILED` | ERROR | TikZ picture failed standalone compilation |
| `T3_DOUBLE_SUBSCRIPT` | ERROR | Double subscript without braces (e.g. `x_a_b`) |
| `T3_BROKEN_FRAC` | ERROR | Incomplete `\frac{...}` missing denominator |
| `T3_UNMATCHED_DOLLAR` | WARNING | Odd count of `$` math delimiters on line |
| `T3_KEY_FORMULA_MISSING` | WARNING | Expected syllabus formula pattern missing |
| `T4_BUILD_EXIT_NON_ZERO` | CRITICAL | `latexmk` exited with non-zero return code |
| `T4_LATEX_FATAL_ERROR` | CRITICAL | Fatal error in `main.log` |
| `T4_UNDEFINED_REFERENCE` | ERROR | Undefined `\ref` or `\Cref` reference |
| `T4_MAJOR_OVERFULL_HBOX` | WARNING | Significant overfull horizontal box (> 20pt) |
| `T4_PDF_NOT_FOUND` | CRITICAL | Output `main.pdf` was not produced |
| `T4_TOC_MISSING_CHAPTER` | WARNING | Chapter missing from Table of Contents |

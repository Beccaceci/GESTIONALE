# 📚 University Lecture Notes — Management Engineering (University of Pisa)

[![LaTeX](https://img.shields.io/badge/LaTeX-Typeset-008080?style=flat&logo=latex&logoColor=white)](https://www.latex-project.org/)
[![University](https://img.shields.io/badge/University-University%20of%20Pisa-002D62?style=flat&logo=academia&logoColor=white)](https://www.unipi.it/)
[![Degree](https://img.shields.io/badge/B.Sc.-Management%20Engineering-FF8C00?style=flat)](https://www.ingegneria.unipi.it/)
[![Build and Release](https://github.com/Beccaceci/GESTIONALE/actions/workflows/build-and-release.yml/badge.svg)](https://github.com/Beccaceci/GESTIONALE/actions/workflows/build-and-release.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A comprehensive, rigorous, and modular collection of study guides, lecture summaries, and solved exercises typeset in **LaTeX** for the **B.Sc. in Management Engineering (*Ingegneria Gestionale*)** at the **University of Pisa (*Università di Pisa*)**.

Each document is structured into distinct chapters covering in-depth theoretical foundations, step-by-step mathematical proofs, TikZ conceptual diagrams, and exam problem walkthroughs.

---

## 📥 1-Click Downloads

### 📦 Download Complete Bundle (All Courses in 1-Click)
[![Download All Notes ZIP](https://img.shields.io/badge/Download_All_Notes-Complete_ZIP_Archive-1e293b?style=for-the-badge&logo=zip&logoColor=white)](https://github.com/Beccaceci/GESTIONALE/archive/refs/heads/main.zip)

---

### 📄 Download Individual Course PDFs
Click any button below to download the latest compiled high-definition **PDF** directly from the repository:

| Course | Key Topics | Direct 1-Click PDF Download |
| :--- | :--- | :---: |
| **Linear Algebra and Geometry** (*Algebra Lineare e Geometria*) | Logic & set theory, complex numbers, vector spaces, linear transformations, matrices & linear systems, determinants, eigenvalues & eigenvectors, inner products & spectral theorem, guided exam problems. | [![Download Linear Algebra](https://img.shields.io/badge/Download-Linear__Algebra.pdf-0052cc?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](https://github.com/Beccaceci/GESTIONALE/raw/main/courses/ALGEBRA_LINEARE/main.pdf) |
| **Calculus 1** (*Analisi Matematica 1*) | Number sets, trigonometry, limits & continuity, differential calculus, Taylor expansions, abstract analysis, integral calculus, ordinary differential equations (ODEs), past exam walkthroughs. | [![Download Calculus 1](https://img.shields.io/badge/Download-Calculus__1.pdf-d32f2f?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](https://github.com/Beccaceci/GESTIONALE/raw/main/courses/ANALISI1/main.pdf) |
| **Calculus 2** (*Analisi Matematica 2*) | Multivariable topology, differential calculus in $\mathbb{R}^n$, implicit functions (Dini's Theorem), unconstrained & constrained optimization, curves & line integrals, vector calculus & differential forms, multiple integrals, surfaces & surface integrals, Gauss-Green and Stokes theorems. | [![Download Calculus 2](https://img.shields.io/badge/Download-Calculus__2.pdf-7b1fa2?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](https://github.com/Beccaceci/GESTIONALE/raw/main/courses/ANALISI2/main.pdf) |
| **Economics & Business Organization** (*Economia*) | Economic principles, microeconomics, consumer theory & demand, production & cost theory, market structures, risk & information, macroeconomics, IS-LM and AD-AS models, inflation, unemployment, foreign trade & exchange rates. | [![Download Economics](https://img.shields.io/badge/Download-Economics.pdf-2e7d32?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](https://github.com/Beccaceci/GESTIONALE/raw/main/courses/ECONOMIA/main.pdf) |
| **General Physics** (*Fisica Generale*) | Particle kinematics & dynamics, relative motion & non-inertial frames, work & energy, multi-particle systems & collisions, angular momentum & rotation, rigid body dynamics, gravitation & central forces, oscillations & waves, fluid mechanics, thermodynamics & entropy. | [![Download Physics](https://img.shields.io/badge/Download-Physics.pdf-e65100?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](https://github.com/Beccaceci/GESTIONALE/raw/main/courses/FISICA/main.pdf) |
| **Probability and Statistics** (*Calcolo delle Probabilità e Statistica*) | Descriptive statistics, probability spaces, conditional probability & independence, discrete & continuous random variables, expected value & variance, sums of random variables & Central Limit Theorem (CLT), point estimation & MLE, confidence intervals, hypothesis testing. | [![Download Statistics](https://img.shields.io/badge/Download-Statistics.pdf-00838f?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](https://github.com/Beccaceci/GESTIONALE/raw/main/courses/STATISTICA/main.pdf) |

> 📌 **Note:** All buttons stream the raw binary files directly from GitHub, triggering an instant 1-click download without intermediate pages.

---

## 📂 Repository Structure

All subjects are neatly organized inside the [`courses/`](courses/) directory:

```text
GESTIONALE/
├── .github/
│   └── workflows/
│       └── build-and-release.yml    # Automated CI/CD compilation & release pipeline
├── courses/                         # All university courses wrapped in one clean directory
│   ├── ALGEBRA_LINEARE/
│   │   ├── config/                  # Packages, environments, and custom math macros
│   │   ├── chapters/                # Modular chapter files
│   │   ├── figures/                 # Vector graphics (TikZ) and diagrams
│   │   └── main.tex                 # Master LaTeX file
│   ├── ANALISI1/
│   ├── ANALISI2/
│   ├── ECONOMIA/
│   ├── FISICA/
│   └── STATISTICA/
├── .gitignore                       # Build artifacts filter
└── README.md
```

---

## ⚙️ Local Compilation

If you wish to edit the sources or compile the notes locally, run `latexmk` with a full **TeX Live** or **MacTeX** distribution:

```bash
# Example: compiling Linear Algebra and Geometry
cd courses/ALGEBRA_LINEARE
latexmk -pdf -interaction=nonstopmode main.tex

# Clean auxiliary files after build
latexmk -c
```

---

## 🤖 Continuous Integration & Automated Builds

The repository includes a GitHub Actions pipeline (`.github/workflows/build-and-release.yml`):
1. Runs automatically on every `git push` to `main` across a **6-way parallel matrix**.
2. Compiles all master documents using TeX Live.
3. Packages an **All-in-One ZIP Bundle** and publishes all individual PDFs to GitHub Releases.

---

## 📄 License & Academic Attribution

These study notes are released for academic study, review, and reference purposes under the [MIT License](LICENSE).
Feel free to star ⭐️ the repository or contribute if you find these notes helpful!

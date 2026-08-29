# 📚 Appunti Universitari & Dispense di Studio (STEM & Economia)

[![LaTeX](https://img.shields.io/badge/LaTeX-Typeset-008080?style=flat&logo=latex&logoColor=white)](https://www.latex-project.org/)
[![Build and Release](https://github.com/Beccaceci/GESTIONALE/actions/workflows/build-and-release.yml/badge.svg)](https://github.com/Beccaceci/GESTIONALE/actions/workflows/build-and-release.yml)
[![Latest Release](https://img.shields.io/github/v/release/Beccaceci/GESTIONALE?label=Latest%20Release&color=blue)](https://github.com/Beccaceci/GESTIONALE/releases/latest)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Raccolta completa, rigorosa e modulare di dispense universitarie scritte in **LaTeX**. Ogni corso include teoria approfondita, dimostrazioni passo-passo, schemi concettuali ed esercizi/temi d'esame guidati.

---

## 📥 Download Diretto Dispense (1-Click)

Clicca sui pulsanti sottostanti per scaricare direttamente l'ultima versione compilata in formato **PDF** ad alta definizione:

| Corso | Argomenti Principali | Download Diretto PDF |
| :--- | :--- | :---: |
| **Algebra Lineare e Geometria** | Logica e insiemi, numeri complessi, spazi vettoriali, applicazioni lineari, matrici e sistemi, determinanti, autovalori/autovettori, prodotti scalari e teorema spettrale, esercizi d'esame. | [![Download Algebra Lineare](https://img.shields.io/badge/Download-Algebra__Lineare.pdf-0052cc?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](https://github.com/Beccaceci/GESTIONALE/releases/latest/download/Algebra_Lineare.pdf) |
| **Analisi Matematica 1** | Insiemi numerici, trigonometria, limiti e continuità, calcolo differenziale, polinomi di Taylor, analisi astratta, calcolo integrale, equazioni differenziali ordinarie, temi d'esame. | [![Download Analisi 1](https://img.shields.io/badge/Download-Analisi__1.pdf-d32f2f?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](https://github.com/Beccaceci/GESTIONALE/releases/latest/download/Analisi_1.pdf) |
| **Analisi Matematica 2** | Topologia multivariabile, calcolo differenziale per funzioni di più variabili, funzioni implicite (Dini), ottimizzazione libera e vincolata, curve e integrali di linea, calcolo vettoriale e forme differenziali, integrali doppi/tripli, superfici e integrali superficiali, teoremi di Gauss-Green e Stokes. | [![Download Analisi 2](https://img.shields.io/badge/Download-Analisi__2.pdf-7b1fa2?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](https://github.com/Beccaceci/GESTIONALE/releases/latest/download/Analisi_2.pdf) |
| **Economia** | Scienza economica, microeconomia, teoria del consumatore e della domanda, teoria dell'offerta, strutture di mercato, incertezza e rischio, macroeconomia, modelli IS-LM e AD-AS, inflazione, disoccupazione e tassi di cambio. | [![Download Economia](https://img.shields.io/badge/Download-Economia.pdf-2e7d32?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](https://github.com/Beccaceci/GESTIONALE/releases/latest/download/Economia.pdf) |
| **Fisica Generale** | Cinematica e dinamica del punto materiale, moti relativi e forze fittizie, lavoro ed energia, sistemi di punti e urti, momento angolare e rotazioni, dinamica del corpo rigido, gravitazione, oscillazioni e onde, fluidi, termodinamica ed entropia. | [![Download Fisica](https://img.shields.io/badge/Download-Fisica.pdf-e65100?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](https://github.com/Beccaceci/GESTIONALE/releases/latest/download/Fisica.pdf) |
| **Calcolo delle Probabilità e Statistica** | Statistica descrittiva, spazi di probabilità, probabilità condizionata e indipendenza, variabili aleatorie discrete e continue, valore atteso e varianza, somme di v.a. e TLC, teoria della stima, intervalli di confidenza, test d'ipotesi parametrici e non parametrici. | [![Download Statistica](https://img.shields.io/badge/Download-Statistica.pdf-00838f?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](https://github.com/Beccaceci/GESTIONALE/releases/latest/download/Statistica.pdf) |

> 📌 **Nota sui Link:** I pulsanti di download puntano all'ultima release automatica generata via GitHub Actions (`releases/latest/download/...`).

---

## 📂 Organizzazione del Repository

La struttura del progetto è modulare: ciascuna materia risiede in una propria directory autonoma contenente configurazioni grafiche, macro, capitoli suddivisi e figure:

```text
GESTIONALE/
├── .github/
│   └── workflows/
│       └── build-and-release.yml    # CI/CD di compilazione automatica & rilascio PDF
├── ALGEBRA_LINEARE/
│   ├── config/                      # Pacchetti, ambienti personalizzati e macro
│   ├── chapters/                    # Capitoli modulari
│   ├── figures/                     # Immagini, grafici e vettoriali TikZ
│   └── main.tex                     # Master file del documento
├── ANALISI1/
├── ANALISI2/
├── ECONOMIA/
├── FISICA/
├── STATISTICA/
├── .gitignore                       # Esclusione file ausiliari LaTeX
└── README.md
```

---

## ⚙️ Compilazione Locale

Se desideri modificare i sorgenti o compilare localmente i file LaTeX, è consigliato utilizzare `latexmk` o `pdflatex` (distribuzione completa **TeX Live** o **MacTeX**):

```bash
# Esempio: compilazione di Algebra Lineare
cd ALGEBRA_LINEARE
latexmk -pdf -interaction=nonstopmode main.tex

# Pulizia dei file ausiliari
latexmk -c
```

---

## 🤖 Integrazione Continua (CI/CD)

Il repository include una pipeline GitHub Actions configurata in `.github/workflows/build-and-release.yml`:
1. Ad ogni `git push` sul branch `main` o creazione di un tag di versione (`v*`), la pipeline avvia 6 job paralleli.
2. Compila i master file `main.tex` di ciascun corso con TeX Live.
3. Rinomina gli artefatti in modo leggibile (`Algebra_Lineare.pdf`, `Analisi_1.pdf`, ecc.).
4. Aggiorna automaticamente la release `latest` su GitHub, garantendo che i pulsanti di download nel README siano sempre sincronizzati con l'ultima versione del codice.

---

## 📄 Licenza

Questo materiale è rilasciato per scopi di studio e consultazione accademica.
Distribuito sotto licenza [MIT](LICENSE) (o di pubblico dominio accademico).

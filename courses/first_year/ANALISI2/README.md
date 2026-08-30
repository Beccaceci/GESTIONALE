# Appunti di Analisi Matematica 2 - Struttura del Progetto LaTeX

Questo progetto è strutturato in modo **modulare, flessibile ed estensibile** per digitalizzare, ricostruire con rigore e arricchire gli appunti del corso di Analisi Matematica 2 (Corso di Laurea in Ingegneria Gestionale).

---

## 📁 Architettura delle Cartelle

```text
ANALISI2/
│
├── main.tex                                          # Master document: include configurazioni e capitoli
├── main.pdf                                          # PDF compilato finale
│
├── config/                                           # Configurazioni globali e stile
│   ├── packages.tex                                  # Caricamento pacchetti (AMS, TikZ 3D, tcolorbox, esint, ecc.)
│   ├── environments.tex                              # Box personalizzati (Definizioni, Teoremi, Esempi, Esame, Metodi)
│   └── macros.tex                                    # Scorciatoie e comandi di calcolo multivariabile e vettoriale
│
├── chapters/                                         # Cartelle modulari per ciascun capitolo
│   ├── 01_topologia_funzioni_multivariabile/         # Topologia Rn, curve di livello, limiti e continuità
│   │   └── main.tex
│   ├── 02_differenziale_e_derivate/                  # Derivate parziali/direzionali, differenziale, piano tangente, Schwarz, Taylor
│   │   └── main.tex
│   ├── 03_funzioni_implicite/                        # Teorema del Dini, retta/piano tangente a insiemi di livello, inversione locale
│   │   └── main.tex
│   ├── 04_minimi_e_massimi/                          # Ottimizzazione libera/vincolata, Hessiana, Moltiplicatori di Lagrange
│   │   └── main.tex
│   ├── 05_curve_e_integrali_curvilinei/              # Curve regolari, lunghezza, integrali di I e II specie
│   │   └── main.tex
│   ├── 06_calcolo_vettoriale_e_forme_differenziali/  # Gradiente, divergenza, rotore, campi conservativi, forme esatte e chiuse
│   │   └── main.tex
│   ├── 07_integrali_multipli/                        # Integrali doppi e tripli, cambio coordinate (polari, cilindriche, sferiche)
│   │   └── main.tex
│   ├── 08_superfici_e_integrali_di_superficie/       # Superfici parametriche, piano tangente, area, flusso di campi vettoriali
│   │   └── main.tex
│   ├── 09_teoremi_integrali_calcolo_vettoriale/      # Gauss-Green, Teorema della Divergenza (Gauss), Teorema del Rotore (Stokes)
│   │   └── main.tex
│   └── 10_raccolta_esami_risolti/                    # Temi d'esame e quesiti d'orale svolti passo-passo
│       └── main.tex
│
├── exams/                                            # Archivio temi d'esame ufficiali con soluzioni per anno (2020-2023)
│   ├── 2020/
│   ├── 2021/
│   ├── 2022/
│   ├── 2023/
│   └── README.md
│
├── figures/                                          # Grafici TikZ, immagini vettoriali o plot 3D PGFPlots
├── sources/                                          # Materiale sorgente e dispense
└── scans/                                            # Scansioni PDF degli appunti cartacei
```

---

## ⚡ Flessibilità: Aggiungere o Rimuovere Capitoli

1. **Aggiungere o riordinare un capitolo**:
   - Creare una nuova cartella sotto `chapters/`, es. `chapters/11_serie_di_fourier/main.tex`.
   - Aggiungere la riga `\include{chapters/11_serie_di_fourier/main}` in `main.tex`.

2. **Compilazione rapida di un solo capitolo**:
   - Nel file `main.tex`, basta scommentare `\includeonly{...}` e specificare solo il capitolo su cui stai lavorando (es. `chapters/04_minimi_e_massimi/main`). La compilazione richiederà solo una frazione di secondo preservando numeri di pagina e riferimenti incrociati.

---

## 🎨 Ambienti Visivi Disponibili

Nel testo sono preconfigurati i seguenti ambienti stilizzati con `tcolorbox`:
- `\begin{definizione}{Titolo}{label}`: Box blu per definizioni rigorose.
- `\begin{teorema}{Titolo}{label}`: Box verde smeraldo per teoremi con ipotesi e tesi.
- `\begin{proposizione}{Titolo}{label}` / `\begin{corollario}{Titolo}{label}`: Box blu chiaro per proposizioni.
- `\begin{dimostrazione}`: Ambiente formale con quadratino di fine prova $\blacksquare$.
- `\begin{esempio}{Titolo}{label}`: Box violetto per esempi completi ed esercizi guidati.
- `\begin{osservazione}[Titolo]`: Box grigio/blu per note teoriche e chiarimenti concettuali.
- `\begin{esame}[Titolo]`: Box rosso/bordeaux per errori comuni, trabocchetti e consigli d'esame.
- `\begin{metodo}[Titolo]`: Box ambra/arancio per algoritmi risolutivi step-by-step.

---

## 🔨 Come Compilare

Dal terminale all'interno della cartella `ANALISI2`:
```bash
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```
oppure con `latexmk`:
```bash
latexmk -pdf main.tex
```

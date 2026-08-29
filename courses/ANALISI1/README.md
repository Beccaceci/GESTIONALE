# Appunti di Analisi Matematica 1 - Struttura del Progetto LaTeX

Questo progetto è strutturato in modo **modulare, flessibile ed estensibile** per digitalizzare, ricostruire con rigore e arricchire gli appunti del corso di Analisi Matematica 1.

---

## 📁 Architettura delle Cartelle

```text
ANALISI1/
│
├── main.tex                         # Master document: include configurazioni e capitoli
├── main.pdf                         # PDF compilato finale
│
├── config/                          # Configurazioni globali e stile
│   ├── packages.tex                 # Caricamento pacchetti (AMS, TikZ, tcolorbox, ecc.)
│   ├── environments.tex             # Box personalizzati (Definizioni, Teoremi, Esempi, Esame)
│   └── macros.tex                   # Scorciatoie e comandi matematici personalizzati
│
├── chapters/                        # Cartelle modulari per ciascun capitolo
│   ├── 01_insiemi_funzioni/         # Insiemi, funzioni e trasformazioni dei grafici
│   │   └── main.tex
│   ├── 02_trigonometria/            # Nozioni di base di trigonometria e formule
│   │   └── main.tex
│   ├── 03_limiti_continuita/        # Limiti, continuità e teoremi globali
│   │   └── main.tex
│   ├── 04_calcolo_differenziale/    # Derivate, teoremi differenziali e studio di funzione
│   │   └── main.tex
│   ├── 05_taylor_sviluppi/          # Taylor, McLaurin, o-piccolo e calcolo dei limiti
│   │   └── main.tex
│   ├── 06_analisi_astratta/         # Spazi metrici, topologia della retta reale, completezza
│   │   └── main.tex
│   ├── 07_calcolo_integrale/        # Integrali di Riemann, Torricelli-Barrow, impropri
│   │   └── main.tex
│   └── 08_equazioni_differenziali/  # ODE variabili separabili, 1° ordine, 2° ordine costanti
│       └── main.tex
│
├── figures/                         # Grafici TikZ, immagini vettoriali o plot PGFPlots
└── scans/                           # Scansioni PDF degli appunti cartacei
```

---

## ⚡ Flessibilità: Aggiungere o Rimuovere Capitoli

1. **Aggiungere un nuovo capitolo**:
   - Creare una nuova cartella sotto `chapters/`, es. `chapters/09_successioni_serie/main.tex`.
   - Aggiungere una riga `\include{chapters/09_successioni_serie/main}` all'interno di `main.tex`.

2. **Compilazione rapida di un solo capitolo**:
   - Nel file `main.tex`, basta scommentare `\includeonly{...}` e specificare solo il capitolo su cui stai lavorando (es. `chapters/03_limiti_continuita/main`). La compilazione richiederà solo una frazione di secondo preservando numeri di pagina e riferimenti incrociati.

---

## 🎨 Ambienti Visivi Disponibili

Nel testo sono preconfigurati i seguenti ambienti stilizzati con `tcolorbox`:
- `\begin{definizione}{Titolo}{label}`: Box azzurro/blu per definizioni rigorose.
- `\begin{teorema}{Titolo}{label}`: Box verde smeraldo per teoremi con ipotesi e tesi.
- `\begin{proposizione}{Titolo}{label}` / `\begin{corollario}{Titolo}{label}`: Box blu per proposizioni.
- `\begin{dimostrazione}`: Ambiente formale con quadratino di fine prova $\blacksquare$.
- `\begin{esempio}{Titolo}{label}`: Box violetto per esempi completi ed esercizi guidati.
- `\begin{osservazione}[Titolo]`: Box grigio/blu per note teoriche e chiarimenti concettuali.
- `\begin{esame}[Titolo]`: Box rosso/bordeaux per errori comuni, trabocchetti e consigli d'esame.
- `\begin{metodo}[Titolo]`: Box ambra/arancio per algoritmi risolutivi step-by-step.

---

## 🔨 Come Compilare

Dal terminale all'interno della cartella `ANALISI1`:
```bash
pdflatex -interaction=nonstopmode main.tex
```
oppure con `latexmk`:
```bash
latexmk -pdf main.tex
```

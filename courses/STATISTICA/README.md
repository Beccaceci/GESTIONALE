# Statistica e Calcolo delle Probabilità - Appunti di Studio

Raccolta modulare, formalizzata e digitalizzata degli appunti del corso di **Statistica e Calcolo delle Probabilità** (Ingegneria Gestionale).

---

## 📁 Struttura del Progetto

```
STATISTICA/
├── config/
│   ├── packages.tex          # Pacchetti tipografici, matematici e grafici
│   ├── environments.tex      # Box tematici tcolorbox (Definizioni, Teoremi, Esame, Metodi, ecc.)
│   └── macros.tex            # Notazioni e operatori per Statistica e Probabilità
├── figures/                  # Grafici TikZ, diagrammi e illustrazioni
├── sources/                  # Scansioni PDF originali e appunti manoscritti
├── chapters/
│   ├── 01_statistica_descrittiva/
│   ├── 02_elementi_di_probabilita/
│   ├── 03_indipendenza_e_probabilita_condizionata/
│   ├── 04_variabili_aleatorie/
│   ├── 05_valore_atteso_e_varianza/
│   ├── 06_somma_variabili_indipendenti/
│   ├── 07_classi_di_leggi_discrete/
│   ├── 08_classi_di_leggi_continue/
│   ├── 09_campione_statistico_e_stimatori/
│   ├── 10_intervalli_di_confidenza/
│   ├── 11_test_statistici/
│   └── 12_raccolta_esami_risolti/
├── main.tex                  # File master (Frontespizio, ToC, \include dei capitoli)
└── README.md                 # Questo documento
```

---

## 🛠️ Compilazione

### Compilazione completa
Per generare il documento PDF completo con indice e riferimenti incrociati:
```bash
pdflatex -interaction=nonstopmode main.tex && pdflatex -interaction=nonstopmode main.tex
```
oppure con `latexmk`:
```bash
latexmk -pdf main.tex
```

### Compilazione selettiva di singoli capitoli
Nel file `main.tex`, de-commentare il comando `\includeonly{...}` specificando solo i capitoli su cui si sta lavorando per velocizzare la compilazione:
```latex
\includeonly{
  chapters/01_statistica_descrittiva/main
}
```

---

## 🔄 Flessibilità nell'aggiunta / riorganizzazione dei capitoli
Per aggiungere un nuovo capitolo (ad esempio `chapters/13_processi_stocastici`):
1. Creare la cartella `chapters/13_processi_stocastici/` e il file `main.tex` al suo interno.
2. Inserire `\include{chapters/13_processi_stocastici/main}` nel file `main.tex`.

---

## 📋 Standard di Digitalizzazione e Box Tematici

Gli appunti utilizzano ambienti stilizzati dedicati:
- `\begin{definizione}{Titolo}{label}`: Definizioni formali rigorose con quantificatori.
- `\begin{teorema}{Titolo}{label}`: Teoremi, proposizioni e lemmi con dimostrazione.
- `\begin{proprieta}{Titolo}{label}`: Proprietà operative e caratteristiche notevoli.
- `\begin{esempio}{Titolo}{label}` / `\begin{esercizio}{Titolo}{label}`: Esempi numerici ed esercizi guidati.
- `\begin{dimostrazione}`: Dimostrazioni step-by-step con simbolo di chiusura $\blacksquare$.
- `\begin{metodo}[Titolo]`: Algoritmi operativi e schemi di risoluzione standard.
- `\begin{esame}[Attenzione / Consiglio Esame]`: Segnalazione di tranelli e controesempi frequenti.
- `\begin{osservazione}[Titolo]`: Note teoriche e commenti a margine.

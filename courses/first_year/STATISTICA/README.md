# Statistica e Calcolo delle Probabilità - Appunti di Studio e Archivio Esami
**Corso di Laurea in Ingegneria Gestionale — Università di Pisa**

Raccolta modulare, formalizzata e digitalizzata degli appunti completi e dell'archivio storico delle prove d'esame del corso di **Statistica e Calcolo delle Probabilità** (Prof. Andrea Agazzi).

---

## 📁 Struttura del Progetto

```
STATISTICA/
├── config/
│   ├── packages.tex          # Pacchetti tipografici, matematici e grafici
│   ├── environments.tex      # Box tematici tcolorbox (Definizioni, Teoremi, Esame, Metodi, ecc.)
│   └── macros.tex            # Notazioni e operatori per Statistica e Probabilità
├── figures/                  # Grafici vettoriali TikZ, diagrammi e illustrazioni
├── sources/                  # Scansioni PDF originali, appunti manoscritti e materiale docente
├── exams/                    # Archivio storico completo delle prove scritte ed eserciziari
│   ├── 2024/                 # Appelli 2024 con soluzioni analitiche e codice R
│   ├── 2023/                 # Appelli 2023 con soluzioni ufficiali
│   ├── 2022/                 # Appelli 2022, pre-test e straordinari con soluzioni
│   ├── 2021/                 # Appelli 2021 con soluzioni analitiche
│   ├── 2020/                 # Appelli 2020 con soluzioni analitiche
│   ├── fogli_esercizi/       # Fogli di esercizi settimanali 1–10 con soluzioni del docente
│   └── README.md             # Indice dettagliato con collegamenti ai PDF
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
│   ├── 12_raccolta_temi_esame/
│   └── 13_archivio_esami_risolti/
├── main.tex                  # File master (Frontespizio, ToC, \include dei capitoli)
├── main.pdf                  # Trattato completo compilato (101 pagine)
└── README.md                 # Questo documento
```

---

## 🛠️ Compilazione

### Compilazione completa del volume
Per generare il documento PDF completo con indice e riferimenti incrociati:
```bash
pdflatex -interaction=nonstopmode main.tex && pdflatex -interaction=nonstopmode main.tex
```

---

## 📋 Standard di Digitalizzazione e Box Tematici

Gli appunti utilizzano ambienti stilizzati dedicati:
- `\begin{definizione}{Titolo}{label}`: Definizioni formali rigorose con quantificatori.
- `\begin{teorema}{Titolo}{label}`: Teoremi, proposizioni e lemmi con dimostrazione.
- `\begin{proprieta}{Titolo}{label}`: Proprietà operative e caratteristiche notevoli.
- `\begin{esercizio}{Titolo}{label}`: Esempi numerici ed esercizi guidati.
- `\begin{dimostrazione}`: Dimostrazioni step-by-step con simbolo di chiusura $\blacksquare$.
- `\begin{metodo}[Titolo]`: Algoritmi operativi e schemi di risoluzione standard.
- `\begin{esame}[Attenzione / Consiglio Esame]`: Segnalazione di tranelli e controesempi frequenti.
- `\begin{osservazione}[Titolo]`: Note teoriche e commenti a margine.

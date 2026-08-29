# Corso di Fisica Generale I — Appunti Digitali e Codice LaTeX

Progetto modulare per la digitalizzazione, la formalizzazione teorica e la produzione del manuale completo in PDF per l'insegnamento di **Fisica Generale 1** (Meccanica, Oscillazioni, Dinamica dei Fluidi e Termodinamica), Corso di Laurea in Ingegneria Gestionale.

---

## 🏛️ Architettura delle Cartelle del Progetto

```
FISICA/
├── config/                                # Moduli di configurazione globale LaTeX
│   ├── packages.tex                       # Pacchetti matematici, fisici, grafici e layout
│   ├── environments.tex                   # Ambienti tcolorbox (definizioni, teoremi, esami, metodi)
│   └── macros.tex                         # Macro vettoriali, differenziali, costanti e simboli
├── chapters/                              # Capitoli modulari suddivisi nelle 4 Macro-Aree
│   ├── 01_introduzione_vettori/           # Cap. 01: Grandezze, SI, analisi dimensionale, vettori
│   ├── 02_cinematica_punto/               # Cap. 02: Cinematica 1D, 2D, curvilinea, polari
│   ├── 03_dinamica_punto/                 # Cap. 03: Principi di Newton, forze, vincoli, attrito
│   ├── 04_sistemi_non_inerziali/          # Cap. 04: Moti relativi, forze apparenti, Coriolis
│   ├── 05_lavoro_energia/                 # Cap. 05: Lavoro, energia cinetica, potenziale, conservazione
│   ├── 06_sistemi_punti_urti/             # Cap. 06: Sistemi di punti, centro di massa, urti
│   ├── 07_momento_angolare_rotazione/     # Cap. 07: Momento angolare, momento meccanico, rotazioni
│   ├── 08_dinamica_statica_corpo_rigido/  # Cap. 08: Corpo rigido, inerzia, Huygens-Steiner, rotolamento
│   ├── 09_gravitazione_forze_centrali/    # Cap. 09: Gravitazione universale, Keplero, orbite
│   ├── 10_oscillazioni_onde/              # Cap. 10: Moto armonico, smorzato, risonanza, onde
│   ├── 11_meccanica_fluidi/               # Cap. 11: Idrostatica (Stevino, Archimede) e idrodinamica (Bernoulli)
│   ├── 12_termodinamica_fondamenti/       # Cap. 12: Temperatura, principio zero, calore, calorimetria
│   ├── 13_gas_ideali_teoria_cinetica/     # Cap. 13: Gas perfetti, modello cinetico, equipartizione
│   ├── 14_primo_principio_trasformazioni/ # Cap. 14: Lavoro PV, primo principio, adiabatiche di Poisson
│   └── 15_secondo_principio_entropia/     # Cap. 15: Secondo principio, Carnot, Clausius, entropia, Boltzmann
├── figures/                               # Grafici vettoriali TikZ / Pgfplots
├── scans/                                 # Repository per le scansioni degli appunti manoscritti
├── trascrizioni/                          # 40 trascrizioni complete estratte da MacWhisper
│   ├── README.md                          # Indice generale delle trascrizioni con sommario tematico
│   ├── Lezione_01_...md                   # Lezione 01 con timestamp e metadati
│   └── ...                                # da Lezione 02 a Lezione 40
├── main.tex                               # Documento principale (Book)
└── main.pdf                               # Manuale PDF compilato
```

---

## 📚 Mappatura tra le 4 Macro-Aree e i 15 Capitoli

### Macro-Area 1: Introduzione, Cinematica e Dinamica del Punto Materiale
- **Capitolo 1**: [Introduzione alla Fisica, Grandezze e Calcolo Vettoriale](file:///Users/nicolabeccaceci/Documents/GEST/FISICA/chapters/01_introduzione_vettori/main.tex)
- **Capitolo 2**: [Cinematica del Punto Materiale in 1D, 2D e 3D](file:///Users/nicolabeccaceci/Documents/GEST/FISICA/chapters/02_cinematica_punto/main.tex)
- **Capitolo 3**: [Dinamica del Punto Materiale e Principi di Newton](file:///Users/nicolabeccaceci/Documents/GEST/FISICA/chapters/03_dinamica_punto/main.tex)
- **Capitolo 4**: [Moti Relativi e Sistemi di Riferimento Non Inerziali](file:///Users/nicolabeccaceci/Documents/GEST/FISICA/chapters/04_sistemi_non_inerziali/main.tex)

### Macro-Area 2: Leggi di Conservazione, Urti e Moto del Corpo Rigido
- **Capitolo 5**: [Lavoro, Energia, Forze Conservative e Conservazione](file:///Users/nicolabeccaceci/Documents/GEST/FISICA/chapters/05_lavoro_energia/main.tex)
- **Capitolo 6**: [Dinamica dei Sistemi di Punti Materiali e Urti](file:///Users/nicolabeccaceci/Documents/GEST/FISICA/chapters/06_sistemi_punti_urti/main.tex)
- **Capitolo 7**: [Momento Angolare, Momento della Forza e Rotazioni](file:///Users/nicolabeccaceci/Documents/GEST/FISICA/chapters/07_momento_angolare_rotazione/main.tex)
- **Capitolo 8**: [Statica e Dinamica del Corpo Rigido](file:///Users/nicolabeccaceci/Documents/GEST/FISICA/chapters/08_dinamica_statica_corpo_rigido/main.tex)

### Macro-Area 3: Gravitazione e Meccanica dei Fluidi (con Oscillazioni)
- **Capitolo 9**: [Gravitazione Universale e Dinamica Planetaria](file:///Users/nicolabeccaceci/Documents/GEST/FISICA/chapters/09_gravitazione_forze_centrali/main.tex)
- **Capitolo 10**: [Oscillazioni Meccaniche, Risonanza e Fenomeni Ondulatori](file:///Users/nicolabeccaceci/Documents/GEST/FISICA/chapters/10_oscillazioni_onde/main.tex)
- **Capitolo 11**: [Meccanica dei Fluidi: Statica e Dinamica](file:///Users/nicolabeccaceci/Documents/GEST/FISICA/chapters/11_meccanica_fluidi/main.tex)

### Macro-Area 4: Termodinamica
- **Capitolo 12**: [Fondamenti di Termodinamica, Temperatura e Calore](file:///Users/nicolabeccaceci/Documents/GEST/FISICA/chapters/12_termodinamica_fondamenti/main.tex)
- **Capitolo 13**: [Gas Perfetti e Teoria Cinetica Molecolare](file:///Users/nicolabeccaceci/Documents/GEST/FISICA/chapters/13_gas_ideali_teoria_cinetica/main.tex)
- **Capitolo 14**: [Lavoro Termodinamico e Primo Principio della Termodinamica](file:///Users/nicolabeccaceci/Documents/GEST/FISICA/chapters/14_primo_principio_trasformazioni/main.tex)
- **Capitolo 15**: [Secondo Principio della Termodinamica, Ciclo di Carnot ed Entropia](file:///Users/nicolabeccaceci/Documents/GEST/FISICA/chapters/15_secondo_principio_entropia/main.tex)

---

## 🛠️ Istruzioni di Compilazione

### 1. Compilazione dell'intero volume
Dalla cartella `FISICA/`:
```bash
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```
oppure con `latexmk`:
```bash
latexmk -pdf main.tex
```

### 2. Compilazione rapida di singoli capitoli (`\includeonly`)
Nel file [`main.tex`](file:///Users/nicolabeccaceci/Documents/GEST/FISICA/main.tex), scommentare il blocco `\includeonly{...}` specificando solo il capitolo su cui si sta lavorando per velocizzare la build:
```latex
\includeonly{
  chapters/03_dinamica_punto/main
}
```

---

## 🎨 Box Tematici e Notazione Adottata

| Ambiente | Colore Bordo/Titolo | Utilizzo Principale |
|---|---|---|
| `\begin{definizione}{Nome}{label}` | **Navy Blue** | Grandezze fisiche, coordinate e concetti operativi |
| `\begin{legge}{Nome}{label}` | **Purple Accent** | Principi di Newton, primo e secondo principio termodinamica |
| `\begin{teorema}{Nome}{label}` | **Forest Green** | Teoremi cardine (forze vive, conservazione, Carnot, Bernoulli) |
| `\begin{dimostrazione}` | **Verde barra sx** | Dimostrazioni passo-passo con simbolo finale $\blacksquare$ |
| `\begin{metodo}{Titolo}` | **Warm Amber** | Algoritmi procedurali step-by-step per problemi d'esame |
| `\begin{esame}{Titolo}` | **Crimson Red** | Errori concettuali comuni, tranelli e suggerimenti d'esame |
| `\begin{esercizio}{Titolo}` | **Amber** | Esercizi guidati completi con calcoli espliciti |
| `\begin{esperimento}{Titolo}` | **Dark Cyan** | Fenomenologia sperimentale ed evidenze fisiche |
| `\begin{osservazione}` | **Slate Gray** | Note teoriche e limiti di validità dei modelli |

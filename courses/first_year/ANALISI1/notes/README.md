# 📘 Appunti Digitalizzati di Analisi Matematica I — Manuale Completo in LaTeX
**Corso di Laurea in Ingegneria Gestionale — Università di Pisa**

[![LaTeX Typeset](https://img.shields.io/badge/LaTeX-Typeset_Book-008080?style=flat&logo=latex&logoColor=white)](https://www.latex-project.org/)
[![Pagine](https://img.shields.io/badge/Volume-96_Pagine-orange.svg)](#)
[![1-Click PDF Download](https://img.shields.io/badge/Download_PDF-appuntiAnalisi1.pdf-0052cc?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](https://github.com/Beccaceci/GESTIONALE/raw/main/courses/first_year/ANALISI1/notes/appuntiAnalisi1.pdf)

Questo repository contiene l'infrastruttura completa e modulare in \LaTeX{} per la digitalizzazione, la formalizzazione teorica e l'approfondimento rigoroso del corso di **Analisi Matematica I** (SSD MAT/05, 12 CFU) per il Corso di Laurea in Ingegneria Gestionale dell'Università di Pisa.

---

## 📥 Download Diretto del Manuale Compilato (1-Click)

È possibile scaricare il trattato completo ad altissima definizione direttamente dal link sottostante:

> 📄 **[Download `appuntiAnalisi1.pdf`](https://github.com/Beccaceci/GESTIONALE/raw/main/courses/first_year/ANALISI1/notes/appuntiAnalisi1.pdf)**

---

## 🏛️ Architettura Modulare del Progetto

Il progetto adotta una struttura a moduli indipendenti:

```text
ANALISI1/notes/
├── config/                                           # Configurazioni globali e preambolo LaTeX
│   ├── packages.tex                                  # Pacchetti (amsmath, amssymb, tikz, pgfplots, tcolorbox, booktabs)
│   ├── environments.tex                              # Box tematici personalizzati (Definizione, Teorema, Metodo, Esame)
│   └── macros.tex                                    # Macro e scorciatoie per limiti, derivate, integrali, ODE, Landau
├── chapters/                                         # Moduli indipendenti dei singoli capitoli
│   ├── 01_insiemi_funzioni/                          # Insiemi numerici, Dedekind, funzioni, grafici deducibili, coordinate polari
│   │   └── main.tex
│   ├── 02_trigonometria/                             # Circonferenza goniometrica, formule analitiche, funzioni iperboliche
│   │   └── main.tex
│   ├── 03_limiti_continuita/                         # Topologia di R, definizione ε-δ, limiti notevoli, Weierstrass, Zeri
│   │   └── main.tex
│   ├── 04_calcolo_differenziale/                     # Derivate, punti singolari, Rolle, Lagrange, Cauchy, de L'Hôpital, studio di funzione
│   │   └── main.tex
│   ├── 05_taylor_sviluppi/                           # Simboli di Landau, formula di Taylor (Peano e Lagrange), sviluppi notevoli
│   │   └── main.tex
│   ├── 06_analisi_astratta/                          # Spazi metrici, intorni, compattezza, Bolzano-Weierstrass, completezza
│   │   └── main.tex
│   ├── 07_calcolo_integrale/                         # Somme di Riemann, Torricelli-Barrow, tecniche di integrazione, integrali impropri
│   │   └── main.tex
│   ├── 08_equazioni_differenziali/                   # Problema di Cauchy, Cauchy-Lipschitz, ODE a variabili separabili, lineari I e II ordine
│   │   └── main.tex
│   └── 09_raccolta_esami_risolti/                    # Problemi d'esame risolti con guida metodologica passo-passo
│       └── main.tex
├── figures/                                          # Grafici vettoriali TikZ, plot PGFPlots e diagrammi geometrici
├── appuntiAnalisi1.pdf                               # Trattato completo compilato in PDF ad alta risoluzione (96 pag.)
├── main.tex                                          # Documento radice master (Frontespizio, ToC, inclusioni capitoli)
└── README.md                                         # Questo documento di guida e documentazione
```

---

## 📚 Indice Dettagliato dei Capitoli e Mappa Concettuale

### Capitolo 1: Insiemi, Funzioni e Grafici
- **Insiemi Numerici e Struttura di $\mathbb{R}$:** Assiomatica dei numeri reali, proprietà di campo ordinato, assioma di completezza (Dedekind), estremo superiore ($\sup$) ed estremo inferiore ($\inf$), massimi e minimi.
- **Funzioni Reali di Variabile Reale:** Dominio, codominio, immagine, iniettività, suriettività, biiettività e funzione inversa, monotonia stretta e debole, parità e periodicità.
- **Algebra delle Trasformazioni Geometriche:** Traslazioni cartesiane, dilatazioni e contrazioni, ribaltamenti e valore assoluto applicati ai grafici elementari.
- **Sistemi di Coordinate:** Coordinate cartesiane e coordinate polari nel piano reale.

### Capitolo 2: Nozioni di Base di Trigonometria e Funzioni Goniometriche
- **La Circonferenza Goniometrica:** Definizioni geometriche di seno, coseno, tangente e cotangente, identità fondamentale $\sin^2 x + \cos^2 x = 1$.
- **Archi Associati e Formulario Analitico:** Formule di addizione e sottrazione, duplicazione, bisezione, prostaferesi e formule parametriche razionali con $t = \tan(x/2)$.
- **Funzioni Inverse e Iperboliche:** Dominio e grafici di $\arcsin x, \arccos x, \arctan x$; definizione analitica delle funzioni iperboliche $\sinh x, \cosh x, \tanh x$ e relative identità notevoli.

### Capitolo 3: Limiti e Continuità
- **Topologia della Retta Reale:** Intorni sferici, aperti e chiusi, punti interni, punti di frontiera, punti isolati e punti di accumulazione.
- **Definizione Formale di Limite:** Definizione metrica $\varepsilon$-$\delta$ per limiti finiti e infiniti al finito e all'infinito, unicità del limite, permanenza del segno.
- **Teoremi di Confronto e Limiti Notevoli:** Teorema dei Carabinieri, algebra delle forme indeterminate, dimostrazione geometrica dei limiti notevoli trigonometrici ed esponenziali:
  $$\lim_{x\to 0}\frac{\sin x}{x} = 1, \qquad \lim_{x\to 0}\frac{e^x - 1}{x} = 1, \qquad \lim_{x\to 0}\frac{\ln(1+x)}{x} = 1$$
- **Continuità e Teoremi Globali:** Continuità puntuale e su intervalli, classificazione delle discontinuità (eliminabile, salto di I specie, essenziale di II specie), **Teorema di Weierstrass** (esistenza di massimi e minimi su compatti), **Teorema degli Zeri** e **Teorema dei Valori Intermedi**.

### Capitolo 4: Calcolo Differenziale e Studio di Funzione
- **Derivabilità e Retta Tangente:** Rapporto incrementale, definizione di derivata prima $f'(x_0)$, significato geometrico della retta tangente e legame tra derivabilità e continuità.
- **Punti di Non Derivabilità:** Punti angolosi, cuspidi e flessi a tangente verticale.
- **Algebra delle Derivate:** Regole per somma, prodotto (Leibniz), quoziente, derivata della funzione composta (chain rule) e derivata della funzione inversa.
- **Teoremi Fondamentali del Calcolo Differenziale:** **Teorema di Fermat** sui punti stazionari interni, **Teorema di Rolle**, **Teorema del Valor Medio di Lagrange** e relative conseguenze sulla monotonia, **Teorema di Cauchy** e **Teorema di de L'Hôpital** per le forme indeterminate $[0/0]$ e $[\infty/\infty]$.
- **Derivata Seconda e Studio Qualitativo:** Convessità e concavità analitica, punti di flesso, asintoti orizzontali, verticali e obliqui, e schema operativo per lo studio di funzione.

### Capitolo 5: Sviluppi di Taylor, Parti Principali e Limiti
- **Simboli di Landau e Calcolo Asintotico:** Definizione formale di $o$-piccolo, $\mathcal{O}$-grande e relazione di equivalenza asintotica ($\sim$), algebra degli infinitesimi.
- **Formula di Taylor:** Polinomio osculatore, formula di Taylor con **resto di Peano** e con **resto di Lagrange**.
- **Tavola degli Sviluppi di Maclaurin Notevoli:** Sviluppi completi con termine generale di $e^x, \sin x, \cos x, \ln(1+x), (1+x)^\alpha, \tan x, \arctan x, \sinh x, \cosh x$.
- **Calcolo dei Limiti Indeterminati:** Principio di cancellazione, arresto dello sviluppo all'ordine minimo utile e risoluzione di limiti algebricamente complessi.

### Capitolo 6: Elementi di Analisi Matematica Astratta
- **Spazi Metrici:** Definizione assiomatica di metrica, disuguaglianza triangolare e spazi euclidei.
- **Topologia Generale:** Palle aperte e chiuse, insiemi aperti, chiusi, limitati, chiusura e derivato.
- **Compattezza e Completezza:** Compattezza per successioni, Teorema di Bolzano-Weierstrass, successioni di Cauchy e completezza metrica.

### Capitolo 7: Calcolo Integrale
- **Costruzione dell'Integrale di Riemann:** Suddivisioni, somme inferiori e superiori di Darboux, integrabilità delle funzioni continue e monotone, proprietà di linearità e additività.
- **Teoremi Fondamentali:** Teorema della Media Integrale, funzione integrale $F(x)$, **Teorema Fondamentale del Calcolo Integrale (Torricelli-Barrow)** e formula fondamentale:
  $$\int_a^b f(x)\,dx = G(b) - G(a)$$
- **Tecniche di Integrazione:** Integrazione per parti, integrazione per sostituzione (diretta e inversa), integrazione delle funzioni razionali fratte (decomposizione in fratti semplici).
- **Integrali Impropri:** Integrazione su semirette $[a, +\infty)$ e per funzioni non limitate, criteri di convergenza del confronto e del confronto asintotico, integrali notevoli del tipo $\int_1^{+\infty}\frac{1}{x^p}\,dx$ e $\int_0^1 \frac{1}{x^p}\,dx$.

### Capitolo 8: Equazioni Differenziali Ordinarie (ODE)
- **Problema di Cauchy:** Definizione di equazione differenziale ordinaria, ordine, soluzione generale e particolare, formulazione del problema di Cauchy e Teorema di Cauchy-Lipschitz di esistenza e unicità.
- **ODE a Variabili Separabili:** Metodo risolutivo analitico, studio qualitativo delle soluzioni costanti (stazionarie), determinazione dell'intervallo massimale di esistenza e fenomeno del blow-up in tempo finito.
- **ODE Lineari del Primo Ordine:** Metodo del fattore integrante e formula risolutiva esplicita.
- **ODE Lineari del Secondo Ordine a Coefficienti Costanti:** Equazione omogenea associata e radici del polinomio caratteristico (reali distinte, reali coincidenti, complesse coniugate); equazione completa con metodo di somiglianza e principio di sovrapposizione.

### Capitolo 9: Raccolta Tematica di Esami Risolti
- Svolgimenti completi e commentati di quesiti di Parte A e problemi di Parte B (limiti di Taylor, studi di funzione completi, integrali impropri e problemi di Cauchy) tratti dalle prove d'esame ufficiali.

---

## 🎨 Ambienti Tipografici e Box Tematici (`tcolorbox`)

| Ambiente | Colore Bordo / Titolo | Finalità Didattica |
| :--- | :--- | :--- |
| `\begin{definizione}{Nome}{label}` | **Navy Blue** (`#003366`) | Definizioni formali rigorose con quantificatori matematici |
| `\begin{teorema}{Nome}{label}` | **Forest Green** (`#2E7D32`) | Enunciati completi di teoremi con evidenziazione di ipotesi e tesi |
| `\begin{proposizione}{Nome}{label}` | **Teal Blue** (`#00838F`) | Proposizioni e proprietà analitiche intermedie |
| `\begin{corollario}{Nome}{label}` | **Cyan** (`#0097A7`) | Corollari e deduzioni dirette dai teoremi |
| `\begin{dimostrazione}` | **Verde barra sinistra** | Dimostrazioni analitiche rigorose chiuse da $\blacksquare$ |
| `\begin{metodo}[Titolo]` | **Warm Amber** (`#FF8F00`) | Algoritmi risolutivi procedurali (es. studio di funzione, Taylor) |
| `\begin{esame}[Titolo]` | **Crimson Red** (`#C62828`) | Consigli d'esame, errori comuni e tranelli tipici |
| `\begin{esempio}{Nome}{label}` | **Deep Purple** (`#6A1B9A`) | Esempi numerici svolti ed esercizi guidati |
| `\begin{osservazione}[Titolo]` | **Steel Blue** (`#37474F`) | Note teoriche a margine e chiarimenti intuitivi |

---

## 🛠️ Istruzioni per la Compilazione Locale

### 1. Compilazione Completa del Volume
Per compilare l'intero trattato e generare `appuntiAnalisi1.pdf`:

```bash
# Tramite latexmk (consigliato, gestisce automaticamente ToC e riferimenti incrociati):
latexmk -pdf main.tex

# Oppure tramite pdflatex (eseguire due volte per allineare la numerazione delle pagine):
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```

### 2. Compilazione Rapida di Singoli Capitoli (`\includeonly`)
Nel file [`main.tex`](./main.tex), scommentare la direttiva `\includeonly{...}` specificando solo il capitolo di lavoro per una compilazione sub-secondo:

```latex
\includeonly{
  chapters/04_calcolo_differenziale/main
}
```

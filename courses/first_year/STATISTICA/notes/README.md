# 📘 Appunti Digitalizzati di Statistica e Calcolo delle Probabilità — Manuale Completo in LaTeX
**Corso di Laurea in Ingegneria Gestionale — Università di Pisa**

[![LaTeX Typeset](https://img.shields.io/badge/LaTeX-Typeset_Book-008080?style=flat&logo=latex&logoColor=white)](https://www.latex-project.org/)
[![Pagine](https://img.shields.io/badge/Volume-101_Pagine-orange.svg)](#)
[![1-Click PDF Download](https://img.shields.io/badge/Download_PDF-appuntiStatistica.pdf-0052cc?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](https://github.com/Beccaceci/GESTIONALE/raw/main/courses/first_year/STATISTICA/notes/appuntiStatistica.pdf)

Questo repository contiene l'infrastruttura completa e modulare in \LaTeX{} per la digitalizzazione, la formalizzazione teorica e l'approfondimento rigoroso del corso di **Statistica e Calcolo delle Probabilità** (SSD MAT/06, 6 CFU) per il Corso di Laurea in Ingegneria Gestionale dell'Università di Pisa.

---

## 📥 Download Diretto del Manuale Compilato (1-Click)

È possibile scaricare il trattato completo ad altissima definizione direttamente dal link sottostante:

> 📄 **[Download `appuntiStatistica.pdf`](https://github.com/Beccaceci/GESTIONALE/raw/main/courses/first_year/STATISTICA/notes/appuntiStatistica.pdf)**

---

## 🏛️ Architettura Modulare del Progetto

Il progetto adotta un'architettura modulare e disaccoppiata:

```text
STATISTICA/notes/
├── config/                                           # Configurazioni globali e stile tipografico LaTeX
│   ├── packages.tex                                  # Pacchetti (amsmath, amssymb, tikz, pgfplots, tcolorbox, booktabs)
│   ├── environments.tex                              # Box tematici stilizzati (Definizione, Teorema, Proprietà, Metodo, Esame)
│   └── macros.tex                                    # Macro e notazioni per probabilità, variabili aleatorie, inferenza e test
├── chapters/                                         # 13 Moduli tematici indipendenti
│   ├── 01_statistica_descrittiva/                    # Frequenze, indici di posizione e variabilità, regressione lineare
│   │   └── main.tex
│   ├── 02_elementi_di_probabilita/                   # Assiomatica di Kolmogorov, calcolo combinatorio, inclusion-exclusion
│   │   └── main.tex
│   ├── 03_indipendenza_e_probabilita_condizionata/   # Probabilità condizionata, Probabilità Totali, Teorema di Bayes
│   │   └── main.tex
│   ├── 04_variabili_aleatorie/                       # CDF, PMF discrete, PDF continue, quantili, vettori aleatori
│   │   └── main.tex
│   ├── 05_valore_atteso_e_varianza/                  # Speranza E[X], LOTUS, varianza, covarianza, Markov, Chebyshev
│   │   └── main.tex
│   ├── 06_somma_variabili_indipendenti/              # Integrale di convoluzione, MGF, Legge Grandi Numeri (LLN), CLT
│   │   └── main.tex
│   ├── 07_classi_di_leggi_discrete/                  # Bernoulli, Binomiale, Geometrica (memoryless), Poisson, Ipergeometrica
│   │   └── main.tex
│   ├── 08_classi_di_leggi_continue/                  # Uniforme, Esponenziale, Normale Gaussiana, Chi-quadro, Student, Fisher
│   │   └── main.tex
│   ├── 09_campione_statistico_e_stimatori/           # Campione i.i.d., stimatori, MSE, Metodo Momenti, MLE, Cramér-Rao
│   │   └── main.tex
│   ├── 10_intervalli_di_confidenza/                  # Quantità pivotali, intervalli per media, varianza e proporzioni
│   │   └── main.tex
│   ├── 11_test_statistici/                           # Verifica ipotesi, errori I/II tipo, potenza, p-value, Z/t-test, Chi-quadro
│   │   └── main.tex
│   ├── 12_raccolta_esami_risolti/                    # Temi d'esame risolti con guida metodologica passo-passo
│   │   └── main.tex
│   └── 13_archivio_esami_risolti/                    # Prove scritte d'appello recenti (2020-2024) ed eserciziari con codice R
│       └── main.tex
├── figures/                                          # Grafici vettoriali TikZ, curve gaussiane, distribuzioni e boxplot
├── appuntiStatistica.pdf                             # Trattato completo compilato in PDF ad alta risoluzione (101 pag.)
├── main.tex                                          # Documento master radice (Frontespizio, ToC, inclusioni)
└── README.md                                         # Questo documento di guida e documentazione
```

---

## 📚 Indice Dettagliato dei Capitoli e Mappa Concettuale

### Modulo I: Statistica Descrittiva e Calcolo delle Probabilità
- **Capitolo 1 — Statistica Descrittiva:** Scale di misura qualitative e quantitative (nominali, ordinali, ad intervalli, a rapporti); distribuzioni di frequenza assolute, relative, percentuali e cumulate; indici di posizione e tendenza centrale (media aritmetica, geometrica, armonica, mediana, moda e quantili); indici di variabilità e dispersione (campo di variazione, scarto interquartile IQR, varianza campionaria $s^2$, deviazione standard $s$, coefficiente di variazione CV); analisi bivariata, covarianza campionaria $s_{xy}$, coefficiente di correlazione di Pearson $r_{xy}$ e determinazione della retta di regressione lineare con il metodo dei minimi quadrati ordinari (OLS).
- **Capitolo 2 — Elementi di Teoria della Probabilità e Calcolo Combinatorio:** Spazio campionario $\Omega$ ed eventi aleatori; assiomatica di Kolmogorov; teoremi fondamentali (probabilità dell'evento complementare, monotonia, formula di inclusione-esclusione di Poincaré); calcolo combinatorio (disposizioni semplici e con ripetizione, permutazioni, combinazioni semplici e coefficiente binomiale).
- **Capitolo 3 — Probabilità Condizionata, Formula di Bayes e Indipendenza:** Definizione di probabilità condizionata $P(A|B) = \frac{P(A \cap B)}{P(B)}$; regola del prodotto stocastico; **Teorema delle Probabilità Totali** per una partizione di eventi; **Teorema di Bayes** e revisione a posteriori delle probabilità delle cause; indipendenza stocastica a coppie e globale.

### Modulo II: Variabili Aleatorie e Teoremi Limite
- **Capitolo 4 — Variabili Aleatorie Discrete, Continue e Vettori Aleatori:** Definizione di variabile aleatoria $X:\Omega \to \mathbb{R}$; Funzione di Ripartizione cumulativa (CDF) $F_X(x) = P(X \le x)$ e proprietà analitiche (monotonia, continuità da destra, asintoti); variabili discrete e Funzione di Massa (PMF) $p_X(x_k)$; variabili continue e Funzione di Densità di Probabilità (PDF) $f_X(x) = F_X'(x)$; quantili teorici; introduzione ai vettori aleatori $(X,Y)$, densità congiunte $f_{X,Y}(x,y)$, densità marginali e condizionate.
- **Capitolo 5 — Valore Atteso, Varianza, Covarianza e Disuguaglianze:** Valore atteso (speranza matematica) $\mathbb{E}[X]$ e proprietà di linearità; Teorema del Trasporto (LOTUS) per $Y = g(X)$; Varianza teorica $\operatorname{Var}(X) = \mathbb{E}[(X-\mu)^2] = \mathbb{E}[X^2] - (\mathbb{E}[X])^2$ e scarto quadratico medio $\sigma$; covarianza $\operatorname{Cov}(X,Y)$, correlazione $\rho_{XY}$, varianza di combinazioni lineari; disuguaglianze notevoli: **Disuguaglianza di Markov** per variabili non negative e **Disuguaglianza di Chebyshev** per il controllo della dispersione attorno alla media.
- **Capitolo 6 — Somma di Variabili Aleatorie, Convoluzione e Teoremi Limite:** Distribuzione della somma di variabili indipendenti tramite **integrale di convoluzione** $f_{X+Y}(z) = \int f_X(x)f_Y(z-x)\,dx$; Funzione Generatrice dei Momenti (MGF) $M_X(t) = \mathbb{E}[e^{tX}]$; **Legge Debole dei Grandi Numeri (LLN)**; enunciato e applicazioni operative del **Teorema del Limite Centrale (CLT)** per somme e medie campionarie standardizzate:
  $$\frac{S_n - n\mu}{\sigma\sqrt{n}} \xrightarrow{d} \mathcal{N}(0,1)$$

### Modulo III: Famiglie Notevoli di Distribuzioni
- **Capitolo 7 — Classi di Leggi di Probabilità Discrete:** Modelli parametrici con PMF, valore atteso, varianza e MGF per:
  - *Bernoulli* $\operatorname{Ber}(p)$;
  - *Binomiale* $\operatorname{Bin}(n,p)$ per il numero di successi su $n$ prove;
  - *Geometrica* $\operatorname{Geom}(p)$ con dimostrazione della proprietà di **assenza di memoria**;
  - *Ipergeometrica* $\operatorname{Hyg}(N, K, n)$ per estrazioni senza reinserimento;
  - *Poisson* $\operatorname{Poiss}(\lambda)$ per eventi rari su intervalli continui e limite della binomiale.
- **Capitolo 8 — Classi di Leggi di Probabilità Continue:** Modelli parametrici con PDF, CDF, parametri e quantili per:
  - *Uniforme Continua* $\mathcal{U}(a,b)$;
  - *Esponenziale* $\operatorname{Exp}(\lambda)$ (assenza di memoria nel continuo e legame con i tempi di interarrivo di Poisson);
  - *Normale Gaussiana* $\mathcal{N}(\mu, \sigma^2)$, standardizzazione $Z = (X-\mu)/\sigma$ e consultazione delle tavole della normale standard $\Phi(z)$;
  - *Distribuzioni Inferenziali:* $\chi^2_k$ (Chi-quadro), $t_k$ di Student e $F_{d_1, d_2}$ di Fisher-Snedecor.

### Modulo IV: Statistica Inferenziale — Stima Puntuale, Intervalli e Test d'Ipotesi
- **Capitolo 9 — Campione Statistico, Teoria della Stima Puntuale e Massima Verosimiglianza:** Campione casuale i.i.d., statistica campionaria e stimatore $T$; criteri di ottimalità: non-distorsione / correttezza ($E[T] = \theta$), varianza, Errore Quadratico Medio $\operatorname{MSE}(T) = \operatorname{Var}(T) + [B(T)]^2$, consistenza in probabilità; media campionaria $\bar{X}_n$ e varianza campionaria corretta $S^2$; **Metodo dei Momenti**; **Metodo della Massima Verosimiglianza (MLE)**, funzione di verosimiglianza $L(\theta)$ ed equazione di score; **Informazione di Fisher** $I_n(\theta)$ e **Limite Inferiore di Cramér-Rao (CRLB)** per la verifica di efficienza asintotica.
- **Capitolo 10 — Intervalli di Confidenza:** Metodo generale della quantità pivotale; intervallo per la media $\mu$ con varianza $\sigma^2$ nota ($Z$-pivot) e con varianza $\sigma^2$ incognita ($t$-pivot di Student con $n-1$ g.d.l.); intervallo di confidenza per la varianza $\sigma^2$ con pivot $\chi^2$; intervalli di confidenza asintotici per proporzioni campionarie bernoulliane $\hat{p}$.
- **Capitolo 11 — Verifica delle Ipotesi Statistiche (Test di Significatività):** Formulazione delle ipotesi $H_0$ e $H_1$; matrice degli errori decisionali: errore di I tipo $\alpha$ (livello di significatività) ed errore di II tipo $\beta$, potenza del test $1-\beta$; regioni di accettazione e di rifiuto; calcolo del **$p$-value**; **Lemma di Neyman-Pearson**; test per la media ($Z$-test e $t$-test); test non parametrici del $\chi^2$ (test di adattamento e test di indipendenza in tabelle di contingenza).
- **Capitolo 12 & 13 — Raccolta e Archivio Temi d'Esame Risolti:** Prove scritte d'esame complete dal 2020 al 2024 ed eserciziari settimanali svolti con procedimenti analitici rigorosi e verifiche computazionali in linguaggio R.

---

## 🎨 Ambienti Tipografici e Box Tematici (`tcolorbox`)

| Ambiente | Colore Bordo / Titolo | Finalità Didattica |
| :--- | :--- | :--- |
| `\begin{definizione}{Nome}{label}` | **Navy Blue** (`#003366`) | Definizioni formali di probabilità, distribuzioni e stimatori |
| `\begin{teorema}{Nome}{label}` | **Forest Green** (`#2E7D32`) | Grandi teoremi (Bayes, LLN, CLT, Cramér-Rao, Neyman-Pearson) |
| `\begin{proposizione}{Nome}{label}` | **Teal Blue** (`#00838F`) | Proposizioni e proprietà statistiche intermedie |
| `\begin{proprieta}{Nome}{label}` | **Sky Blue** (`#0288D1`) | Proprietà notevoli di distribuzioni, medie e varianze |
| `\begin{corollario}{Nome}{label}` | **Cyan** (`#0097A7`) | Conseguenze immediate dei teoremi stocastici |
| `\begin{dimostrazione}` | **Verde barra sinistra** | Dimostrazioni passo-passo con quadratino $\blacksquare$ |
| `\begin{metodo}[Titolo]` | **Warm Amber** (`#FF8F00`) | Algoritmi di calcolo (stima MLE, intervalli pivotali, test) |
| `\begin{esame}[Titolo]` | **Crimson Red** (`#C62828`) | Consigli d'esame, errori concettuali e trabocchetti probabilistici |
| `\begin{esercizio}{Nome}{label}` | **Deep Purple** (`#6A1B9A`) | Esercizi d'esame applicativi completi |
| `\begin{osservazione}[Titolo]` | **Steel Blue** (`#37474F`) | Note teoriche a margine e chiarimenti inferenziali |

---

## 🛠️ Istruzioni per la Compilazione Locale

### 1. Compilazione Completa del Volume
Per compilare l'intero trattato e generare `appuntiStatistica.pdf`:

```bash
# Tramite latexmk (consigliato):
latexmk -pdf main.tex

# Oppure tramite pdflatex:
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```

### 2. Compilazione Rapida di Singoli Capitoli (`\includeonly`)
Nel file [`main.tex`](./main.tex), scommentare la direttiva `\includeonly{...}` specificando il capitolo desiderato:

```latex
\includeonly{
  chapters/09_campione_statistico_e_stimatori/main
}
```

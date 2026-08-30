# 📘 Appunti Digitalizzati di Analisi Matematica II — Manuale Completo in LaTeX
**Corso di Laurea in Ingegneria Gestionale — Università di Pisa**

[![LaTeX Typeset](https://img.shields.io/badge/LaTeX-Typeset_Book-008080?style=flat&logo=latex&logoColor=white)](https://www.latex-project.org/)
[![Pagine](https://img.shields.io/badge/Volume-114_Pagine-orange.svg)](#)
[![1-Click PDF Download](https://img.shields.io/badge/Download_PDF-appuntiAnalisi2.pdf-0052cc?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](https://github.com/Beccaceci/GESTIONALE/raw/main/courses/first_year/ANALISI2/notes/appuntiAnalisi2.pdf)

Questo repository contiene l'infrastruttura completa e modulare in \LaTeX{} per la digitalizzazione, la formalizzazione teorica e l'approfondimento rigoroso del corso di **Analisi Matematica II** (SSD MAT/05, 6 CFU) per il Corso di Laurea in Ingegneria Gestionale dell'Università di Pisa.

---

## 📥 Download Diretto del Manuale Compilato (1-Click)

È possibile scaricare il volume completo ad altissima definizione direttamente dal link sottostante:

> 📄 **[Download `appuntiAnalisi2.pdf`](https://github.com/Beccaceci/GESTIONALE/raw/main/courses/first_year/ANALISI2/notes/appuntiAnalisi2.pdf)**

---

## 🏛️ Architettura Modulare del Progetto

Il progetto adotta una struttura modulare e disaccoppiata:

```text
ANALISI2/notes/
├── config/                                           # Configurazioni globali e preambolo LaTeX
│   ├── packages.tex                                  # Pacchetti (amsmath, amssymb, tikz, pgfplots, tcolorbox, booktabs)
│   ├── environments.tex                              # Box tematici personalizzati (Definizione, Teorema, Metodo, Esame)
│   └── macros.tex                                    # Macro e scorciatoie per gradiente, rotore, divergenza, integrali multipli
├── chapters/                                         # Moduli indipendenti dei singoli capitoli
│   ├── 01_topologia_funzioni_multivariabile/         # Topologia Rn, curve di livello, limiti e continuità multivariabile
│   │   └── main.tex
│   ├── 02_differenziale_e_derivate/                  # Derivate parziali/direzionali, differenziale, piano tangente, Schwarz, Taylor
│   │   └── main.tex
│   ├── 03_funzioni_implicite/                        # Teorema del Dini, retta/piano tangente a insiemi di livello, inversione locale
│   │   └── main.tex
│   ├── 04_minimi_e_massimi/                          # Ottimizzazione libera/vincolata, Hessiana, Moltiplicatori di Lagrange
│   │   └── main.tex
│   ├── 05_curve_e_integrali_curvilinei/              # Curve regolari, lunghezza d'arco, integrali di I e II specie
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
├── figures/                                          # Grafici TikZ, immagini vettoriali e plot 3D PGFPlots
├── appuntiAnalisi2.pdf                               # Trattato completo compilato in PDF ad alta risoluzione (114 pag.)
├── main.tex                                          # Documento master radice (Frontespizio, ToC, inclusioni)
└── README.md                                         # Questo documento di guida e documentazione
```

---

## 📚 Indice Dettagliato dei Capitoli e Mappa Concettuale

### Capitolo 1: Topologia in $\mathbb{R}^n$ e Funzioni Multivariabili
- **Struttura Euclidea di $\mathbb{R}^n$:** Vettori, prodotto scalare, norma euclidea $\|x\| = \sqrt{\sum x_i^2}$, disuguaglianza di Cauchy-Schwarz, disuguaglianza triangolare e distanza euclidea.
- **Topologia di $\mathbb{R}^n$:** Intorni sferici, insiemi aperti, chiusi, limitati, compatti (Teorema di Heine-Borel), punti interni, di frontiera e di accumulazione.
- **Funzioni di Più Variabili e Insiemi di Livello:** Dominio, codominio, curve di livello per funzioni $f:\mathbb{R}^2\to\mathbb{R}$ e superfici di livello per $f:\mathbb{R}^3\to\mathbb{R}$.
- **Limiti Multidimensionali:** Definizione formale $\varepsilon$-$\delta$, non-esistenza tramite fasci di rette $y=mx$, parabole $y=kx^2$ e curve generiche, calcolo di limiti mediante coordinate polari e disuguaglianze uniformi rispetto all'angolo $\theta$.
- **Continuità Multivariabile:** Continuità puntuale e su insiemi compatti, Teorema di Weierstrass in $\mathbb{R}^n$.

### Capitolo 2: Calcolo Differenziale Multivariabile e Derivate
- **Derivate Parziali e Gradiente:** Definizione di derivata parziale $\frac{\partial f}{\partial x_i}$, vettore gradiente $\nabla f$, significato geometrico di massima pendenza.
- **Derivate Direzionali:** Definizione di $D_{\mathbf{v}}f(x_0)$ lungo versori arbitrari.
- **Differenziabilità e Piano Tangente:** Definizione di differenziale totale, Teorema del Differenziale Totale (continuità delle derivate parziali come condizione sufficiente), formula del gradiente per le derivate direzionali ($D_{\mathbf{v}}f = \nabla f \cdot \mathbf{v}$), equazione cartesiana dell'iperpiano tangente al grafico:
  $$z = f(x_0, y_0) + \frac{\partial f}{\partial x}(x_0, y_0)(x - x_0) + \frac{\partial f}{\partial y}(x_0, y_0)(y - y_0)$$
- **Derivate di Ordine Superiore:** **Teorema di Schwarz** sull'inversione dell'ordine di derivazione per funzioni $C^2$, matrice Hessiana $H_f(x_0)$ e sviluppi di Taylor al secondo ordine.

### Capitolo 3: Teorema delle Funzioni Implicite e Invertibilità Locale
- **Geometria delle Funzioni Implicite:** Curve di livello $F(x,y)=0$ e superfici $F(x,y,z)=0$.
- **Teorema del Dini (Due Variabili):** Condizione $\frac{\partial F}{\partial y}(x_0,y_0) \ne 0$, esistenza e unicità locale della funzione esplicita $y = g(x)$, formula della derivata prima implicita:
  $$g'(x) = -\frac{\frac{\partial F}{\partial x}(x, g(x))}{\frac{\partial F}{\partial y}(x, g(x))}$$
- **Teorema del Dini in Tre Variabili e Sistemi:** Piani tangenti a superfici implicite, Teorema del Dini vettoriale per sistemi con matrice Jacobiana, Teorema di Inversione Locale.

### Capitolo 4: Ottimizzazione: Minimi e Massimi Liberi e Vincolati
- **Ottimizzazione Libera:** Punti stazionari interni ($\nabla f(\mathbf{x}_0) = \mathbf{0}$), matrice Hessiana e studio del segno degli autovalori (minimo relativo, massimo relativo, punto di sella, caso semidefinito).
- **Ottimizzazione su Compatti (Teorema di Weierstrass):** Ricerca degli estremi assoluti combinando l'analisi dei punti interni con lo studio della frontiera.
- **Metodo dei Moltiplicatori di Lagrange:** Funzione Lagrangiana $\mathcal{L}(\mathbf{x}, \lambda) = f(\mathbf{x}) - \lambda g(\mathbf{x})$, significato geometrico di tangenza tra curve di livello, discussione dei punti critici vincolati.
- **Frontiere Non Regolari:** Ottimizzazione su domini poligonali e spezzate, parametrizzazione della frontiera e matrici Hessiane orlate.

### Capitolo 5: Curve Parametriche e Integrali Curvilinei
- **Geometria delle Curve:** Curve parametriche $\mathbf{r}(t)$ in $\mathbb{R}^2$ e $\mathbb{R}^3$, regolarità, vettore velocità $\mathbf{r}'(t)$, versore tangente, retta tangente.
- **Rettificazione e Lunghezza d'Arco:** Ascissa curvilinea $s(t) = \int_{t_0}^t \|\mathbf{r}'(\tau)\|\,d\tau$, calcolo della lunghezza di una curva $L(\gamma) = \int_a^b \|\mathbf{r}'(t)\|\,dt$.
- **Integrali Curvilinei di Prima Specie:** Definizione di $\int_\gamma f\,ds = \int_a^b f(\mathbf{r}(t))\|\mathbf{r}'(t)\|\,dt$, applicazioni a massa, baricentri e momenti d'inerzia di fili.
- **Integrali Curvilinei di Seconda Specie (Lavoro):** Definizione di $\int_\gamma \mathbf{F}\cdot d\mathbf{r} = \int_a^b \mathbf{F}(\mathbf{r}(t))\cdot\mathbf{r}'(t)\,dt$, dipendenza dall'orientazione e circuitazione lungo curve chiuse.

### Capitolo 6: Calcolo Vettoriale, Campi Conservativi e Forme Differenziali
- **Operatori Differenziali:** Gradiente, divergenza $\operatorname{div}\mathbf{F} = \nabla \cdot \mathbf{F}$, rotore $\operatorname{rot}\mathbf{F} = \nabla \times \mathbf{F}$ e operatore Laplaciano $\Delta = \nabla^2$.
- **Campi Conservativi e Potenziali:** Definizione di campo conservativo $\mathbf{F} = \nabla U$, indipendenza dal cammino per il lavoro, circuitazione nulla lungo qualsiasi linea chiusa.
- **Forme Differenziali Lineari:** Forme chiuse ($d\omega = 0$), forme esatte ($\omega = df$), domini semplicemente connessi e **Lemma di Poincaré** (in un dominio semplicemente connesso, ogni forma chiusa è esatta).

### Capitolo 7: Integrali Multipli: Integrali Doppi e Tripli
- **Integrali Doppi su Domini Normali:** Definizione di Riemann, domini $x$-semplici e $y$-semplici, formule di riduzione di Fubini-Tonelli:
  $$\iint_D f(x,y)\,dx\,dy = \int_a^b \left(\int_{\phi_1(x)}^{\phi_2(x)} f(x,y)\,dy\right) dx$$
- **Cambiamenti di Coordinate negli Integrali Doppi:** Coordinate polari cartesiane ($x = r\cos\theta, y = r\sin\theta$) con fattore Jacobiano $J = r$.
- **Integrali Tripli:** Riduzione per fili e per strati su solidi tridimensionali.
- **Coordinate Cilindriche e Sferiche:** Coordinate cilindriche ($J=r$) e sferiche ($x=\rho\sin\phi\cos\theta, y=\rho\sin\phi\sin\theta, z=\rho\cos\phi$, con $J=\rho^2\sin\phi$), calcolo di volumi, baricentri e momenti d'inerzia.

### Capitolo 8: Superfici Parametriche e Integrali di Superficie
- **Geometria delle Superfici:** Superfici parametriche $\mathbf{r}(u,v)$, regolarità, vettori tangenti $\mathbf{r}_u, \mathbf{r}_v$, vettore normale fondamentale $\mathbf{N} = \mathbf{r}_u \times \mathbf{r}_v$, piano tangente e superfici cartesiane $z = g(x,y)$.
- **Integrali di Superficie di Prima Specie:** Elemento d'area $d\sigma = \|\mathbf{N}\|\,du\,dv$, calcolo dell'area di superfici e massa di lamine curve.
- **Flusso di un Campo Vettoriale:** Definizione di $\iint_\Sigma \mathbf{F}\cdot\mathbf{n}\,d\sigma$, superfici orientabili, scelta del verso del versore normale uscente.

### Capitolo 9: I Grandi Teoremi Integrali del Calcolo Vettoriale
- **Teorema di Gauss-Green nel Piano:** Relazione tra integrale doppio sul dominio $D$ e integrale curvilineo lungo la frontiera orientata positivamente $\partial^+ D$:
  $$\iint_D \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right) dx\,dy = \oint_{\partial^+ D} (P\,dx + Q\,dy)$$
  Formule per il calcolo dell'area di $D$ tramite integrali di linea ($\operatorname{Area}(D) = \oint x\,dy = -\oint y\,dx = \frac{1}{2}\oint (x\,dy - y\,dx)$).
- **Teorema della Divergenza (di Gauss in 3D):** Uguaglianza tra il flusso uscente da una superficie chiusa $\partial \Omega$ e l'integrale triplo della divergenza nel volume $\Omega$:
  $$\iint_{\partial \Omega} \mathbf{F}\cdot\mathbf{n}_{\text{ext}}\,d\sigma = \iiint_\Omega \operatorname{div}\mathbf{F}\,dx\,dy\,dz$$
- **Teorema del Rotore (di Stokes/Kelvin):** Uguaglianza tra la circuitazione di $\mathbf{F}$ lungo il bordo orientato $\partial^+ \Sigma$ e il flusso del rotore attraverso la superficie $\Sigma$:
  $$\oint_{\partial^+ \Sigma} \mathbf{F}\cdot d\mathbf{r} = \iint_\Sigma (\operatorname{rot}\mathbf{F})\cdot\mathbf{n}\,d\sigma$$

### Capitolo 10: Raccolta Temi d'Esame e Quesiti d'Orale Svolti
- Risoluzioni complete passo-passo di temi d'esame ufficiali (volumi, integrali di flusso, ottimizzazioni vincolate, campi conservativi) e domande tipiche della prova orale.

---

## 🎨 Ambienti Tipografici e Box Tematici (`tcolorbox`)

| Ambiente | Colore Bordo / Titolo | Finalità Didattica |
| :--- | :--- | :--- |
| `\begin{definizione}{Nome}{label}` | **Navy Blue** (`#003366`) | Definizioni formali rigorose in $\mathbb{R}^n$ |
| `\begin{teorema}{Nome}{label}` | **Forest Green** (`#2E7D32`) | Grandi teoremi (Dini, Schwarz, Gauss-Green, Stokes, Gauss) |
| `\begin{proposizione}{Nome}{label}` | **Teal Blue** (`#00838F`) | Proprietà geometriche e analitiche intermedie |
| `\begin{corollario}{Nome}{label}` | **Cyan** (`#0097A7`) | Conseguenze immediate dei teoremi integrali |
| `\begin{dimostrazione}` | **Verde barra sinistra** | Dimostrazioni complete chiuse da $\blacksquare$ |
| `\begin{metodo}[Titolo]` | **Warm Amber** (`#FF8F00`) | Algoritmi di calcolo (Lagrange, cambi di coordinate, flusso) |
| `\begin{esame}[Titolo]` | **Crimson Red** (`#C62828`) | Consigli d'esame, tranelli geometrici ed errori frequenti |
| `\begin{esempio}{Nome}{label}` | **Deep Purple** (`#6A1B9A`) | Esempi numerici svolti ed esercizi guidati |
| `\begin{osservazione}[Titolo]` | **Steel Blue** (`#37474F`) | Intuizioni geometriche 3D e note fisiche a margine |

---

## 🛠️ Istruzioni per la Compilazione Locale

### 1. Compilazione Completa del Volume
Per compilare l'intero trattato e generare `appuntiAnalisi2.pdf`:

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
  chapters/04_minimi_e_massimi/main
}
```

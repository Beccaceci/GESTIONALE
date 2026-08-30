# 📘 Appunti Digitalizzati di Algebra Lineare e Geometria — Manuale Completo in LaTeX
**Corso di Laurea in Ingegneria Gestionale — Università di Pisa**

[![LaTeX Typeset](https://img.shields.io/badge/LaTeX-Typeset_Book-008080?style=flat&logo=latex&logoColor=white)](https://www.latex-project.org/)
[![Pagine](https://img.shields.io/badge/Volume-61_Pagine-orange.svg)](#)
[![1-Click PDF Download](https://img.shields.io/badge/Download_PDF-appuntiAlgebraLineare.pdf-0052cc?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](https://github.com/Beccaceci/GESTIONALE/raw/main/courses/first_year/ALGEBRA_LINEARE/notes/appuntiAlgebraLineare.pdf)

Questo repository contiene l'infrastruttura completa e modulare in \LaTeX{} per la digitalizzazione, la formalizzazione teorica e l'approfondimento rigoroso del corso di **Algebra Lineare e Geometria** (SSD MAT/03, 6 CFU) per il Corso di Laurea in Ingegneria Gestionale dell'Università di Pisa.

---

## 📥 Download Diretto del Manuale Compilato (1-Click)

È possibile scaricare il volume completo ad altissima definizione direttamente dal link sottostante:

> 📄 **[Download `appuntiAlgebraLineare.pdf`](https://github.com/Beccaceci/GESTIONALE/raw/main/courses/first_year/ALGEBRA_LINEARE/notes/appuntiAlgebraLineare.pdf)**

---

## 🏛️ Architettura Modulare del Progetto

Il progetto adotta un'architettura rigorosamente disaccoppiata e strutturata a capitoli indipendenti:

```text
ALGEBRA_LINEARE/notes/
├── config/                                           # Configurazioni globali del documento LaTeX
│   ├── packages.tex                                  # Pacchetti (amsmath, amssymb, tikz, tcolorbox, nicematrix, booktabs)
│   ├── environments.tex                              # Box tematici stilizzati tcolorbox (Definizione, Teorema, Metodo, Esame)
│   └── macros.tex                                    # Macro e scorciatoie per vettori, matrici, operatori algebrici
├── chapters/                                         # Moduli indipendenti dei capitoli
│   ├── 00_fondamenti_logica_insiemistica/            # Logica proposizionale, quantificatori, metodi dimostrativi, insiemi
│   │   └── main.tex
│   ├── 01_numeri_complessi/                          # Forma algebrica, trigonometrica/esponenziale, radici n-esime, De Moivre
│   │   └── main.tex
│   ├── 02_spazi_vettoriali/                          # Assiomatica su K, Span, basi, coordinate, dimensione, Formula di Grassmann
│   │   └── main.tex
│   ├── 03_applicazioni_lineari/                      # Omomorfismi, nucleo, immagine, Teorema della Dimensione, isomorfismi
│   │   └── main.tex
│   ├── 04_matrici_sistemi/                           # Matrice associata, cambio base, rango, Gauss-Jordan, Rouché-Capelli
│   │   └── main.tex
│   ├── 05_determinanti/                              # Assiomi, sviluppi di Laplace, Teorema di Binet, matrice inversa, Cramer
│   │   └── main.tex
│   ├── 06_autovalori_autovettori/                    # Polinomio caratteristico, molteplicità algebrica/geometrica, diagonalizzazione
│   │   └── main.tex
│   ├── 07_prodotti_scalari_spettrale/                # Forme bilineari, Cauchy-Schwarz, Gram-Schmidt, Teorema Spettrale reale
│   │   └── main.tex
│   └── 08_esercizi_esami/                            # Quesiti sintetici d'esame e temi d'appello completi risolti
│       └── main.tex
├── figures/                                          # Illustrazioni vettoriali TikZ e diagrammi geometrici
├── appuntiAlgebraLineare.pdf                         # Manuale PDF completo compilato ad alta risoluzione (61 pag.)
├── main.tex                                          # Master document LaTeX (Frontespizio, ToC, inclusioni)
└── README.md                                         # Questo documento di guida e documentazione
```

---

## 📚 Indice Dettagliato dei Capitoli e Mappa Concettuale

### Capitolo 0: Fondamenti di Logica Matematica e Teoria degli Insiemi
- **Logica Proposizionale:** Proposizioni, connettivi logici ($\land, \lor, \neg, \implies, \iff$), tavole di verità, tautologie e contraddizioni.
- **Quantificatori e Predicati:** Quantificatore universale ($\forall$) ed esistenziale ($\exists$), negazione di proposizioni quantificate.
- **Metodi di Dimostrazione Matematica:** Dimostrazione diretta, dimostrazione per assurdo (dimostrazione dell'irrazionalità di $\sqrt{2}$), dimostrazione per contrapposizione, Principio di Induzione Matematica.
- **Insiemistica:** Operazioni tra insiemi, prodotto cartesiano, diagrammi di Venn in TikZ, relazioni di equivalenza e partizioni.

### Capitolo 1: Numeri Complessi
- **Forma Algebrica:** Introduzione dell'unità immaginaria $i^2=-1$, campo $\mathbb{C}$, parte reale e immaginaria, coniugato complesso, modulo e proprietà.
- **Rappresentazione Geometrica:** Piano di Gauss-Argand, forma trigonometrica $z = r(\cos\theta + i\sin\theta)$ e forma esponenziale di Eulero $z = re^{i\theta}$.
- **Operazioni e Teoremi:** Formula di De Moivre, prodotto e quoziente in forma esponenziale, calcolo geometrico delle **radici $n$-esime dell'unità** nel piano complesso.
- **Equazioni Algebriche in $\mathbb{C}$:** Risoluzione di equazioni polinomiali, radici complesse coniugate e Teorema Fondamentale dell'Algebra.

### Capitolo 2: Spazi e Sottospazi Vettoriali
- **Assiomatica di Spazio Vettoriale:** Assiomi di spazio vettoriale su un campo generico $\mathbb{K}$ ($\mathbb{R}$ o $\mathbb{C}$).
- **Sottospazi Vettoriali:** Definizione e criterio di caratterizzazione (chiusura rispetto a combinazioni lineari).
- **Generatori e Indipendenza Lineare:** Combinazioni lineari, $\operatorname{Span}(v_1, \dots, v_k)$, dipendenza e indipendenza lineare di insiemi di vettori.
- **Basi e Dimensione:** Definizione di base, esistenza della base in dimensione finita, coordinate di un vettore, unicità della rappresentazione e concetto di dimensione $\dim(V)$.
- **Operazioni tra Sottospazi:** Intersezione e somma di sottospazi, somma diretta ($U \oplus W$) e **Formula di Grassmann**:
  $$\dim(U + W) = \dim(U) + \dim(W) - \dim(U \cap W)$$

### Capitolo 3: Applicazioni Lineari, Nucleo e Immagine
- **Omomorfismi di Spazi Vettoriali:** Definizione di linearità, proprietà elementari e conservazione delle combinazioni lineari.
- **Nucleo e Immagine:** Definizione di $\ker(f)$ e $\operatorname{Im}(f)$, verifica della struttura di sottospazio, condizioni di iniettività ($\ker(f) = \{0\}$) e suriettività.
- **Teorema della Dimensione (Nullità più Rango):** Enunciato e dimostrazione costruttiva:
  $$\dim(V) = \dim(\ker(f)) + \dim(\operatorname{Im}(f))$$
- **Isomorfismi:** Teorema di isomorfismo tra spazi di pari dimensione finita con $\mathbb{K}^n$, composizione di applicazioni lineari e invertibilità.

### Capitolo 4: Matrice Associata e Sistemi Lineari
- **Matrice Associata ad un'Applicazione:** Costruzione di $M_{\mathcal{B}}^{\mathcal{C}}(f)$, isomorfismo tra $\operatorname{Hom}(V, W)$ e lo spazio delle matrici $\mathcal{M}_{m,n}(\mathbb{K})$.
- **Cambiamento di Base:** Matrice del cambiamento di base $M_{\mathcal{B}}^{\mathcal{B'}}$, formula di trasformazione per le coordinate e per le matrici associate (matrici simili $A' = P^{-1}AP$).
- **Rango di una Matrice:** Definizione per righe e per colonne, coincidenza dei ranghi e proprietà.
- **Eliminazione di Gauss-Jordan:** Algoritmo a gradini per matrici aumentate, calcolo di basi di nucleo e immagine.
- **Teorema di Rouché-Capelli:** Condizione necessaria e sufficiente di compatibilità per sistemi lineari $A\mathbf{x} = \mathbf{b}$, dimensione dello spazio delle soluzioni affine $S = \mathbf{x}_0 + \ker(A)$, e discussione di sistemi lineari parametrici.

### Capitolo 5: Determinanti
- **Definizione Assiomatica:** Proprietà del determinante come funzione multilineare alternata delle righe (o colonne).
- **Calcolo del Determinante:** Regola di Sarrus per matrici $3\times 3$, **sviluppi di Laplace** per una riga o colonna qualsiasi.
- **Teoremi Cardine:** **Teorema di Binet** ($\det(AB) = \det(A)\det(B)$), determinante della trasposta ($\det(A^T) = \det(A)$), determinante dell'inversa.
- **Invertibilità e Matrice Inversa:** Condizione necessaria e sufficiente $\det(A) \ne 0$, formula analitica dell'inversa mediante la matrice dei cofattori:
  $$A^{-1} = \frac{1}{\det(A)} (\operatorname{cof}(A))^T$$
- **Regola di Cramer:** Risoluzione analitica di sistemi lineari quadrati non singolari.

### Capitolo 6: Autovalori, Autovettori e Diagonalizzazione
- **Autovalori e Autovettori:** Definizione geometrica $Av = \lambda v$ ($v \ne 0$), autospazi $V_\lambda = \ker(A - \lambda I)$.
- **Polinomio Caratteristico:** $p_A(\lambda) = \det(A - \lambda I)$, invarianza per similitudine (traccia e determinante come invarianti spettrali).
- **Molteplicità Algebrica e Geometrica:** Definizione di $m_a(\lambda)$ e $m_g(\lambda)$, dimostrazione della disuguaglianza fondamentale $1 \le m_g(\lambda) \le m_a(\lambda)$.
- **Criteri di Diagonalizzabilità:** Teorema fondamentale di diagonalizzabilità (tutte le radici in $\mathbb{K}$ e $m_g(\lambda) = m_a(\lambda)$ per ogni autovalore), costruzione della matrice diagonalizzante $P$ e della forma diagonale $D = P^{-1}AP$.

### Capitolo 7: Prodotti Scalari e Matrici Simmetriche
- **Forme Bilineari e Prodotti Scalari Reali:** Definizione assiomatica di prodotto scalare $\langle u, v \rangle$, simmetria, bilinearità e positività definita.
- **Norma Euclidea e Angoli:** Definizione di norma $\|v\| = \sqrt{\langle v, v \rangle}$, disuguaglianza di Cauchy-Schwarz ($|\langle u, v \rangle| \le \|u\|\|v\|$), disuguaglianza triangolare e angolo tra vettori.
- **Ortogonalità e Algoritmo di Gram-Schmidt:** Insiemi ortogonali e ortonormali, proiezione ortogonale, algoritmo costruttivo di Gram-Schmidt per l'ortonormalizzazione di una base arbitraria.
- **Matrici Ortogonali:** Caratterizzazione ($Q^T Q = I$), conservazione delle lunghezze e degli angoli.
- **Teorema Spettrale Reale:** Enunciato e dimostrazione della diagonalizzabilità ortogonale di ogni matrice simmetrica reale $A = A^T$ mediante matrice ortogonale $Q$ ($Q^T A Q = D$).

### Capitolo 8: Esercizi ed Esami Ufficiali Svolti
- **Quesiti Rapidi d'Esame:** Raccolta di quesiti teorico-pratici a risposta sintetica risolti e commentati.
- **Temi d'Esame Integrali:** Svolgimenti completi passo-passo di prove scritte ufficiali di appello e compitini.

---

## 🎨 Ambienti Tipografici e Box Tematici (`tcolorbox`)

Il volume impiega un sistema cromatico coerente e professionale basato sul pacchetto `tcolorbox`:

| Ambiente | Colore Bordo / Titolo | Finalità Didattica |
| :--- | :--- | :--- |
| `\begin{definizione}{Nome}{label}` | **Navy Blue** (`#003366`) | Definizioni formali rigorose con notazione algebrica esatta |
| `\begin{teorema}{Nome}{label}` | **Forest Green** (`#2E7D32`) | Enunciati dei teoremi fondamentali con ipotesi e tesi |
| `\begin{proposizione}{Nome}{label}` | **Teal Blue** (`#00838F`) | Proposizioni intermedie e proprietà strutturali |
| `\begin{corollario}{Nome}{label}` | **Cyan** (`#0097A7`) | Conseguenze dirette e corollari dei teoremi principali |
| `\begin{lemma}{Nome}{label}` | **Slate Gray** (`#455A64`) | Risultati preliminari e lemmi tecnici di supporto |
| `\begin{dimostrazione}` | **Verde barra sinistra** | Dimostrazioni passo-passo concluse dal quadratino $\blacksquare$ |
| `\begin{metodo}[Titolo]` | **Warm Amber** (`#FF8F00`) | Algoritmi operativi di calcolo (Gauss, Laplace, Gram-Schmidt) |
| `\begin{esame}[Titolo]` | **Crimson Red** (`#C62828`) | Consigli d'esame, trabocchetti frequenti ed errori comuni |
| `\begin{esempio}{Nome}{label}` | **Deep Purple** (`#6A1B9A`) | Esempi numerici svolti ed esercizi guidati |
| `\begin{osservazione}[Titolo]` | **Steel Blue** (`#37474F`) | Note teoriche a margine e chiarimenti geometrici |

---

## 🛠️ Istruzioni per la Compilazione Locale

### 1. Compilazione Completa del Volume
Per compilare l'intero trattato e generare `appuntiAlgebraLineare.pdf`:

```bash
# Tramite latexmk (consigliato, gestisce automaticamente ToC e riferimenti):
latexmk -pdf main.tex

# Oppure tramite pdflatex (eseguire due volte per allineare l'indice):
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```

### 2. Compilazione Rapida di Singoli Capitoli (`\includeonly`)
Nel file [`main.tex`](./main.tex), scommentare la direttiva `\includeonly{...}` specificando esclusivamente il capitolo su cui si intende lavorare:

```latex
\includeonly{
  chapters/06_autovalori_autovettori/main
}
```
Questo consente una compilazione istantanea preservando numeri di pagina, riferimenti incrociati e numerazione globale.

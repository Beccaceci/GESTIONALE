# Algebra Lineare e Geometria - Repository degli Appunti Digitalizzati

Questo repository contiene l'infrastruttura completa e modulare in \LaTeX{} per la digitalizzazione, la formalizzazione teorica e l'approfondimento rigoroso del corso di **Algebra Lineare e Geometria** (Corso di Laurea in Ingegneria Gestionale).

---

## 📁 Struttura delle Cartelle

```text
ALGEBRA_LINEARE/
├── config/
│   ├── packages.tex          # Pacchetti LaTeX (TikZ, tcolorbox, amsmath, nicematrix, ecc.)
│   ├── environments.tex      # Box colorati (Definizione, Teorema, Esempio, Esame, Metodo, Dimostrazione)
│   └── macros.tex            # Macro matematiche (Spazi, Matrici, Autovalori, Prodotti scalari, Notazioni)
├── chapters/
│   ├── 01_numeri_complessi/
│   │   └── main.tex          # Forma algebrica, trigonometrica/esponenziale, radici n-esime, equazioni
│   ├── 02_spazi_vettoriali/
│   │   └── main.tex          # Assiomatica, Span, Indipendenza, Basi, Dimensione, Somma diretta, Grassmann
│   ├── 03_applicazioni_lineari/
│   │   └── main.tex          # Omomorfismi, Nucleo, Immagine, Teorema della Dimensione, Isomorfismi
│   ├── 04_matrici_sistemi/
│   │   └── main.tex          # Matrice associata, Cambiamento base, Rango, Rouché-Capelli, Gauss-Jordan
│   ├── 05_determinanti/
│   │   └── main.tex          # Assiomi, Laplace, Binet, Inversa con cofattori, Regola di Cramer
│   ├── 06_autovalori_autovettori/
│   │   └── main.tex          # Spettro, Molteplicità algebrica/geometrica, Criteri di diagonalizzabilità
│   └── 07_prodotti_scalari_spettrale/
│       └── main.tex          # Forme bilineari, Cauchy-Schwarz, Gram-Schmidt, Teorema Spettrale reale
├── figures/                  # Grafici TikZ, immagini e diagrammi
├── scans/                    # Cartella per i file PDF di scansione degli appunti cartacei
├── main.tex                  # Documento Master (Frontespizio, TOC, Guida alla lettura, Inclusioni)
└── README.md                 # Guida all'utilizzo, compilazione e workflow di digitalizzazione
```

---

## 🚀 Flessibilità e Aggiunta / Modifica di Capitoli

La struttura è progettata per essere **estremamente flessibile**:
1. **Compilazione selettiva rapida**: Nel file `main.tex`, basta decommentare `\includeonly{chapters/...}` per compilare solo il capitolo su cui si sta lavorando in quel momento, accelerando i tempi di build.
2. **Aggiunta dinamica di nuovi capitoli**:
   - Creare una nuova cartella sotto `chapters/` (es. `chapters/08_geometria_affine_euclidea/main.tex`).
   - Aggiungere `\include{chapters/08_geometria_affine_euclidea/main}` in `main.tex`.
3. **Riorganizzazione o fusione**: Spostare o rinominare i capitoli è immediato grazie al disaccoppiamento modulare.

---

## 🛠️ Come Compilare il Documento

È possibile compilare tramite terminale con:
```bash
# Compilazione diretta con pdflatex (eseguire due volte per aggiornare indice e riferimenti incrociati)
cd /Users/nicolabeccaceci/Documents/GEST/ALGEBRA_LINEARE
pdflatex main.tex
pdflatex main.tex

# Oppure compilazione automatica con latexmk:
latexmk -pdf main.tex
```

---

## 🔄 Workflow di Conversione degli Appunti Scansionati

Quando alleghi un PDF con le scansioni degli appunti manoscritti:
1. **Filtro del rumore ed eliminazione errori**: Correggo sviste di calcolo, simboli ambigui o passaggi mancanti tipici della scrittura a mano.
2. **Integrazione teorica completa**: Arricchisco gli appunti con definizioni formali, quantificatori rigorosi, dimostrazioni dettagliate passo-passo e spiegazioni geometriche intuitive.
3. **Box d'esame e Metodi Risolutivi**: Inserisco box dedicati alle trappole d'esame e algoritmi di risoluzione standard.
4. **Scrittura e Compilazione LaTeX**: Il codice viene integrato nel capitolo di competenza e compilato in PDF.

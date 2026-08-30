# 📚 Analisi Matematica II — Ingegneria Gestionale (UniPi)

[![Corso](https://img.shields.io/badge/Corso-Laurea_Triennale_Ingegneria_Gestionale-blue.svg)](#)
[![Universita](https://img.shields.io/badge/UniPi-Universit%C3%A0_di_Pisa-003366.svg)](https://www.unipi.it/)
[![CFU](https://img.shields.io/badge/CFU-6_CFU-orange.svg)](#)
[![SSD](https://img.shields.io/badge/SSD-MAT%2F05-green.svg)](#)
[![Semestre](https://img.shields.io/badge/Semestre-2%C2%B0_Semestre-purple.svg)](#)
[![Docente](https://img.shields.io/badge/Docente-Prof._Marco_Ghimenti_%2F_Prof._Vladimir_Georgiev-lightblue.svg)](#)
[![Appunti PDF](https://img.shields.io/badge/Appunti_PDF-appuntiAnalisi2.pdf-0052cc?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](https://github.com/Beccaceci/GESTIONALE/raw/main/courses/first_year/ANALISI2/notes/appuntiAnalisi2.pdf)
[![Archivio Esami](https://img.shields.io/badge/Archivio_Esami-Temi_Svolti_(2020--2023)-darkgreen?style=for-the-badge&logo=googledocs&logoColor=white)](./exams/)

> **Corso di Laurea Triennale in Ingegneria Gestionale — Università di Pisa**  
> *Anno di Corso:* Primo Anno | *Crediti:* 6 CFU | *Settore Scientifico Disciplinare:* MAT/05 (Analisi Matematica)

---

## 🎯 Presentazione del Corso e Obiettivi Formativi

### Inquadramento Didattico
Il corso di **Analisi Matematica II** estende i concetti fondamentali del calcolo infinitesimale allo spazio multidimensionale ($\mathbb{R}^n$, $n \ge 2$), integrando geometria differenziale, calcolo vettoriale e teoria dell'integrazione multipla. Questo insegnamento rappresenta il completamento naturale di *Analisi Matematica I* e di *Algebra Lineare e Geometria*, fornendo gli strumenti analitici indispensabili per l'elettromagnetismo, la fluidodinamica, la meccanica dei continui e per i moderni modelli di ottimizzazione vincolata e programmazione matematica dell'Ingegneria Gestionale.

### Competenze Acquisite
Al termine del corso, lo studente è in grado di:
- Analizzare la topologia dello spazio euclideo $\mathbb{R}^n$ (intorni sferici, aperti, chiusi, frontiera, compattezza, connessione).
- Calcolare limiti multivariabili verificandone l'esistenza tramite coordinate polari/sferiche e disuguaglianze, o provandone la non-esistenza mediante fasci di rette, parabole o restrizioni opportune.
- Padroneggiare la derivazione parziale, le derivate direzionali, il vettore gradiente, il **differenziale totale** e la costruzione dell'iperpiano tangente a grafici e superfici.
- Applicare il **Teorema di Schwarz** per derivate di ordine superiore, la matrice Hessiana e la formula di Taylor al secondo ordine con resto di Peano e Lagrange.
- Utilizzare il **Teorema delle Funzioni Implicite (Teorema del Dini)** per lo studio locale di curve e superfici di livello e per l'inversione locale di campi vettoriali.
- Risolvere problemi di **ottimizzazione libera** (classificazione di punti stazionari tramite autovalori dell'Hessiana) e di **ottimizzazione vincolata** su compatti tramite il **metodo dei Moltiplicatori di Lagrange** e l'analisi della frontiera (parametrizzazione, spezzate, matrici orlate).
- Calcolare integrali curvilinei di prima specie (massa di fili, baricentri) e di seconda specie (lavoro e circuitazione di campi vettoriali lungo curve regolari e a tratti).
- Studiare campi conservativi, calcolare potenziali scalari, verificare l'irrotazionalità e applicare il **Lemma di Poincaré** su domini semplicemente connessi e forme differenziali lineari.
- Calcolare **integrali doppi e tripli** su domini normali applicando le formule di riduzione di Fubini-Tonelli e trasformazioni di coordinate (polari, ellittiche, cilindriche, sferiche) con il rispettivo fattore di scala Jacobiano.
- Calcolare integrali di superficie (area di superfici parametriche, grafici cartesiani, superfici di rotazione) e il **flusso di campi vettoriali** attraverso superfici orientate.
- Padroneggiare e applicare i grandi teoremi integrali del calcolo vettoriale: **Formule di Gauss-Green nel piano**, **Teorema della Divergenza di Gauss** nello spazio 3D e **Teorema del Rotore di Stokes/Kelvin**.

### Programma Modulare per Macro-Aree
1. **Topologia Multivariabile e Calcolo Differenziale:** Spazio euclideo $\mathbb{R}^n$, insiemi e curve di livello, limiti multidimensionali, continuità, derivate parziali, gradiente, differenziabilità, piano tangente, Teorema di Schwarz, matrice Hessiana e sviluppi di Taylor al secondo ordine.
2. **Funzioni Implicite e Ottimizzazione:** Teorema del Dini per equazioni scalari e sistemi, rette/piani tangenti a insiemi di livello, matrice Jacobiana, punti stazionari, Hessiano, Teorema di Weierstrass su domini compatti, metodo dei Moltiplicatori di Lagrange e ottimizzazione vincolata su frontiere non regolari.
3. **Curve, Forme Differenziali e Campi Conservativi:** Curve parametriche regolari in $\mathbb{R}^2$ e $\mathbb{R}^3$, lunghezza d'arco, integrali curvilinei di I e II specie, operatori vettoriali ($\nabla, \operatorname{div}, \operatorname{rot}, \Delta$), forme differenziali esatte e chiuse, campi conservativi, potenziale e Lemma di Poincaré.
4. **Integrali Multipli, Superfici e Teoremi Integrali:** Integrali doppi e tripli, formule di Fubini-Tonelli, cambi di coordinate (polari, cilindriche, sferiche), superfici parametriche, elemento d'area $d\sigma$, flusso vettoriale, Formule di Gauss-Green, Teorema della Divergenza e Teorema di Stokes.

---

## 📋 Regolamento Ufficiale d'Esame

L'esame di *Analisi Matematica II* è strutturato per verificare la padronanza operativa del calcolo multivariabile avanzato e la solidità nell'impostazione logico-teorica delle dimostrazioni.

### 1. Prove Scritte (Modalità Ordinaria e Appelli)
- **Formato e Durata:** La prova scritta ordinaria ha una durata di **2 ore - 2 ore e 30 minuti** ed è composta da 3–4 problemi a svolgimento completo ed esaustivo:
  - *Problema 1:* Calcolo differenziale e ottimizzazione (limiti multivariabili con parametri, differenziabilità, massimi/minimi liberi o vincolati con Moltiplicatori di Lagrange su domini chiusi e limitati);
  - *Problema 2:* Curve, forme differenziali e campi vettoriali (integrali di linea di I e II specie, calcolo del potenziale, lavoro lungo curve orientate o spezzate);
  - *Problema 3:* Integrali multipli (integrali doppi/tripli su solidi normali o di rotazione con cambi di variabili in coordinate cilindriche/sferiche);
  - *Problema 4:* Superfici e Teoremi Integrali (calcolo di aree superficiali, flusso diretto di campi vettoriali, applicazione del Teorema della Divergenza o del Teorema del Rotore/Stokes).
- **Punteggio e Ammissione:** Il punteggio totale è di $30/30$. La soglia minima di ammissione al colloquio orale o di superamento dello scritto è fissata a **$18/30$**.

### 2. Prove in Itinere (Compitini / Esoneri)
Durante il secondo semestre sono previste due prove scritte intermedie di esonero (*compitini*):
- **Primo Compitino (a metà semestre):** Copre Topologia in $\mathbb{R}^n$, Limiti e Continuità multivariabile, Derivate Parziali/Direzionali, Differenziale, Teorema di Schwarz, Taylor, Teorema del Dini e Ottimizzazione Libera/Vincolata con Moltiplicatori di Lagrange.
- **Secondo Compitino (a fine semestre):** Copre Curve, Integrali Curvilinei, Forme Differenziali e Campi Conservativi, Integrali Doppi e Tripli, Superfici Parametriche, Flusso, Gauss-Green, Teorema della Divergenza e Teorema di Stokes.
- **Formula di Esonero:** Lo studente che sostiene entrambi i compitini ottiene l'esonero dalla prova scritta se:
  1. Consegue una votazione non inferiore a **$15/30$** in ciascuna delle due prove;
  2. La **media aritmetica** delle due prove è $\ge 18/30$:
     $$V_{\text{scritto}} = \frac{V_1 + V_2}{2} \ge 18$$

### 3. Prova Orale
- **Accesso:** Riservato a tutti gli studenti che hanno conseguito almeno $18/30$ nella prova scritta (o tramite la media dei compitini).
- **Struttura del Colloquio:** Il colloquio orale prevede la revisione critica della prova scritta e una serie di domande teoriche volte ad accertare:
  - Definizioni formali esatte (differenziabilità, piano tangente, forme chiuse ed esatte, regolarità di curve e superfici, orientabilità);
  - Enunciati precisi di tutti i teoremi e lemmi del programma;
  - **Dimostrazioni integrali dei teoremi cardine** (es. Teorema del Differenziale Totale, Teorema di Schwarz sull'inversione delle derivate miste, Teorema del Dini in due variabili, Condizioni di ottimalità del I e II ordine, Lemma di Poincaré in aperti stellati, Teorema di Gauss-Green nel piano, Teorema della Divergenza di Gauss, Teorema di Stokes del rotore).

### 4. Criteri di Valutazione e Validità dei Voti
- **Voto Finale:** Determinato dalla sintesi complessiva tra le capacità di calcolo evidenziate nello scritto e la maturità teorico-concettuale dimostrata all'orale.
- **Validità dei Compitini:** Gli esoneri da compitino sono utilizzabili per tutti gli appelli della sessione estiva (giugno-luglio) e della sessione autunnale (settembre) dell'anno accademico di erogazione del corso.
- **Validità dello Scritto:** Il superamento dello scritto in un appello ordinario è valido per sostenere l'orale nel medesimo appello o nell'appello successivo della stessa sessione.

---

## 🗂️ Navigazione Rapida e Risorse Disponibili

- 📘 [**Appunti delle Lezioni (`./notes/`)**](./notes/): Trattato completo in LaTeX (114 pagine), struttura modulare in 10 capitoli e link per il download in 1-click di `appuntiAnalisi2.pdf`.
- 📝 [**Archivio Temi d'Esame Risolti (`./exams/`)**](./exams/): Archivio storico cronologico delle prove scritte d'esame con testi e soluzioni svolte passo-passo (2020–2023).
- 📦 [**Materiale Didattico e Dispense (`./sources/`)**](./sources/): Dispense universitarie, formulari e approfondimenti tematici.

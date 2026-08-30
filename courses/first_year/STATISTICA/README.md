# 📚 Statistica e Calcolo delle Probabilità — Ingegneria Gestionale (UniPi)

[![Corso](https://img.shields.io/badge/Corso-Laurea_Triennale_Ingegneria_Gestionale-blue.svg)](#)
[![Universita](https://img.shields.io/badge/UniPi-Universit%C3%A0_di_Pisa-003366.svg)](https://www.unipi.it/)
[![CFU](https://img.shields.io/badge/CFU-6_CFU-orange.svg)](#)
[![SSD](https://img.shields.io/badge/SSD-MAT%2F06-green.svg)](#)
[![Semestre](https://img.shields.io/badge/Semestre-2%C2%B0_Semestre-purple.svg)](#)
[![Docente](https://img.shields.io/badge/Docente-Prof._Andrea_Agazzi-lightblue.svg)](#)
[![Appunti PDF](https://img.shields.io/badge/Appunti_PDF-appuntiStatistica.pdf-0052cc?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](https://github.com/Beccaceci/GESTIONALE/raw/main/courses/first_year/STATISTICA/notes/appuntiStatistica.pdf)
[![Archivio Esami](https://img.shields.io/badge/Archivio_Esami-Appelli_(2020--2024)_%2B_10_Fogli_Esercizi-darkgreen?style=for-the-badge&logo=googledocs&logoColor=white)](./exams/)

> **Corso di Laurea Triennale in Ingegneria Gestionale — Università di Pisa**  
> *Anno di Corso:* Primo Anno | *Crediti:* 6 CFU | *Settore Scientifico Disciplinare:* MAT/06 (Probabilità e Statistica Matematica)

---

## 🎯 Presentazione del Corso e Obiettivi Formativi

### Inquadramento Didattico
Il corso di **Statistica e Calcolo delle Probabilità** fornisce l'apparato teorico e metodologico per modellizzare e analizzare fenomeni casuali, gestire il rischio e prendere decisioni razionali in condizioni di incertezza. Nel percorso dell'Ingegnere Gestionale, questo insegnamento costituisce il fondamento per il controllo statistico di qualità, la gestione dei processi produttivi e della supply chain, l'analisi dei dati di mercato, il data science e le simulazioni stocastiche di supporto alle decisioni aziendali.

### Competenze Acquisite
Al termine del corso, lo studente è in grado di:
- Analizzare dataset empirici attraverso gli strumenti della **statistica descrittiva** (distribuzioni di frequenza, indici di posizione come media, mediana e quantili, indici di dispersione come varianza e IQR, covarianza e retta di regressione lineare dei minimi quadrati).
- Formalizzare eventi casuali mediante l'**assiomatica di Kolmogorov**, applicare il calcolo combinatorio e calcolare probabilità composte.
- Padroneggiare la probabilità condizionata, il **Teorema delle Probabilità Totali** e il **Teorema di Bayes** per l'aggiornamento stocastico delle credenze e l'inversione causa-effetto.
- Definire e analizzare **variabili aleatorie unidimensionali e multidimensionali**, determinandone funzione di ripartizione (CDF), funzione di massa (PMF) o funzione di densità di probabilità (PDF).
- Calcolare valore atteso ($\mathbb{E}[X]$), varianza ($\operatorname{Var}(X)$), covarianza e matrice di covarianza, applicando il teorema LOTUS e le **disuguaglianze di Markov, Chebyshev e Jensen**.
- Studiare somme e trasformazioni di variabili aleatorie mediante **integrali di convoluzione** e funzioni generatrici dei momenti (MGF).
- Applicare i grandi teoremi asintotici del calcolo delle probabilità: la **Legge Debole dei Grandi Numeri (LLN)** e il **Teorema del Limite Centrale (CLT)** per l'approssimazione gaussiana di campioni finiti e dimensionamenti probabilistici.
- Padroneggiare le principali famiglie parametriche: **discrete** (Bernoulli, Binomiale, Poisson, Geometrica con assenza di memoria, Ipergeometrica, Binomiale Negativa) e **continue** (Uniforme, Esponenziale, Gaussiana, Gamma, Chi-quadro $\chi^2$, $t$ di Student, $F$ di Fisher-Snedecor).
- Costruire e valutare **stimatori puntuali** per campioni i.i.d., verificandone non-distorsione, errore quadratico medio (MSE) e consistenza, applicando il **Metodo dei Momenti** e il **Metodo della Massima Verosimiglianza (MLE)**, e valutando l'efficienza asintotica tramite l'**Informazione di Fisher** e il **Limite di Cramér-Rao**.
- Costruire **intervalli di confidenza** per media, varianza e proporzioni attraverso il metodo della quantità pivotale.
- Impostare ed eseguire **test di verifica delle ipotesi parametriche e non parametriche** ($H_0$ vs $H_1$, errori di I e II tipo $\alpha, \beta$, potenza $1-\beta$, $p$-value, Lemma di Neyman-Pearson, Z-test, t-test, test $\chi^2$ di indipendenza e bontà di adattamento).

### Programma Modulare per Macro-Aree
1. **Statistica Descrittiva e Probabilità Assiomatica:** Scale di misura, indici di posizione e variabilità, regressione lineare, assiomi di Kolmogorov, calcolo combinatorio, probabilità condizionata, formula delle probabilità totali e Teorema di Bayes.
2. **Variabili Aleatorie e Teoria dei Momenti:** CDF, PMF, PDF, quantili, valore atteso, varianza, disuguaglianze notevoli (Markov, Chebyshev), vettori aleatori congiunti e marginali, covarianza, convoluzione, MGF, Legge dei Grandi Numeri e Teorema del Limite Centrale.
3. **Classi di Leggi Notevoli:** Distribuzioni discrete notevoli e processo di Poisson; distribuzioni continue (Uniforme, Esponenziale, Normale standard e generale, $\chi^2$, Student, Fisher).
4. **Statistica Inferenziale (Stima Puntuale, Intervallare e Test d'Ipotesi):** Campione causale, proprietà degli stimatori, Metodo dei Momenti, Massima Verosimiglianza, Informazione di Fisher, Intervalli di confidenza con quantità pivotali, test d'ipotesi, regione critica, $p$-value, test $Z$, test $t$ di Student e test $\chi^2$.

---

## 📋 Regolamento Ufficiale d'Esame

L'esame di *Statistica e Calcolo delle Probabilità* verifica sia la capacità di risolvere problemi applicativi quantitativi sia la rigorosa comprensione teorico-matematica delle distribuzioni e dell'inferenza statistica.

### 1. Prove Scritte (Modalità Ordinaria e Appelli)
- **Formato e Durata:** La prova scritta ordinaria ha una durata di **2 ore - 2 ore e 30 minuti** ed è strutturata in 3–4 problemi articolati in vari punti:
  - *Problema 1 (Calcolo delle Probabilità & Bayes):* Modelli combinatori, probabilità condizionata, Teorema di Bayes o problemi di affidabilità a stadi multipli.
  - *Problema 2 (Variabili Aleatorie e Teoremi Limite):* Variabili continue o vettori bivariati con densità congiunta, calcolo di parametri, convoluzioni o dimensionamento campionario con il Teorema del Limite Centrale (CLT).
  - *Problema 3 (Stima Puntuale e Massima Verosimiglianza):* Modello parametrico, derivazione analitica degli stimatori di Massima Verosimiglianza (MLE) o Metodo dei Momenti, calcolo dell'Informazione di Fisher e verifica di efficienza.
  - *Problema 4 (Intervalli di Confidenza o Test d'Ipotesi):* Costruzione di intervalli di confidenza con quantità pivotali oppure esecuzione di un test d'ipotesi parametrico ($Z$-test, $t$-test) o non parametrico ($\chi^2$) con calcolo della regione di rifiuto e del $p$-value.
- **Punteggio e Soglia di Ammissione:** Il punteggio totale è di $30/30$. La soglia minima per il superamento o l'ammissione all'orale è di **$18/30$**.
- **Strumenti Ammessi:** È consentito l'uso di una calcolatrice scientifica non programmabile e delle tavole statistiche ufficiali (distribuzione Normale standard $\Phi(z)$, $t$ di Student, $\chi^2$).

### 2. Prove in Itinere (Compitini / Esoneri)
Nel corso del secondo semestre sono previste due prove scritte intermedie:
- **Primo Compitino (a metà semestre):** Copre Statistica descrittiva, Probabilità assiomatica, Calcolo combinatorio, Bayes, Variabili aleatorie discrete e continue, e Vettori aleatori (Capitoli 1–6).
- **Secondo Compitino (a fine semestre):** Copre Classi di leggi notevoli, Teoremi Limite (CLT/LLN), Teoria della Stima Puntuale, Massima Verosimiglianza, Intervalli di Confidenza e Test d'Ipotesi (Capitoli 7–11).
- **Regola di Esonero:** Lo studente ottiene l'esonero dalla prova scritta complessiva se consegue una votazione non inferiore a **$15/30$** in ciascun compitino e una media aritmetica complessiva $\ge 18/30$:
  $$V_{\text{scritto}} = \frac{V_1 + V_2}{2} \ge 18$$

### 3. Prova Orale
- **Ammissione:** Riservata a chi ha conseguito una votazione scritta $\ge 18/30$ (o esonero tramite compitini).
- **Contenuti dell'Orale:** Colloquio teorico approfondito con discussione dello scritto ed esposizione di:
  - Definizioni e proprietà formali dei modelli stocastici e delle quantità inferenziali.
  - **Dimostrazioni dei teoremi fondamentali** (es. Proprietà della CDF e PDF, Disuguaglianza di Chebyshev, Legge Debole dei Grandi Numeri da Chebyshev, Proprietà asintotiche degli stimatori MLE, Teorema di fattorizzazione, Limite di Cramér-Rao, Lemma di Neyman-Pearson).
  - Interpretazione probabilistica e geometrica dei modelli analitici e delle decisioni statistiche.

### 4. Criteri di Valutazione e Validità dei Voti
- **Voto Finale:** Risultante dalla valutazione congiunta della prova scritta e del colloquio orale.
- **Validità dei Compitini:** Gli esoneri da compitino sono utilizzabili per tutti gli appelli della sessione estiva e autunnale dell'anno accademico di erogazione.
- **Validità dello Scritto:** La prova scritta ordinaria è valida per sostenere l'orale nella medesima sessione d'esame.

---

## 🗂️ Navigazione Rapida e Risorse Disponibili

- 📘 [**Appunti delle Lezioni (`./notes/`)**](./notes/): Manuale completo in LaTeX (101 pagine), organizzato in 13 capitoli modulari con link per il download in 1-click di `appuntiStatistica.pdf`.
- 📝 [**Archivio Temi d'Esame Risolti (`./exams/`)**](./exams/): Archivio completo con tutti gli appelli d'esame ufficiali dal 2020 al 2024 e **10 fogli di esercizi settimanali** con soluzioni dettagliate e codici in linguaggio R.
- 📦 [**Materiale Didattico e Dispense (`./sources/`)**](./sources/): Dispense del docente, tavole statistiche e codici sorgente.

# 📚 Raccolta Temi d'Esame Passati con Soluzioni — Statistica I

Questa cartella raccoglie l'archivio completo di tutte le prove d'esame scritte ufficiali (compresi pre-test e appelli straordinari) e dei fogli di esercitazione settimanali di **Statistica I** (Corso di Laurea in Ingegneria Gestionale, Docente: Prof. Andrea Agazzi), organizzate per anno e nominate secondo lo standard cronologico ISO (`YYYY-MM-DD_<tipo_prova>.pdf` / `foglio_NN_<tipo>.pdf`).

Ogni file di soluzione include il **testo ufficiale della prova** seguito dallo **svolgimento analitico completo passo-passo**, con passaggi matematici espliciti, distribuzioni notevoli, calcoli numerici e codice R per le simulazioni computazionali e i metodi Monte Carlo.

---

## 🗂️ Struttura dell'Archivio

```
exams/
├── 2020/
│   ├── 2020-06_appello_1_soluzione.pdf
│   ├── 2020-06_appello_1_testo.pdf
│   ├── 2020-07_appello_2_soluzione.pdf
│   ├── 2020-07_appello_2_testo.pdf
│   ├── 2020-07_appello_3_soluzione.pdf
│   └── 2020-07_appello_3_testo.pdf
├── 2021/
│   ├── 2021-09-15_appello_2_soluzione.pdf
│   └── 2021-09-15_appello_2_testo.pdf
├── 2022/
│   ├── 2022-01-11_appello_straordinario_soluzione.pdf
│   ├── 2022-01-11_appello_straordinario_testo.pdf
│   ├── 2022-01-26_pretest_soluzione.pdf
│   ├── 2022-01-26_pretest_testo.pdf
│   ├── 2022-06-08_appello_1_soluzione.pdf
│   ├── 2022-06-08_appello_1_soluzione_ufficiale.pdf
│   ├── 2022-06-08_appello_1_testo.pdf
│   ├── 2022-07-20_appello_3_soluzione.pdf
│   ├── 2022-07-20_appello_3_soluzione_ufficiale.pdf
│   └── 2022-07-20_appello_3_testo.pdf
├── 2023/
│   ├── 2023-06-06_appello_1_soluzione.pdf
│   ├── 2023-06-06_appello_1_soluzione_ufficiale.pdf
│   ├── 2023-06-06_appello_1_testo.pdf
│   ├── 2023-06-27_appello_2_soluzione.pdf
│   ├── 2023-06-27_appello_2_soluzione_ufficiale.pdf
│   └── 2023-06-27_appello_2_testo.pdf
├── 2024/
│   ├── 2024-06-04_appello_1_soluzione.pdf
│   ├── 2024-06-04_appello_1_testo.pdf
│   ├── 2024-06-25_appello_2_soluzione.pdf
│   └── 2024-06-25_appello_2_testo.pdf
└── fogli_esercizi/
    ├── foglio_01_soluzione.pdf
    ├── foglio_01_testo.pdf
    ├── foglio_02_soluzione.pdf
    ├── foglio_02_testo.pdf
    ├── foglio_03_soluzione.pdf
    ├── foglio_03_testo.pdf
    ├── foglio_04_soluzione.pdf
    ├── foglio_04_testo.pdf
    ├── foglio_05_soluzione.pdf
    ├── foglio_05_testo.pdf
    ├── foglio_06_soluzione.pdf
    ├── foglio_06_testo.pdf
    ├── foglio_07_soluzione.pdf
    ├── foglio_07_testo.pdf
    ├── foglio_08_soluzione.pdf
    ├── foglio_08_testo.pdf
    ├── foglio_09_soluzione.pdf
    ├── foglio_09_testo.pdf
    ├── foglio_10_soluzione.pdf
    └── foglio_10_testo.pdf
```

---

## 📋 Dettaglio degli Appelli Disponibili

### 📅 Anno 2024
* [2024-06-04_appello_1_soluzione.pdf](2024/2024-06-04_appello_1_soluzione.pdf) (4 pagine - Soluzione completa) | [Testo PDF](2024/2024-06-04_appello_1_testo.pdf) (2 pagine)
  * Problema 1: Durata telefonate al centralino con legge esponenziale ($\lambda=1/3$), proprietà di assenza di memoria e calcolo di probabilità condizionate;
  * Problema 2: Processo di Poisson per difetti su valvole industriali ($\mu=7/6$), distribuzione della somma di v.a. di Poisson e approssimazione normale con Teorema del Limite Centrale (CLT);
  * Problema 3: Controllo qualità scarti chimici su 8 lotti, stima puntuale di media e varianza campionaria, Test $t$ di Student a 7 gradi di libertà (bilaterale) e calcolo del p-value;
  * Problema 4: Campione continuo da densità parametrizzata $f_\theta(x) = \frac{x}{\theta^2}e^{-x/\theta}$ (famiglia Gamma/Rayleigh), log-verosimiglianza, stimatore di massima verosimiglianza $\widehat{\theta}_{\text{MLE}}$, verifica di non distorsione (unbiasedness) e varianza asintotica;
  * Problema 5: Algoritmo di simulazione stocastica Monte Carlo in linguaggio R per l'approssimazione numerica di integrale fratto con peso gaussiano su intervallo infinito.
* [2024-06-25_appello_2_soluzione.pdf](2024/2024-06-25_appello_2_soluzione.pdf) (3 pagine - Soluzione completa) | [Testo PDF](2024/2024-06-25_appello_2_testo.pdf) (2 pagine)
  * Problema 1: Estrazione in blocco senza reinserimento da urna contenente 30 biglie tricolori, legge ipergeometrica multivariata e probabilità congiunte;
  * Problema 2: Confronto vendite boutique moda Parigi ($n_1=6$) vs Londra ($n_2=5$), Test $Z$ a due campioni indipendenti a varianze note, intervallo di confidenza per la differenza $\mu_1 - \mu_2$;
  * Problema 3: Diagnostica clinica su patologia rara, sensibilità e specificità del test, Teorema di Bayes su screening ripetuti indipendenti e probabilità a posteriori;
  * Problema 4: Campione da popolazione di Bernoulli($\theta$), derivazione esplicita dello stimatore MLE $\widehat{\theta} = \bar{X}_n$, calcolo dell'Informazione di Fisher $I_n(\theta)$ e verifica del raggiungimento del limite inferiore di Cramér-Rao (efficienza);
  * Problema 5: Integrazione Monte Carlo in R con densità di proposta uniforme per il calcolo di integrali definiti non risolubili elementarmente.

### 📅 Anno 2023
* [2023-06-06_appello_1_soluzione.pdf](2023/2023-06-06_appello_1_soluzione.pdf) (5 pagine - Soluzione estesa) | [Soluzione Ufficiale](2023/2023-06-06_appello_1_soluzione_ufficiale.pdf) (5 pagine) | [Testo PDF](2023/2023-06-06_appello_1_testo.pdf) (2 pagine)
  * Problema 1: Mazzo di 40 carte italiane, tempo di attesa per l'estrazione di una figura (legge Geometrica e Binomiale Negativa), valore atteso e varianza;
  * Problema 2: Durata di batterie alcaline Marca A vs Marca B, Test $Z$ su medie a varianza nota e intervallo di confidenza al $95\%$;
  * Problema 3: Modello di call center con flussi di arrivo di Poisson bivariati indipendenti ($\lambda_A=2, \lambda_B=3$), distribuzione della somma e probabilità condizionata;
  * Problema 4: Densità di Rayleigh parametrizzata $f_\theta(x) = \frac{2}{\theta}x e^{-x^2/\theta}$, stimatore MLE $\widehat{\theta}_{\text{MLE}} = \frac{1}{n}\sum X_i^2$, verifica di correttezza e consistenza;
  * Problema 5: Schema di integrazione Monte Carlo su intervallo limitato $[-3, 5]$ con stima dell'errore standard e script R.
* [2023-06-27_appello_2_soluzione.pdf](2023/2023-06-27_appello_2_soluzione.pdf) (5 pagine - Soluzione estesa) | [Soluzione Ufficiale](2023/2023-06-27_appello_2_soluzione_ufficiale.pdf) (5 pagine) | [Testo PDF](2023/2023-06-27_appello_2_testo.pdf) (2 pagine)
  * Problema 1: Scelta tra diverse linee produttive e pezzi difettosi, formula delle probabilità totali e Teorema di Bayes per l'attribuzione della causa del difetto;
  * Problema 2: Misurazione della concentrazione di PCB in 8 campioni biologici di salmone, media campionaria, intervallo di confidenza $t$-Student e test di ipotesi unilaterale;
  * Problema 3: Monitoraggio difetti di fabbricazione con processo di Poisson ($\lambda=1.5$), probabilità di assenza di anomalie in blocchi temporali e convergenza CLT;
  * Problema 4: Campionamento da popolazione con legge di potenza $f_\theta(x) = (1+\theta)x^\theta$ in $(0,1)$, calcolo dello stimatore MLE $\widehat{\theta}_{\text{MLE}} = -1 - \frac{n}{\sum \log X_i}$;
  * Problema 5: Metodo Monte Carlo in ambiente R per integrale gaussiano a campionamento ponderato (importance sampling).

### 📅 Anno 2022
* [2022-01-11_appello_straordinario_soluzione.pdf](2022/2022-01-11_appello_straordinario_soluzione.pdf) (5 pagine) | [Testo PDF](2022/2022-01-11_appello_straordinario_testo.pdf) (2 pagine)
  * Problema 1: Estrazione sequenziale da urne con composizione variabile e aggiornamento bayesiano;
  * Problema 2: Variabili aleatorie binarie a valori in $\{0,1\}$, indipendenza stocastica e distribuzione della somma discreta;
  * Problema 3: Indagine statistica sulla distanza casa-lavoro per i dipendenti di una startup, intervallo di confidenza per la media $\mu$ e Test $Z$;
  * Problema 4: Densità $f_\theta(x) = \theta^2 x e^{-\theta x}$, confronto tra stimatore ottenuto col Metodo dei Momenti e stimatore di Massima Verosimiglianza (MLE);
  * Problema 5: Simulazione Monte Carlo in R per integrale improprio a componente oscillante.
* [2022-01-26_pretest_soluzione.pdf](2022/2022-01-26_pretest_soluzione.pdf) (4 pagine) | [Testo PDF](2022/2022-01-26_pretest_testo.pdf) (2 pagine)
  * Problema 1: Analisi combinatoria per lotteria a premi multipli ed estrazioni senza reimmissione;
  * Problema 2: Variabili uniformi discrete su $\{-1, 0, 1\}$, convoluzione discreta e legge della somma;
  * Problema 3: Confronto prezzi di dispositivi elettronici su 7 piattaforme e-commerce, stima della media e deviazione standard, Test $t$ di Student;
  * Problema 4: Popolazione continua con CDF $F_\theta(x) = x^\theta$, determinazione dei quantili e costruzione di uno stimatore puntuale;
  * Problema 5: Integrazione Monte Carlo per funzione simmetrica su retta reale in R.
* [2022-06-08_appello_1_soluzione.pdf](2022/2022-06-08_appello_1_soluzione.pdf) (5 pagine) | [Soluzione Ufficiale](2022/2022-06-08_appello_1_soluzione_ufficiale.pdf) (3 pagine) | [Testo PDF](2022/2022-06-08_appello_1_testo.pdf) (2 pagine)
  * Problema 1: Variabili di Bernoulli indipendenti, probabilità congiunte e controllo qualità componenti;
  * Problema 2: Vettore aleatorio continuo definito su dominio triangolare con densità $f(x,y)=c(x+y)$, densità congiunta e marginali;
  * Problema 3: Somma di 100 variabili aleatorie uniformi indipendenti su $[-1, 5]$, calcolo di probabilità tramite approssimazione con Teorema del Limite Centrale;
  * Problema 4: Campione da densità uniforme traslata $f_\theta(x) = c_\theta \mathbf{1}_{[\theta, 1]}(x)$, stimatore MLE basato sulla statistica d'ordine minimo campionario $X_{(1)}$;
  * Problema 5: Integrazione Monte Carlo con integranda trigonometrica-esponenziale in R.
* [2022-07-20_appello_3_soluzione.pdf](2022/2022-07-20_appello_3_soluzione.pdf) (5 pagine) | [Soluzione Ufficiale](2022/2022-07-20_appello_3_soluzione_ufficiale.pdf) (3 pagine) | [Testo PDF](2022/2022-07-20_appello_3_testo.pdf) (3 pagine)
  * Problema 1: Modello di guasti con distribuzione di Poisson ($\lambda=2$) e approssimazione normale su base annuale con CLT;
  * Problema 2: Vettore aleatorio continuo su dominio rettangolare, densità congiunta e valore atteso condizionato;
  * Problema 3: Approssimazione Monte Carlo di integrale fratto nell'intervallo $[5, 9]$;
  * Problema 4: Misurazioni di temperatura, test di conformità della media con 8 osservazioni e intervallo di confidenza per la varianza con Chi-Quadro;
  * Problema 5: Campione con legge geometrica parametrizzata, stima MLE e intervallo di confidenza asintotico.

### 📅 Anno 2021
* [2021-09-15_appello_2_soluzione.pdf](2021/2021-09-15_appello_2_soluzione.pdf) (5 pagine - Soluzione completa) | [Testo PDF](2021/2021-09-15_appello_2_testo.pdf) (2 pagine)
  * Problema 1: Vettore aleatorio binario $(X,Y)$, determinazione della tabella di probabilità congiunta e calcolo dell'indice di correlazione lineare $\rho(X,Y)$;
  * Problema 2: 42 variabili uniformi indipendenti, trasformazione esponenziale $Y_i = -\log(X_i)$ e somma con Teorema del Limite Centrale;
  * Problema 3: Calcolo del carico per montacarichi ($2000\text{ kg}$), somma di pesi con distribuzione normale e probabilità di sovraccarico;
  * Problema 4: Densità triangolare simmetrica $f_a(x)$, stima del parametro $a$ con Metodo dei Momenti applicato a dataset CSV;
  * Problema 5: Analisi della percorrenza chilometrica di un campione di 200 autovetture, intervallo di confidenza al $99\%$ e test sulla media.

### 📅 Anno 2020
* [2020-06_appello_1_soluzione.pdf](2020/2020-06_appello_1_soluzione.pdf) (7 pagine - Soluzione completa) | [Testo PDF](2020/2020-06_appello_1_testo.pdf) (2 pagine)
  * Problema 1: Somma di v.a. Poisson($\lambda=3$) e Binomiale($n=4, p=1/2$), calcolo esplicito di valore atteso, varianza e funzione generatrice dei momenti;
  * Problema 2: Integrazione Monte Carlo in R per $\int_{-1}^1 \frac{e^{e^x}}{1+x^2}\mathrm{d}x$;
  * Problema 3: Distribuzione di Pareto con parametro di forma $\theta$, derivazione dello stimatore di massima verosimiglianza $\widehat{\theta}_{\text{MLE}}$;
  * Problema 4: Esperimento con lancio di 3 monete, formalizzazione dello spazio probabilistico $(\Omega, \mathcal{F}, \mathbb{P})$ e verifica di indipendenza stocastica;
  * Problema 5: Teoria asintotica: convergenza quasi certa e in probabilità per medie empiriche di variabili Esponenziali e Bernoulli;
  * Problema 6: Statistica descrittiva ed esplorativa su dataset CSV (istogramma delle frequenze, boxplot, quantili e media campionaria).
* [2020-07_appello_2_soluzione.pdf](2020/2020-07_appello_2_soluzione.pdf) (5 pagine - Soluzione completa) | [Testo PDF](2020/2020-07_appello_2_testo.pdf) (2 pagine)
  * Problema 1: Formula delle probabilità totali e Teorema di Bayes con eventi complementari e partizioni dello spazio campionario;
  * Problema 2: Simulazione Monte Carlo per integrale fratto su dominio illimitato con tracciamento grafico della convergenza in PDF;
  * Problema 3: Media empirica di $n$ variabili aleatorie di Poisson indipendenti e standardizzazione mediante Teorema del Limite Centrale;
  * Problema 4: Campione da popolazione $\operatorname{Unif}(-\theta, 4\theta)$, derivazione dello stimatore non distorto mediante il Metodo dei Momenti;
  * Problema 5: Vettore di variabili bernoulliane e calcolo della probabilità di eventi congiunti basati su minimo e massimo;
  * Problema 6: Sperimentazione clinica su efficacia terapeutica, test d'ipotesi unilaterale per proporzioni binarie a livello di significatività $\alpha=0.05$.
* [2020-07_appello_3_soluzione.pdf](2020/2020-07_appello_3_soluzione.pdf) (5 pagine - Soluzione completa) | [Testo PDF](2020/2020-07_appello_3_testo.pdf) (2 pagine)
  * Problema 1: Variabili aleatorie standardizzate indipendenti, disuguaglianza di Chebyshev sulla combinazione lineare $Z = X + Y$;
  * Problema 2: Algoritmo Monte Carlo in linguaggio R per la convergenza numerica di integrali definiti complessi;
  * Problema 3: Popolazione con funzione di ripartizione $F_\theta(x) = 1 - e^{-2\theta\sqrt{x}}$, stimatore MLE e metodo dell'inversione per la generazione di numeri pseudo-casuali;
  * Problema 4: Somma di 50 variabili uniformi indipendenti su $[-1, 1]$ con Teorema del Limite Centrale;
  * Problema 5: Controllo di conformità dimensionale su mine per matite, calcolo di media e deviazione standard campionaria, Test $t$ di Student a 2 code.

---

### 📝 Fogli di Esercitazione Settimanale (`fogli_esercizi/`)
I 10 fogli di esercitazione settimanali coprono in modo sistematico tutti i moduli teorico-pratici del corso di Statistica I:

* [foglio_01_soluzione.pdf](fogli_esercizi/foglio_01_soluzione.pdf) (2 pagine) | [Testo PDF](fogli_esercizi/foglio_01_testo.pdf) (1 pagina)
  * **Modulo:** Statistica descrittiva ed esplorativa dei dati;
  * **Contenuti:** Frequenze assolute e relative, media campionaria, varianza campionaria corretta, deviazione standard, mediana, quantili e rappresentazioni grafiche (istogrammi e boxplot).
* [foglio_02_soluzione.pdf](fogli_esercizi/foglio_02_soluzione.pdf) (5 pagine) | [Testo PDF](fogli_esercizi/foglio_02_testo.pdf) (1 pagina)
  * **Modulo:** Calcolo combinatorio e probabilità classica;
  * **Contenuti:** Disposizioni semplici e con ripetizione, permutazioni, combinazioni (coefficiente binomiale), partizioni d'insiemi ed estrazioni da urne.
* [foglio_03_soluzione.pdf](fogli_esercizi/foglio_03_soluzione.pdf) (4 pagine) | [Testo PDF](fogli_esercizi/foglio_03_testo.pdf) (1 pagina)
  * **Modulo:** Probabilità condizionata e indipendenza;
  * **Contenuti:** Definizione di probabilità condizionata, indipendenza stocastica tra eventi, formula delle probabilità totali e Teorema di Bayes (inferenza bayesiana).
* [foglio_04_soluzione.pdf](fogli_esercizi/foglio_04_soluzione.pdf) (3 pagine) | [Testo PDF](fogli_esercizi/foglio_04_testo.pdf) (1 pagina)
  * **Modulo:** Variabili aleatorie discrete unidimensionali;
  * **Contenuti:** Funzione di massa di probabilità (PMF), funzione di ripartizione cumulativa (CDF), valore atteso $\mathbb{E}[X]$, varianza $\operatorname{Var}(X)$ e proprietà di linearità.
* [foglio_05_soluzione.pdf](fogli_esercizi/foglio_05_soluzione.pdf) (5 pagine) | [Testo PDF](fogli_esercizi/foglio_05_testo.pdf) (1 pagina)
  * **Modulo:** Modelli probabilistici discreti notevoli;
  * **Contenuti:** Distribuzione di Bernoulli, Binomiale, Geometrica (assenza di memoria discreta), Binomiale Negativa, Ipergeometrica e Poisson (legge degli eventi rari).
* [foglio_06_soluzione.pdf](fogli_esercizi/foglio_06_soluzione.pdf) (7 pagine) | [Testo PDF](fogli_esercizi/foglio_06_testo.pdf) (1 pagina)
  * **Modulo:** Variabili aleatorie continue unidimensionali;
  * **Contenuti:** Funzione di densità di probabilità (PDF), valore atteso, varianza, percentili, distribuzione uniforme continua ed esponenziale con proprietà di assenza di memoria continua.
* [foglio_07_soluzione.pdf](fogli_esercizi/foglio_07_soluzione.pdf) (9 pagine) | [Testo PDF](fogli_esercizi/foglio_07_testo.pdf) (1 pagina)
  * **Modulo:** Vettori aleatori e distribuzioni multivariate;
  * **Contenuti:** Densità congiunte, distribuzioni marginali, distribuzioni condizionate, indipendenza stocastica, covarianza $\operatorname{Cov}(X,Y)$ e coefficiente di correlazione lineare $\rho(X,Y)$.
* [foglio_08_soluzione.pdf](fogli_esercizi/foglio_08_soluzione.pdf) (12 pagine) | [Testo PDF](fogli_esercizi/foglio_08_testo.pdf) (2 pagine)
  * **Modulo:** Distribuzione Normale (Gaussiana) e Teoremi Limite;
  * **Contenuti:** Variabile normale standard $\mathcal{N}(0,1)$, standardizzazione, uso delle tavole statistiche, combinazioni lineari gaussiane, Legge dei Grandi Numeri (WLLN/SLLN) e Teorema del Limite Centrale (CLT).
* [foglio_09_soluzione.pdf](fogli_esercizi/foglio_09_soluzione.pdf) (7 pagine) | [Testo PDF](fogli_esercizi/foglio_09_testo.pdf) (1 pagina)
  * **Modulo:** Teoria della stima puntuale e intervallare;
  * **Contenuti:** Metodo dei Momenti, stimatori di Massima Verosimiglianza (MLE), non distorsione, consistenza, Informazione di Fisher, limite di Cramér-Rao e intervalli di confidenza per la media a varianza nota/incognita.
* [foglio_10_soluzione.pdf](fogli_esercizi/foglio_10_soluzione.pdf) (9 pagine) | [Testo PDF](fogli_esercizi/foglio_10_testo.pdf) (2 pagine)
  * **Modulo:** Verifica delle ipotesi statistiche;
  * **Contenuti:** Ipotesi nulla $H_0$ e alternativa $H_1$, errori di I e II tipo, livello di significatività $\alpha$, potenza del test, Test $Z$, Test $t$ di Student a 1 e 2 campioni, calcolo analitico del $p$-value e regioni critiche di rifiuto.

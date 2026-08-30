# 📘 Appunti Digitalizzati di Fisica Generale I — Manuale Completo in LaTeX
**Corso di Laurea in Ingegneria Gestionale — Università di Pisa**

[![LaTeX Typeset](https://img.shields.io/badge/LaTeX-Typeset_Book-008080?style=flat&logo=latex&logoColor=white)](https://www.latex-project.org/)
[![Pagine](https://img.shields.io/badge/Volume-114_Pagine-orange.svg)](#)
[![1-Click PDF Download](https://img.shields.io/badge/Download_PDF-appuntiFisica.pdf-0052cc?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](https://github.com/Beccaceci/GESTIONALE/raw/main/courses/first_year/FISICA/notes/appuntiFisica.pdf)

Questo repository contiene l'opera completa e modulare in \LaTeX{} per la digitalizzazione, la formalizzazione teorica e l'approfondimento rigoroso del corso di **Fisica Generale I** (Meccanica Classica e Termodinamica, SSD FIS/01, 12 CFU) per il Corso di Laurea in Ingegneria Gestionale dell'Università di Pisa.

---

## 📥 Download Diretto del Manuale Compilato (1-Click)

È possibile scaricare il trattato completo ad altissima definizione direttamente dal link sottostante:

> 📄 **[Download `appuntiFisica.pdf`](https://github.com/Beccaceci/GESTIONALE/raw/main/courses/first_year/FISICA/notes/appuntiFisica.pdf)**

---

## 🏛️ Architettura Modulare del Progetto

Il progetto adotta un'architettura rigorosamente disaccoppiata e strutturata a capitoli indipendenti:

```text
FISICA/notes/
├── config/                                           # Configurazioni globali e stile tipografico LaTeX
│   ├── packages.tex                                  # Pacchetti (amsmath, amssymb, tikz, pgfplots, tcolorbox, siunitx, booktabs)
│   ├── environments.tex                              # Box tematici personalizzati (Definizione, Teorema, Legge, Metodo, Esame)
│   └── macros.tex                                    # Macro per vettori fisici, derivate temporali, termodinamica e operatori
├── chapters/                                         # 15 Moduli tematici indipendenti
│   ├── 01_introduzione_vettori/                      # Metodo scientifico, SI, analisi dimensionale, calcolo vettoriale
│   │   └── main.tex
│   ├── 02_cinematica_punto/                          # Vettori cinematici 1D/2D/3D, moti piani, terna intrinseca di Frenet
│   │   └── main.tex
│   ├── 03_dinamica_punto/                            # Principi di Newton, forze vincolari, attrito Coulomb-Amontons, molle
│   │   └── main.tex
│   ├── 04_sistemi_non_inerziali/                     # Moti relativi, accelerazione di trascinamento e forza di Coriolis
│   │   └── main.tex
│   ├── 05_lavoro_energia/                            # Lavoro, potenza, forze vive, forze conservative, potenziale ed energia
│   │   └── main.tex
│   ├── 06_sistemi_punti_urti/                        # Centro di massa, prima equazione cardinale, quantità di moto e urti
│   │   └── main.tex
│   ├── 07_momento_angolare_rotazione/                # Momento meccanico, momento angolare, seconda equazione cardinale, König
│   │   └── main.tex
│   ├── 08_dinamica_statica_corpo_rigido/             # Corpo rigido, Huygens-Steiner, puro rotolamento, percussioni e statica
│   │   └── main.tex
│   ├── 09_gravitazione_forze_centrali/               # Gravitazione di Newton, leggi di Keplero, potenziale efficace, orbite
│   │   └── main.tex
│   ├── 10_oscillazioni_onde/                         # Oscillatore armonico semplice, smorzato, forzato, risonanza, onde
│   │   └── main.tex
│   ├── 11_meccanica_fluidi/                          # Statica dei fluidi (Stevino, Pascal, Archimede), dinamica (Bernoulli)
│   │   └── main.tex
│   ├── 12_termodinamica_fondamenti/                  # Sistemi termodinamici, Principio Zero, temperatura, calorimetria
│   │   └── main.tex
│   ├── 13_gas_ideali_teoria_cinetica/                # Gas perfetti, teoria cinetica microscopica, equipartizione dell'energia
│   │   └── main.tex
│   ├── 14_primo_principio_trasformazioni/            # Lavoro nei piani P-V, Primo Principio, energia interna, Poisson
│   │   └── main.tex
│   └── 15_secondo_principio_entropia/                # Secondo Principio, Ciclo di Carnot, Disuguaglianza di Clausius, Entropia
│       └── main.tex
├── figures/                                          # Illustrazioni vettoriali TikZ, schemi cinematici e diagrammi P-V
├── appuntiFisica.pdf                                 # Manuale completo compilato in PDF ad alta risoluzione (114 pag.)
├── main.tex                                          # Documento radice master (Frontespizio, Indice generale, inclusioni)
└── README.md                                         # Questo documento di guida e documentazione
```

---

## 📚 Indice Dettagliato dei Capitoli e Mappa Concettuale

### Macro-Area 1: Cinematica e Dinamica del Punto Materiale
- **Capitolo 1 — Introduzione alla Fisica, Grandezze e Calcolo Vettoriale:** Il metodo scientifico galileiano, grandezze fondamentali e derivate del Sistema Internazionale (SI), omogeneità ed analisi dimensionale, propagazione delle incertezze, calcolo vettoriale (prodotto scalare, prodotto vettoriale con interpretazione geometrica dell'area del parallelogramma, prodotto misto e volume del parallelepipedo), stime di Fermi e ordini di grandezza.
- **Capitolo 2 — Cinematica del Punto Materiale in 1D, 2D e 3D:** Vettore posizione $\mathbf{r}(t)$, vettore velocità $\mathbf{v}(t) = \dot{\mathbf{r}}$ e accelerazione $\mathbf{a}(t) = \ddot{\mathbf{r}}$; problema inverso della cinematica con condizioni iniziali; moto rettilineo uniforme e uniformemente accelerato; cinematica bidimensionale dei proiettili nel piano verticale; coordinate polari piane; moto circolare uniforme e vario, velocità e accelerazione angolare ($\boldsymbol{\omega}, \boldsymbol{\alpha}$); terna intrinseca di Frenet-Serret con scomposizione dell'accelerazione in componente tangenziale ($a_t = \dot{v}$) e centripeta ($a_n = v^2/\rho$).
- **Capitolo 3 — Dinamica del Punto Materiale e Principi di Newton:** I tre principi fondamentali della dinamica newtoniana (principio d'inerzia e sistemi inerziali, equazione fondamentale $\mathbf{F} = m\mathbf{a}$, principio di azione e reazione); interazioni fondamentali della meccanica: forza peso, forze vincolari normali e di reazione, forza elastica lineare di Hooke; forze di attrito radente statico ($F_s \le \mu_s N$) e dinamico ($F_d = \mu_d N$) col modello di Coulomb-Amontons; moto in mezzo viscoso laminare con forza di Stokes e determinazione della velocità limite.
- **Capitolo 4 — Moti Relativi e Sistemi di Riferimento Non Inerziali:** Trasformazioni galileiane di coordinate e velocità; Teorema di composizione delle accelerazioni di Coriolis:
  $$\mathbf{a}_a = \mathbf{a}_r + \mathbf{a}_O + \boldsymbol{\alpha}\times\mathbf{r}' + \boldsymbol{\omega}\times(\boldsymbol{\omega}\times\mathbf{r}') + 2\boldsymbol{\omega}\times\mathbf{v}_r$$
  Dinamica nei riferimenti accelerati e forze fittizie: forza di trascinamento $\mathbf{F}_t = -m\mathbf{a}_t$ e **forza di Coriolis** $\mathbf{F}_C = -2m(\boldsymbol{\omega}\times\mathbf{v}_r)$; effetti della rotazione terrestre sulla caduta dei gravi e sul pendolo di Foucault.

### Macro-Area 2: Leggi di Conservazione, Urti e Dinamica del Corpo Rigido
- **Capitolo 5 — Lavoro, Energia, Forze Conservative e Conservazione:** Lavoro infinitesimo $\delta W = \mathbf{F}\cdot d\mathbf{r}$ e integrale curvilineo di lavoro lungo una traiettoria; potenza istantanea e media $P = \mathbf{F}\cdot\mathbf{v}$; **Teorema dell'Energia Cinetica (delle Forze Vive)** $W_{\text{tot}} = \Delta E_k$; campi di forza conservativi e condizione di irrotazionalità $\nabla \times \mathbf{F} = \mathbf{0}$; energia potenziale $E_p$ legata alla forza da $\mathbf{F} = -\nabla E_p$; legge di conservazione dell'energia meccanica totale $E_m = E_k + E_p$; bilancio energetico in presenza di forze non conservative $W_{nc} = \Delta E_m$.
- **Capitolo 6 — Sistemi di Punti Materiali, Centro di Massa e Urti:** Posizione e velocità del centro di massa $\mathbf{r}_{CM} = \frac{1}{M}\sum m_i \mathbf{r}_i$, quantità di moto totale $\mathbf{P} = M\mathbf{v}_{CM}$; **Prima Equazione Cardinale della Meccanica** $\mathbf{R}^{(E)} = \frac{d\mathbf{P}}{dt}$ e conservazione della quantità di moto per sistemi isolati; teoria generale degli urti meccanici (istantaneità e forze impulsive): urti perfettamente elastici (conservazione di $\mathbf{P}$ ed $E_k$), urti completamente anelastici (massima dissipazione di energia con moto solidale finale) e urti parzialmente anelastici con coefficiente di restituzione nel laboratorio e nel riferimento del centro di massa.
- **Capitolo 7 — Momento Angolare, Momento Meccanico e Rotazioni:** Momento meccanico di una forza rispetto a un polo $\boldsymbol{\tau} = \mathbf{r}\times\mathbf{F}$; momento angolare $\mathbf{L} = \mathbf{r}\times\mathbf{p}$; **Seconda Equazione Cardinale della Meccanica**:
  $$\mathbf{M}^{(E)}_O = \frac{d\mathbf{L}_O}{dt} + \mathbf{v}_O \times \mathbf{P}$$
  **Secondo Teorema di König** per il momento angolare ($\mathbf{L}_O = \mathbf{L}'_{CM} + \mathbf{r}_{CM}\times M\mathbf{v}_{CM}$); legge di conservazione del momento angolare in campi centrali e sistemi con momenti esterni nulli.
- **Capitolo 8 — Statica e Dinamica del Corpo Rigido:** Cinematica dei corpi indeformabili, formula fondamentale $\mathbf{v}_P = \mathbf{v}_O + \boldsymbol{\omega}\times\mathbf{r}_{OP}$; calcolo del momento d'inerzia $I_z = \int r_\perp^2\,dm$ per geometrie notevoli (aste, dischi, cilindri, sfere); **Teorema di Huygens-Steiner degli assi paralleli** ($I_z = I_{CM} + M d^2$); equazione del moto rotatorio attorno a un asse fisso $\tau_z = I_z \alpha$; **Primo Teorema di König** per l'energia cinetica $E_k = \frac{1}{2}M v_{CM}^2 + \frac{1}{2}I_{CM}\omega^2$; condizioni cinematiche e dinamiche di **puro rotolamento** ($v_{CM} = \omega R$ e $a_{CM} = \alpha R$) con attrito statico; equazioni cardinali della statica e percussioni su corpi rigidi.

### Macro-Area 3: Gravitazione, Meccanica dei Fluidi ed Oscillazioni
- **Capitolo 9 — Gravitazione Universale e Dinamica Planetaria:** Legge di gravitazione universale di Newton, energia potenziale gravitazionale $E_p(r) = -G\frac{Mm}{r}$, calcolo della velocità di fuga, studio del moto in campo centrale con conservazione del momento angolare, costanza della velocità areolare e Seconda Legge di Keplero, potenziale efficace unidimensionale $V_{\text{eff}}(r) = \frac{L^2}{2mr^2} - \frac{GMm}{r}$, classificazione delle orbite coniche (ellittiche, paraboliche, iperboliche) e Terza Legge di Keplero.
- **Capitolo 10 — Oscillazioni Meccaniche, Risonanza e Fenomeni Ondulatori:** Oscillatore armonico semplice libero $\ddot{x} + \omega_0^2 x = 0$, determinazione della pulsazione naturale $\omega_0$, ampiezza e fase iniziale; pendolo semplice e pendolo fisico; oscillatore armonico smorzato viscoso (regime sottosmorzato con decadimento esponenziale, smorzamento critico e sovrasmorzato); oscillatore armonico forzato con forzante sinusoidale, risposta in regime permanente, curva di risonanza dell'ampiezza e fattore di qualità $Q$; introduzione alle onde meccaniche e propagazione.
- **Capitolo 11 — Meccanica dei Fluidi: Statica e Dinamica:** Statica dei fluidi continui, pressione idrostatica, **Legge di Stevino** $p = p_0 + \rho g h$, **Principio di Pascal** e torchio idraulico, **Principio di Archimede** e stabilità del galleggiamento; dinamica dei fluidi ideali (incomprimibili e non viscosi): linee di flusso, portata volumetrica ed equazione di continuità ($S_1 v_1 = S_2 v_2$), **Teorema di Bernoulli**:
  $$p + \frac{1}{2}\rho v^2 + \rho g z = \text{costante}$$
  Applicazioni ingegneristiche: tubo di Venturi, tubo di Pitot, e svuotamento di serbatoi con la formula di Torricelli.

### Macro-Area 4: Termodinamica Classica e Teoria Cinetica
- **Capitolo 12 — Fondamenti di Termodinamica, Temperatura e Calore:** Sistemi termodinamici (aperti, chiusi, isolati), pareti diabatiche e adiabatiche, variabili di stato macroscopiche e condizioni di equilibrio termodinamico, **Principio Zero della Termodinamica** e definizione di temperatura empirica, calore come forma di scambio microscopico di energia, capacità termica $C$, calore specifico molare e massico, calorimetria a miscela e calori latenti di transizione di fase.
- **Capitolo 13 — Gas Perfetti e Teoria Cinetica Molecolare:** Equazione di stato dei gas perfetti $PV = nRT$, modello microscopico dei gas ideali, derivazione cinetico-meccanica della pressione $P = \frac{2}{3}\frac{N}{V}\langle E_{k,\text{trasl}}\rangle$, interpretazione molecolare della temperatura ($\langle E_k \rangle = \frac{3}{2}k_B T$), **Teorema di Equipartizione dell'Energia**, gradi di libertà molecolari (gas monoatomici e biatomici), calori specifici $C_v, C_p$, e **Relazione di Mayer** ($C_p - C_v = R$).
- **Capitolo 14 — Lavoro Termodinamico e Primo Principio della Termodinamica:** Lavoro termodinamico di variazione volumica $\delta W = P\,dV$ e rappresentazione grafica nel piano di Clapeyron $P$-$V$, **Primo Principio della Termodinamica** ($Q - W = \Delta U$), conservazione dell'energia, energia interna $U$ come funzione di stato dipendente solo da $T$ nei gas ideali ($dU = n C_v dT$); calcolo analitico completo di $Q, W, \Delta U$ per trasformazioni quasi-statiche e reversibili:
  - *Isocore* ($V=\text{cost}$, $W=0$, $Q=\Delta U = n C_v \Delta T$);
  - *Isobare* ($P=\text{cost}$, $W=P\Delta V$, $Q=n C_p \Delta T$, $\Delta U = n C_v \Delta T$);
  - *Isoterme* ($T=\text{cost}$, $\Delta U=0$, $Q=W = nRT\ln(V_f/V_i)$);
  - *Adiabatiche reversibili* ($Q=0$, $W=-\Delta U$, formule di Poisson $PV^\gamma = \text{cost}$, $TV^{\gamma-1} = \text{cost}$, $T^\gamma P^{1-\gamma} = \text{cost}$).
- **Capitolo 15 — Secondo Principio della Termodinamica ed Entropia:** Irreversibilità dei fenomeni naturali e freccia del tempo; macchine termiche motrici e frigorifere, rendimento $\eta = W/Q_h$ e coefficiente di prestazione COP; **enunciato di Kelvin-Planck** e **enunciato di Clausius** del Secondo Principio ed equivalenza formale; il **Ciclo di Carnot** e dimostrazione del **Teorema di Carnot** ($\eta \le 1 - T_c/T_h$); **Disuguaglianza di Clausius** ($\oint \frac{\delta Q}{T} \le 0$); definizione della funzione di stato **Entropia** ($dS = \frac{\delta Q_{\text{rev}}}{T}$); calcolo delle variazioni di entropia del sistema, delle sorgenti e dell'universo; interpretazione statistica di Boltzmann ($S = k_B \ln \Omega$); principio di non-diminuzione dell'entropia dell'universo ($\Delta S_{\text{universo}} \ge 0$).

---

## 🎨 Ambienti Tipografici e Box Tematici (`tcolorbox`)

| Ambiente | Colore Bordo / Titolo | Finalità Didattica |
| :--- | :--- | :--- |
| `\begin{definizione}{Nome}{label}` | **Navy Blue** (`#003366`) | Grandezze fisiche, vettori, coordinate e definizioni operative |
| `\begin{legge}{Nome}{label}` | **Purple Accent** (`#6A1B9A`) | Principi fondamentali di Newton, I e II principio della termodinamica |
| `\begin{teorema}{Nome}{label}` | **Forest Green** (`#2E7D32`) | Teoremi cardine (forze vive, conservazione, König, Carnot, Bernoulli) |
| `\begin{proposizione}{Nome}{label}` | **Teal Blue** (`#00838F`) | Proprietà fisiche e relazioni intermedie |
| `\begin{dimostrazione}` | **Verde barra sinistra** | Dimostrazioni analitiche rigorose chiuse dal quadratino $\blacksquare$ |
| `\begin{metodo}[Titolo]` | **Warm Amber** (`#FF8F00`) | Algoritmi procedurali di impostazione e risoluzione fisica |
| `\begin{esame}[Titolo]` | **Crimson Red** (`#C62828`) | Consigli d'esame, errori concettuali, dimensionali e tranelli |
| `\begin{esercizio}[Titolo]` | **Amber** (`#FFA000`) | Esercizi quantitativi d'esame guidati con calcoli espliciti |
| `\begin{esperimento}[Titolo]` | **Dark Cyan** (`#00838F`) | Fenomenologia sperimentale ed evidenze fisiche di laboratorio |
| `\begin{osservazione}[Titolo]` | **Slate Gray** (`#37474F`) | Note teoriche a margine e limiti di validità dei modelli classici |

---

## 🛠️ Istruzioni per la Compilazione Locale

### 1. Compilazione Completa del Volume
Per compilare l'intero trattato e generare `appuntiFisica.pdf`:

```bash
# Tramite latexmk (consigliato):
latexmk -pdf main.tex

# Oppure tramite pdflatex (eseguire due volte per allineare riferimenti e ToC):
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```

### 2. Compilazione Rapida di Singoli Capitoli (`\includeonly`)
Nel file [`main.tex`](./main.tex), scommentare la direttiva `\includeonly{...}` specificando solo il capitolo su cui si sta lavorando per velocizzare la build:

```latex
\includeonly{
  chapters/08_dinamica_statica_corpo_rigido/main
}
```

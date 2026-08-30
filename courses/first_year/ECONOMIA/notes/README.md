# 📘 Appunti Digitalizzati di Istituzioni di Economia — Manuale Completo in LaTeX
**Corso di Laurea in Ingegneria Gestionale — Università di Pisa**

[![LaTeX Typeset](https://img.shields.io/badge/LaTeX-Typeset_Book-008080?style=flat&logo=latex&logoColor=white)](https://www.latex-project.org/)
[![Pagine](https://img.shields.io/badge/Volume-226_Pagine-orange.svg)](#)
[![1-Click PDF Download](https://img.shields.io/badge/Download_PDF-appuntiEconomia.pdf-0052cc?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](https://github.com/Beccaceci/GESTIONALE/raw/main/courses/first_year/ECONOMIA/notes/appuntiEconomia.pdf)

Questo repository contiene il manuale enciclopedico, formale e integrato in \LaTeX{} per il corso di **Istituzioni di Economia** (Microeconomia e Macroeconomia, SSD SECS-P/01, 9 CFU) per il Corso di Laurea in Ingegneria Gestionale dell'Università di Pisa.

---

## 📥 Download Diretto del Manuale Compilato (1-Click)

È possibile scaricare il volume completo ad altissima definizione direttamente dal link sottostante:

> 📄 **[Download `appuntiEconomia.pdf`](https://github.com/Beccaceci/GESTIONALE/raw/main/courses/first_year/ECONOMIA/notes/appuntiEconomia.pdf)**

---

## 🏛️ Architettura Modulare del Progetto

Il progetto adotta un'architettura modulare a capitoli indipendenti:

```text
ECONOMIA/notes/
├── config/                                           # Configurazioni globali LaTeX
│   ├── packages.tex                                  # Pacchetti (microtype, tikz, pgfplots, booktabs, geometry, amsmath)
│   ├── environments.tex                              # Ambienti tcolorbox stilizzati (Definizione, Modello, Legge, Teorema, Metodo, Esame)
│   └── macros.tex                                    # Notazione economica formale unificata (Micro & Macro)
├── chapters/                                         # 18 Moduli tematici indipendenti
│   ├── 01_scienza_economica/                         # Scarsità, costo opportunità, Frontiera FPP, efficienza economica
│   │   └── main.tex
│   ├── 02_strumenti_analisi_economica/               # Variabili nominali/reali, numeri indice, equazioni e pendenze cartesiane
│   │   └── main.tex
│   ├── 03_domanda_offerta_mercato/                   # Curve di mercato, prezzo di equilibrio, surplus del consumatore/produttore
│   │   └── main.tex
│   ├── 04_elasticita_domanda_offerta/                # Elasticità al prezzo, al reddito, incrociata e relazione con il ricavo
│   │   └── main.tex
│   ├── 05_scelta_consumatore_domanda/                # Curve indifferenza, SMS, vincolo bilancio, ottimo con Lagrange, Hicks/Slutsky
│   │   └── main.tex
│   ├── 06_introduzione_teoria_offerta/               # Impresa, massimizzazione profitto, ricavo/costo marginale, chiusura
│   │   └── main.tex
│   ├── 07_tecnologia_costi/                          # Cobb-Douglas, rendimenti di scala, SMST, costi breve/lungo periodo
│   │   └── main.tex
│   ├── 08_strutture_mercato/                         # Concorrenza perfetta, monopolio, Lerner, oligopoli Cournot/Bertrand/Stackelberg
│   │   └── main.tex
│   ├── 09_informazione_rischio/                      # Utilità attesa Von Neumann-Morgenstern, adverse selection, moral hazard
│   │   └── main.tex
│   ├── 10_introduzione_macroeconomia/                # PIL (spesa, valore aggiunto, reddito), PIN, PNL, contabilità nazionale
│   │   └── main.tex
│   ├── 11_prodotto_nazionale_spesa_aggregata/        # Modello reddito-spesa, croce keynesiana, moltiplicatore della spesa
│   │   └── main.tex
│   ├── 12_politica_fiscale_commercio_estero/         # Spesa pubblica, imposte, deficit, debito pubblico, moltiplicatore aperto
│   │   └── main.tex
│   ├── 13_moneta_politica_monetaria/                 # Moneta M1/M2/M3, moltiplicatore monetario, domanda di moneta, BCE
│   │   └── main.tex
│   ├── 14_mercato_monetario_reale_is_lm/             # Costruzione curve IS e LM, equilibrio congiunto, crowding out, trappola liquidità
│   │   └── main.tex
│   ├── 15_equilibrio_domanda_offerta_aggregata/      # Modello AD-AS, derivazione AD da IS-LM, offerta classica/keynesiana, stagflazione
│   │   └── main.tex
│   ├── 16_inflazione_disoccupazione/                 # Disoccupazione, Legge di Okun, Curva di Phillips, tasso naturale NAIRU
│   │   └── main.tex
│   ├── 17_tassi_cambio_bilancia_pagamenti/           # Cambi nominali/reali, Forex, PPP, UIP, struttura Bilancia dei Pagamenti
│   │   └── main.tex
│   └── 18_macroeconomia_sistemi_aperti/              # Modello Mundell-Fleming (IS-LM-BP), regimi di cambio fissi/flessibili, Trilemma
│       └── main.tex
├── figures/                                          # Oltre 100 grafici e curve analitiche TikZ e PGFPlots
├── appuntiEconomia.pdf                               # Trattato enciclopedico compilato in PDF ad alta risoluzione (226 pag.)
├── main.tex                                          # Documento master (Frontespizio, Indice generale, inclusioni)
└── README.md                                         # Questo documento di guida e documentazione
```

---

## 📚 Indice Dettagliato dei Capitoli e Mappa Concettuale

### Modulo I: Fondamenti Metodologici e Strumenti Quantitativi
- **Capitolo 1 — La Scienza Economica:** Concetto di scarsità, bisogni e risorse, costo opportunità, Frontiera delle Possibilità Produttive (FPP), efficienza produttiva ed allocativa, trade-off microeconomici, economia positiva vs economia normativa.
- **Capitolo 2 — Gli Strumenti dell'Analisi Economica:** Costruzione dei modelli economici, variabili endogene ed esogene, grandezze nominali e reali, numeri indice, serie storiche, pendenza cartesiana, interpretazione della derivata come valore marginale.

### Modulo II: Microeconomia — Teoria del Consumo, Produzione e Mercato
- **Capitolo 3 — Domanda, Offerta e Mercato:** Scheda e curva di domanda, scheda e curva di offerta, prezzo di equilibrio walrasiano, meccanismo di aggiustamento dei prezzi, statica comparata, surplus del consumatore, surplus del produttore ed efficienza economica paretiana.
- **Capitolo 4 — Elasticità di Domanda e Offerta:** Elasticità della domanda al prezzo $\varepsilon_p = -\frac{\% \Delta Q}{\% \Delta P}$, punto elastico, anelastico e a elasticità unitaria; relazione analitica tra elasticità e ricavo totale $TR = P \cdot Q$; elasticità della domanda al reddito (beni normali, necessari, di lusso e inferiori); elasticità incrociata (beni sostituti e complementi); elasticità dell'offerta nel breve e lungo periodo.
- **Capitolo 5 — Teoria del Consumatore:** Assiomi di preferenza (completezza, transitività, monotonicità, convessità), funzione di utilità ordinale $U(x_1, x_2)$, curve di indifferenza e Saggio Marginale di Sostituzione (SMS), vincolo di bilancio $p_1 x_1 + p_2 x_2 \le I$, massimizzazione vincolata dell'utilità con moltiplicatori di Lagrange ($SMS = p_1/p_2$), derivazione della curva di domanda individuale, effetto prezzo, scomposizione in **effetto sostituzione ed effetto reddito (metodi di Slutsky e Hicks)**, paradosso dei beni di Giffen.
- **Capitolo 6 — Teoria dell'Offerta e dell'Impresa:** L'impresa come funzione di trasformazione, massimizzazione del profitto economico $\Pi = TR - TC$, ricavo medio e marginale ($MR$), costo marginale ($MC$), condizione marginale di ottimo $MR = MC$, condizioni di sospensione dell'attività nel breve periodo e di uscita dal mercato nel lungo periodo.
- **Capitolo 7 — Tecnologia e Costi di Produzione:** Funzione di produzione $Q = F(K,L)$, isoquanti, Saggio Marginale di Sostituzione Tecnica (SMST), legge dei rendimenti decrescenti del lavoro, rendimenti di scala (crescenti, costanti, decrescenti), funzione Cobb-Douglas; sentiero di espansione della produzione e isocosti; struttura dei costi di breve periodo (TFC, TVC, TC, AFC, AVC, ATC, MC) e inviluppo delle curve di costo medio di lungo periodo (LRAC), economie e diseconomie di scala.
- **Capitolo 8 — Strutture di Mercato:** 
  - *Concorrenza Perfetta:* Price-taking, curva di offerta dell'impresa $P = MC$, equilibrio di breve e lungo periodo con profitto economico nullo $P = \min(ATC)$.
  - *Monopolio Puro:* Monopolista monoricavo, condizione $MR = MC$, indice di potere monopolistico di Lerner $L = \frac{P-MC}{P} = \frac{1}{|\varepsilon|}$, perdita secca di monopolio (*deadweight loss*), discriminazione di prezzo di I, II e III grado.
  - *Concorrenza Monopolistica:* Differenziazione del prodotto, equilibrio tangenziale di Chamberlin nel lungo periodo.
  - *Oligopoli Non Cooperativi:* Modello di Cournot (scelta simultanea delle quantità e funzioni di reazione), modello di Bertrand (competizione di prezzo e paradosso di Bertrand), modello di Stackelberg (gioco sequenziale con leader e follower).
- **Capitolo 9 — Informazione e Incertezza:** Scelte in condizioni di rischio, teoria dell'utilità attesa di Von Neumann-Morgenstern $E[U]$, attitudine al rischio (avversione, neutralità, propensione), equivalente certo e premio per il rischio; asimmetrie informative contrattuali: selezione avversa (*adverse selection* nel mercato dei limoni di Akerlof e modelli di segnalazione) e azzardo morale (*moral hazard* nel rapporto principale-agente e contratti di incentivazione).

### Modulo III: Macroeconomia — Contabilità, Mercati Reali e Monetari (IS-LM)
- **Capitolo 10 — Introduzione alla Macroeconomia e Contabilità Nazionale:** Flusso circolare del reddito, identità fondamentale della contabilità nazionale, Prodotto Interno Lordo (PIL) calcolato con il metodo della spesa ($Y = C + I + G + NX$), del valore aggiunto e del reddito dei fattori; PIL nominale, PIL reale, deflatore del PIL, PIN, PNL e reddito disponibile.
- **Capitolo 11 — Prodotto Nazionale e Spesa Aggregata:** Il modello reddito-spesa keynesiano, la croce keynesiana a 45 gradi, funzione del consumo keynesiana $C = C_0 + cY$, propensione marginale al consumo $c$, investimenti esogeni, equilibrio macroeconomico del reddito e moltiplicatore della spesa autonoma $\alpha = \frac{1}{1-c}$.
- **Capitolo 12 — Politica Fiscale e Settore Estero:** Spesa pubblica $G$, imposte esogene $T_0$ e proporzionali al reddito $tY$, bilancio dello Stato, disavanzo pubblico e debito pubblico; stabilizzatori automatici; importazioni, esportazioni e moltiplicatore in economia aperta $\alpha_{\text{aperta}} = \frac{1}{1-c(1-t)+m}$.
- **Capitolo 13 — Moneta, Sistema Bancario e Politica Monetaria:** Funzioni della moneta, aggregati M1, M2, M3; la Banca Centrale, banche commerciali, coefficiente di riserva, base monetaria e moltiplicatore monetario dei depositi; la domanda di moneta keynesiana (transattiva, precauzionale, speculativa in funzione del tasso d'interesse $i$); equilibrio sul mercato monetario e strumenti della BCE.
- **Capitolo 14 — Il Modello IS-LM:** Derivazione geometrica ed analitica della curva IS (equilibrio sul mercato dei beni) e della curva LM (equilibrio sul mercato monetario); equilibrio simultaneo $(Y^*, i^*)$; analisi delle politiche fiscali espansive ed **effetto spiazzamento (*crowding-out*)** della spesa privata; efficacia della politica monetaria, **trappola della liquidità** keynesiana e mix di politica economica.

### Modulo IV: Macroeconomia Dinamica — AD-AS, Inflazione, Lavoro e Sistemi Aperti
- **Capitolo 15 — Il Modello Domanda-Offerta Aggregata (AD-AS):** Derivazione della curva di Domanda Aggregata AD dal modello IS-LM al variare del livello dei prezzi $P$; curva di Offerta Aggregata AS classica verticale nel lungo periodo e AS inclinata positivamente nel breve periodo; equilibrio macroeconomico generale, shock di domanda, shock da costi di offerta e fenomeno della **stagflazione**.
- **Capitolo 16 — Inflazione, Disoccupazione e Curva di Phillips:** Indicatori del mercato del lavoro (tasso di occupazione, disoccupazione, inattività); disoccupazione frizionale, strutturale e ciclica; **Legge di Okun**; cause e costi dell'inflazione; la **Curva di Phillips originaria** (trade-off inflazione-disoccupazione), la critica monetarista di Friedman-Phelps, aspettative adattive, tasso naturale di disoccupazione (NAIRU) e curva di Phillips verticale di lungo periodo.
- **Capitolo 17 — Tassi di Cambio e Bilancia dei Pagamenti:** Mercato valutario Forex, tasso di cambio nominale (quotazione certo per incerto), tasso di cambio reale e competitività delle esportazioni, teoria della **Parità dei Poteri d'Acquisto (PPP)**, condizione di **Parità Scoperta dei Tassi d'Interesse (UIP)**; struttura contabile della Bilancia dei Pagamenti (Conto Corrente, Conto Capitale, Conto Finanziario) e saldo complessivo.
- **Capitolo 18 — Macroeconomia dei Sistemi Aperti: Il Modello Mundell-Fleming:** Estensione del modello IS-LM ad un'economia aperta con perfetta mobilità dei capitali (curva BP orizzontale al livello del tasso d'interesse mondiale $i = i^*$); efficacia della politica fiscale e monetaria in regime di **tassi di cambio fissi**; efficacia della politica fiscale e monetaria in regime di **tassi di cambio flessibili**; formulazione del **Trilemma di Politica Monetaria di Mundell** (impossibilità di coesistenza tra cambi fissi, perfetta mobilità dei capitali e autonomia della politica monetaria).

---

## 🎨 Ambienti Tipografici e Box Tematici (`tcolorbox`)

| Ambiente | Colore Bordo / Titolo | Finalità Didattica |
| :--- | :--- | :--- |
| `\begin{definizione}{Nome}{label}` | **Corporate Blue** (`#003366`) | Definizioni formali dei concetti economici e variabili di stato |
| `\begin{modello}{Nome}{label}` | **Deep Violet** (`#4A148C`) | Modelli analitici (IS-LM, AD-AS, Mundell-Fleming, Cournot) |
| `\begin{legge}{Nome}{label}` | **Teal Accent** (`#00695C`) | Leggi di mercato, assiomi di preferenza e principi universali |
| `\begin{teorema}{Nome}{label}` | **Forest Green** (`#2E7D32`) | Teoremi economici, proprietà analitiche e condizioni di ottimo |
| `\begin{dimostrazione}` | **Verde barra sinistra** | Derivazioni algebriche e dimostrazioni formali chiuse da $\blacksquare$ |
| `\begin{metodo}[Titolo]` | **Warm Amber** (`#FF8F00`) | Algoritmi procedurali di calcolo (es. moltiplicatori, equilibri) |
| `\begin{esame}[Titolo]` | **Crimson Red** (`#C62828`) | Consigli d'esame, errori concettuali e trabocchetti frequenti |
| `\begin{esempio}[Titolo]` | **Cobalt Blue** (`#1565C0`) | Esempi numerici di mercato ed esercizi guidati |
| `\begin{osservazione}[Titolo]` | **Slate Gray** (`#37474F`) | Intuizione economica e commenti di politica economica a margine |

---

## 🛠️ Istruzioni per la Compilazione Locale

### 1. Compilazione Completa del Volume
Per compilare l'intero trattato e generare `appuntiEconomia.pdf`:

```bash
# Tramite latexmk (consigliato):
latexmk -pdf main.tex

# Oppure tramite pdflatex (eseguire due volte per allineare l'indice analitico):
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```

### 2. Compilazione Rapida di Singoli Capitoli (`\includeonly`)
Nel file [`main.tex`](./main.tex), scommentare la direttiva `\includeonly{...}` indicando il capitolo specifico per una compilazione istantanea:

```latex
\includeonly{
  chapters/14_mercato_monetario_reale_is_lm/main
}
```

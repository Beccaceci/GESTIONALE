# Project: Istituzioni di Economia — Digitalizzazione e Trattazione Integrale

## Architecture
- **Master Root**: `ECONOMIA/main.tex` (book class, fronte-retro, 5 Parti tematiche).
- **Configuration Modules**:
  * `ECONOMIA/config/packages.tex`: pacchetti tipografici, matematici, TikZ e pgfplots.
  * `ECONOMIA/config/environments.tex`: palette colori istituzionale e 11 ambienti `tcolorbox` (`definizione`, `modello`, `legge`, `teorema`, `dimostrazione`, `metodo`, `esame`, `esempio`, `esercizio`, `osservazione`, `empirico`).
  * `ECONOMIA/config/macros.tex`: notazione standardizzata Micro e Macro.
- **Modular Chapters**: `ECONOMIA/chapters/01_...` a `18_...` con inclusione dinamica in `main.tex`.
- **E2E Test Harness**: Script di verifica e compilazione automatizzata per conformità tipografica, copertura delle lezioni, presenza di grafici TikZ e assenza di errori LaTeX.

## Feature Inventory
| # | Feature / Topic | Description | Milestone | Source |
|---|-----------------|-------------|-----------|--------|
| 1 | Metodologia e Dati Economici | Cap. 02: Strumenti dell'analisi, modelli, serie storiche, valori nominali/reali, numeri indice, pendenza/elasticità | M1 | Lezione 2, pp. 6-12 |
| 2 | Domanda, Offerta ed Equilibrio | Cap. 03: Determinanti, legge domanda/offerta, equilibrio statico, surplus consumatore/produttore, controlli di prezzo | M2 | Lezioni 3-4, pp. 13-27 |
| 3 | Teoria dell'Elasticità | Cap. 04: Elasticità prezzo, spesa/ricavo totale, elasticità reddito (Engel), elasticità incrociata, breve vs lungo periodo | M2 | Lezione 5, pp. 28-36 |
| 4 | Teoria della Scelta del Consumatore | Cap. 05: Vincolo di bilancio, assiomi, curve di indifferenza, SMS, ottimo del consumatore, scomposizione Hicks e Slutsky | M2 | Lezioni 6-7, pp. 37-53 |
| 5 | Teoria dell'Impresa e Offerta | Cap. 06: Obiettivo del profitto, ricavi marginali/medi, massimizzazione RMg=CMg, regola di chiusura breve/lungo periodo | M3 | Lezione 8, pp. 54-61 |
| 6 | Tecnologia e Costi di Produzione | Cap. 07: Funzione di produzione, legge rendimenti decrescenti, isoquanti/isocosti, SMST, costi fissi/variabili/medi/marginali a U | M3 | Lezione 9, pp. 62-72 |
| 7 | Strutture di Mercato | Cap. 08: Concorrenza perfetta (equilibrio breve/lungo), Monopolio naturale e regolamentazione, Indice di Lerner, Concorrenza monopolistica, Oligopoli (Cournot, Bertrand, Stackelberg, Leadership) | M3 | Lezioni 10-11, pp. 73-90 |
| 8 | Informazione, Rischio e Asimmetrie | Cap. 09: Utilità attesa, avversione al rischio, premio al rischio, assicurazioni, selezione avversa (Akerlof), azzardo morale | M3 | Lezione 12, pp. 91-100 |
| 9 | Introduzione alla Macroeconomia e PIL | Cap. 10 & 11: Contabilità nazionale, 3 metodi di calcolo PIL, flusso circolare a 4 settori, deflatore PIL vs IPC | M4 | Lezioni 15-16, pp. 104-122 |
| 10 | Croce Keynesiana e Moltiplicatore | Cap. 11: Funzione del consumo e risparmio, propensione marginale, equilibrio della spesa programmata, moltiplicatore del reddito | M4 | Lezione 16, pp. 115-127 |
| 11 | Politica Fiscale e Settore Estero | Cap. 12: Imposte fisse e proporzionali, bilancio pubblico, debito pubblico, teorema di Haavelmo, commercio estero e propensione marginale all'importazione | M4 | Lezione 17, pp. 128-138 |
| 12 | Moneta e Politica Monetaria | Cap. 13: Funzioni moneta, aggregati M1/M2/M3, domanda transattiva/precauzionale/speculativa, base monetaria e moltiplicatore bancario, equilibrio monetario | M4 | Lezione 18, pp. 139-148 |
| 13 | Modello IS-LM Congiunto | Cap. 14: Derivazione curva IS, derivazione curva LM, equilibrio congiunto reale-monetario, spiazzamento (crowding out), efficacia politiche | M5 | Lezioni 19-20, pp. 149-160 |
| 14 | Domanda e Offerta Aggregata (AD-AS) | Cap. 15: Derivazione curva AD da IS-LM, curve AS keynesiana, classica e intermedia, shock di domanda e di offerta (stagflazione) | M5 | Begg Capp. 25-26, Lezione 20 |
| 15 | Inflazione e Disoccupazione | Cap. 16: Tipi di disoccupazione (frizionale, strutturale, ciclica), Curva di Phillips originaria, Curva di Phillips corretta con aspettative, NAIRU e tasso naturale | M5 | Begg Cap. 27, Lezione 20 |
| 16 | Tassi di Cambio e Bilancia Pagamenti | Cap. 17: Tassi nominali e reali, parità potere d'acquisto (PPP), parità tassi interesse (UIP), struttura BP (Conto Corrente, Capitale, Finanziario), regimi di cambio | M5 | Lezione 21, pp. 161-168 |
| 17 | Macroeconomia dei Sistemi Aperti (IS-LM-BP) | Cap. 18: Modello Mundell-Fleming, curva BP con mobilità imperfetta e perfetta dei capitali, efficacia politiche in cambi fissi vs flessibili, Trilemma di Mundell | M5 | Lezione 21, pp. 161-168 |
| 18 | Eserciziari Svolti e Prove Ufficiali d'Esame | Esercitazioni di Microeconomia (pp. 169-175), Macroeconomia (pp. 176-197), Prove d'esame 11/01/2021 e 27/01/2021 (pp. 198-221) | M6 | Sbobine pp. 169-221 |
| 19 | Test Suite E2E e Verifica Globale | Test runner automatizzato per validazione LaTeX, conformità capitoli, copertura formule e grafici TikZ | M0 & M7 | ORIGINAL_REQUEST.md |

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| M0 | E2E Test Suite & Test Infra | Suite di validazione automatica (Tiers 1-4) per il monitoraggio di tutti i capitoli | None | IN_PROGRESS |
| M1 | Metodologia ed Economia Applicata | Capitolo 02: Strumenti dell'analisi economica | None | PLANNED |
| M2 | Consumatore, Domanda ed Elasticità | Capitoli 03, 04, 05: Domanda, offerta, elasticità, teoria del consumatore e scomposizione Hicks/Slutsky | None | PLANNED |
| M3 | Produzione, Costi e Strutture di Mercato | Capitoli 06, 07, 08, 09: Teoria dell'offerta, costi, concorrenza perfetta, monopolio, oligopolio, asimmetrie | M2 | PLANNED |
| M4 | Macroeconomia Reale, Fisco e Moneta | Capitoli 10, 11, 12, 13: Introduzione macro, contabilità PIL, Croce Keynesiana, fisco, moneta | None | PLANNED |
| M5 | Mercati Congiunti e Sistemi Aperti | Capitoli 14, 15, 16, 17, 18: IS-LM, AD-AS, Phillips/NAIRU, cambi/BP, Mundell-Fleming | M4 | PLANNED |
| M6 | Esercizi d'Esame e Formulario | Integrazione eserciziari (pp. 169-197) e prove d'esame ufficiali (pp. 198-221) | M1, M2, M3, M4, M5 | PLANNED |
| M7 | E2E Final Pass & Compilazione Globale | Validazione 100% test suite, compilazione finale senza errori, revisione estetica ed audit | M0-M6 | PLANNED |

## Interface Contracts
### `chapters/XX_.../main.tex` ↔ `main.tex`
- Ogni capitolo deve iniziare con `\chapter{Titolo del Capitolo}` e label `\label{chap:XX_...}`.
- Non deve contenere `\documentclass` o `\begin{document}`.
- Utilizza rigorosamente gli ambienti standardizzati in `config/environments.tex` (`definizione`, `modello`, `legge`, `teorema`, `dimostrazione`, `metodo`, `esame`, `esempio`, `esercizio`, `osservazione`, `empirico`).
- Utilizza le macro matematiche ed economiche in `config/macros.tex`.
- Tutti i grafici TikZ devono essere racchiusi in `\begin{figure}[htbp] \centering \begin{tikzpicture} ... \end{tikzpicture} \caption{...}\label{fig:...} \end{figure}`.

## Code Layout
```
ECONOMIA/
├── config/
│   ├── packages.tex
│   ├── environments.tex
│   └── macros.tex
├── chapters/
│   ├── 01_scienza_economica/main.tex
│   ├── 02_strumenti_analisi_economica/main.tex
│   ├── 03_domanda_offerta_mercato/main.tex
│   ├── 04_elasticita_domanda_offerta/main.tex
│   ├── 05_scelta_consumatore_domanda/main.tex
│   ├── 06_introduzione_teoria_offerta/main.tex
│   ├── 07_tecnologia_costi/main.tex
│   ├── 08_strutture_mercato/main.tex
│   ├── 09_informazione_rischio/main.tex
│   ├── 10_introduzione_macroeconomia/main.tex
│   ├── 11_prodotto_nazionale_spesa_aggregata/main.tex
│   ├── 12_politica_fiscale_commercio_estero/main.tex
│   ├── 13_moneta_politica_monetaria/main.tex
│   ├── 14_mercato_monetario_reale_is_lm/main.tex
│   ├── 15_equilibrio_domanda_offerta_aggregata/main.tex
│   ├── 16_inflazione_disoccupazione/main.tex
│   ├── 17_tassi_cambio_bilancia_pagamenti/main.tex
│   └── 18_macroeconomia_sistemi_aperti/main.tex
├── tests/
│   ├── run_e2e_tests.py
│   └── test_suites/
├── figures/
├── source/
│   └── Sbobine Istituzioni di economia (siria).pdf
├── main.tex
└── main.pdf
```

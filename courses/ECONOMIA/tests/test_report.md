# E2E Test Suite Execution Report
**Timestamp**: `2026-08-29T15:49:01.719324`  
**Overall Status**: `FAILED`  
**Tested Chapters**: `18/18`  

## Summary Metrics
- **Total Source Lines**: 2,506
- **Total Word Count**: 23,128
- **Total Didactic Environments**: 143
- **Total TikZ Figures**: 8

## Chapter Breakdown
| # | Chapter ID | Lines | Words | Envs | TikZ | Tier 1 | Tier 2 | Tier 3 | Status |
|---|------------|-------|-------|------|------|--------|--------|--------|--------|
| 01 | `01_scienza_economica` | 325 | 3289 | 24 | 2 | PASS | PASS | PASS | **PASS** |
| 02 | `02_strumenti_analisi_economica` | 530 | 5163 | 26 | 2 | PASS | PASS | PASS | **PASS** |
| 03 | `03_domanda_offerta_mercato` | 88 | 658 | 6 | 1 | PASS | PASS | PASS | **PASS** |
| 04 | `04_elasticita_domanda_offerta` | 76 | 620 | 5 | 0 | PASS | PASS | PASS | **PASS** |
| 05 | `05_scelta_consumatore_domanda` | 80 | 721 | 5 | 0 | PASS | PASS | PASS | **PASS** |
| 06 | `06_introduzione_teoria_offerta` | 58 | 459 | 4 | 0 | PASS | PASS | PASS | **PASS** |
| 07 | `07_tecnologia_costi` | 70 | 582 | 7 | 0 | PASS | PASS | PASS | **PASS** |
| 08 | `08_strutture_mercato` | 75 | 544 | 3 | 0 | PASS | PASS | PASS | **PASS** |
| 09 | `09_informazione_rischio` | 51 | 507 | 3 | 0 | PASS | PASS | PASS | **PASS** |
| 10 | `10_introduzione_macroeconomia` | 649 | 6380 | 20 | 3 | FAIL | PASS | PASS | **FAIL** |
| 11 | `11_prodotto_nazionale_spesa_aggregata` | 77 | 596 | 7 | 0 | PASS | PASS | PASS | **PASS** |
| 12 | `12_politica_fiscale_commercio_estero` | 66 | 507 | 5 | 0 | PASS | PASS | PASS | **PASS** |
| 13 | `13_moneta_politica_monetaria` | 67 | 547 | 5 | 0 | PASS | PASS | PASS | **PASS** |
| 14 | `14_mercato_monetario_reale_is_lm` | 65 | 557 | 6 | 0 | PASS | PASS | PASS | **PASS** |
| 15 | `15_equilibrio_domanda_offerta_aggregata` | 45 | 425 | 3 | 0 | PASS | PASS | PASS | **PASS** |
| 16 | `16_inflazione_disoccupazione` | 61 | 454 | 5 | 0 | PASS | PASS | PASS | **PASS** |
| 17 | `17_tassi_cambio_bilancia_pagamenti` | 65 | 585 | 5 | 0 | PASS | PASS | PASS | **PASS** |
| 18 | `18_macroeconomia_sistemi_aperti` | 58 | 534 | 4 | 0 | PASS | PASS | PASS | **PASS** |

## Issues and Diagnostics
| Severity | Tier | Chapter | Rule ID | Message |
|----------|------|---------|---------|---------|
| WARNING | Tier 3 | `02_strumenti_analisi_economica` (line 164) | `T3_UNMATCHED_DOLLAR` | Odd number of '$' math delimiters (13) on line |
| WARNING | Tier 3 | `02_strumenti_analisi_economica` (line 166) | `T3_UNMATCHED_DOLLAR` | Odd number of '$' math delimiters (1) on line |
| WARNING | Tier 3 | `02_strumenti_analisi_economica` (line 171) | `T3_UNMATCHED_DOLLAR` | Odd number of '$' math delimiters (1) on line |
| WARNING | Tier 3 | `02_strumenti_analisi_economica` (line 173) | `T3_UNMATCHED_DOLLAR` | Odd number of '$' math delimiters (1) on line |
| WARNING | Tier 3 | `02_strumenti_analisi_economica` (line 278) | `T3_UNMATCHED_DOLLAR` | Odd number of '$' math delimiters (1) on line |
| WARNING | Tier 3 | `02_strumenti_analisi_economica` (line 283) | `T3_UNMATCHED_DOLLAR` | Odd number of '$' math delimiters (1) on line |
| WARNING | Tier 3 | `02_strumenti_analisi_economica` (line 285) | `T3_UNMATCHED_DOLLAR` | Odd number of '$' math delimiters (1) on line |
| WARNING | Tier 3 | `02_strumenti_analisi_economica` (line 286) | `T3_UNMATCHED_DOLLAR` | Odd number of '$' math delimiters (1) on line |
| WARNING | Tier 3 | `02_strumenti_analisi_economica` (line 288) | `T3_UNMATCHED_DOLLAR` | Odd number of '$' math delimiters (1) on line |
| WARNING | Tier 3 | `02_strumenti_analisi_economica` (line 340) | `T3_UNMATCHED_DOLLAR` | Odd number of '$' math delimiters (3) on line |
| WARNING | Tier 3 | `02_strumenti_analisi_economica` (line 344) | `T3_UNMATCHED_DOLLAR` | Odd number of '$' math delimiters (1) on line |
| WARNING | Tier 3 | `02_strumenti_analisi_economica` (line 345) | `T3_UNMATCHED_DOLLAR` | Odd number of '$' math delimiters (3) on line |
| WARNING | Tier 3 | `02_strumenti_analisi_economica` | `T3_KEY_FORMULA_MISSING` | Key theoretical formula / notation patterns missing: \\text\{Valore Reale\}, I_t |
| WARNING | Tier 3 | `03_domanda_offerta_mercato` | `T3_KEY_FORMULA_MISSING` | Key theoretical formula / notation patterns missing: Q_d, Q_s, P\^\\* |
| WARNING | Tier 1 | `04_elasticita_domanda_offerta` | `T1_MISSING_REQ_ENVS` | Missing recommended didactic environments: legge, metodo, esame |
| WARNING | Tier 3 | `04_elasticita_domanda_offerta` | `T3_KEY_FORMULA_MISSING` | Key theoretical formula / notation patterns missing: \\RMg|RMg |
| WARNING | Tier 1 | `05_scelta_consumatore_domanda` | `T1_MISSING_REQ_ENVS` | Missing recommended didactic environments: legge, metodo, esame |
| WARNING | Tier 3 | `05_scelta_consumatore_domanda` | `T3_KEY_FORMULA_MISSING` | Key theoretical formula / notation patterns missing: p_1.*x_1.*p_2.*x_2.*R |
| WARNING | Tier 1 | `06_introduzione_teoria_offerta` | `T1_MISSING_REQ_ENVS` | Missing recommended didactic environments: modello, metodo |
| WARNING | Tier 1 | `07_tecnologia_costi` | `T1_MISSING_REQ_ENVS` | Missing recommended didactic environments: metodo, esame |
| WARNING | Tier 1 | `08_strutture_mercato` | `T1_MISSING_REQ_ENVS` | Missing recommended didactic environments: definizione, metodo, esame |
| WARNING | Tier 1 | `09_informazione_rischio` | `T1_MISSING_REQ_ENVS` | Missing recommended didactic environments: modello, metodo, esame |
| WARNING | Tier 3 | `09_informazione_rischio` | `T3_KEY_FORMULA_MISSING` | Key theoretical formula / notation patterns missing: CE|Equivalente\s+Certo, RP|Premio.*Rischio |
| WARNING | Tier 1 | `10_introduzione_macroeconomia` | `T1_MISSING_REQ_ENVS` | Missing recommended didactic environments: modello |
| ERROR | Tier 1 | `10_introduzione_macroeconomia` (line 181) | `T1_TABLE_SINGLE_BACKSLASH` | Table row ends with single backslash '\' instead of newline '\\' |
| ERROR | Tier 1 | `10_introduzione_macroeconomia` (line 188) | `T1_TABLE_SINGLE_BACKSLASH` | Table row ends with single backslash '\' instead of newline '\\' |
| ERROR | Tier 1 | `10_introduzione_macroeconomia` (line 196) | `T1_TABLE_SINGLE_BACKSLASH` | Table row ends with single backslash '\' instead of newline '\\' |
| ERROR | Tier 1 | `10_introduzione_macroeconomia` (line 204) | `T1_TABLE_SINGLE_BACKSLASH` | Table row ends with single backslash '\' instead of newline '\\' |
| WARNING | Tier 3 | `10_introduzione_macroeconomia` (line 48) | `T3_UNMATCHED_DOLLAR` | Odd number of '$' math delimiters (1) on line |
| WARNING | Tier 3 | `10_introduzione_macroeconomia` (line 55) | `T3_UNMATCHED_DOLLAR` | Odd number of '$' math delimiters (1) on line |
| WARNING | Tier 3 | `10_introduzione_macroeconomia` (line 66) | `T3_UNMATCHED_DOLLAR` | Odd number of '$' math delimiters (1) on line |
| WARNING | Tier 3 | `10_introduzione_macroeconomia` (line 67) | `T3_UNMATCHED_DOLLAR` | Odd number of '$' math delimiters (1) on line |
| WARNING | Tier 3 | `10_introduzione_macroeconomia` (line 73) | `T3_UNMATCHED_DOLLAR` | Odd number of '$' math delimiters (1) on line |
| WARNING | Tier 3 | `10_introduzione_macroeconomia` (line 96) | `T3_UNMATCHED_DOLLAR` | Odd number of '$' math delimiters (1) on line |
| WARNING | Tier 3 | `10_introduzione_macroeconomia` (line 97) | `T3_UNMATCHED_DOLLAR` | Odd number of '$' math delimiters (1) on line |
| WARNING | Tier 3 | `10_introduzione_macroeconomia` (line 127) | `T3_UNMATCHED_DOLLAR` | Odd number of '$' math delimiters (3) on line |
| WARNING | Tier 3 | `10_introduzione_macroeconomia` (line 137) | `T3_UNMATCHED_DOLLAR` | Odd number of '$' math delimiters (1) on line |
| WARNING | Tier 3 | `10_introduzione_macroeconomia` (line 148) | `T3_UNMATCHED_DOLLAR` | Odd number of '$' math delimiters (3) on line |
| WARNING | Tier 3 | `10_introduzione_macroeconomia` (line 162) | `T3_UNMATCHED_DOLLAR` | Odd number of '$' math delimiters (1) on line |
| WARNING | Tier 3 | `10_introduzione_macroeconomia` (line 185) | `T3_UNMATCHED_DOLLAR` | Odd number of '$' math delimiters (3) on line |
| WARNING | Tier 3 | `10_introduzione_macroeconomia` (line 186) | `T3_UNMATCHED_DOLLAR` | Odd number of '$' math delimiters (3) on line |
| WARNING | Tier 3 | `10_introduzione_macroeconomia` (line 187) | `T3_UNMATCHED_DOLLAR` | Odd number of '$' math delimiters (3) on line |
| WARNING | Tier 3 | `10_introduzione_macroeconomia` (line 194) | `T3_UNMATCHED_DOLLAR` | Odd number of '$' math delimiters (3) on line |
| WARNING | Tier 3 | `10_introduzione_macroeconomia` (line 204) | `T3_UNMATCHED_DOLLAR` | Odd number of '$' math delimiters (1) on line |
| WARNING | Tier 3 | `10_introduzione_macroeconomia` (line 221) | `T3_UNMATCHED_DOLLAR` | Odd number of '$' math delimiters (1) on line |
| WARNING | Tier 3 | `10_introduzione_macroeconomia` (line 222) | `T3_UNMATCHED_DOLLAR` | Odd number of '$' math delimiters (3) on line |
| WARNING | Tier 3 | `10_introduzione_macroeconomia` (line 223) | `T3_UNMATCHED_DOLLAR` | Odd number of '$' math delimiters (3) on line |
| WARNING | Tier 3 | `10_introduzione_macroeconomia` (line 257) | `T3_UNMATCHED_DOLLAR` | Odd number of '$' math delimiters (1) on line |
| WARNING | Tier 3 | `10_introduzione_macroeconomia` (line 259) | `T3_UNMATCHED_DOLLAR` | Odd number of '$' math delimiters (1) on line |
| WARNING | Tier 3 | `10_introduzione_macroeconomia` (line 260) | `T3_UNMATCHED_DOLLAR` | Odd number of '$' math delimiters (1) on line |
| WARNING | Tier 3 | `10_introduzione_macroeconomia` (line 263) | `T3_UNMATCHED_DOLLAR` | Odd number of '$' math delimiters (1) on line |
| WARNING | Tier 3 | `10_introduzione_macroeconomia` (line 264) | `T3_UNMATCHED_DOLLAR` | Odd number of '$' math delimiters (1) on line |
| WARNING | Tier 3 | `10_introduzione_macroeconomia` (line 265) | `T3_UNMATCHED_DOLLAR` | Odd number of '$' math delimiters (1) on line |
| WARNING | Tier 3 | `10_introduzione_macroeconomia` (line 268) | `T3_UNMATCHED_DOLLAR` | Odd number of '$' math delimiters (1) on line |
| WARNING | Tier 3 | `10_introduzione_macroeconomia` (line 269) | `T3_UNMATCHED_DOLLAR` | Odd number of '$' math delimiters (1) on line |
| WARNING | Tier 3 | `10_introduzione_macroeconomia` (line 270) | `T3_UNMATCHED_DOLLAR` | Odd number of '$' math delimiters (1) on line |
| WARNING | Tier 3 | `10_introduzione_macroeconomia` (line 282) | `T3_UNMATCHED_DOLLAR` | Odd number of '$' math delimiters (1) on line |
| WARNING | Tier 3 | `10_introduzione_macroeconomia` (line 288) | `T3_UNMATCHED_DOLLAR` | Odd number of '$' math delimiters (1) on line |
| WARNING | Tier 3 | `10_introduzione_macroeconomia` (line 292) | `T3_UNMATCHED_DOLLAR` | Odd number of '$' math delimiters (3) on line |
| WARNING | Tier 3 | `10_introduzione_macroeconomia` (line 311) | `T3_UNMATCHED_DOLLAR` | Odd number of '$' math delimiters (1) on line |
| WARNING | Tier 3 | `10_introduzione_macroeconomia` (line 362) | `T3_UNMATCHED_DOLLAR` | Odd number of '$' math delimiters (1) on line |
| WARNING | Tier 3 | `10_introduzione_macroeconomia` (line 380) | `T3_UNMATCHED_DOLLAR` | Odd number of '$' math delimiters (1) on line |
| WARNING | Tier 3 | `10_introduzione_macroeconomia` (line 384) | `T3_UNMATCHED_DOLLAR` | Odd number of '$' math delimiters (1) on line |
| WARNING | Tier 3 | `10_introduzione_macroeconomia` (line 396) | `T3_UNMATCHED_DOLLAR` | Odd number of '$' math delimiters (3) on line |
| WARNING | Tier 3 | `10_introduzione_macroeconomia` (line 408) | `T3_UNMATCHED_DOLLAR` | Odd number of '$' math delimiters (3) on line |
| WARNING | Tier 3 | `10_introduzione_macroeconomia` (line 464) | `T3_UNMATCHED_DOLLAR` | Odd number of '$' math delimiters (3) on line |
| WARNING | Tier 3 | `10_introduzione_macroeconomia` (line 496) | `T3_UNMATCHED_DOLLAR` | Odd number of '$' math delimiters (1) on line |
| WARNING | Tier 3 | `10_introduzione_macroeconomia` (line 500) | `T3_UNMATCHED_DOLLAR` | Odd number of '$' math delimiters (1) on line |
| WARNING | Tier 3 | `10_introduzione_macroeconomia` (line 507) | `T3_UNMATCHED_DOLLAR` | Odd number of '$' math delimiters (1) on line |
| WARNING | Tier 3 | `10_introduzione_macroeconomia` (line 509) | `T3_UNMATCHED_DOLLAR` | Odd number of '$' math delimiters (1) on line |
| WARNING | Tier 3 | `10_introduzione_macroeconomia` (line 511) | `T3_UNMATCHED_DOLLAR` | Odd number of '$' math delimiters (1) on line |
| WARNING | Tier 3 | `10_introduzione_macroeconomia` (line 533) | `T3_UNMATCHED_DOLLAR` | Odd number of '$' math delimiters (3) on line |
| WARNING | Tier 3 | `10_introduzione_macroeconomia` (line 544) | `T3_UNMATCHED_DOLLAR` | Odd number of '$' math delimiters (1) on line |
| WARNING | Tier 3 | `10_introduzione_macroeconomia` (line 548) | `T3_UNMATCHED_DOLLAR` | Odd number of '$' math delimiters (1) on line |
| WARNING | Tier 3 | `10_introduzione_macroeconomia` (line 554) | `T3_UNMATCHED_DOLLAR` | Odd number of '$' math delimiters (1) on line |
| WARNING | Tier 3 | `10_introduzione_macroeconomia` (line 609) | `T3_UNMATCHED_DOLLAR` | Odd number of '$' math delimiters (1) on line |
| WARNING | Tier 1 | `11_prodotto_nazionale_spesa_aggregata` | `T1_MISSING_REQ_ENVS` | Missing recommended didactic environments: metodo |
| WARNING | Tier 1 | `12_politica_fiscale_commercio_estero` | `T1_MISSING_REQ_ENVS` | Missing recommended didactic environments: modello, metodo, esame |
| WARNING | Tier 1 | `13_moneta_politica_monetaria` | `T1_MISSING_REQ_ENVS` | Missing recommended didactic environments: metodo, esame |
| WARNING | Tier 1 | `14_mercato_monetario_reale_is_lm` | `T1_MISSING_REQ_ENVS` | Missing recommended didactic environments: metodo |
| WARNING | Tier 1 | `15_equilibrio_domanda_offerta_aggregata` | `T1_MISSING_REQ_ENVS` | Missing recommended didactic environments: metodo, esame |
| WARNING | Tier 1 | `16_inflazione_disoccupazione` | `T1_MISSING_REQ_ENVS` | Missing recommended didactic environments: metodo, esame |
| WARNING | Tier 3 | `16_inflazione_disoccupazione` | `T3_KEY_FORMULA_MISSING` | Key theoretical formula / notation patterns missing: Okun |
| WARNING | Tier 1 | `17_tassi_cambio_bilancia_pagamenti` | `T1_MISSING_REQ_ENVS` | Missing recommended didactic environments: modello, metodo, esame |
| WARNING | Tier 3 | `17_tassi_cambio_bilancia_pagamenti` (line 37) | `T3_UNMATCHED_DOLLAR` | Odd number of '$' math delimiters (1) on line |
| WARNING | Tier 3 | `17_tassi_cambio_bilancia_pagamenti` | `T3_KEY_FORMULA_MISSING` | Key theoretical formula / notation patterns missing: Marshall-Lerner|Curva\s+a\s+J |
| WARNING | Tier 1 | `18_macroeconomia_sistemi_aperti` | `T1_MISSING_REQ_ENVS` | Missing recommended didactic environments: definizione, metodo, esame |

# Istituzioni di Economia (Microeconomia e Macroeconomia)

Questo repository contiene il testo completo, formale e integrato del corso di **Istituzioni di Economia** per il Corso di Laurea in Ingegneria Gestionale, redatto in LaTeX modulare e pronto per la compilazione in PDF.

---

## 🏛️ Architettura del Progetto

Il progetto adotta una struttura a moduli indipendenti:

```
ECONOMIA/
├── config/
│   ├── packages.tex          # Pacchetti LaTeX, microtype, TikZ, pgfplots, booktabs, geometry
│   ├── environments.tex      # Ambienti tcolorbox stilizzati (definizione, modello, legge, teorema, metodo, esame, esempio, osservazione)
│   └── macros.tex            # Notazione economica unificata (Micro & Macro)
├── chapters/
│   ├── 01_scienza_economica/
│   ├── 02_strumenti_analisi_economica/
│   ├── 03_domanda_offerta_mercato/
│   ├── 04_elasticita_domanda_offerta/
│   ├── 05_scelta_consumatore_domanda/
│   ├── 06_introduzione_teoria_offerta/
│   ├── 07_tecnologia_costi/
│   ├── 08_strutture_mercato/
│   ├── 09_informazione_rischio/
│   ├── 10_introduzione_macroeconomia/
│   ├── 11_prodotto_nazionale_spesa_aggregata/
│   ├── 12_politica_fiscale_commercio_estero/
│   ├── 13_moneta_politica_monetaria/
│   ├── 14_mercato_monetario_reale_is_lm/
│   ├── 15_equilibrio_domanda_offerta_aggregata/
│   ├── 16_inflazione_disoccupazione/
│   ├── 17_tassi_cambio_bilancia_pagamenti/
│   └── 18_macroeconomia_sistemi_aperti/
├── figures/                  # Grafici, schemi e immagini vettoriali dedicate
├── source/                   # Sbobine e appunti originali (PDF di riferimento)
├── main.tex                  # File radice master
└── README.md                 # Questo documento
```

---

## 🚀 Compilazione del Documento

### Compilazione Completa (Tutti i Capitoli)
Per compilare l'intero volume e generare `main.pdf`:

```bash
cd /Users/nicolabeccaceci/Documents/GEST/ECONOMIA
latexmk -pdf -interaction=nonstopmode main.tex
```

### Compilazione Selettiva (Singolo Capitolo)
Per velocizzare la compilazione durante la stesura o revisione di un capitolo specifico, è sufficiente aprire `main.tex` e scommentare la direttiva `\includeonly{...}` indicando il percorso del capitolo desiderato, ad esempio:

```latex
\includeonly{
  chapters/03_domanda_offerta_mercato/main
}
```

---

## 🧩 Box Tematici e Stile Visivo

Il codice LaTeX utilizza ambienti `tcolorbox` dedicati per distinguere visivamente i vari contenuti:
- `\begin{definizione}{Nome}{label}`: Definizioni economiche formali con sfondo blu istituzionale.
- `\begin{modello}{Nome}{label}`: Modelli e formulazioni analitiche con sfondo viola.
- `\begin{legge}{Nome}{label}`: Assiomi e leggi di mercato con bordo ottanio.
- `\begin{teorema}{Nome}{label}`: Teoremi e proposizioni con bordo verde foresta.
- `\begin{dimostrazione}`: Dimostrazioni matematiche passo-passo chiuse dal quadratino $\blacksquare$.
- `\begin{metodo}[Titolo]`: Procedure algoritmiche di calcolo con sfondo ambra.
- `\begin{esame}[Titolo]`: Consigli d'esame, errori e tranelli frequenti con bordo rosso cremisi.
- `\begin{esempio}[Titolo]`: Esempi numerici ed economici applicativi.
- `\begin{osservazione}[Titolo]`: Intuizione economica e note teoriche a margine.

---

## 🔄 Flessibilità di Espansione

L'architettura è pienamente flessibile:
1. Per **aggiungere un nuovo capitolo**: creare una nuova cartella in `chapters/XX_nuovo_capitolo/main.tex` e inserire `\include{chapters/XX_nuovo_capitolo/main}` in `main.tex`.
2. Per **spostare o unire argomenti**: è sufficiente modificare i puntatori `\include` in `main.tex` senza alcuna interferenza con il resto del testo.

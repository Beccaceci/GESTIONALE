#!/usr/bin/env python3
"""
split_exams.py - Analisi 1 Exam PDF Splitting Engine

Splits master yearly compilations of past exams into single-session PDFs:
  YYYY-MM-DD_<tipo_sessione>.pdf
Ensures every generated PDF contains BOTH problem statements and complete official solutions.
- Archetype A (2011-12 to 2017-18): Merges corresponding Testi pages and Soluzioni pages.
- Archetype B (2020-21, 2021-22, 2023-24, 2024-25): Slices contiguous problem+solution pages.
- 2022-23 (AM1): Merges Testi pages (pp. 7-22) and Soluzioni pages (pp. 24-75).
"""

import os
import sys
import fitz

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../courses/first_year/ANALISI1/esami"))

# Master session definitions (1-indexed page numbers matching master compilation PDF)
EXAM_SESSION_DEFINITIONS = {
    "2024-25": {
        "master_pdf": "esami_2024-25.pdf",
        "archetype": "B",
        "sessions": [
            {"date": "2025-02-10", "slug": "primo_compitino", "pages": (6, 12), "title": "Primo compitino (10 febbraio 2025)"},
            {"date": "2025-05-30", "slug": "secondo_compitino", "pages": (13, 20), "title": "Secondo compitino (30 maggio 2025)"},
            {"date": "2025-06-24", "slug": "primo_appello", "pages": (21, 28), "title": "Primo appello (24 giugno 2025)"},
            {"date": "2025-07-21", "slug": "secondo_appello", "pages": (29, 34), "title": "Secondo appello (21 luglio 2025)"},
            {"date": "2025-09-18", "slug": "terzo_appello", "pages": (35, 43), "title": "Terzo appello (18 settembre 2025)"},
            {"date": "2026-01-22", "slug": "quarto_appello", "pages": (44, 50), "title": "Quarto appello (22 gennaio 2026)"},
            {"date": "2026-02-19", "slug": "quinto_appello", "pages": (51, 59), "title": "Quinto appello (19 febbraio 2026)"},
        ]
    },
    "2023-24": {
        "master_pdf": "esami_2023-24.pdf",
        "archetype": "B",
        "sessions": [
            {"date": "2024-01-29", "slug": "primo_compitino", "pages": (6, 12), "title": "Primo compitino (29 gennaio 2024)"},
            {"date": "2024-04-13", "slug": "compitino_recupero", "pages": (13, 18), "title": "Compitino di recupero (13 aprile 2024)"},
            {"date": "2024-05-30", "slug": "secondo_compitino", "pages": (19, 27), "title": "Secondo compitino (30 maggio 2024)"},
            {"date": "2024-06-24", "slug": "primo_appello", "pages": (28, 35), "title": "Primo appello (24 giugno 2024)"},
            {"date": "2024-07-15", "slug": "secondo_appello", "pages": (36, 44), "title": "Secondo appello (15 luglio 2024)"},
            {"date": "2024-09-05", "slug": "terzo_appello", "pages": (45, 53), "title": "Terzo appello (5 settembre 2024)"},
            {"date": "2025-01-13", "slug": "quarto_appello", "pages": (54, 59), "title": "Quarto appello (13 gennaio 2025)"},
            {"date": "2025-02-03", "slug": "quinto_appello", "pages": (60, 64), "title": "Quinto appello (3 febbraio 2025)"},
        ]
    },
    "2022-23": {
        "master_pdf": "esami_2022-23.pdf",
        "archetype": "A",
        "sessions": [
            {"date": "2023-02-23", "slug": "primo_compitino", "testi": (7, 8), "soluzioni": (24, 30), "title": "Primo compitino (23 febbraio 2023)"},
            {"date": "2023-04-06", "slug": "compitino_recupero", "testi": (9, 10), "soluzioni": (31, 34), "title": "Compitino di recupero (6 aprile 2023)"},
            {"date": "2023-05-19", "slug": "secondo_compitino", "testi": (11, 12), "soluzioni": (35, 41), "title": "Secondo compitino (19 maggio 2023)"},
            {"date": "2023-06-26", "slug": "primo_appello", "testi": (13, 14), "soluzioni": (42, 47), "title": "Primo appello (26 giugno 2023)"},
            {"date": "2023-07-20", "slug": "secondo_appello", "testi": (15, 16), "soluzioni": (48, 54), "title": "Secondo appello (20 luglio 2023)"},
            {"date": "2023-09-18", "slug": "terzo_appello", "testi": (17, 18), "soluzioni": (55, 61), "title": "Terzo appello (18 settembre 2023)"},
            {"date": "2024-01-22", "slug": "quarto_appello", "testi": (19, 20), "soluzioni": (62, 67), "title": "Quarto appello (22 gennaio 2024)"},
            {"date": "2024-02-19", "slug": "quinto_appello", "testi": (21, 22), "soluzioni": (68, 75), "title": "Quinto appello (19 febbraio 2024)"},
        ]
    },
    "2021-22": {
        "master_pdf": "esami_2021-22.pdf",
        "archetype": "B",
        "sessions": [
            {"date": "2021-11-27", "slug": "primo_compitino", "pages": (5, 8), "title": "Primo compitino (27 novembre 2021)"},
            {"date": "2022-01-07", "slug": "secondo_compitino_e_primo_appello", "pages": (9, 14), "title": "Secondo compitino e primo appello (7 gennaio 2022)"},
            {"date": "2022-01-24", "slug": "secondo_appello", "pages": (15, 18), "title": "Secondo appello (24 gennaio 2022)"},
            {"date": "2022-02-14", "slug": "terzo_appello", "pages": (19, 22), "title": "Terzo appello (14 febbraio 2022)"},
            {"date": "2022-06-06", "slug": "quarto_appello", "pages": (23, 26), "title": "Quarto appello (6 giugno 2022)"},
            {"date": "2022-06-27", "slug": "quinto_appello", "pages": (27, 30), "title": "Quinto appello (27 giugno 2022)"},
            {"date": "2022-07-18", "slug": "sesto_appello", "pages": (31, 34), "title": "Sesto appello (18 luglio 2022)"},
            {"date": "2022-09-12", "slug": "settimo_appello", "pages": (35, 38), "title": "Settimo appello (12 settembre 2022)"},
        ]
    },
    "2020-21": {
        "master_pdf": "esami_2020-21.pdf",
        "archetype": "B",
        "sessions": [
            {"date": "2020-11-21", "slug": "primo_compitino", "pages": (5, 10), "title": "Primo compitino (21 novembre 2020)"},
            {"date": "2021-01-04", "slug": "secondo_compitino", "pages": (11, 15), "title": "Secondo compitino (4 gennaio 2021)"},
            {"date": "2021-01-07", "slug": "primo_appello", "pages": (16, 20), "title": "Primo appello (7 gennaio 2021)"},
            {"date": "2021-01-25", "slug": "secondo_appello", "pages": (21, 25), "title": "Secondo appello (25 gennaio 2021)"},
            {"date": "2021-02-15", "slug": "terzo_appello", "pages": (26, 31), "title": "Terzo appello (15 febbraio 2021)"},
            {"date": "2021-06-07", "slug": "quarto_appello", "pages": (32, 35), "title": "Quarto appello (7 giugno 2021)"},
            {"date": "2021-06-28", "slug": "quinto_appello", "pages": (36, 39), "title": "Quinto appello (28 giugno 2021)"},
            {"date": "2021-07-19", "slug": "sesto_appello", "pages": (40, 43), "title": "Sesto appello (19 luglio 2021)"},
            {"date": "2021-09-13", "slug": "settimo_appello", "pages": (44, 47), "title": "Settimo appello (13 settembre 2021)"},
        ]
    },
    "2017-18": {
        "master_pdf": "esami_2017-18.pdf",
        "archetype": "A",
        "sessions": [
            {"date": "2017-11-18", "slug": "primo_compitino", "testi": (5, 8), "soluzioni": (44, 50), "title": "Primo compitino (18 novembre 2017)"},
            {"date": "2018-01-15", "slug": "secondo_compitino_e_primo_appello", "testi": (9, 14), "soluzioni": (51, 58), "title": "Secondo compitino e primo appello (15 gennaio 2018)"},
            {"date": "2018-02-05", "slug": "secondo_appello", "testi": (15, 19), "soluzioni": (59, 65), "title": "Secondo appello (5 febbraio 2018)"},
            {"date": "2018-02-19", "slug": "terzo_appello", "testi": (20, 25), "soluzioni": (66, 72), "title": "Terzo appello (19 febbraio 2018)"},
            {"date": "2018-06-07", "slug": "quarto_appello", "testi": (26, 30), "soluzioni": (73, 80), "title": "Quarto appello (7 giugno 2018)"},
            {"date": "2018-06-25", "slug": "quinto_appello", "testi": (31, 34), "soluzioni": (81, 86), "title": "Quinto appello (25 giugno 2018)"},
            {"date": "2018-07-16", "slug": "sesto_appello", "testi": (35, 39), "soluzioni": (87, 93), "title": "Sesto appello (16 luglio 2018)"},
            {"date": "2018-09-10", "slug": "settimo_appello", "testi": (40, 42), "soluzioni": (94, 98), "title": "Settimo appello (10 settembre 2018)"},
        ]
    },
    "2016-17": {
        "master_pdf": "esami_2016-17.pdf",
        "archetype": "A",
        "sessions": [
            {"date": "2016-11-12", "slug": "primo_compitino", "testi": (5, 8), "soluzioni": (36, 42), "title": "Primo compitino (12 novembre 2016)"},
            {"date": "2017-01-12", "slug": "secondo_compitino_e_primo_appello", "testi": (9, 13), "soluzioni": (43, 51), "title": "Secondo compitino e primo appello (12 gennaio 2017)"},
            {"date": "2017-02-01", "slug": "secondo_appello", "testi": (14, 18), "soluzioni": (52, 59), "title": "Secondo appello (1 febbraio 2017)"},
            {"date": "2017-02-20", "slug": "terzo_appello", "testi": (19, 23), "soluzioni": (60, 65), "title": "Terzo appello (20 febbraio 2017)"},
            {"date": "2017-06-12", "slug": "quarto_appello", "testi": (24, 26), "soluzioni": (66, 69), "title": "Quarto appello (12 giugno 2017)"},
            {"date": "2017-07-03", "slug": "quinto_appello", "testi": (27, 29), "soluzioni": (70, 73), "title": "Quinto appello (3 luglio 2017)"},
            {"date": "2017-07-24", "slug": "sesto_appello", "testi": (30, 32), "soluzioni": (74, 77), "title": "Sesto appello (24 luglio 2017)"},
            {"date": "2017-09-14", "slug": "settimo_appello", "testi": (33, 34), "soluzioni": (78, 82), "title": "Settimo appello (14 settembre 2017)"},
        ]
    },
    "2015-16": {
        "master_pdf": "esami_2015-16.pdf",
        "archetype": "A",
        "sessions": [
            {"date": "2015-11-14", "slug": "primo_compitino", "testi": (5, 10), "soluzioni": (40, 48), "title": "Primo compitino (14 novembre 2015)"},
            {"date": "2016-01-15", "slug": "secondo_compitino_e_primo_appello", "testi": (11, 16), "soluzioni": (49, 58), "title": "Secondo compitino e primo appello (15 gennaio 2016)"},
            {"date": "2016-02-04", "slug": "secondo_appello", "testi": (17, 21), "soluzioni": (59, 66), "title": "Secondo appello (4 febbraio 2016)"},
            {"date": "2016-02-23", "slug": "terzo_appello", "testi": (22, 27), "soluzioni": (67, 73), "title": "Terzo appello (23 febbraio 2016)"},
            {"date": "2016-06-09", "slug": "quarto_appello", "testi": (28, 30), "soluzioni": (74, 79), "title": "Quarto appello (9 giugno 2016)"},
            {"date": "2016-06-30", "slug": "quinto_appello", "testi": (31, 33), "soluzioni": (80, 85), "title": "Quinto appello (30 giugno 2016)"},
            {"date": "2016-07-21", "slug": "sesto_appello", "testi": (34, 36), "soluzioni": (86, 89), "title": "Sesto appello (21 luglio 2016)"},
            {"date": "2016-09-13", "slug": "settimo_appello", "testi": (37, 38), "soluzioni": (90, 92), "title": "Settimo appello (13 settembre 2016)"},
        ]
    },
    "2014-15": {
        "master_pdf": "esami_2014-15.pdf",
        "archetype": "A",
        "sessions": [
            {"date": "2014-11-22", "slug": "primo_compitino", "testi": (5, 9), "soluzioni": (38, 43), "title": "Primo compitino (22 novembre 2014)"},
            {"date": "2015-01-14", "slug": "secondo_compitino_e_primo_appello", "testi": (10, 14), "soluzioni": (44, 51), "title": "Secondo compitino e primo appello (14 gennaio 2015)"},
            {"date": "2015-01-30", "slug": "secondo_appello", "testi": (15, 19), "soluzioni": (52, 58), "title": "Secondo appello (30 gennaio 2015)"},
            {"date": "2015-02-19", "slug": "terzo_appello", "testi": (20, 24), "soluzioni": (59, 67), "title": "Terzo appello (19 febbraio 2015)"},
            {"date": "2015-06-10", "slug": "quarto_appello", "testi": (25, 28), "soluzioni": (68, 74), "title": "Quarto appello (10 giugno 2015)"},
            {"date": "2015-07-08", "slug": "quinto_appello", "testi": (29, 31), "soluzioni": (75, 80), "title": "Quinto appello (8 luglio 2015)"},
            {"date": "2015-07-29", "slug": "sesto_appello", "testi": (32, 34), "soluzioni": (81, 86), "title": "Sesto appello (29 luglio 2015)"},
            {"date": "2015-09-14", "slug": "settimo_appello", "testi": (35, 36), "soluzioni": (87, 89), "title": "Settimo appello (14 settembre 2015)"},
        ]
    },
    "2013-14": {
        "master_pdf": "esami_2013-14.pdf",
        "archetype": "A",
        "sessions": [
            {"date": "2013-11-23", "slug": "primo_compitino", "testi": (5, 9), "soluzioni": (33, 39), "title": "Primo compitino (23 novembre 2013)"},
            {"date": "2014-01-11", "slug": "secondo_compitino", "testi": (10, 11), "soluzioni": (40, 43), "title": "Secondo compitino (11 gennaio 2014)"},
            {"date": "2014-01-14", "slug": "primo_appello", "testi": (12, 14), "soluzioni": (44, 48), "title": "Primo appello (14 gennaio 2014)"},
            {"date": "2014-02-01", "slug": "secondo_appello", "testi": (15, 18), "soluzioni": (49, 54), "title": "Secondo appello (1 febbraio 2014)"},
            {"date": "2014-02-20", "slug": "terzo_appello", "testi": (19, 22), "soluzioni": (55, 59), "title": "Terzo appello (20 febbraio 2014)"},
            {"date": "2014-06-18", "slug": "quarto_appello", "testi": (23, 24), "soluzioni": (60, 64), "title": "Quarto appello (18 giugno 2014)"},
            {"date": "2014-07-03", "slug": "quinto_appello", "testi": (25, 27), "soluzioni": (65, 68), "title": "Quinto appello (3 luglio 2014)"},
            {"date": "2014-07-24", "slug": "sesto_appello", "testi": (28, 29), "soluzioni": (69, 72), "title": "Sesto appello (24 luglio 2014)"},
            {"date": "2014-09-18", "slug": "settimo_appello", "testi": (30, 31), "soluzioni": (73, 76), "title": "Settimo appello (18 settembre 2014)"},
        ]
    },
    "2012-13": {
        "master_pdf": "esami_2012-13.pdf",
        "archetype": "A",
        "sessions": [
            {"date": "2012-11-24", "slug": "primo_compitino", "testi": (5, 8), "soluzioni": (31, 36), "title": "Primo compitino (24 novembre 2012)"},
            {"date": "2012-12-17", "slug": "secondo_compitino", "testi": (9, 9), "soluzioni": (37, 39), "title": "Secondo compitino (17 dicembre 2012)"},
            {"date": "2013-01-08", "slug": "primo_appello", "testi": (10, 10), "soluzioni": (40, 41), "title": "Primo appello (8 gennaio 2013)"},
            {"date": "2013-02-02", "slug": "secondo_appello", "testi": (11, 14), "soluzioni": (42, 47), "title": "Secondo appello (2 febbraio 2013)"},
            {"date": "2013-02-18", "slug": "terzo_appello", "testi": (15, 18), "soluzioni": (48, 52), "title": "Terzo appello (18 febbraio 2013)"},
            {"date": "2013-06-13", "slug": "quarto_appello", "testi": (19, 21), "soluzioni": (53, 57), "title": "Quarto appello (13 giugno 2013)"},
            {"date": "2013-07-03", "slug": "quinto_appello", "testi": (22, 24), "soluzioni": (58, 62), "title": "Quinto appello (3 luglio 2013)"},
            {"date": "2013-07-24", "slug": "sesto_appello", "testi": (25, 27), "soluzioni": (63, 66), "title": "Sesto appello (24 luglio 2013)"},
            {"date": "2013-09-16", "slug": "settimo_appello", "testi": (28, 29), "soluzioni": (67, 69), "title": "Settimo appello (16 settembre 2013)"},
        ]
    },
    "2011-12": {
        "master_pdf": "esami_2011-12.pdf",
        "archetype": "A",
        "sessions": [
            {"date": "2011-12-05", "slug": "compitino_prova", "testi": (4, 4), "soluzioni": (18, 18), "title": "Compitino di prova (5 dicembre 2011)"},
            {"date": "2011-12-19", "slug": "primo_compitino", "testi": (5, 6), "soluzioni": (19, 21), "title": "Primo compitino (19 dicembre 2011)"},
            {"date": "2012-01-20", "slug": "compitino_recupero", "testi": (7, 8), "soluzioni": (22, 23), "title": "Compitino di recupero (20 gennaio 2012)"},
            {"date": "2012-04-20", "slug": "secondo_compitino", "testi": (9, 10), "soluzioni": (24, 27), "title": "Secondo compitino (20 aprile 2012)"},
            {"date": "2012-06-06", "slug": "terzo_compitino_e_primo_appello", "testi": (11, 12), "soluzioni": (28, 31), "title": "Terzo compitino e primo appello (6 giugno 2012)"},
            {"date": "2012-07-18", "slug": "secondo_appello", "testi": (13, 13), "soluzioni": (32, 33), "title": "Secondo appello (18 luglio 2012)"},
            {"date": "2012-09-03", "slug": "terzo_appello", "testi": (14, 14), "soluzioni": (34, 35), "title": "Terzo appello (3 settembre 2012)"},
            {"date": "2013-01-14", "slug": "quarto_appello", "testi": (15, 15), "soluzioni": (36, 37), "title": "Quarto appello (14 gennaio 2013)"},
            {"date": "2013-02-13", "slug": "quinto_appello", "testi": (16, 16), "soluzioni": (38, 39), "title": "Quinto appello (13 febbraio 2013)"},
        ]
    },
}

def split_session_archetype_b(src_doc: fitz.Document, session: dict, out_path: str) -> None:
    p_start, p_end = session["pages"]
    # 0-indexed: from (p_start - 1) to (p_end - 1)
    new_doc = fitz.open()
    new_doc.insert_pdf(src_doc, from_page=p_start - 1, to_page=p_end - 1)
    new_doc.save(out_path, deflate=True)
    new_doc.close()

def split_session_archetype_a(src_doc: fitz.Document, session: dict, out_path: str) -> None:
    t_start, t_end = session["testi"]
    s_start, s_end = session["soluzioni"]
    # 0-indexed insert
    new_doc = fitz.open()
    new_doc.insert_pdf(src_doc, from_page=t_start - 1, to_page=t_end - 1)
    new_doc.insert_pdf(src_doc, from_page=s_start - 1, to_page=s_end - 1)
    new_doc.save(out_path, deflate=True)
    new_doc.close()

def process_year(year: str, config: dict) -> int:
    year_dir = os.path.join(BASE_DIR, year)
    master_path = os.path.join(year_dir, config["master_pdf"])
    
    if not os.path.exists(master_path):
        print(f"  [ERROR] Master PDF not found: {master_path}")
        return 0
    
    src_doc = fitz.open(master_path)
    count = 0
    
    print(f"\nProcessing {year} (Archetype {config['archetype']}) — Master: {config['master_pdf']} ({len(src_doc)} pp)")
    
    for session in config["sessions"]:
        filename = f"{session['date']}_{session['slug']}.pdf"
        out_path = os.path.join(year_dir, filename)
        
        if config["archetype"] == "B":
            split_session_archetype_b(src_doc, session, out_path)
        elif config["archetype"] == "A":
            split_session_archetype_a(src_doc, session, out_path)
        else:
            raise ValueError(f"Unknown archetype {config['archetype']}")
        
        # Verify created file
        out_doc = fitz.open(out_path)
        p_count = len(out_doc)
        out_doc.close()
        print(f"  -> Generated {filename} ({p_count} pages) — {session['title']}")
        count += 1
        
    src_doc.close()
    return count

def main():
    print("=" * 70)
    print("ANALISI 1 EXAM SPLITTER — PyMuPDF Slicing & Merging Engine")
    print("=" * 70)
    
    total_split = 0
    for year, config in sorted(EXAM_SESSION_DEFINITIONS.items()):
        total_split += process_year(year, config)
        
    print("\n" + "=" * 70)
    print(f"Splitting Complete: {total_split} session PDFs generated across {len(EXAM_SESSION_DEFINITIONS)} academic years.")
    print("=" * 70)

if __name__ == "__main__":
    main()

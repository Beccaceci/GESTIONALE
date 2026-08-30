#!/usr/bin/env python3
"""
download_archive.py - Analisi 1 Past Exams Archive Downloader

Retrieves master compilations of past exam papers and official solutions
from Prof. Giovanni Alberti's didactics archive (Università di Pisa).
Target path: courses/first_year/ANALISI1/esami/<YYYY-YY>/
"""

import os
import sys
import time
import urllib.request
import fitz

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../courses/first_year/ANALISI1/esami"))

ARCHIVE_SOURCES = [
    {
        "year": "2024-25",
        "course": "Analisi Matematica 1 (Matematica)",
        "url": "https://pagine.dm.unipi.it/alberti/didattica/corsi/24-25_AM1/AM1_24-25_esami_testi+soluzioni.pdf",
        "filename": "esami_2024-25.pdf",
        "expected_pages": 59
    },
    {
        "year": "2023-24",
        "course": "Analisi Matematica 1 (Matematica)",
        "url": "https://pagine.dm.unipi.it/alberti/didattica/corsi/23-24_AM1/AM1_23-24_esami_testi+soluzioni.pdf",
        "filename": "esami_2023-24.pdf",
        "expected_pages": 64
    },
    {
        "year": "2022-23",
        "course": "Analisi Matematica 1 (Matematica)",
        "url": "https://pagine.dm.unipi.it/alberti/didattica/corsi/22-23_AM1/AM1_22-23_esami_testi+soluzioni.pdf",
        "filename": "esami_2022-23.pdf",
        "expected_pages": 75
    },
    {
        "year": "2022-23",
        "course": "Analisi Matematica (Ing. Gestionale)",
        "url": "https://pagine.dm.unipi.it/alberti/didattica/corsi/22-23_AMgest/AMgest_22-23_esami_testi+soluzioni.pdf",
        "filename": "esami_2022-23_AMgest.pdf",
        "expected_pages": 38
    },
    {
        "year": "2021-22",
        "course": "Analisi Matematica I (Ing. Gestionale)",
        "url": "https://pagine.dm.unipi.it/alberti/didattica/corsi/21-22_AM1gest/AM1gest_21-22_esami_testi+soluzioni.pdf",
        "filename": "esami_2021-22.pdf",
        "expected_pages": 38
    },
    {
        "year": "2020-21",
        "course": "Analisi Matematica I (Ing. Gestionale)",
        "url": "https://pagine.dm.unipi.it/alberti/didattica/corsi/20-21_AM1gest/AM1gest_20-21_esami_testi+soluzioni.pdf",
        "filename": "esami_2020-21.pdf",
        "expected_pages": 47
    },
    {
        "year": "2017-18",
        "course": "Analisi Matematica I (Ing. Gestionale)",
        "url": "https://pagine.dm.unipi.it/alberti/didattica/corsi/17-18_AM1Gest/AM1Gest_17-18_esami.pdf",
        "filename": "esami_2017-18.pdf",
        "expected_pages": 98
    },
    {
        "year": "2016-17",
        "course": "Analisi Matematica I (Ing. Gestionale)",
        "url": "https://pagine.dm.unipi.it/alberti/didattica/corsi/16-17_AM1Gest/AM1Gest_16-17_esami.pdf",
        "filename": "esami_2016-17.pdf",
        "expected_pages": 82
    },
    {
        "year": "2015-16",
        "course": "Analisi Matematica I (Ing. Gestionale)",
        "url": "https://pagine.dm.unipi.it/alberti/didattica/corsi/15-16_AM1Gest/AM1Gest_15-16_esami.pdf",
        "filename": "esami_2015-16.pdf",
        "expected_pages": 92
    },
    {
        "year": "2014-15",
        "course": "Analisi Matematica I (Ing. Gestionale)",
        "url": "https://pagine.dm.unipi.it/alberti/didattica/corsi/14-15_AM1Gest/AM1Gest_14-15_esami.pdf",
        "filename": "esami_2014-15.pdf",
        "expected_pages": 89
    },
    {
        "year": "2013-14",
        "course": "Analisi Matematica I (Ing. Gestionale)",
        "url": "https://pagine.dm.unipi.it/alberti/didattica/corsi/13-14_AM1Gest/AM1Gest_13-14_esami.pdf",
        "filename": "esami_2013-14.pdf",
        "expected_pages": 76
    },
    {
        "year": "2012-13",
        "course": "Analisi Matematica I (Ing. Gestionale)",
        "url": "https://pagine.dm.unipi.it/alberti/didattica/corsi/12-13_AM1Gest/AM1Gest_12-13_esami.pdf",
        "filename": "esami_2012-13.pdf",
        "expected_pages": 69
    },
    {
        "year": "2011-12",
        "course": "Matematica (Scienze Geologiche)",
        "url": "https://pagine.dm.unipi.it/alberti/didattica/corsi/11-12_MateGeo/MateGeo_11-12_esami.pdf",
        "filename": "esami_2011-12.pdf",
        "expected_pages": 39
    },
]

def download_file(url: str, dest_path: str, max_retries: int = 3) -> bool:
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"}
    )
    for attempt in range(1, max_retries + 1):
        try:
            print(f"  Downloading {url} (Attempt {attempt}/{max_retries})...")
            with urllib.request.urlopen(req, timeout=30) as resp:
                if resp.status != 200:
                    print(f"  [ERROR] HTTP Status {resp.status}")
                    time.sleep(2)
                    continue
                content = resp.read()
                with open(dest_path, "wb") as f:
                    f.write(content)
            
            # Validate PDF with fitz
            doc = fitz.open(dest_path)
            page_count = len(doc)
            doc.close()
            print(f"  [SUCCESS] Saved {dest_path} ({len(content):,} bytes, {page_count} pages)")
            return True
        except Exception as e:
            print(f"  [ERROR] Attempt {attempt} failed: {e}")
            time.sleep(2)
    return False

def main():
    print("=" * 70)
    print("ANALISI 1 ARCHIVE DOWNLOADER — Prof. G. Alberti (UniPi)")
    print("=" * 70)
    print(f"Target directory: {BASE_DIR}\n")
    
    success_count = 0
    total = len(ARCHIVE_SOURCES)
    
    for item in ARCHIVE_SOURCES:
        year = item["year"]
        dest = os.path.join(BASE_DIR, year, item["filename"])
        print(f"\n[{item['year']}] {item['course']}")
        if os.path.exists(dest):
            try:
                doc = fitz.open(dest)
                if len(doc) == item["expected_pages"]:
                    print(f"  [EXISTS] {dest} already present and valid ({len(doc)} pages).")
                    doc.close()
                    success_count += 1
                    continue
                doc.close()
            except Exception:
                pass
        
        ok = download_file(item["url"], dest)
        if ok:
            success_count += 1
        else:
            print(f"  [FAILED] Could not retrieve {item['url']}")

    print("\n" + "=" * 70)
    print(f"Download Summary: {success_count}/{total} files successfully verified.")
    print("=" * 70)
    
    if success_count < total:
        sys.exit(1)

if __name__ == "__main__":
    main()

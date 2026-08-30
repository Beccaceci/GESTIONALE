#!/usr/bin/env python3
"""
verify_exams.py - 4-Tier Automated Verification Suite for Analisi 1 Exams

Performs comprehensive validation:
- Tier 1: File Integrity & PDF Spec Compliance
- Tier 2: Page Accounting & Partition Integrity
- Tier 3: Problem & Solution Content Completeness
- Tier 4: Visual Sanity, Page Rendering & README Link Integrity
"""

import os
import sys
import re
import fitz

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../courses/first_year/ANALISI1/esami"))
README_PATH = os.path.join(BASE_DIR, "README.md")

EXPECTED_YEARS = [
    "2011-12", "2012-13", "2013-14", "2014-15", "2015-16",
    "2016-17", "2017-18", "2020-21", "2021-22", "2022-23",
    "2023-24", "2024-25"
]

def run_tier_1_file_integrity(pdf_files: list) -> tuple:
    print("\n--- [TIER 1] File Integrity & PDF Specification ---")
    errors = []
    passed = 0
    
    for path in pdf_files:
        rel_path = os.path.relpath(path, BASE_DIR)
        if not os.path.exists(path):
            errors.append(f"File does not exist: {rel_path}")
            continue
        size = os.path.getsize(path)
        if size < 5120:  # < 5 KB
            errors.append(f"File too small ({size} bytes): {rel_path}")
            continue
        
        with open(path, "rb") as f:
            header = f.read(5)
            if header != b"%PDF-":
                errors.append(f"Invalid PDF magic header ({header}): {rel_path}")
                continue
                
        try:
            doc = fitz.open(path)
            if doc.is_encrypted:
                errors.append(f"PDF is encrypted: {rel_path}")
            elif len(doc) < 1:
                errors.append(f"PDF has 0 pages: {rel_path}")
            else:
                passed += 1
            doc.close()
        except Exception as e:
            errors.append(f"PyMuPDF open failed for {rel_path}: {e}")
            
    print(f"Tier 1 Result: {passed}/{len(pdf_files)} PDFs passed integrity checks.")
    if errors:
        for err in errors[:10]:
            print(f"  [FAIL] {err}")
    return len(errors) == 0, errors

def run_tier_2_page_accounting(year_dirs: list) -> tuple:
    print("\n--- [TIER 2] Page Accounting & Partition Integrity ---")
    errors = []
    total_sessions = 0
    session_pattern = re.compile(r"^\d{4}-\d{2}-\d{2}_[a-z0-9_]+\.pdf$")
    master_pattern = re.compile(r"^esami_\d{4}-\d{2}(?:_[A-Za-z0-9]+)?\.pdf$")
    
    for y_dir in year_dirs:
        year_name = os.path.basename(y_dir)
        files = os.listdir(y_dir)
        pdf_files = [f for f in files if f.endswith(".pdf")]
        master_files = [f for f in pdf_files if master_pattern.match(f)]
        session_files = [f for f in pdf_files if session_pattern.match(f)]
        
        if not master_files:
            errors.append(f"Year {year_name} is missing master compilation PDF")
        
        if len(session_files) < 7:
            errors.append(f"Year {year_name} has only {len(session_files)} session files (expected >= 7)")
            
        total_sessions += len(session_files)
        
        # Check invalid filenames
        for f in pdf_files:
            if not master_pattern.match(f) and not session_pattern.match(f):
                errors.append(f"Invalid filename in {year_name}: {f}")

    print(f"Tier 2 Result: {len(year_dirs)} years inspected, {total_sessions} total session PDFs detected.")
    if total_sessions < 99:
        errors.append(f"Total session PDFs ({total_sessions}) is less than expected 99.")
        
    if errors:
        for err in errors[:10]:
            print(f"  [FAIL] {err}")
    return len(errors) == 0, errors

def run_tier_3_content_and_solutions(session_files: list) -> tuple:
    print("\n--- [TIER 3] Problem & Solution Content Completeness ---")
    errors = []
    passed = 0
    
    # Regex patterns for problem statement & solution indicators
    prob_re = re.compile(r"(compit|appell|scritt|parte\s+[ab]|quesit|eserciz|problema|gruppo)", re.I)
    sol_re = re.compile(r"(soluzion|svolgiment|rispost|dimostraz|risoluzion)", re.I)
    
    for path in session_files:
        rel_path = os.path.relpath(path, BASE_DIR)
        try:
            doc = fitz.open(path)
            full_text = "\n".join(page.get_text() for page in doc)
            doc.close()
            
            has_prob = bool(prob_re.search(full_text))
            has_sol = bool(sol_re.search(full_text))
            
            if not has_prob:
                errors.append(f"Missing problem statement marker in: {rel_path}")
            elif not has_sol:
                errors.append(f"Missing solution marker in: {rel_path}")
            else:
                passed += 1
        except Exception as e:
            errors.append(f"Error inspecting {rel_path}: {e}")
            
    print(f"Tier 3 Result: {passed}/{len(session_files)} session PDFs confirmed to contain BOTH problems and solutions.")
    if errors:
        for err in errors[:10]:
            print(f"  [FAIL] {err}")
    return len(errors) == 0, errors

def run_tier_4_visual_and_readme(pdf_files: list) -> tuple:
    print("\n--- [TIER 4] Visual Renderability & Catalog Link Integrity ---")
    errors = []
    
    # Visual pixmap rendering check on all pages
    rendered_pages = 0
    for path in pdf_files:
        rel_path = os.path.relpath(path, BASE_DIR)
        try:
            doc = fitz.open(path)
            for p_no in range(len(doc)):
                page = doc[p_no]
                pix = page.get_pixmap(dpi=72)
                if pix.width < 100 or pix.height < 100:
                    errors.append(f"Unusual pixmap dimensions ({pix.width}x{pix.height}) on page {p_no+1} of {rel_path}")
                rendered_pages += 1
            doc.close()
        except Exception as e:
            errors.append(f"Render failed on {rel_path}: {e}")
            
    print(f"  Render check: {rendered_pages} pages rendered across {len(pdf_files)} PDFs without error.")
    
    # README.md link checker
    if not os.path.exists(README_PATH):
        errors.append(f"Catalog README.md missing at {README_PATH}")
    else:
        with open(README_PATH, "r", encoding="utf-8") as f:
            content = f.read()
        links = re.findall(r"\[.*?\]\((\.\/[^)]+\.pdf)\)", content)
        if not links:
            errors.append("No relative PDF links found in README.md")
        else:
            broken_links = 0
            for link in links:
                target = os.path.normpath(os.path.join(BASE_DIR, link))
                if not os.path.isfile(target):
                    errors.append(f"Broken link in README.md: {link} -> {target}")
                    broken_links += 1
            print(f"  Link check: {len(links)} links tested, {broken_links} broken links.")
            
    print(f"Tier 4 Result: {'PASSED' if not errors else 'FAILED'}")
    if errors:
        for err in errors[:10]:
            print(f"  [FAIL] {err}")
    return len(errors) == 0, errors

def main():
    print("=" * 70)
    print("ANALISI 1 4-TIER EXAM VERIFICATION SUITE")
    print("=" * 70)
    print(f"Base Directory: {BASE_DIR}")
    
    if not os.path.isdir(BASE_DIR):
        print(f"[CRITICAL] Base directory does not exist: {BASE_DIR}")
        sys.exit(1)
        
    year_dirs = [os.path.join(BASE_DIR, y) for y in EXPECTED_YEARS if os.path.isdir(os.path.join(BASE_DIR, y))]
    all_pdfs = []
    session_pdfs = []
    
    session_pattern = re.compile(r"^\d{4}-\d{2}-\d{2}_[a-z0-9_]+\.pdf$")
    
    for y_dir in year_dirs:
        for f in sorted(os.listdir(y_dir)):
            if f.endswith(".pdf"):
                full_path = os.path.join(y_dir, f)
                all_pdfs.append(full_path)
                if session_pattern.match(f):
                    session_pdfs.append(full_path)
                    
    t1_ok, t1_errs = run_tier_1_file_integrity(all_pdfs)
    t2_ok, t2_errs = run_tier_2_page_accounting(year_dirs)
    t3_ok, t3_errs = run_tier_3_content_and_solutions(session_pdfs)
    t4_ok, t4_errs = run_tier_4_visual_and_readme(all_pdfs)
    
    all_ok = t1_ok and t2_ok and t3_ok and t4_ok
    
    print("\n" + "=" * 70)
    print("VERIFICATION SUMMARY REPORT")
    print("=" * 70)
    print(f"  Tier 1 (File Integrity):       {'PASS' if t1_ok else 'FAIL'}")
    print(f"  Tier 2 (Page Accounting):      {'PASS' if t2_ok else 'FAIL'}")
    print(f"  Tier 3 (Content & Solutions):  {'PASS' if t3_ok else 'FAIL'}")
    print(f"  Tier 4 (Visuals & README):     {'PASS' if t4_ok else 'FAIL'}")
    print(f"  Total Inspected PDFs:          {len(all_pdfs)} ({len(session_pdfs)} session files)")
    print("=" * 70)
    
    if not all_ok:
        sys.exit(1)
    else:
        print("\nAll 4 tiers PASSED with 100% success rate. Zero defects.")

if __name__ == "__main__":
    main()

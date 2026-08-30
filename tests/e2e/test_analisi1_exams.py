"""
test_analisi1_exams.py - End-to-End Test Suite for Analisi 1 Past Exams Archive
"""

import os
import re
import fitz
import pytest

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../courses/first_year/ANALISI1/esami"))
README_PATH = os.path.join(BASE_DIR, "README.md")

EXPECTED_YEARS = [
    "2011-12", "2012-13", "2013-14", "2014-15", "2015-16",
    "2016-17", "2017-18", "2020-21", "2021-22", "2022-23",
    "2023-24", "2024-25"
]

@pytest.fixture(scope="session")
def exam_environment():
    assert os.path.isdir(BASE_DIR), f"Base exams directory missing: {BASE_DIR}"
    year_dirs = [os.path.join(BASE_DIR, y) for y in EXPECTED_YEARS]
    for yd in year_dirs:
        assert os.path.isdir(yd), f"Year directory missing: {yd}"
    return {
        "base_dir": BASE_DIR,
        "year_dirs": year_dirs
    }

def test_all_12_years_exist(exam_environment):
    """Test 1: Check that all 12 academic year folders exist."""
    for y in EXPECTED_YEARS:
        yd = os.path.join(BASE_DIR, y)
        assert os.path.isdir(yd), f"Missing academic year folder {y}"

def test_master_compilations_present(exam_environment):
    """Test 2: Check that each year has a master compilation PDF."""
    for y in EXPECTED_YEARS:
        master_path = os.path.join(BASE_DIR, y, f"esami_{y}.pdf")
        assert os.path.isfile(master_path), f"Missing master compilation for {y}: {master_path}"
        doc = fitz.open(master_path)
        assert len(doc) >= 30, f"Master compilation for {y} has too few pages: {len(doc)}"
        doc.close()

def test_session_pdf_naming_and_count(exam_environment):
    """Test 3: Verify that >=99 session PDFs exist and match YYYY-MM-DD_<slug>.pdf format."""
    session_pattern = re.compile(r"^\d{4}-\d{2}-\d{2}_[a-z0-9_]+\.pdf$")
    total_sessions = 0
    for y in EXPECTED_YEARS:
        yd = os.path.join(BASE_DIR, y)
        files = [f for f in os.listdir(yd) if f.endswith(".pdf") and f != f"esami_{y}.pdf" and not f.startswith("esami_")]
        assert len(files) >= 7, f"Year {y} has only {len(files)} sessions"
        for f in files:
            assert session_pattern.match(f), f"Invalid session filename: {f} in {y}"
            total_sessions += 1
    assert total_sessions >= 99, f"Total session files ({total_sessions}) is less than 99"

def test_tier1_pdf_integrity(exam_environment):
    """Test 4: Tier 1 File integrity for all PDFs in the archive."""
    for root, _, files in os.walk(BASE_DIR):
        for f in files:
            if f.endswith(".pdf"):
                path = os.path.join(root, f)
                assert os.path.getsize(path) >= 5120, f"PDF too small: {path}"
                with open(path, "rb") as fp:
                    header = fp.read(5)
                assert header == b"%PDF-", f"Invalid PDF header: {path}"
                doc = fitz.open(path)
                assert not doc.is_encrypted, f"PDF encrypted: {path}"
                assert len(doc) >= 1, f"PDF has 0 pages: {path}"
                doc.close()

def test_tier3_problem_and_solution_presence(exam_environment):
    """Test 5: Tier 3 Problem statements and solutions presence across all session PDFs."""
    prob_re = re.compile(r"(compit|appell|scritt|parte\s+[ab]|quesit|eserciz|problema|gruppo)", re.I)
    sol_re = re.compile(r"(soluzion|svolgiment|rispost|dimostraz|risoluzion)", re.I)
    
    session_pattern = re.compile(r"^\d{4}-\d{2}-\d{2}_[a-z0-9_]+\.pdf$")
    
    checked = 0
    for root, _, files in os.walk(BASE_DIR):
        for f in files:
            if session_pattern.match(f):
                path = os.path.join(root, f)
                doc = fitz.open(path)
                full_text = "\n".join(page.get_text() for page in doc)
                doc.close()
                
                assert prob_re.search(full_text), f"Missing problem statements in {f}"
                assert sol_re.search(full_text), f"Missing solution in {f}"
                checked += 1
                
    assert checked >= 99, f"Checked only {checked} sessions"

def test_tier4_readme_catalog_and_links(exam_environment):
    """Test 6: Tier 4 README catalog exists and contains 0 broken links."""
    assert os.path.isfile(README_PATH), f"README.md missing at {README_PATH}"
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    
    links = re.findall(r"\[.*?\]\((\.\/[^)]+\.pdf)\)", content)
    assert len(links) >= 100, f"Expected >=100 links in README.md, found {len(links)}"
    
    for rel_link in links:
        target = os.path.normpath(os.path.join(BASE_DIR, rel_link))
        assert os.path.isfile(target), f"Broken link in README.md: {rel_link} -> {target}"

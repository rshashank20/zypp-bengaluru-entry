#!/usr/bin/env python3
"""Lightweight integrity checks for the Zypp Bengaluru fleet-sizing case."""
from pathlib import Path
import sys
import zipfile
from openpyxl import load_workbook

ROOT = Path(__file__).resolve().parent
EXPECTED_SHEETS = {
    "zypp_sizing_model.xlsx": {"00_Cover", "01_Inputs", "02_Demand", "03_Sizing", "04_Target", "05_Scenarios", "06_Sources"},
    "zypp_tco_model.xlsx": {"00_Cover", "01_Inputs", "02_EV_TCO", "03_Petrol_TCO", "04_Comparison", "05_Sensitivity", "06_Sources"},
}
errors = []

for filename, expected in EXPECTED_SHEETS.items():
    path = ROOT / "excel" / filename
    if not path.exists():
        errors.append(f"Missing workbook: {path.relative_to(ROOT)}")
        continue
    if not zipfile.is_zipfile(path):
        errors.append(f"Not a valid XLSX/ZIP archive: {path.relative_to(ROOT)}")
        continue
    try:
        wb = load_workbook(path, data_only=False, read_only=True)
        actual = set(wb.sheetnames)
        missing = expected - actual
        if missing:
            errors.append(f"{filename} missing sheets: {', '.join(sorted(missing))}")
        formula_count = 0
        for ws in wb.worksheets:
            for row in ws.iter_rows():
                for cell in row:
                    value = cell.value
                    if isinstance(value, str) and value.startswith("="):
                        formula_count += 1
                        if "#REF!" in value:
                            errors.append(f"{filename}:{ws.title}!{cell.coordinate} has #REF! formula")
        if formula_count == 0:
            errors.append(f"{filename} contains no formulas")
        print(f"PASS workbook: {filename} | sheets={len(wb.sheetnames)} | formulas={formula_count}")
        wb.close()
    except Exception as exc:  # fail the validation visibly rather than silently skip
        errors.append(f"Could not read {filename}: {exc}")

dashboard = ROOT / "dashboard" / "index.html"
if not dashboard.exists():
    errors.append("Missing dashboard/index.html")
else:
    html = dashboard.read_text(encoding="utf-8")
    required = ["1.69M", "507K", "110,019", "₹2.22/km", "₹4.17/km", "2023", "static snapshot"]
    for phrase in required:
        if phrase.lower() not in html.lower():
            errors.append(f"Dashboard missing expected current reference: {phrase}")
    stale = ["1.73M", "518K", "₹2.17", "₹4.01", "unachievable", "live formula"]
    for phrase in stale:
        if phrase.lower() in html.lower():
            errors.append(f"Dashboard still contains stale/overstated text: {phrase}")
    print("PASS dashboard: current scenario labels and caveats checked")

readme = ROOT / "README.md"
if not readme.exists():
    errors.append("Missing README.md")
else:
    txt = readme.read_text(encoding="utf-8")
    for phrase in ["build_sizing.py", "build_tco.py", "dashboard/index.html", "static snapshot"]:
        if phrase.lower() not in txt.lower():
            errors.append(f"README missing workflow detail: {phrase}")
    print("PASS README: rebuild and static-dashboard notes checked")

if errors:
    print("\nVALIDATION FAILED")
    for err in errors:
        print(f" - {err}")
    sys.exit(1)

print("\nAll lightweight project integrity checks passed.")

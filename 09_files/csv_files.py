"""
09_files / csv_files.py
Topic: CSV Parsing and Writing

JAVASCRIPT vs PYTHON CSV:
-------------------------
In Node.js:
    Requires an external npm library (like 'csv-parser' or 'papaparse').
In Python:
    The `csv` module is BUILT INTO the standard library!
    - `csv.DictWriter`: Writes lists of dictionaries directly into CSV rows.
    - `csv.DictReader`: Reads CSV rows as dictionaries mapped by column header!
"""
import csv
from pathlib import Path

csv_file = Path("temp_team.csv")

team_members = [
    {"id": 101, "name": "Elena Vance", "role": "Frontend Lead", "city": "Seattle"},
    {"id": 102, "name": "Gordon Freeman", "role": "Research Scientist", "city": "Boston"},
    {"id": 103, "name": "Alyx Vance", "role": "Security Engineer", "city": "Seattle"},
]

# 1. Writing CSV with DictWriter
fieldnames = ["id", "name", "role", "city"]

with open(csv_file, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(team_members)

# 2. Reading CSV with DictReader
print("--- Reading CSV Records ---")
with open(csv_file, mode="r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"[{row['id']}] {row['name']} -> {row['role']} ({row['city']})")

# Cleanup
if csv_file.exists():
    csv_file.unlink()
    print("Cleaned up temp_team.csv")

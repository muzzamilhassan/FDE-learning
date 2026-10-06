"""
=====================================================================
TOPIC: CSV Files
=====================================================================

SCENARIO
--------
A small shop tracks sales in a CSV sheet: item, quantity, price. You
write a script that saves new sales and adds up the day's total by
reading the file back row by row.

TOPIC
-----
The csv module reads/writes rows safely (handles quotes and commas).
csv.DictReader turns each row into a dict keyed by the header names.
csv.DictWriter needs fieldnames= plus a writeheader() call first.
Always open CSV files with newline="" to avoid blank rows on some platforms.
Gotcha: every value comes back as a STRING; convert with int()/float().

QUESTIONS
---------
Q1. Predict the output: the type of a price read back from a CSV.
Q2. Concept check: why newline="" when opening CSV files?
Q3. Spot the bug: DictReader treats the first data row as the header.
Q4. Write code: read sales.csv and print the day's total.

Run: python 08_files/csv_files.py
Answers: answers/08_files.py
=====================================================================
"""

# ------------------------------------------------------------------
# TOPIC EXAMPLES
# ------------------------------------------------------------------
import csv
import shutil
from pathlib import Path

DEMO_DIR = Path(__file__).parent / "demo_files"

try:
    if DEMO_DIR.exists():
        shutil.rmtree(DEMO_DIR)  # fresh start so every run is identical
    DEMO_DIR.mkdir()

    sales_file = DEMO_DIR / "sales.csv"
    rows = [
        {"item": "pen", "qty": "3", "price": "1.50"},
        {"item": "notebook", "qty": "2", "price": "4.00"},
    ]

    # newline="" is the csv module's rule: it prevents doubled blank rows
    with open(sales_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["item", "qty", "price"])
        writer.writeheader()  # the first row, built from fieldnames
        writer.writerows(rows)

    print("--- raw file ---")
    print(sales_file.read_text())

    # DictReader uses the header row as the keys of each row dict
    total = 0.0
    with open(sales_file, "r", newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            # values are strings, so convert before doing any math
            total += int(row["qty"]) * float(row["price"])
            print(f"{row['item']}: {row['qty']} x {row['price']}")
    print(f"Total: {total:.2f}")

finally:
    if DEMO_DIR.exists():
        shutil.rmtree(DEMO_DIR)  # leave no demo files behind

# ------------------------------------------------------------------
# QUESTIONS - try them yourself, then check answers/08_files.py
# ------------------------------------------------------------------
# Q1: rows.csv holds "item,price" then "pen,3". Predict the output:
#         with open("rows.csv", newline="") as f:
#             row = next(csv.DictReader(f))
#             print(row["item"], type(row["price"]).__name__)
#
# Q2: Why must CSV files be opened with newline=""?
#
# Q3: Spot the bug -- DictReader picks up wrong keys and missing rows:
#         with open("sales.csv", "w", newline="") as f:
#             writer = csv.DictWriter(f, fieldnames=["item", "price"])
#             writer.writerow({"item": "pen", "price": "3"})
#
# Q4: Write code: read sales.csv (columns: item, qty, price) and print
#     the day's total, where each row contributes qty * price.

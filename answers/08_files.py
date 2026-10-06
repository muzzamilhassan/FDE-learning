"""
Answers for 08_files - try the questions first!
"""

import csv
import json
import tempfile
from pathlib import Path

# Any answer that touches disk uses a temp folder that deletes itself,
# so running this file repeatedly is always safe.

# ------------------------------------------------------------------
# text_files.py
# ------------------------------------------------------------------
# Q1: Prints "hithere". write() sends exactly the characters you give
#     it and never adds newlines -- you must put "\n" in yourself.
with tempfile.TemporaryDirectory() as tmp:
    out = Path(tmp) / "out.txt"
    with open(out, "w", encoding="utf-8") as f:
        f.write("hi")
        f.write("there")
    with open(out, "r", encoding="utf-8") as f:
        print("text Q1:", repr(f.read()))  # 'hithere'

# Q2: The with-block closes the file the moment it exits, even if an
#     error is raised inside. Without it, a crash before close() leaves
#     the file open and unwritten buffered data can be lost.
print("text Q2: with closes the file even when errors happen")

# Q3: The second open uses "w", and write mode always starts a FRESH
#     file, throwing away "start". Use "a" (append) to keep old text.
with tempfile.TemporaryDirectory() as tmp:
    log = Path(tmp) / "log.txt"
    with open(log, "w", encoding="utf-8") as f:
        f.write("start")
    with open(log, "a", encoding="utf-8") as f:  # fix: "a" not "w"
        f.write("end")
    print("text Q3:", log.read_text())  # startend

# Q4: "a" appends AND creates the file if it does not exist yet, then
#     read the whole thing back with .read().
with tempfile.TemporaryDirectory() as tmp:
    journal = Path(tmp) / "journal.txt"
    with open(journal, "a", encoding="utf-8") as f:
        f.write("Done for today\n")
    with open(journal, "r", encoding="utf-8") as f:
        print("text Q4:", f.read().strip())

# ------------------------------------------------------------------
# json_files.py
# ------------------------------------------------------------------
# Q1: {"ok": true, "count": 2, "tags": null} -- dumps maps Python types
#     to JSON: True -> true, None -> null.
data = {"ok": True, "count": 2, "tags": None}
print("json Q1:", json.dumps(data))

# Q2: dumps/loads convert between objects and STRINGS (network, logs);
#     dump/load read and write FILE objects directly (saving to disk).
print("json Q2: dumps/loads = strings, dump/load = files")

# Q3: JSON object keys are always strings, so the int key 1 came back
#     as "1". Read it with loaded["1"] (or use string keys up front).
loaded = json.loads(json.dumps({1: "one"}))
print("json Q3:", loaded["1"])  # one

# Q4: dump to write straight to a file, load to read it back.
settings = {"theme": "dark", "volume": 80, "notifications": True}
with tempfile.TemporaryDirectory() as tmp:
    path = Path(tmp) / "settings.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(settings, f, indent=2)
    with open(path, "r", encoding="utf-8") as f:
        print("json Q4 theme:", json.load(f)["theme"])  # dark

# ------------------------------------------------------------------
# csv_files.py
# ------------------------------------------------------------------
# Q1: "pen <class 'str'>" -- DictReader hands back dicts, but every
#     value is a STRING, so convert with int()/float() before math.
with tempfile.TemporaryDirectory() as tmp:
    path = Path(tmp) / "rows.csv"
    path.write_text("item,price\npen,3\n", encoding="utf-8")
    with open(path, newline="", encoding="utf-8") as f:
        row = next(csv.DictReader(f))
        print("csv Q1:", row["item"], type(row["price"]).__name__)

# Q2: Without newline="" the raw newlines get translated twice on some
#     platforms, leaving a blank row after every record.
print("csv Q2: open CSVs with newline='' to avoid blank rows")

# Q3: writeheader() was never called, so the file starts with the data
#     row and DictReader uses "pen" as a column name. Call it first.
with tempfile.TemporaryDirectory() as tmp:
    path = Path(tmp) / "fixed.csv"
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["item", "price"])
        writer.writeheader()  # the missing line
        writer.writerow({"item": "pen", "price": "3"})
    print("csv Q3:", path.read_text().strip())  # item,price / pen,3

# Q4: Stream the rows with DictReader, convert each field, sum it up.
with tempfile.TemporaryDirectory() as tmp:
    path = Path(tmp) / "sales.csv"
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["item", "qty", "price"])
        w.writeheader()
        w.writerows([
            {"item": "pen", "qty": "3", "price": "1.50"},
            {"item": "notebook", "qty": "2", "price": "4.00"},
        ])
    total = 0.0
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            total += int(row["qty"]) * float(row["price"])
    print(f"csv Q4 total: {total:.2f}")  # 12.50

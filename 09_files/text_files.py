"""
09_files / text_files.py
Topic: Reading and Writing Text Files with Context Managers (`with open`)

JAVASCRIPT (Node.js) vs PYTHON FILE I/O:
----------------------------------------
In Node.js:
    const fs = require('fs');
    // Synchronous:
    fs.writeFileSync('sample.txt', 'Hello world');
    const content = fs.readFileSync('sample.txt', 'utf-8');

In Python:
    The `with` statement acts as a Context Manager:
    It GUARANTEES that the file descriptor is closed automatically,
    even if an unhandled error occurs midway through reading or writing!
"""
from pathlib import Path

sample_path = Path("demo_text.txt")

# 1. Writing to a text file ('w' mode creates or overwrites)
# JS: fs.writeFileSync('demo_text.txt', 'Line 1\nLine 2');
with open(sample_path, mode="w", encoding="utf-8") as file:
    file.write("First line of notes.\n")
    file.write("Second line: Python automatically closes files via context manager.\n")

# 2. Appending to a text file ('a' mode)
# JS: fs.appendFileSync('demo_text.txt', 'Appended line\n');
with open(sample_path, mode="a", encoding="utf-8") as file:
    file.write("Third line: Appended content.\n")

# 3. Reading the file line-by-line (Memory Efficient!)
# In Python, an open file object is an iterable of lines:
print("--- Reading Lines ---")
with open(sample_path, mode="r", encoding="utf-8") as file:
    for line_number, line in enumerate(file, start=1):
        print(f"Line {line_number}: {line.strip()}")

# Cleanup temporary file
if sample_path.exists():
    sample_path.unlink()
    print("Cleaned up demo_text.txt")

"""
=====================================================================
TOPIC: Text Files
=====================================================================

SCENARIO
--------
You are building a tiny study journal. Each evening the app saves your
notes to a plain text file, and each morning it prints them back so you
can review yesterday before starting fresh.

TOPIC
-----
open(path, mode) opens a file: "w" write (OVERWRITES!), "a" append, "r" read.
Use `with open(...) as f:` -- the file closes automatically, even on errors.
Pass encoding="utf-8" so text reads the same on every machine.
f.write(text) writes exactly what you give it -- it never adds newlines.
Looping over the file object reads it line by line (memory friendly).

QUESTIONS
---------
Q1. Predict the output: two write() calls, then reading the file back.
Q2. Concept check: why `with` instead of open() plus close()?
Q3. Spot the bug: a second "w" open makes earlier text vanish.
Q4. Write code: append one line, then print the whole file.

Run: python 08_files/text_files.py
Answers: answers/08_files.py
=====================================================================
"""

# ------------------------------------------------------------------
# TOPIC EXAMPLES
# ------------------------------------------------------------------
import shutil
from pathlib import Path

DEMO_DIR = Path(__file__).parent / "demo_files"

try:
    if DEMO_DIR.exists():
        shutil.rmtree(DEMO_DIR)  # fresh start so every run is identical
    DEMO_DIR.mkdir()

    journal = DEMO_DIR / "journal.txt"
    # "w" creates the file, or WIPES it if it already exists
    with open(journal, "w", encoding="utf-8") as f:
        f.write("Day 1: learned open()\n")
        f.write("Day 2: learned with blocks\n")

    # "a" keeps what is already there and adds to the end
    with open(journal, "a", encoding="utf-8") as f:
        f.write("Day 3: reviewed it all\n")

    # .read() returns the whole file as one string
    with open(journal, "r", encoding="utf-8") as f:
        print("--- whole file ---")
        print(f.read())

    # Looping reads line by line -- better for big files
    with open(journal, "r", encoding="utf-8") as f:
        print("--- line by line ---")
        for number, line in enumerate(f, start=1):
            print(number, line.strip())

finally:
    if DEMO_DIR.exists():
        shutil.rmtree(DEMO_DIR)  # leave no demo files behind

# ------------------------------------------------------------------
# QUESTIONS - try them yourself, then check answers/08_files.py
# ------------------------------------------------------------------
# Q1: Predict the output:
#         with open("out.txt", "w") as f:
#             f.write("hi")
#             f.write("there")
#         with open("out.txt", "r") as f:
#             print(f.read())
#     (Hint: does write() add a newline for you?)
#
# Q2: Why is `with open(...) as f:` safer than calling f.close() yourself?
#
# Q3: Spot the bug -- the coder expected the file to contain "startend":
#         with open("log.txt", "w") as f:
#             f.write("start")
#         with open("log.txt", "w") as f:
#             f.write("end")
#
# Q4: Write code: append "Done for today" to journal.txt (create it if
#     missing), then print the entire file contents.

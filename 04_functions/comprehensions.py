"""
=====================================================================
TOPIC: Comprehensions
=====================================================================

SCENARIO
--------
You are adding search to a notes app. Incoming tags arrive messy:
duplicates, stray whitespace, mixed case. Comprehensions let you
build the clean list, the lookup dict, and the unique-letter set in
one readable line each - no temp lists, no four-line loops.

TOPIC
-----
Syntax: [expression for item in iterable if condition].
The `if` filters; the expression transforms - each part is optional.
Dicts: {k: v for ...}. Sets: {x for ...} (dedupes, unordered).
Rule of thumb: two loops or tangled conditions? A plain for-loop
is usually easier to read.

QUESTIONS
---------
Q1. Predict the output of the odd-squares comprehension.
Q2. Spot the bug: why is the "uppercased" list full of weird objects?
Q3. Write ONE dict comprehension keeping only passing scores.
Q4. Predict the set comprehension output - and explain its catch.

Run: python 04_functions/comprehensions.py
Answers: answers/04_functions.py
=====================================================================
"""

# ------------------------------------------------------------------
# TOPIC EXAMPLES
# ------------------------------------------------------------------

tags = ["  tech ", "NEWS", "tech", "  ", "fun"]

# Transform: the expression on the left runs for every item.
clean = [t.strip().lower() for t in tags]
print(clean)                       # ['tech', 'news', 'tech', '', 'fun']

# Filter: the trailing `if` decides what gets kept.
kept = [t for t in clean if t]     # '' is falsy, so blanks drop out
print(kept)                        # ['tech', 'news', 'tech', 'fun']

# Transform + filter together in a single line.
short = [t.upper() for t in kept if len(t) <= 4]
print(short)                       # ['TECH', 'NEWS', 'TECH', 'FUN']

# Dict comprehension: build key -> value pairs in one pass.
prices = {"pen": 3, "bag": 25, "cup": 9}
with_tax = {item: round(price * 1.2, 2) for item, price in prices.items()}
print(with_tax)                    # {'pen': 3.6, 'bag': 30.0, 'cup': 10.8}

# Set comprehension: like a list comp, but duplicates collapse.
letters = {t[0] for t in kept}
print(letters)                     # {'t', 'n', 'f'} (any print order)

# Borderline: two `for`s in one comp is legal but getting dense.
matrix = [[1, 2], [3, 4]]
flat = [n for row in matrix for n in row]
print(flat)                        # [1, 2, 3, 4]

# ------------------------------------------------------------------
# QUESTIONS - try them yourself, then check answers/04_functions.py
# ------------------------------------------------------------------
# Q1: Predict the output:
#     nums = [1, 2, 3, 4, 5]
#     print([n * n for n in nums if n % 2 == 1])
#
# Q2: Spot the bug - the result holds method objects, not text. Why?
#     What one character fixes it?
#     names = ["ada", "bo"]
#     caps = [n.upper for n in names]
#
# Q3: Given scores = [("ada", 90), ("bo", 55), ("cy", 72)], write ONE
#     dict comprehension producing {"ada": 90, "cy": 72} - names
#     scoring 60 or more.
#
# Q4: Predict the output, then explain why the order is not guaranteed:
#     words = ["ant", "bee", "ape", "bee"]
#     print({w[0] for w in words})

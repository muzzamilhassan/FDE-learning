"""
=====================================================================
TOPIC: Strings
=====================================================================

SCENARIO
--------
Users of your recipe app type display names with extra spaces and
odd capitalisation, and they enter tags as one lump such as
"dessert,cake,quick". Before anything reaches the screen you need
to clean, slice, and rebuild those strings.

TOPIC
-----
- f-strings: f"Hi {name}" drops values straight into the text.
- Index with s[0]; negative indexes count from the end: s[-1].
- Slices: s[start:stop] - the stop index is NOT included.
- Strings are immutable: every method returns a NEW string.
- Common methods: .strip() .upper() .lower() .title()
  .replace(old, new) .split(sep) and sep.join(list).
- Gotcha: s[0] on an empty string raises IndexError.

QUESTIONS
---------
Q1. (predict) What does "Python"[1:4] give, and why not "Pyt"?
Q2. (bug spot) shout = "hey", then shout.upper() - why is shout
    still "hey" afterwards?
Q3. (write code) Clean "  ada LOVELACE  " into "Ada Lovelace".
Q4. (write code) Turn "red,green,blue" into "red | green | blue".

Run: python 01_basics/strings.py
Answers: answers/01_basics.py
=====================================================================
"""

# ------------------------------------------------------------------
# TOPIC EXAMPLES
# ------------------------------------------------------------------

name = "Sarah"
role = "chef"
print(f"Hello, {name} the {role}!")        # f-string interpolation

recipe = "Pancakes"
print("First char:", recipe[0])            # P
print("Last char:", recipe[-1])            # s (counts from the end)
print("Slice [0:4]:", recipe[0:4])         # Panc - stop not included
print("Reverse:", recipe[::-1])            # sekacnaP

# Methods return new strings - the original never changes
messy = "  banana bread  "
clean = messy.strip()                      # removes outer spaces
print(f"{messy!r} became {clean!r}")
print("Titled:", clean.title())            # Banana Bread

# split() cuts a string into a list; join() glues a list back
tags = "dessert,cake,quick".split(",")
print("Tags:", tags)                       # ['dessert', 'cake', 'quick']
print("Rejoined:", " | ".join(tags))       # dessert | cake | quick

# replace() swaps every occurrence
print("Fixed:", "choco.chip".replace(".", "-"))

# ------------------------------------------------------------------
# QUESTIONS - try them yourself, then check answers/01_basics.py
# ------------------------------------------------------------------
# Q1: Predict the output of: print("Python"[1:4])
# Q2: Spot the bug - why does this print lowercase "hey"?
#       shout = "hey"
#       shout.upper()
#       print(shout)
# Q3: Write code: clean "  ada LOVELACE  " into "Ada Lovelace"
#     (strip the spaces, then fix the capitalisation) and print it.
# Q4: Write code: turn "red,green,blue" into "red | green | blue".

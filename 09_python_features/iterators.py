"""
=====================================================================
TOPIC: Iterators
=====================================================================

SCENARIO
--------
You are scanning a huge log file, but you only ever need one line at a
time. The iterator protocol lets you walk any collection value by
value, without loading the whole thing into memory.

TOPIC
-----
iter(obj) gets an iterator; next(it) asks it for the next value.
When nothing is left, next() raises StopIteration.
A for loop is exactly this: iter() once, then next() until
StopIteration arrives (which the loop catches for you).
Lists, strings, dicts and files are all iterable.
Gotcha: an iterator is one-way; once exhausted it stays empty, so
call iter() again for a fresh pass.

QUESTIONS
---------
Q1. Predict the output: three next() calls on iter("hi").
Q2. Concept check: what does a for loop do behind the scenes?
Q3. Spot the bug: the second sum(it) returns 0.
Q4. Write code: a Countdown class you can loop over.

Run: python 09_python_features/iterators.py
Answers: answers/09_python_features.py
=====================================================================
"""

# ------------------------------------------------------------------
# TOPIC EXAMPLES
# ------------------------------------------------------------------

letters = ["a", "b", "c"]

# iter() grabs an iterator; next() asks for the next value
it = iter(letters)
print(next(it))  # a
print(next(it))  # b
print(next(it))  # c

# A fresh iterator starts from the beginning; the old one is spent
it = iter(letters)
print(next(it))  # a

# One more next(it) here would raise StopIteration -- the "empty" signal

# This is ALL a for loop does: iter() + next() until StopIteration
manual = iter(["x", "y"])
while True:
    try:
        print(next(manual))
    except StopIteration:
        break  # the loop's "we are done" signal

# Strings are iterable too -- character by character
for char in "ok":
    print(char)

# ------------------------------------------------------------------
# QUESTIONS - try them yourself, then check answers/09_python_features.py
# ------------------------------------------------------------------
# Q1: Predict the output (including any error):
#         it = iter("hi")
#         print(next(it))
#         print(next(it))
#         print(next(it))
#
# Q2: A for loop hides three steps. Name them, and show the same job
#     with iter(), next() and try/except.
#
# Q3: Spot the bug -- the first print shows 6 but the second shows 0:
#         nums = [1, 2, 3]
#         it = iter(nums)
#         print(sum(it))
#         print(sum(it))
#
# Q4: Write code: a Countdown(start) class with __iter__ and __next__
#     so that list(Countdown(3)) == [3, 2, 1].

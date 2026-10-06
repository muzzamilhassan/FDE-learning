"""
=====================================================================
TOPIC: Tuples - Fixed Collections That Cannot Change
=====================================================================

SCENARIO
--------
Your app passes GPS coordinates and (min, max) stats between
functions. You want to hand these values around knowing nothing can
silently modify them. A tuple is an ordered collection that is
locked once created - ideal for data with a fixed shape.

TOPIC
-----
- Ordered and IMMUTABLE: created with (a, b), never changed after.
- Single-element tuple NEEDS a comma: (42,) - (42) is just the int 42.
- Parentheses are often optional: point = 10, 20 works too.
- Unpack straight into variables: x, y = point.
- Immutability makes tuples hashable, so they work as dict keys.
- Only two methods exist: .count(x) and .index(x). No append, no sort.

QUESTIONS
---------
Q1. Predict: print(type((5))) and print(type((5,)))
Q2. Spot the bug: coords = (10, 20) followed by coords[0] = 15
Q3. Write code: a function min_max(numbers) that returns BOTH the
    smallest and largest value as a tuple, then unpack the result.
Q4. Concept: why can a tuple be a dictionary key but a list cannot?

Run: python 02_collections/tuples.py
Answers: answers/02_collections.py
"""

# ------------------------------------------------------------------
# TOPIC EXAMPLES
# ------------------------------------------------------------------

point = (10, 20)
print("Point:", point)

# Unpacking pulls values out in one line.
x, y = point
print(f"x={x}, y={y}")

# The classic gotcha: the comma makes the tuple, not the parentheses.
single = (42,)          # a tuple with one item
oops = (42)             # a plain int - parentheses were just grouping
print(type(single), type(oops))

# Changing a tuple raises TypeError:
# point[0] = 99  ->  TypeError: 'tuple' object does not support item assignment
# The fix is to build a NEW tuple from the old one.
moved = (99,) + point[1:]
print("Moved:", moved)

# count() and index() are the only lookup methods a tuple offers.
rolls = (3, 1, 3, 5, 3)
print("Count of 3:", rolls.count(3))
print("Index of 5:", rolls.index(5))

# Hashable values can be dictionary keys - tuples qualify.
locations = {
    (40.71, -74.00): "New York",
    (51.50, -0.12): "London",
}
print("City at (40.71, -74.00):", locations[(40.71, -74.00)])

# Functions return tuples to hand back several values at once.
def divide(a, b):
    return a // b, a % b        # two values packed into one tuple

quotient, remainder = divide(17, 5)
print(f"17 // 5 = {quotient}, remainder {remainder}")

# ------------------------------------------------------------------
# QUESTIONS - try them yourself, then check answers/02_collections.py
# ------------------------------------------------------------------
# Q1: Predict the output of each line:
#     print(type((5)))
#     print(type((5,)))
#
# Q2: This line crashes. Which error, and how do you get (99, 20)
#     starting from coords = (10, 20)?
#     coords[0] = 99
#
# Q3: Write a function min_max(numbers) that returns the smallest
#     and largest value as a tuple. Call it and unpack into low, high.
#
# Q4: Concept: why is {(1, 2): "ok"} legal, while {[1, 2]: "no"}
#     raises TypeError?

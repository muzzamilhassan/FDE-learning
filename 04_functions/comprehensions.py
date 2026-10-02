"""
04_functions / comprehensions.py
Topic: List, Dictionary, and Set Comprehensions (Python's Killer Feature!)

JAVASCRIPT DEVELOPER MENTAL MODEL:
----------------------------------
In JavaScript, transforming arrays requires chaining methods:
    const evens = numbers.filter(x => x % 2 === 0);
    const doubled = numbers.map(x => x * 2);
    const doubledEvens = numbers.filter(x => x % 2 === 0).map(x => x * 2);

In Python, Comprehensions replace .map() and .filter() with clean, readable syntax:
    Syntax: [ <expression> for <item> in <iterable> if <condition> ]
    - Reads like natural English!
    - Runs faster at the bytecode level than manual loops or lambda functions.
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# ------------------------------------------------------------------------------
# 1. List Comprehension vs JS filter & map
# ------------------------------------------------------------------------------
# JS: numbers.filter(x => x % 2 === 0)
evens = [x for x in numbers if x % 2 == 0]

# JS: numbers.map(x => x ** 2)
squares = [x ** 2 for x in numbers]

# JS: numbers.filter(x => x % 2 === 0).map(x => x ** 2)
even_squares = [x ** 2 for x in numbers if x % 2 == 0]

print("Evens (filter):", evens)
print("Squares (map):", squares)
print("Even Squares (filter + map):", even_squares)


# ------------------------------------------------------------------------------
# 2. Dictionary Comprehension
# ------------------------------------------------------------------------------
# JS: Object.fromEntries(names.map(name => [name, name.length]))
names = ["Alice", "Bob", "Charlotte", "Dave"]
name_lengths = {name: len(name) for name in names}
print("Dictionary comprehension:", name_lengths)

# Inverting a dictionary (swapping keys and values):
# JS: Object.fromEntries(Object.entries(ports).map(([k, v]) => [v, k]))
ports = {"http": 80, "https": 443, "ssh": 22}
inverted_ports = {v: k for k, v in ports.items()}
print("Inverted dict:", inverted_ports)


# ------------------------------------------------------------------------------
# 3. Set Comprehension (Unique values)
# ------------------------------------------------------------------------------
# JS: new Set(["apple", "banana", "APPLE"].map(w => w.toLowerCase()))
words = ["apple", "banana", "APPLE", "orange", "BANANA"]
unique_lower = {w.lower() for w in words}
print("Set comprehension (unique lowercase):", unique_lower)


# ------------------------------------------------------------------------------
# 4. Generator Expressions (Lazy Evaluation)
# ------------------------------------------------------------------------------
# When you use parentheses () instead of brackets [], you get a GENERATOR:
# It does NOT compute all million numbers in memory! It computes them on-demand:
million_squares = (x ** 2 for x in range(1_000_000))
print("Generator expression object (memory efficient):", million_squares)
print("First item on-demand:", next(million_squares))
print("Second item on-demand:", next(million_squares))

"""
=====================================================================
TOPIC: Lambda
=====================================================================

SCENARIO
--------
Your game app shows a leaderboard. Players are dicts, and the UI
needs them sorted by score, with ties broken by name. Writing a full
named function just to pick one sort key feels heavy - a lambda is
the small, throwaway tool built for exactly this job.

TOPIC
-----
Syntax: lambda params: expression. It IS a function, just unnamed.
One expression only - no statements, no return keyword, no new lines.
Shines as the key= argument for sorted(), min(), max(), and map().
Binding a lambda to a name works, but `def` is the clearer habit.

QUESTIONS
---------
Q1. Predict the sorted() output when the key is the word length.
Q2. Spot the bug: why does sorting the user dicts directly crash?
Q3. Use sorted(key=...) and max(key=...) on the products list.
Q4. Predict add(5) when the lambda has a default value.

Run: python 04_functions/lambda.py
Answers: answers/04_functions.py
=====================================================================
"""

# ------------------------------------------------------------------
# TOPIC EXAMPLES
# ------------------------------------------------------------------

# A lambda is a value like any other - passable, callable, storable.
double = lambda n: n * 2     # fine for demos; prefer `def` in real code
print(double(21))            # 42

# The main use: a tiny key that tells sorted() WHAT to compare.
players = [
    {"name": "Ada", "score": 90},
    {"name": "Bo", "score": 75},
    {"name": "Cy", "score": 90},
]

by_score = sorted(players, key=lambda p: p["score"])
print([p["name"] for p in by_score])    # ['Bo', 'Ada', 'Cy'] (stable sort)

# Sort by score DESCENDING, ties broken by name: use a tuple key.
ranked = sorted(players, key=lambda p: (-p["score"], p["name"]))
print([p["name"] for p in ranked])      # ['Ada', 'Cy', 'Bo']

# min() and max() accept the same key= argument.
print(min(players, key=lambda p: p["score"])["name"])   # Bo

# Lambdas take defaults and keyword params, just like def.
power = lambda base, exp=2: base ** exp
print(power(5), power(3, exp=3))        # 25 27

# ------------------------------------------------------------------
# QUESTIONS - try them yourself, then check answers/04_functions.py
# ------------------------------------------------------------------
# Q1: Predict the output:
#     words = ["banana", "fig", "pear"]
#     print(sorted(words, key=lambda w: len(w)))
#
# Q2: Spot the bug - sorted(users) raises TypeError. Why, and what
#     one-line change fixes it?
#     users = [{"name": "Ann", "age": 30}, {"name": "Bo", "age": 25}]
#
# Q3: Given:
#     products = [{"name": "pen", "price": 3},
#                 {"name": "bag", "price": 25},
#                 {"name": "cup", "price": 9}]
#     use sorted(key=lambda ...) to list the names from cheapest to
#     priciest, and max(key=lambda ...) to get the priciest name.
#
# Q4: Predict the output:
#     add = lambda a, b=10: a + b
#     print(add(5), add(5, b=1))

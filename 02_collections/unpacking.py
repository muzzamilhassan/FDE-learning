"""
=====================================================================
TOPIC: Unpacking - Splitting and Spreading Values
=====================================================================

SCENARIO
--------
Your app stores settings rows like ("theme", "dark"), merges user
overrides into defaults, and passes a whole list of values into a
function in one call. Unpacking splits collections into variables -
and spreads them back out - in a single clean line.

TOPIC
-----
- Assignment: x, y = point pulls items straight into variables.
- A star catches "everything left": first, *rest = items.
- Underscore marks a value you are ignoring: a, _, c = items.
- ** in a dict literal merges: {**base, **extra} (extra wins).
- At CALL time: fn(*my_list) spreads items as positional args;
  fn(**my_dict) spreads pairs as keyword arguments.

QUESTIONS
---------
Q1. Predict: a, *b, c = [1, 2, 3, 4, 5] then print(b)
Q2. Spot the bug: first, second = [1, 2, 3]
Q3. Predict: {**base, **user} when user = {"quality": "high"}
Q4. Write code: define report(*names, **details) printing each name
    then each key/value, and call it using * and ** spreads.

Run: python 02_collections/unpacking.py
Answers: answers/02_collections.py
"""

# ------------------------------------------------------------------
# TOPIC EXAMPLES
# ------------------------------------------------------------------

# 1) Unpack a tuple or list into variables - the counts must match.
point = (10, 20)
x, y = point
print(f"x={x}, y={y}")

# 2) A star catches "everything left"; _ receives but ignores a value.
first, *rest = [1, 2, 3, 4]
print("first:", first, "- rest:", rest)

first, *middle, last = [1, 2, 3, 4, 5]
print("middle:", middle)

name, _, city = ("Ada", 37, "London")
print(f"{name} lives in {city}")

# 3) ** merges dictionaries inside a literal - later keys win.
defaults = {"theme": "light", "lang": "en"}
overrides = {"theme": "dark"}
config = {**defaults, **overrides}
print("Merged config:", config)

# 4) * spreads a list into separate positional arguments.
def add(a, b, c):
    return a + b + c

values = [5, 10, 15]
print("add(*values):", add(*values))    # same as add(5, 10, 15)

# 5) ** spreads a dict into keyword arguments.
def greet(name, greeting):
    return f"{greeting}, {name}!"

info = {"name": "Ada", "greeting": "Hello"}
print(greet(**info))

# ------------------------------------------------------------------
# QUESTIONS - try them yourself, then check answers/02_collections.py
# ------------------------------------------------------------------
# Q1: Predict the output:
#     a, *b, c = [1, 2, 3, 4, 5]
#     print(b)
#
# Q2: This line crashes. Which error, and name two ways to fix it?
#     first, second = [1, 2, 3]
#
# Q3: Predict the output:
#     base = {"volume": 5, "quality": "low"}
#     user = {"quality": "high"}
#     print({**base, **user})
#
# Q4: Write code: define report(*names, **details) that prints each
#     name, then each key/value in details. Call it with
#     report(*["Ana", "Raj"], topic="sets", level=1).

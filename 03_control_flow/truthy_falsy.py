"""
=====================================================================
TOPIC: Truthy and Falsy Values
=====================================================================

SCENARIO
--------
Your app asks users to type a coupon code. An empty box, the number 0,
and an empty list of saved codes should all count as "no code".
Python judges every value as True or False inside an if, so you need
to know exactly which values count as False.

TOPIC
-----
- Falsy values: False, None, 0, 0.0, "", [], {}, set(), range(0).
- Everything else is truthy -- including "0", [0], " " and -1.
- bool(value) shows how Python will judge any value in an if.
- Truthiness lets you write "if items:" instead of a length check.
- Gotcha: 0 is falsy, so "if count:" hides a valid answer of zero.

QUESTIONS
---------
Q1. Predict the output of the Q1 code.
Q2. Which of these are falsy: "False", 0.0, [""], {}, None?
Q3. Spot the bug: the stock counter never prints "0 items left".
Q4. Write first_item(cart): return the first item, or
    "Cart is empty" when the cart has nothing in it.

Run: python 03_control_flow/truthy_falsy.py
Answers: answers/03_control_flow.py
=====================================================================
"""

# ------------------------------------------------------------------
# TOPIC EXAMPLES
# ------------------------------------------------------------------

# bool() reveals exactly how an if would judge each value.
print(bool(0), bool(""), bool([]), bool({}))       # False False False False
print(bool(0.0), bool(set()), bool(None), bool(False))
print(bool("0"), bool([0]), bool(" "), bool(-1))   # all True: non-empty content

# Truthiness makes empty checks read like plain English.
cart = []
if not cart:                       # preferred over len(cart) == 0
    print("Cart is empty -- show the 'start shopping' banner")

# The complete falsy family in one line.
candidates = [False, None, 0, 0.0, "", [], {}, set(), range(0)]
print("All falsy:", [bool(v) for v in candidates])

# Gotcha: 0 is falsy, so "is not None" is the right check when
# zero is a meaningful answer.
items_left = 0
if items_left is not None:
    print(f"Items left: {items_left}")   # still prints, despite 0 being falsy

# ------------------------------------------------------------------
# QUESTIONS - try them yourself, then check answers/03_control_flow.py
# ------------------------------------------------------------------

# Q1: What does this print?
#     print(bool("0"), bool([0]), bool(""), bool(set()))

# Q2: Which of these values are falsy?
#     "False", 0.0, [""], {}, None

# Q3: Spot the bug -- why does "0 items left" never appear?
#     items_left = 0
#     if items_left:
#         print(f"{items_left} items left")

# Q4: Write first_item(cart) that returns the first item, or
#     "Cart is empty" for an empty cart.
#     Test it with ["apple"] and with [].

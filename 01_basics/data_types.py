"""
=====================================================================
TOPIC: Data Types
=====================================================================

SCENARIO
--------
Your coffee-cart checkout takes an order: the item count is a whole
number, the price has decimals, the coupon code is text, and the
gift-note field can be empty. Every value in Python has a type, and
the type decides what you can do with that value.

TOPIC
-----
- Core types: int, float, str, bool, and None (no value at all).
- type(x) shows the type; isinstance(x, int) checks it safely.
- Convert with int(), float(), str(), bool().
- int(3.99) truncates to 3 (it never rounds); int("19.99") raises
  ValueError because that string is not a whole number.
- bool() follows the emptiness rule: 0, 0.0, "", and None are False.
- Gotcha: 7 / 1 is a float because / ALWAYS produces a float.

QUESTIONS
---------
Q1. (predict) What are type(7) and type(7 / 1)?
Q2. (bug spot) Why does int(price_text) crash when
    price_text = "19.99"?
Q3. (write code) Convert "42" to a number, double it, and print the
    result together with its type.
Q4. (predict) What do bool(0), bool(""), and bool("0") return?

Run: python 01_basics/data_types.py
Answers: answers/01_basics.py
=====================================================================
"""

# ------------------------------------------------------------------
# TOPIC EXAMPLES
# ------------------------------------------------------------------

item_count = 3              # int   -> whole numbers, unlimited size
price = 4.50                # float -> decimal numbers
coupon_code = "SAVE10"      # str   -> text in quotes
gift_note = None            # None  -> "nothing here yet"

print("types:", type(item_count).__name__, type(price).__name__)
print("is price a float?:", isinstance(price, float))
print("is item_count an int?:", isinstance(item_count, int))

# Conversions - the function name matches the target type
quantity_text = "7"
quantity = int(quantity_text)     # "7" -> 7
label = str(9.5)                  # 9.5 -> "9.5"
print(f"quantity={quantity} (was {quantity_text!r}), label={label!r}")

# int() truncates toward zero; it does NOT round
slices = int(3.99)
print("int(3.99) =", slices)

# The emptiness rule for bool()
print("bool(0):", bool(0))        # False - zero is "empty"
print("bool(''):", bool(""))      # False - empty string
print("bool('0'):", bool("0"))    # True  - non-empty string!

# ------------------------------------------------------------------
# QUESTIONS - try them yourself, then check answers/01_basics.py
# ------------------------------------------------------------------
# Q1: Predict the output of:
#       print(type(7).__name__, type(7 / 1).__name__)
# Q2: Spot the bug - with price_text = "19.99", int(price_text)
#     raises an error. Which one, and what would you use instead?
# Q3: Write code: convert the string "42" to an int, double it, and
#     print the result and its type on one line.
# Q4: Predict the output of:
#       print(bool(0), bool(""), bool("0"))

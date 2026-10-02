"""
05_js_to_python / equality.py
Topic: Equality and Identity: JavaScript (== vs ===) vs Python (== vs is)

JAVASCRIPT vs PYTHON EQUALITY:
------------------------------
JavaScript:
    ==   (Loose equality: converts types implicitly, e.g. 0 == '' is true)
    ===  (Strict equality: checks value AND type without coercion)

Python:
    ==   (Value equality: checks if values are equal. Does deep equality for lists/dicts!)
    is   (Identity comparison: checks if two variables point to the EXACT same memory address)
"""

# ------------------------------------------------------------------------------
# 1. Value Equality (==)
# ------------------------------------------------------------------------------
# In JS:
#   [1, 2] === [1, 2]  // FALSE! (In JS, arrays compare by reference, not value)
#
# In Python:
#   [1, 2] == [1, 2]   // TRUE! (Python's == checks structural content!)
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print("list1 == list2 (structural value equality):", list1 == list2)  # True


# ------------------------------------------------------------------------------
# 2. Identity Comparison (is)
# ------------------------------------------------------------------------------
# `is` checks memory reference (like JS reference check `list1 === list2`):
print("list1 is list2 (same memory address?):", list1 is list2)       # False

list3 = list1
print("list1 is list3 (same memory address?):", list1 is list3)       # True


# ------------------------------------------------------------------------------
# 3. Checking for None (Best Practice!)
# ------------------------------------------------------------------------------
# In JS:
#   if (val === null || val === undefined) { ... }
#
# In Python:
#   ALWAYS use `is None` or `is not None` instead of `== None`!
#   `None` is a singleton in Python (only one instance ever exists in memory).
api_response = None

if api_response is None:
    print("Correct Python idiom: 'api_response is None'")

if api_response is not None:
    print("Will not execute")

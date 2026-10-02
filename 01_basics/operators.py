"""
01_basics / operators.py
Topic: Operators in Python vs JavaScript

KEY DIFFERENCES:
----------------
Logical Operators:
  JS:      &&     ||     !
  Python:  and    or     not

Division:
  JS:      15 / 4 === 3.75; Math.floor(15 / 4) === 3
  Python:  15 / 4 == 3.75  (regular division always returns float)
           15 // 4 == 3    (floor / integer division built-in!)

Equality:
  JS:      == (loose coercion), === (strict value & type)
  Python:  == (value equality), is (identity / reference check)
"""

# ------------------------------------------------------------------------------
# 1. Arithmetic Operators
# ------------------------------------------------------------------------------
a, b = 15, 4

print("Addition (+):", a + b)
print("Subtraction (-):", a - b)
print("Multiplication (*):", a * b)
print("Float Division (/):", a / b)         # Always returns float: 3.75
print("Floor Division (//):", a // b)       # JS: Math.floor(a / b) -> 3
print("Modulus (%):", a % b)                # Remainder: 3
print("Exponentiation (**):", a ** b)       # JS: a ** b or Math.pow(a, b) -> 50625


# ------------------------------------------------------------------------------
# 2. Logical Operators: and, or, not
# ------------------------------------------------------------------------------
# JS: const hasToken = true; const isExpired = false;
# JS: const canAccess = hasToken && !isExpired;
has_token = True
is_expired = False

can_access = has_token and not is_expired
print("Can access (and / not):", can_access)

fallback_access = False or True
print("Fallback access (or):", fallback_access)


# ------------------------------------------------------------------------------
# 3. Membership Operator: in, not in
# ------------------------------------------------------------------------------
# In JS:
#   [1, 2, 3].includes(2)
#   "name" in { name: "Alice" }
#
# In Python:
#   `in` works seamlessly across lists, tuples, sets, strings, and dictionary keys!
numbers = [1, 2, 3, 4, 5]
print("Is 3 in numbers?:", 3 in numbers)
print("Is 10 not in numbers?:", 10 not in numbers)
print("Is 'cat' in 'caterpillar'?:", "cat" in "caterpillar")


# ------------------------------------------------------------------------------
# 4. Identity Operator: is vs ==
# ------------------------------------------------------------------------------
# In Python:
#   `==` checks if the VALUES are equal (like deep equality).
#   `is` checks if both variables point to the EXACT SAME OBJECT IN MEMORY.
#
# JS Comparison:
#   const list1 = [1, 2]; const list2 = [1, 2];
#   list1 === list2  // false in JS (different references)
#   In Python:
#   list1 == list2   // TRUE in Python (values match!)
#   list1 is list2   // FALSE in Python (different memory addresses)

list_a = [1, 2, 3]
list_b = [1, 2, 3]
list_c = list_a

print("list_a == list_b (Values equal?):", list_a == list_b)  # True!
print("list_a is list_b (Same memory object?):", list_a is list_b)  # False!
print("list_a is list_c (Same memory object?):", list_a is list_c)  # True!

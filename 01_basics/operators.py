"""
=====================================================================
TOPIC: Operators
=====================================================================

SCENARIO
--------
You are wiring up the rules of your online store: totals need
arithmetic, the admin page needs permission checks, and the search
bar must know whether a tag exists. Operators are the tools for all
three jobs - and picking the wrong one quietly breaks the maths.

TOPIC
-----
- Arithmetic: + - * / // % ** where / gives a float and // gives
  a whole-number floor (rounds down).
- % is the remainder - perfect for "is it even?" (n % 2 == 0).
- Logic uses plain words: and, or, not.
- Membership: in / not in test whether a collection holds a value.
- Comparison: == != < <= > >= return True or False (and can chain:
  18 <= age <= 65).
- Gotcha: // floors toward negative infinity, so -7 // 2 is -4.

QUESTIONS
---------
Q1. (predict) What do 7 // 2 and 7 % 2 print?
Q2. (bug spot) half = 9 / 2 prints 4.5 but the cashier wants whole
    items - which operator gives 4?
Q3. (write code) With age = 20 and has_ticket = True, print one
    expression that is True only if age >= 18 AND has_ticket.
Q4. (predict) What do "py" in "python" and 3 in [1, 2] return?

Run: python 01_basics/operators.py
Answers: answers/01_basics.py
=====================================================================
"""

# ------------------------------------------------------------------
# TOPIC EXAMPLES
# ------------------------------------------------------------------

# Arithmetic in action
print("15 / 4 =", 15 / 4)      # 3.75  float division
print("15 // 4 =", 15 // 4)    # 3     floor division (rounds down)
print("15 % 4 =", 15 % 4)      # 3     remainder after dividing
print("2 ** 3 =", 2 ** 3)      # 8     power

# The remainder is the go-to "does it divide evenly?" test
cart_total = 24
print("Even total?:", cart_total % 2 == 0)

# Logical operators combine booleans in plain English words
is_admin = True
is_logged_in = False
print("Admin AND logged in:", is_admin and is_logged_in)
print("Admin OR logged in:", is_admin or is_logged_in)
print("NOT logged in:", not is_logged_in)

# Membership: does this collection hold this value?
tags = ["sale", "new"]
print("'sale' in tags:", "sale" in tags)
print("'old' not in tags:", "old" not in tags)
print("'py' in 'python':", "py" in "python")

# Comparisons chain naturally
age = 25
print("18 <= age <= 65:", 18 <= age <= 65)

# ------------------------------------------------------------------
# QUESTIONS - try them yourself, then check answers/01_basics.py
# ------------------------------------------------------------------
# Q1: Predict the output of:
#       print(7 // 2, 7 % 2)
# Q2: Spot the bug - the cashier expects whole items:
#       items = 9
#       print(items / 2)     # prints 4.5, but we wanted 4
#     Which operator prints 4?
# Q3: Write code: with age = 20 and has_ticket = True, print one
#     boolean expression that is True only when age >= 18 and
#     has_ticket are both true.
# Q4: Predict the output of:
#       print("py" in "python", 3 in [1, 2])

"""
=====================================================================
TOPIC: Conditions (if / elif / else)
=====================================================================

SCENARIO
--------
You are building the checkout page for a small online store. It must
pick the right shipping fee, badge top scorers, and label the day as
a weekend. Every one of those decisions is a condition, so getting
if / elif / else right is the backbone of the feature.

TOPIC
-----
- if / elif / else: Python runs the FIRST block whose condition is
  True, then skips the rest of the chain.
- The block is defined by indentation (4 spaces), not braces.
- Conditional expression: value_if_true if condition else value_if_false
- Chained comparison: 10 < x < 20 means 10 < x and x < 20.
- Gotcha: order matters -- put the most specific condition first.

QUESTIONS
---------
Q1. Predict the output of the Q1 code.
Q2. Spot the bug: a scorer with 95 points gets "Pass", never
    "Distinction". Why?
Q3. Write shipping_cost(total): returns 0 when total >= 50,
    otherwise 4.99. Use a conditional expression in one line.

Run: python 03_control_flow/conditions.py
Answers: answers/03_control_flow.py
=====================================================================
"""

# ------------------------------------------------------------------
# TOPIC EXAMPLES
# ------------------------------------------------------------------

# Only the first True branch runs; the rest of the chain is skipped.
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:                  # matched here...
    grade = "B"                    # ...so "else" is never checked
else:
    grade = "C"
print(f"Score {score} -> Grade {grade}")

# A conditional expression produces a value in a single line.
age = 20
status = "Adult" if age >= 18 else "Minor"
print(f"Age {age} -> {status}")

# Chained comparison reads like math; both sides must hold.
x = 15
if 10 < x < 20:
    print(f"{x} is between 10 and 20")

# Combine conditions with and / or / not.
day = "Saturday"
is_weekend = day == "Saturday" or day == "Sunday"
print("Weekend?", is_weekend)

# ------------------------------------------------------------------
# QUESTIONS - try them yourself, then check answers/03_control_flow.py
# ------------------------------------------------------------------

# Q1: What does this print?
#     temp = 25
#     label = "Hot" if temp > 20 else "Cold"
#     print(10 < temp < 30, label)

# Q2: A user with score 95 sees "Pass" instead of "Distinction".
#     Why does this happen, and how do you fix it?
#     if score >= 60:
#         grade = "Pass"
#     elif score >= 90:
#         grade = "Distinction"
#     else:
#         grade = "Fail"

# Q3: Write shipping_cost(total) using a conditional expression:
#     0 when total >= 50, otherwise 4.99.
#     Print the cost for totals of 75 and 30.

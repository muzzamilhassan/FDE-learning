"""
=====================================================================
TOPIC: Loops (for, while, range, enumerate)
=====================================================================

SCENARIO
--------
You are printing a receipt for a customer's order. You need a
countdown before the "order confirmed" screen, numbered line items,
and a queue that keeps being served until it is empty. Loops let you
write that repeating logic once and run it as often as needed.

TOPIC
-----
- for loops walk over any sequence: lists, strings, dicts, range().
- range(stop), range(start, stop), range(start, stop, step) --
  the stop value is never included.
- enumerate(items, start=1) hands you (index, item) pairs.
- while repeats while its condition stays True; if nothing inside
  the loop changes that condition, it runs forever.
- break exits the loop early; continue skips to the next round.

QUESTIONS
---------
Q1. Predict the output of the Q1 code (watch what continue skips).
Q2. Spot the bug: this countdown never ends. Why?
Q3. Write a loop that prints a numbered menu from a list of dishes,
    like "1. Pizza", using enumerate.
Q4. Predict what range(5, 0, -1) produces.

Run: python 03_control_flow/loops.py
Answers: answers/03_control_flow.py
=====================================================================
"""

# ------------------------------------------------------------------
# TOPIC EXAMPLES
# ------------------------------------------------------------------

# range(stop) counts from 0 up to (but not including) stop.
for i in range(3):
    print(i, end=" ")
print()                            # 0 1 2

# Loop straight over a list -- no index bookkeeping needed.
fruits = ["apple", "banana", "cherry"]

# enumerate gives the position and the value together.
for position, fruit in enumerate(fruits, start=1):
    print(f"{position}. {fruit}")

# A while loop must move its condition toward False, or it never ends.
queue = 3
while queue > 0:
    print(f"Serving... {queue} left")
    queue -= 1                     # without this line: infinite loop

# break stops the whole loop; continue skips only this round.
for n in range(1, 6):
    if n == 3:
        continue                   # skip 3 entirely
    if n == 5:
        break                      # stop before printing 5
    print(n, end=" ")
print()                            # 1 2 4

# ------------------------------------------------------------------
# QUESTIONS - try them yourself, then check answers/03_control_flow.py
# ------------------------------------------------------------------

# Q1: What does this print?
#     total = 0
#     for n in range(1, 5):
#         if n == 3:
#             continue
#         total += n
#     print(total)

# Q2: Spot the bug -- this countdown never stops. Why?
#     count = 3
#     while count > 0:
#         print(count)

# Q3: Given dishes = ["Pizza", "Salad", "Soup"], write a for loop
#     using enumerate that prints:
#     1. Pizza
#     2. Salad
#     3. Soup

# Q4: What numbers does range(5, 0, -1) produce, in order?

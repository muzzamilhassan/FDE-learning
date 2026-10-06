"""
=====================================================================
TOPIC: Functions
=====================================================================

SCENARIO
--------
You are building a tiny expense tracker. The same "format a receipt"
logic is copy-pasted in three places, so every bug fix means three
edits. Functions let you write the logic once, give it a name, and
reuse it everywhere.

TOPIC
-----
Define with `def name(params):`; the body is indented.
`return` hands a value back and exits the function immediately.
Returning `a, b` packs values into ONE tuple - unpack at the call site.
No return statement means the function quietly returns None.
Define a function before the line that calls it runs.

QUESTIONS
---------
Q1. Predict the output of the classify(85) call.
Q2. Spot the bug: why does "double the price" crash with TypeError?
Q3. Write min_max(numbers) that returns the smallest and largest value.
Q4. Predict the output of the stats() example.

Run: python 04_functions/functions.py
Answers: answers/04_functions.py
=====================================================================
"""

# ------------------------------------------------------------------
# TOPIC EXAMPLES
# ------------------------------------------------------------------

def greet(name: str) -> str:
    """Return a greeting for the given name."""
    return f"Hello, {name}!"


print(greet("Sam"))

# `return` exits right away, so later checks never run - no `else` needed.
def classify(score: int) -> str:
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    return "C"


print(classify(95), classify(85), classify(40))   # A B C

# Multiple return values arrive as one tuple; unpack in a single line.
def min_and_max(numbers: list[int]) -> tuple[int, int]:
    return min(numbers), max(numbers)


low, high = min_and_max([5, 2, 9, 1, 7])
print(f"low={low}, high={high}")                  # low=1, high=9

# Printing is NOT returning: this function hands back None.
def log_event(message: str) -> None:
    print(f"[LOG] {message}")


result = log_event("app started")
print(f"log_event returned: {result}")            # None

# ------------------------------------------------------------------
# QUESTIONS - try them yourself, then check answers/04_functions.py
# ------------------------------------------------------------------
# Q1: What does this print? Why only one letter?
#     def classify(score):
#         if score >= 90: return "A"
#         if score >= 80: return "B"
#         return "C"
#     print(classify(85))
#
# Q2: Spot the bug - the last line raises TypeError. Why? Fix it.
#     def double(n): print(n * 2)
#     price = double(4)
#     print(price * 10)
#
# Q3: Write min_max(numbers) that returns (smallest, largest), then
#     unpack both in one line: smallest, largest = min_max([4, 11, 7, 2])
#
# Q4: What does this print?
#     def stats(nums):
#         return sum(nums), len(nums)
#     total, count = stats([2, 4, 6])
#     print(total, count, total / count)

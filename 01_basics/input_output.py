"""
=====================================================================
TOPIC: Input and Output
=====================================================================

SCENARIO
--------
Your quiz app greets the player by name, shows the score with two
decimals, and asks a question before the first round. Everything
going out goes through print() and everything coming in comes
through input() - so these two functions shape the whole
conversation with your user.

TOPIC
-----
- print(*values) joins values with spaces; sep= and end= change
  the separator and the line ending.
- f-strings format inline: f"Total: {price:.2f}", {n:,} for
  thousands separators, {p:.1%} for percentages.
- input(prompt) ALWAYS returns a string - even if the user types 5.
- Convert immediately: age = int(input("Age: ")).
- `or "default"` turns an empty answer into a friendly fallback.
- Gotcha: input() + 1 raises TypeError - text plus number is not
  allowed; convert first.

QUESTIONS
---------
Q1. (predict) What exactly do these two lines print?
      print("a", "b", sep="-", end="!")
      print("c")
Q2. (bug spot) The user types 5, then nums + "0" prints "50" -
    why is it text, and how would you get the number 50?
Q3. (write code) Read a name and an age from input, then print
    "<name> will be <age + 1> next year." (convert the age!).

Run: python 01_basics/input_output.py
Answers: answers/01_basics.py
=====================================================================
"""

# ------------------------------------------------------------------
# TOPIC EXAMPLES
# ------------------------------------------------------------------

# print() takes several values and joins them with spaces by default
print("Hello", "World", sep=" - ")       # Hello - World
print("No newline here", end=" -> ")     # stays on the same line
print("done")

# f-strings can format values while inserting them
price = 1234.5
print(f"Total: ${price:,.2f}")           # $1,234.50
accuracy = 0.876
print(f"Accuracy: {accuracy:.1%}")       # 87.6%

# input() pauses and ALWAYS gives back a string, even for "5"
name = input("Enter your name (or press enter): ") or "Guest"
print(f"Welcome, {name}!")

# For numbers, convert right away (and remember it can fail):
#   age = int(input("Age: "))
# The `or` above swaps an empty answer for a default.

# ------------------------------------------------------------------
# QUESTIONS - try them yourself, then check answers/01_basics.py
# ------------------------------------------------------------------
# Q1: Predict the exact output of:
#       print("a", "b", sep="-", end="!")
#       print("c")
# Q2: The user types 5 at this prompt:
#       nums = input("Number: ")
#       print(nums + "0")
#     What prints, what type is nums, and how do you get 50 as a
#     number instead?
# Q3: Write code: read a name and an age from input, then print
#     "<name> will be <age + 1> next year." (convert the age!).

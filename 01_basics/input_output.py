"""
01_basics / input_output.py
Topic: Standard Input & Output

JAVASCRIPT vs PYTHON I/O:
-------------------------
JavaScript (Node.js):
    console.log("Hello", name);
    process.stdout.write("No newline");
    // Reading input in Node requires the 'readline' module or 'prompt-sync'.

Python:
    print("Hello", name)
    print("No newline", end="")
    user_input = input("Enter value: ") # Built-in synchronous CLI prompt!
"""

# ------------------------------------------------------------------------------
# 1. Output Formatting with print()
# ------------------------------------------------------------------------------
# print() takes optional keyword arguments:
# - sep: string inserted between values (default: ' ')
# - end: string appended after the last value (default: '
')

# JS: console.log("A", "B", "C") -> prints "A B C
"
print("A", "B", "C", sep=" -> ")

# Preventing newline (similar to process.stdout.write in Node):
print("Loading progress", end="... ")
print("Done!")


# ------------------------------------------------------------------------------
# 2. Number Formatting inside print()
# ------------------------------------------------------------------------------
# JS: (1234.567).toFixed(2) -> "1234.57"
price = 1234.567
discount = 0.15

print(f"Formatted price: ${price:,.2f}")  # Comma as thousand separator, 2 decimals
print(f"Discount percentage: {discount:.0%}")


# ------------------------------------------------------------------------------
# 3. Reading Input with input()
# ------------------------------------------------------------------------------
# IMPORTANT: input() ALWAYS returns a string (str), exactly like prompt() in JS!
# You must explicitly convert it using int() or float() if you need numbers.
print("\n--- Interactive Input Demo ---")
user_name = input("Enter your username (or press enter for default): ") or "guest_user"
user_age_str = input("Enter your age (or press enter for default): ") or "20"

# Convert to integer
user_age = int(user_age_str)
print(f"Hello, {user_name}! Next year you will be {user_age + 1} years old.")

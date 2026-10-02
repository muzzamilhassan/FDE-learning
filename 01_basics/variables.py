"""
01_basics / variables.py
Topic: Variables, Dynamic Typing, and Naming Conventions

JAVASCRIPT DEVELOPER MENTAL MODEL:
----------------------------------
In JavaScript:
    let age = 25;         // mutable variable
    const name = "Alice"; // block-scoped constant (cannot be reassigned)
    var oldVar = 10;      // function-scoped legacy variable (avoid)

In Python:
    - No declaration keywords (no let, const, or var).
    - You simply write `variable_name = value`.
    - Every variable in Python is a reference (label/pointer) to an object in memory.
    - Python has NO real `const` keyword at runtime! Constants are written in
      UPPER_SNAKE_CASE by convention, signaling to developers not to change them.
"""

# ------------------------------------------------------------------------------
# 1. Variable Assignment (No let / const needed)
# ------------------------------------------------------------------------------
# JS: let age = 25;
# JS: const name = "Alice";
# JS: let isActive = true;
age = 25
name = "Alice"
is_active = True        # Note capital 'T' in True (JS uses lowercase 'true')
price = 19.99

print(f"Name: {name}, Age: {age}, Active: {is_active}, Price: ${price}")


# ------------------------------------------------------------------------------
# 2. Dynamic Typing (Variables can change types freely, just like JS)
# ------------------------------------------------------------------------------
# JS: let value = 100; value = "Hello";
value = 100
print(f"Initial value: {value} (type: {type(value).__name__})")

value = "Now I am a string"
print(f"Updated value: {value} (type: {type(value).__name__})")


# ------------------------------------------------------------------------------
# 3. Multiple Assignment & Swapping
# ------------------------------------------------------------------------------
# In JS, to swap two variables without a temp variable, you use destructuring:
# JS: let a = 1, b = 2; [a, b] = [b, a];
# Python has native tuple unpacking for assignment and swapping:
x, y, z = 1, 2, 3
print(f"Assigned multiple: x={x}, y={y}, z={z}")

# Swapping values in Python is clean and elegant:
x, y = y, x
print(f"After swapping: x={x}, y={y}")


# ------------------------------------------------------------------------------
# 4. Naming Conventions (PEP 8 vs JavaScript CamelCase)
# ------------------------------------------------------------------------------
# JAVASCRIPT:
#   const userProfile = { firstName: "John" };  // camelCase for variables/functions
#   const MAX_LIMIT = 50;                       // UPPERCASE for constants
#   class UserAccount {}                        // PascalCase for classes
#
# PYTHON (PEP 8 Standard):
#   user_profile = {"first_name": "John"}       // snake_case for variables & functions
#   MAX_LIMIT = 50                              // UPPER_SNAKE_CASE for constants
#   class UserAccount:                          // PascalCase for classes

MAX_CONNECTIONS = 100   # Constant by convention (linters will warn if changed)
user_first_name = "Bob" # Standard Python snake_case

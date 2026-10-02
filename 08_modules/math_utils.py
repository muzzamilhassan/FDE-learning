"""
08_modules / math_utils.py
Topic: Modular Code & Helper Utilities

JAVASCRIPT vs PYTHON EXPORT/IMPORT:
-----------------------------------
In JavaScript (ESM):
    export function add(a, b) { return a + b; }
    export function multiply(a, b) { return a * b; }

In Python:
    EVERY function or variable defined in a file is automatically exported!
    No `export` keyword is required.
"""

def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


# ------------------------------------------------------------------------------
# WHAT IS `if __name__ == "__main__":`?
# ------------------------------------------------------------------------------
# In JS/Node, if a module is required, top-level code runs automatically.
# In Node you could check `if (require.main === module)` to see if run directly.
#
# In Python:
#   When a file is run directly: `__name__` is set to `"__main__"`.
#   When a file is imported:     `__name__` is set to the module name (`"math_utils"`).
#
# This allows you to include unit tests or CLI demos that only run when the file
# is executed standalone, but remain silent when imported!
if __name__ == "__main__":
    print("--- Running math_utils directly for testing ---")
    print("10 + 20 =", add(10, 20))

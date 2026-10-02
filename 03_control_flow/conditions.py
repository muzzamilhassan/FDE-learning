"""
03_control_flow / conditions.py
Topic: Conditional Logic (if, elif, else) and Ternary Operator

JAVASCRIPT vs PYTHON CONDITIONS:
--------------------------------
JS Syntax:
    if (score >= 90) {
        grade = "A";
    } else if (score >= 80) {
        grade = "B";
    } else {
        grade = "C";
    }

Python Syntax:
    - No parentheses required around conditions.
    - Colon `:` at the end of conditional lines.
    - Indentation defines the block (no curly braces `{}`).
    - `elif` replaces `else if`.
"""

# ------------------------------------------------------------------------------
# 1. Standard if / elif / else
# ------------------------------------------------------------------------------
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"Score: {score} -> Grade: {grade}")


# ------------------------------------------------------------------------------
# 2. Ternary Operator (Conditional Expression)
# ------------------------------------------------------------------------------
# In JS:
#   const status = age >= 18 ? "Adult" : "Minor";
#
# In Python:
#   Syntax: <val_if_true> if <condition> else <val_if_false>
age = 20
status = "Adult" if age >= 18 else "Minor"
print(f"Age {age} status: {status}")


# ------------------------------------------------------------------------------
# 3. Chained Comparisons (Python Superpower!)
# ------------------------------------------------------------------------------
# In JS, you must use logical AND:
#   if (x > 10 && x < 20) { ... }
#
# In Python, you can write mathematical chained comparisons directly:
x = 15
if 10 < x < 20:
    print("x is strictly between 10 and 20 (chained comparison: 10 < x < 20)")


# ------------------------------------------------------------------------------
# 4. Truthiness in Conditions (HUGE GOTCHA FOR JS DEVS!)
# ------------------------------------------------------------------------------
# In JS:
#   if ([]) { console.log("Empty array is TRUTHY in JS!"); }
#   if ({}) { console.log("Empty object is TRUTHY in JS!"); }
#
# In Python:
#   EMPTY COLLECTIONS ARE FALSY!
#   [] -> False
#   {} -> False
#   set() -> False
#   "" -> False
#   0 -> False
#   None -> False

items = []
if not items:
    print("Idiomatic Python: 'if not items:' detects an empty list cleanly!")

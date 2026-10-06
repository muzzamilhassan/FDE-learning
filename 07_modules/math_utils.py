"""
=====================================================================
TOPIC: Modules - Sharing Code Between Files (math_utils)
=====================================================================

SCENARIO
--------
Your study-tracker app needs math helpers in three different files.
Instead of copy-pasting `add` and `multiply` everywhere, they live
once in this file, and every other file imports them from here.

TOPIC
-----
- Any .py file is a module; its name is the file name (math_utils).
- Every top-level function here is importable by other files.
- Code under `if __name__ == "__main__":` runs only when THIS file is
  executed directly - never when it is imported. A perfect spot for
  quick self-tests.

Questions live in main.py - run: cd 07_modules && python main.py
Answers: answers/07_modules.py
=====================================================================
"""

# ------------------------------------------------------------------
# MODULE CODE (imported by main.py)
# ------------------------------------------------------------------

def add(a: float, b: float) -> float:
    return a + b


def multiply(a: float, b: float) -> float:
    return a * b


# ------------------------------------------------------------------
# SELF-TEST - runs ONLY via "python math_utils.py", never on import
# ------------------------------------------------------------------
if __name__ == "__main__":
    print("Running math_utils self-tests...")
    assert add(5, 5) == 10           # assert crashes loudly if wrong
    assert multiply(3, 4) == 12
    print("All math_utils tests passed.")

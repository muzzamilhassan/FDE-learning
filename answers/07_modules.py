"""
Answers for 07_modules - try the questions first!
"""

# ------------------------------------------------------------------
# math_utils.py (no questions - this is how its self-test works)
# ------------------------------------------------------------------
# Running `python math_utils.py` executes its `if __name__ == "__main__":`
# block (assert-based self-tests). Importing it skips that block, because
# an imported module's __name__ is "math_utils", not "__main__".

# ------------------------------------------------------------------
# user_service.py (no questions - one design note)
# ------------------------------------------------------------------
# get_users returns list(self._users), a COPY. A caller sorting or
# appending to their copy cannot corrupt the service's real list.

# ------------------------------------------------------------------
# main.py
# ------------------------------------------------------------------

# Q1: Running `python main.py` prints:
#         my __name__                 = __main__
#         imported module's __name__  = math_utils
# Why: Python sets __name__ to "__main__" only for the file you ran;
# every imported file keeps its module name. `python math_utils.py`
# therefore ALSO runs its self-test block - importing it never does.
import json                            # stdlib module, safe to import anywhere

print("--- main.py answers ---")
print("In this answers file, __name__ =", __name__)   # "__main__" when run
print("An imported module's __name__ =", json.__name__)  # "json"

# Q2: `import math_utils` binds ONLY the name math_utils - `add` lives
# inside it, so bare `add(2, 3)` is a NameError.
# Why: plain imports are namespaced on purpose; two fixes:
#   import math_utils
#   math_utils.add(2, 3)               # fix 1: go through the module
#   from math_utils import add
#   add(2, 3)                          # fix 2: import the name directly


# Q3: Add this to math_utils.py, then use it in main.py.
# Why: sum() / len() is the whole average; the import line goes at the
# top of main.py next to the other imports.
def average(numbers: list[float]) -> float:
    return sum(numbers) / len(numbers)

# In main.py you would write:
#   from math_utils import add, average
#   print(average([2, 4, 9]))          # -> 5.0

assert average([2, 4, 9]) == 5.0
print("Q3 verified: average([2, 4, 9]) =", average([2, 4, 9]))

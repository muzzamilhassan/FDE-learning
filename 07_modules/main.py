"""
=====================================================================
TOPIC: Modules & Imports
=====================================================================

SCENARIO
--------
Your little app now does math AND manages users. Instead of one huge
file, the code lives in math_utils.py and user_service.py, and
main.py glues the pieces together by importing what it needs.

TOPIC
-----
- `import math_utils` -> call things as math_utils.add(...).
- `from user_service import UserService` -> use UserService directly.
- An import runs the module's top-level code exactly ONCE, then
  caches it - later imports of the same module are instant.
- Every module has a __name__: "__main__" for the file you ran, the
  module's own name for every file you imported.
- Run this file from INSIDE its folder so Python finds its siblings:
  cd 07_modules && python main.py

QUESTIONS
---------
Q1. Predict: what are the two __name__ values printed below, and what
    would `python math_utils.py` do?
Q2. Spot the bug: after `import math_utils`, calling `add(2, 3)`
    fails. Why, and what are two fixes?
Q3. Write: add an average(numbers) function to math_utils.py, then
    import it here and print average([2, 4, 9]).

Run (from inside the folder): python main.py
Answers: answers/07_modules.py
=====================================================================
"""

# ------------------------------------------------------------------
# TOPIC EXAMPLES
# ------------------------------------------------------------------
import math_utils                      # style 1: whole module, namespaced
from user_service import UserService   # style 2: one name, used directly


def main() -> None:
    # Style 1 keeps it obvious where each function comes from.
    print("math_utils.add(10, 20)      =", math_utils.add(10, 20))
    print("math_utils.multiply(3, 4)   =", math_utils.multiply(3, 4))

    # Style 2 is shorter - but if two modules export the same name,
    # the later import silently replaces the first.
    service = UserService()
    service.add_user("Alice")
    service.add_user("Bob")
    service.add_user("Alice")           # duplicate: add_user returns False
    print("service.get_users()         =", service.get_users())

    # Q1 material: __name__ differs between the file you ran and imports.
    print("my __name__                 =", __name__)
    print("imported module's __name__  =", math_utils.__name__)


if __name__ == "__main__":
    main()

# ------------------------------------------------------------------
# QUESTIONS - try them yourself, then check answers/07_modules.py
# ------------------------------------------------------------------
# Q1: When you run `python main.py`, what two __name__ values print?
#     And what does `python math_utils.py` do that importing it does not?
#
# Q2: Spot the bug:
#     import math_utils
#     print(add(2, 3))          # NameError - why, and what are two fixes?
#
# Q3: Write an average(numbers) function in math_utils.py, then import
#     it here and print average([2, 4, 9]).  Hint: sum() and len().

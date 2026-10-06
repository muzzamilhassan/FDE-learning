"""
=====================================================================
TOPIC: Type Hints
=====================================================================

SCENARIO
--------
A new teammate joins your project and calls get_price(item_id).
Is item_id an int, a string code, or either? Type hints let you
write the answer directly in the signature: editors autocomplete
correctly, and checkers like mypy catch mistakes before the code
ever runs.

TOPIC
-----
- Annotate variables (`count: int = 0`) and functions
  (`def fee(amount: float) -> str`); `-> str` is the return type.
- `X | Y` is a union: "either type". `X | None` marks a value that
  may be missing.
- Containers take arguments too: list[str], dict[str, int],
  tuple[int, int].
- Hints are NOT enforced at runtime -- Python ignores them while
  executing. They pay off in editors, docs, and static checkers.
- Hinted parameters still work like normal parameters: defaults,
  keyword arguments, everything unchanged.

QUESTIONS
---------
Q1. Predict the output of the snippet in the questions section.
Q2. Concept check: `def split_total(amount, people) -> float:` has a
    return hint but bare parameters. Why is that half-useful, and
    what should the full signature be?
Q3. Write `average(numbers: list[float]) -> float` returning 0.0 for
    an empty list, else the mean. Test on [] and [2, 4, 6].

Run: python 11_typing/type_hints.py
Answers: answers/11_typing.py
=====================================================================
"""

# ------------------------------------------------------------------
# TOPIC EXAMPLES
# ------------------------------------------------------------------

def format_id(user_id: int | str) -> str:
    # Union hint: the caller may pass either an int or a str.
    return f"ID-{user_id}"


def find_email(directory: dict[str, str], name: str) -> str | None:
    # dict[str, str]: keys are str, values are str.
    # str | None: the name might be missing -- say so up front.
    return directory.get(name)


def scale(values: list[float], factor: float) -> list[float]:
    return [v * factor for v in values]


print(format_id(101))                          # ID-101
print(format_id("admin"))                      # ID-admin
print(find_email({"ana": "a@x.com"}, "ana"))   # a@x.com
print(find_email({}, "bob"))                   # None
print(scale([1.0, 2.5], 2.0))                  # [2.0, 5.0]

# Hints do not gatekeep at runtime -- Python happily assigns this:
age: int = "not a number"
print("age was assigned anyway:", age)


# ------------------------------------------------------------------
# QUESTIONS - try them yourself, then check answers/11_typing.py
# ------------------------------------------------------------------
# Q1: What does this print, and why?
#     def repeat(text: str, times: int = 2) -> str:
#         return text * times
#     print(repeat("ha"))
#     print(repeat(3, 3))
# Q2: A teammate wrote `def split_total(amount, people) -> float:`.
#     Why is a return hint alone not enough, and what does the full
#     signature look like?
# Q3: Write average(numbers: list[float]) -> float that returns 0.0
#     for an empty list, otherwise the mean. Test it on [] and [2,4,6].

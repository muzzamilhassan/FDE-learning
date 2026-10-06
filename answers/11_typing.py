"""
Answers for 11_typing - try the questions first!
"""

from dataclasses import dataclass


# ------------------------------------------------------------------
# type_hints.py
# ------------------------------------------------------------------

# Q1: Prints `haha` then `9`. Hints are NOT enforced at runtime:
#     repeat(3, 3) passes an int where str was declared, and 3 * 3
#     evaluates to 9 without complaint. Only a static checker (mypy)
#     flags it -- which is exactly why you run one.

# Q2: A return hint with bare parameters tells readers what comes out
#     but not what must go in, so it cannot catch wrong arguments.
#     Full signature:
#     def split_total(amount: float, people: int) -> float:

# Q3: Working solution:

def average(numbers: list[float]) -> float:
    if not numbers:
        return 0.0  # guard against ZeroDivisionError on []
    return sum(numbers) / len(numbers)


# ------------------------------------------------------------------
# dataclasses.py
# ------------------------------------------------------------------

# Q1: Prints `Point(x=2, y=0)` then `True`. y defaults to 0, so
#     Point(2) fills it in automatically, and dataclass == compares
#     field values -- both points hold x=2, y=0.

# Q2: A bare `= []` would share ONE list across every Cart instance,
#     so dataclasses refuse it with:
#     ValueError: mutable default <class 'list'> for field items is
#     not allowed. Fix: items: list[str] = field(default_factory=list)

# Q3: Working solution:

@dataclass
class Book:
    title: str
    author: str
    pages: int
    shelf: str = "to-read"


def dataclass_demo() -> None:
    b1 = Book("Fluent Python", "Luciano Ramalho", 790)
    b2 = Book("Fluent Python", "Luciano Ramalho", 790)
    print(b1)         # Book(title='Fluent Python', author='Luciano ...')
    print(b1 == b2)   # True


if __name__ == "__main__":
    print("average of []     ->", average([]))
    print("average of [2,4,6]->", average([2, 4, 6]))
    dataclass_demo()

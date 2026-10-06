"""
=====================================================================
TOPIC: Dataclasses
=====================================================================

SCENARIO
--------
Your shop app stores customer records: id, name, tier, and a tag
list. Hand-writing __init__, a readable __repr__, and value equality
for every record type is repetitive and easy to get subtly wrong.
The @dataclass decorator generates all of that boilerplate from a
simple field list.

TOPIC
-----
- Put @dataclass on a class whose fields are declared as type-hinted
  attributes; you get __init__, __repr__, and __eq__ for free.
- repr shows every field: Customer(id=1, name='Ana') -- great for
  logging and debugging.
- == compares field VALUES, not object identity.
- Fields with defaults must come AFTER fields without them.
- Mutable defaults (list, dict, set) need default_factory=list; a
  bare `= []` default is refused with a ValueError, because one
  shared list would leak between instances.
- Gotcha: never name a file after a standard library module. This
  file is called dataclasses.py, so running it directly would shadow
  the real stdlib dataclasses -- that is why we run it with -m.

QUESTIONS
---------
Q1. Predict the output of the Point snippet in the questions section.
Q2. Spot the bug: `@dataclass class Cart: items: list[str] = []`.
    What error does Python raise, and what is the fix?
Q3. Write a Book dataclass (title, author, pages, shelf="to-read"),
    create two identical books, print one, and whether they are ==.

Run: python -m 11_typing.dataclasses   (from the repo root)
Answers: answers/11_typing.py
=====================================================================
"""

from dataclasses import dataclass, field


# ------------------------------------------------------------------
# TOPIC EXAMPLES
# ------------------------------------------------------------------

@dataclass
class Customer:
    id: int
    name: str
    tier: str = "free"
    # default_factory builds a FRESH list for every new instance.
    tags: list[str] = field(default_factory=list)


c1 = Customer(1, "Ana")
c2 = Customer(1, "Ana")

print(c1)                 # Customer(id=1, name='Ana', tier='free', tags=[])
print(c1 == c2)           # True -- compared by field values

c1.tags.append("early")   # only c1's list grows...
print(c2.tags)            # [] -- c2 owns a separate list


# ------------------------------------------------------------------
# QUESTIONS - try them yourself, then check answers/11_typing.py
# ------------------------------------------------------------------
# Q1: What does this print?
#     @dataclass
#     class Point:
#         x: int
#         y: int = 0
#     p = Point(2)
#     q = Point(2, 0)
#     print(p)
#     print(p == q)
# Q2: Spot the bug: `@dataclass class Cart: items: list[str] = []`.
#     What error does Python raise, and what is the correct fix?
# Q3: Write a Book dataclass with title, author, pages, and a shelf
#     default of "to-read". Make two identical books, print one, and
#     print whether they are equal.

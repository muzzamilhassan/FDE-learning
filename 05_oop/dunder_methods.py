"""
=====================================================================
TOPIC: Dunder Methods
=====================================================================

SCENARIO
--------
You are adding books to the shop's search results. You want each
book to print nicely, to compare equal when title and price match,
and to let a checkout page total two books with a plain + sign.
Dunder methods are the hooks that make all of that work.

TOPIC
-----
"Dunder" = double-underscore methods that Python calls FOR you.
__str__: what print(obj) shows - friendly, for users.
__repr__: what the console and lists show - precise, for developers.
__eq__: controls obj == other, so "same data" can mean equal.
__add__ and __len__ hook into the + operator and len().
Gotcha: without __eq__, == asks "same object in memory?" so two
identical-looking instances are never equal.

QUESTIONS
---------
Q1. Predict the output (== without __eq__).
Q2. Concept check: __str__ vs __repr__ - which one ran?
Q3. Write code: add __len__ so len(book) returns pages.
Q4. Spot the bug: why does book == 42 crash?

Run: python 05_oop/dunder_methods.py
Answers: answers/05_oop.py
=====================================================================
"""

# ------------------------------------------------------------------
# TOPIC EXAMPLES
# ------------------------------------------------------------------

class Book:
    def __init__(self, title: str, price: float, pages: int):
        self.title = title
        self.price = price
        self.pages = pages

    def __str__(self):
        # print() and str() call this - keep it friendly
        return f"{self.title} (${self.price})"

    def __repr__(self):
        # the console and containers call this - keep it precise
        return f"Book({self.title!r}, {self.price}, {self.pages})"

    def __eq__(self, other):
        # runs for == : same title AND price counts as the same book
        return self.title == other.title and self.price == other.price

    def __add__(self, other):
        # runs for + : the total price of a two-book bundle
        return self.price + other.price


b1 = Book("Dune", 14.99, 412)
b2 = Book("Dune", 14.99, 500)    # different pages, but still "equal" below
b3 = Book("Hex", 9.99, 300)

print(b1)         # Dune ($14.99)             -> __str__
print(repr(b1))   # Book('Dune', 14.99, 412)  -> __repr__
print(b1 == b2)   # True                      -> __eq__ (pages ignored)
print(b1 + b3)    # 24.98                     -> __add__
print([b1, b3])   # lists print each item with __repr__

# ------------------------------------------------------------------
# QUESTIONS - try them yourself, then check answers/05_oop.py
# ------------------------------------------------------------------
# Q1: Predict the output, and explain why:
#     class Item:
#         def __init__(self, name):
#             self.name = name
#     print(Item("pen") == Item("pen"))
#
# Q2: Concept check - print(book) shows "Dune ($14.99)" but
#     print([book]) shows Book('Dune', 14.99, 412). Which dunder
#     did each print use, and who is each one for?
#
# Q3: Add a __len__ method to Book so len(book) returns the page
#     count. Then print(len(b1)).
#
# Q4: Spot the bug - why does b1 == 42 crash, and how do you make
#     comparisons with non-books safely return False?

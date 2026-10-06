"""
=====================================================================
TOPIC: Properties (@property)
=====================================================================

SCENARIO
--------
Your shop is live and users type anything into the price box,
including negative numbers. You want validation on EVERY price
change, without clunky setter method calls - @property gives you both.

TOPIC
-----
@property makes a method readable like an attribute; @price.setter
runs whenever you ASSIGN: item.price = 5.
Store the real value in self._price - the underscore means "internal".
Gotcha: no setter means read-only - assignment raises AttributeError.
Gotcha: storing in self.price (no underscore) = getter calls itself.

QUESTIONS
---------
Q1. Predict the output (the setter runs even inside __init__).
Q2. Spot the bug (a property with no setter).
Q3. Write code: a validated quantity property.

Run: python 05_oop/properties.py
Answers: answers/05_oop.py
=====================================================================
"""

# ------------------------------------------------------------------
# TOPIC EXAMPLES
# ------------------------------------------------------------------

class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price     # assignment -> the setter runs right here

    @property
    def price(self) -> float:
        return self._price   # getter: runs when you READ item.price

    @price.setter
    def price(self, value: float):
        # setter: runs when you ASSIGN item.price = value
        if value < 0:
            raise ValueError("price cannot be negative")
        self._price = value

item = Product("Laptop", 999.99)
print(item.price)       # 999.99 - looks like data, actually calls the getter

item.price = 899.99     # looks like plain assignment, actually the setter
print(item.price)

try:
    item.price = -5     # invalid: the setter rejects it
except ValueError as e:
    print("Rejected:", e)

# ------------------------------------------------------------------
# QUESTIONS - try them yourself, then check answers/05_oop.py
# ------------------------------------------------------------------
# Q1: Predict the output:
#     class Gauge:
#         def __init__(self):
#             self.level = 0
#         @property
#         def level(self):
#             return self._level
#         @level.setter
#         def level(self, v):
#             print("setting", v)
#             self._level = v
#     g = Gauge()
#     g.level = 25
#     print(g.level)
#
# Q2: Spot the bug - which line crashes, and why?
#     class Deal:
#         def __init__(self):
#             self.price = 10
#         @property
#         def price(self):
#             return self._price
#     d = Deal()
#
# Q3: Write a Stock class with a validated quantity property that
#     rejects negative values. Set it to 5, then try -1 and handle it.

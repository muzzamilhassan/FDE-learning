"""
=====================================================================
TOPIC: Classes and Objects
=====================================================================

SCENARIO
--------
You are building a tiny online shop. Every product has a name and a
price, and every product should be able to describe itself and apply
a discount. A class bundles that data and behavior into one reusable
blueprint, so growing the catalog stays easy.

TOPIC
-----
A class is a blueprint; an object (instance) is one thing built from it.
__init__ runs automatically when you create an instance.
self is the current instance - it is the first parameter of every method.
self.name = ... stores data on that one instance (an attribute).
Gotcha: forget self in a method's parameters and every call
raises TypeError.

QUESTIONS
---------
Q1. Predict the output (two instances with separate data).
Q2. Spot the bug (a method that forgot self).
Q3. Write code: build a Customer class with a greet method.
Q4. Bonus: add a restock method that updates quantity.

Run: python 05_oop/classes.py
Answers: answers/05_oop.py
=====================================================================
"""

# ------------------------------------------------------------------
# TOPIC EXAMPLES
# ------------------------------------------------------------------

class Product:
    def __init__(self, name: str, price: float):
        self.name = name      # attribute: data stored on THIS instance
        self.price = price

    def describe(self):
        # self is how a method reads the instance's own data
        return f"{self.name} costs ${self.price}"

    def apply_discount(self, percent: int) -> float:
        # methods can also CHANGE the instance's data
        self.price = round(self.price * (1 - percent / 100), 2)
        return self.price


pen = Product("Pen", 2.0)      # creating an instance = calling the class
notebook = Product("Notebook", 5.0)

print(pen.describe())          # Pen costs $2.0
print(notebook.describe())     # Notebook costs $5.0

pen.apply_discount(50)
print(pen.describe())          # Pen costs $1.0 - only pen changed
print(notebook.describe())     # Notebook costs $5.0 - untouched

# Each instance keeps its OWN attributes:
pen.price = 999.0
print(pen.price, notebook.price)   # 999.0 5.0

# ------------------------------------------------------------------
# QUESTIONS - try them yourself, then check answers/05_oop.py
# ------------------------------------------------------------------
# Q1: Predict the output (both were built with price 2.0):
#     a = Product("Pen", 2.0)
#     b = Product("Pen", 2.0)
#     a.price = 4.0
#     print(a.name, a.price, "|", b.name, b.price)
#
# Q2: Spot the bug - why does cart.show() crash, and what is the fix?
#     class Cart:
#         def __init__(self):
#             self.items = []
#         def show():
#             return f"{len(self.items)} items"
#
# Q3: Write a Customer class with name and email attributes and a
#     greet() method that returns "Welcome back, <name>!".
#     Create one customer and print greet().
#
# Q4 (bonus): A StockItem has name and quantity attributes. Add a
#     restock(self, amount) method that increases quantity by amount.

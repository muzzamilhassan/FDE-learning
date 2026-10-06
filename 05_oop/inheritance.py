"""
=====================================================================
TOPIC: Inheritance
=====================================================================

SCENARIO
--------
Your shop sells many kinds of products. A book is a product, but it
also has an author and a page count. Instead of copying the Product
code into a new class, inheritance lets Book reuse everything from
Product and only add or change what makes books different.

TOPIC
-----
class Child(Parent) makes Child inherit every method from Parent.
Child.__init__ calls super().__init__(...) so the parent's setup runs.
Overriding = redefining a method in the child; the child's version wins.
super().method() lets a child REUSE the parent's version in an override.
Gotcha: __init__ without super().__init__ skips the parent's setup.
isinstance(obj, Parent) tells you what an object is built from.

QUESTIONS
---------
Q1. Predict the output (which describe() runs?).
Q2. Spot the bug (a child that never calls super().__init__).
Q3. Write code: an eBook subclass with a file size.
Q4. Concept check: what does isinstance() return?

Run: python 05_oop/inheritance.py
Answers: answers/05_oop.py
=====================================================================
"""

# ------------------------------------------------------------------
# TOPIC EXAMPLES
# ------------------------------------------------------------------

class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def describe(self):
        return f"{self.name} costs ${self.price}"

class Book(Product):                     # Book inherits from Product
    def __init__(self, name: str, price: float, author: str, pages: int):
        super().__init__(name, price)    # Product sets up name and price
        self.author = author             # Book-only extras
        self.pages = pages

    def describe(self):                  # override: this version wins
        base = super().describe()        # ...but we still reuse the parent
        return f"{base}, by {self.author} ({self.pages} pages)"


item = Product("Pencil", 1.5)
book = Book("Dune", 14.99, "Frank Herbert", 412)

print(item.describe())             # Pencil costs $1.5
print(book.describe())             # Dune costs $14.99, by Frank Herbert ...
print(isinstance(book, Product))   # True - a Book IS a Product
print(isinstance(item, Book))      # False - not every Product is a Book

# ------------------------------------------------------------------
# QUESTIONS - try them yourself, then check answers/05_oop.py
# ------------------------------------------------------------------
# Q1: Predict the output:
#     class Product:
#         def describe(self):
#             return "generic product"
#     class Book(Product):
#         def describe(self):
#             return "a book"
#     print(Book().describe())
#
# Q2: Spot the bug - why does print(b.price) crash?
#     class Product:
#         def __init__(self, price):
#             self.price = price
#     class Book(Product):
#         def __init__(self, title):
#             self.title = title
#     b = Book("Dune")
#
# Q3: Write an eBook class that inherits from Book and adds a
#     file_size_mb attribute. Give it a describe() that includes it.
#
# Q4: True or False, and why: isinstance(book, Product) and
#     isinstance(item, Book)? (book and item are from the examples)

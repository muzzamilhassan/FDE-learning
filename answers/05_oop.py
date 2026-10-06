"""
Answers for 05_oop - try the questions first!

Each answer is a one-line why plus working code you can run.
Run: python answers/05_oop.py
"""

# ------------------------------------------------------------------
# classes.py
# ------------------------------------------------------------------

# Q1: Output: Pen 4.0 | Pen 2.0
# Why: each instance has its OWN attributes - changing a.price never
# touches b, even though both were built from the same blueprint.
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


a = Product("Pen", 2.0)
b = Product("Pen", 2.0)
a.price = 4.0
print(a.name, a.price, "|", b.name, b.price)   # Pen 4.0 | Pen 2.0


# Q2: Bug - show() forgot self, so Python passes cart and finds no
# parameter to put it in -> TypeError.
# Why: every instance method needs self as its first parameter.
class Cart:
    def __init__(self):
        self.items = []

    def show(self):                    # <-- adding self is the fix
        return f"{len(self.items)} items"


cart = Cart()
print(cart.show())                     # 0 items


# Q3: Customer with name/email plus a greet method.
class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def greet(self):
        return f"Welcome back, {self.name}!"


alice = Customer("Alice", "alice@example.com")
print(alice.greet())                   # Welcome back, Alice!


# Q4: restock updates quantity through self, so the instance stays
# the single source of truth.
class StockItem:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def restock(self, amount):
        self.quantity += amount
        return self.quantity


book_stock = StockItem("Dune", 3)
print(book_stock.restock(10))          # 13


# ------------------------------------------------------------------
# inheritance.py
# ------------------------------------------------------------------

# Q1: Output: a book
# Why: the child's override wins - Book.describe replaces
# Product.describe when you call it on a Book.
class Describable:
    def describe(self):
        return "generic product"


class SimpleBook(Describable):
    def describe(self):
        return "a book"


print(SimpleBook().describe())         # a book


# Q2: Bug - Book.__init__ never calls super().__init__, so Product's
# setup never runs and self.price never exists -> AttributeError.
# Why: defining __init__ in the child REPLACES the parent's __init__.
class Priced:
    def __init__(self, price):
        self.price = price


class FixedBook(Priced):
    def __init__(self, title, price):
        super().__init__(price)        # <-- the fix
        self.title = title


b = FixedBook("Dune", 14.99)
print(b.title, b.price)                # Dune 14.99


# Q3: eBook adds file_size_mb and builds on describe() via super().
class BookBase:
    def __init__(self, name, price, author, pages):
        self.name = name
        self.price = price
        self.author = author
        self.pages = pages

    def describe(self):
        return f"{self.name} by {self.author}"


class eBook(BookBase):
    def __init__(self, name, price, author, pages, file_size_mb):
        super().__init__(name, price, author, pages)
        self.file_size_mb = file_size_mb

    def describe(self):
        return f"{super().describe()} (eBook, {self.file_size_mb} MB)"


dune = eBook("Dune", 9.99, "Frank Herbert", 412, 2.4)
print(dune.describe())                 # Dune by Frank Herbert (eBook, 2.4 MB)


# Q4: isinstance(book, Product) -> True, isinstance(item, Book) -> False.
# Why: every Book IS a Product (it inherited from it), but a plain
# Product is not a Book.
print(isinstance(FixedBook("Dune", 14.99), Priced))    # True
print(isinstance(Priced(1.5), FixedBook))              # False


# ------------------------------------------------------------------
# properties.py
# ------------------------------------------------------------------

# Q1: Output:
# setting 0
# setting 25
# 25
# Why: self.level = 0 inside __init__ is an assignment too, so the
# setter runs there first - properties are active from construction.
class Gauge:
    def __init__(self):
        self.level = 0                 # prints: setting 0

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, v):
        print("setting", v)
        self._level = v


g = Gauge()
g.level = 25                           # prints: setting 25
print(g.level)                         # 25


# Q2: It crashes inside __init__ at self.price = 10.
# Why: a property with no @price.setter is read-only, so even the
# assignment in __init__ raises AttributeError. Fix: add a setter
# (or store to self._price in __init__ and expose a read-only view).
class Deal:
    def __init__(self):
        self._price = 10               # store internally instead

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):            # adding the setter fixes assignment
        self._price = value


d = Deal()
d.price = 20
print(d.price)                         # 20


# Q3: quantity rejects negatives in its setter - validation lives in
# one place and every assignment is checked.
class Stock:
    def __init__(self):
        self.quantity = 0

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value < 0:
            raise ValueError("quantity cannot be negative")
        self._quantity = value


apples = Stock()
apples.quantity = 5
print(apples.quantity)                 # 5
try:
    apples.quantity = -1
except ValueError as e:
    print("Rejected:", e)              # Rejected: quantity cannot be negative


# ------------------------------------------------------------------
# dunder_methods.py
# ------------------------------------------------------------------

# Q1: Output: False
# Why: without __eq__, == checks whether both names point to the SAME
# object in memory - two separate instances are never that object.
class Item:
    def __init__(self, name):
        self.name = name


print(Item("pen") == Item("pen"))      # False


# Q2: print(book) uses __str__ (friendly, for users); print([book])
# uses __repr__ for each element (precise, for developers).
# Why: containers always show repr so debugging stays unambiguous.
class Book:
    def __init__(self, title, price, pages):
        self.title = title
        self.price = price
        self.pages = pages

    def __str__(self):
        return f"{self.title} (${self.price})"

    def __repr__(self):
        return f"Book({self.title!r}, {self.price}, {self.pages})"


book = Book("Dune", 14.99, 412)
print(book)                            # Dune ($14.99)
print([book])                          # [Book('Dune', 14.99, 412)]


# Q3: __len__ hooks into len(), so a book can report its page count
# like any other size.
class BookWithLen(Book):
    def __len__(self):
        return self.pages


print(len(BookWithLen("Dune", 14.99, 412)))    # 412


# Q4: b1 == 42 crashes because __eq__ reads other.title, and an int
# has no title attribute -> AttributeError.
# Why/fix: guard with isinstance and return NotImplemented so Python
# falls back to a safe default instead of exploding.
class SafeBook(Book):
    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.title == other.title and self.price == other.price


print(SafeBook("Dune", 14.99, 412) == SafeBook("Dune", 14.99, 412))  # True
print(SafeBook("Dune", 14.99, 412) == 42)                            # False
print(SafeBook("Dune", 14.99, 412) == "Dune")                        # False

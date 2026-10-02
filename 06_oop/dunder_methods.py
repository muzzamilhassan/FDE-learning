# In JS: obj.toString() or [Symbol.toPrimitive]
# In Python: "Dunder" (double underscore) methods let your class work with
# built-in features like print(), len(), and operators (+, ==).

class Book:
    def __init__(self, title: str, pages: int):
        self.title = title
        self.pages = pages

    # In JS: toString() -> user-friendly string
    def __str__(self):
        return f"'{self.title}' ({self.pages} pages)"

    # In JS: Array length -> Python: len(book)
    def __len__(self):
        return self.pages

    # In JS: book1 === book2 (Python: book1 == book2)
    def __eq__(self, other):
        return self.title == other.title and self.pages == other.pages

b1 = Book("Python Crash Course", 350)
b2 = Book("Python Crash Course", 350)

print(b1)            # Calls __str__: 'Python Crash Course' (350 pages)
print(len(b1))       # Calls __len__: 350
print(b1 == b2)      # Calls __eq__: True

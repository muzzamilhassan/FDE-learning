"""
06_oop / dunder_methods.py
Topic: Dunder (Magic) Methods & Operator Overloading

================================================================================
WHAT ARE DUNDER METHODS?
================================================================================
"Dunder" stands for Double UNDERscore: `__name__`.
They are also called "Magic Methods" or "Special Methods".

JAVASCRIPT COMPARISON:
----------------------
In JavaScript:
    - Custom string representation: `obj.toString()`
    - Custom JSON representation: `obj.toJSON()`
    - Iteration: `obj[Symbol.iterator]()`
    - BUT JavaScript DOES NOT allow operator overloading!
      If you do `obj1 + obj2` in JS, it returns `"[object Object][object Object]"`.

In Python:
    Dunder methods allow YOUR custom classes to integrate seamlessly with
    Python's built-in syntax (+, -, ==, len(), str(), repr(), indexing [])!

ESSENTIAL DUNDER METHODS:
-------------------------
Dunder Method        Triggered by                Purpose
---------------------------------------------------------------------------------
__init__(self)       MyClass(...)                Constructor
__str__(self)        str(obj), print(obj)        Human-friendly display (JS: toString)
__repr__(self)       repr(obj), REPL debug       Developer-friendly debug string
__len__(self)        len(obj)                    Return length of custom collection
__eq__(self, other)  obj1 == obj2                Custom equality comparison
__add__(self, other) obj1 + obj2                 Operator overloading: addition (+)
__getitem__(self, i) obj[i]                      Square bracket indexing (JS: obj[i])
__contains__(self,x) x in obj                    Membership check (in)
"""

class CartItem:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    # __repr__: Unambiguous developer representation (useful for logging & debugging)
    def __repr__(self) -> str:
        return f"CartItem(name='{self.name}', price={self.price})"

    # __str__: User-facing string representation
    def __str__(self) -> str:
        return f"{self.name} (${self.price:.2f})"

    # __eq__: Defines how `item1 == item2` behaves
    def __eq__(self, other) -> bool:
        if not isinstance(other, CartItem):
            return False
        return self.name == other.name and self.price == other.price


class ShoppingCart:
    def __init__(self):
        self._items: list[CartItem] = []

    def add_item(self, item: CartItem):
        self._items.append(item)

    # 1. __len__: Enables `len(cart)`
    def __len__(self) -> int:
        return len(self._items)

    # 2. __getitem__: Enables indexing `cart[0]` and looping `for item in cart:`
    def __getitem__(self, index: int) -> CartItem:
        return self._items[index]

    # 3. __contains__: Enables `item in cart`
    def __contains__(self, item: CartItem) -> bool:
        return item in self._items

    # 4. __add__: Enables merging two carts with `+`: `cart1 + cart2`
    def __add__(self, other: "ShoppingCart") -> "ShoppingCart":
        new_cart = ShoppingCart()
        new_cart._items = self._items + other._items
        return new_cart

    # 5. __str__: Human-readable summary
    def __str__(self) -> str:
        total = sum(item.price for item in self._items)
        return f"ShoppingCart({len(self)} items, Total: ${total:.2f})"


# ==============================================================================
# DEMONSTRATION OF MAGIC IN ACTION
# ==============================================================================
item1 = CartItem("Noise Cancelling Headphones", 199.99)
item2 = CartItem("USB-C Cable", 15.00)
item3 = CartItem("Wireless Mouse", 45.00)

print("str(item1):", str(item1))
print("repr(item1):", repr(item1))

# Testing __eq__:
duplicate_item = CartItem("USB-C Cable", 15.00)
print("item2 == duplicate_item:", item2 == duplicate_item)  # True due to __eq__!

# Creating carts:
cart_a = ShoppingCart()
cart_a.add_item(item1)
cart_a.add_item(item2)

cart_b = ShoppingCart()
cart_b.add_item(item3)

# 1. len() magic:
print(f"Items in Cart A: {len(cart_a)}")

# 2. Indexing [] magic:
print(f"First item in Cart A: {cart_a[0]}")

# 3. Membership `in` magic:
print(f"Is headphones in Cart A?: {item1 in cart_a}")

# 4. Operator overloading `+` magic (Merging two shopping carts):
combined_cart = cart_a + cart_b
print(f"Combined cart (+ operator): {combined_cart}")
print(f"Total items in combined cart: {len(combined_cart)}")

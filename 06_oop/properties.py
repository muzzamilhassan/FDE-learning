"""
06_oop / properties.py
Topic: Encapsulation, Private Attributes, and the @property Decorator

================================================================================
OOP ENCAPSULATION EXPLAINED FOR JAVASCRIPT DEVELOPERS:
================================================================================
Why Encapsulation?
- To protect object state from invalid data.
  For example, price should never be negative, temperature should not violate physics.

JAVASCRIPT GETTERS/SETTERS & PRIVATE FIELDS:
--------------------------------------------
JavaScript (ES2022+):
    class Product {
        #price; // '#' marks a private field (cannot be accessed outside class)
        
        constructor(price) {
            this.price = price; // calls setter
        }
        get price() {
            return this.#price;
        }
        set price(value) {
            if (value < 0) throw new Error("Price cannot be negative");
            this.#price = value;
        }
    }

PYTHON @property GETTERS & SETTERS:
-----------------------------------
In Python:
    1. `_name` (Single underscore): By CONVENTION, indicates "internal / protected".
       Linters warn not to touch it directly, but Python won't strictly block it.
    2. `__name` (Double underscore): Triggers "name mangling" (renamed to `_ClassName__name`)
       to avoid accidental overwrites in subclasses.
    3. `@property`: Defines a GETTER method that can be accessed like an attribute!
    4. `@<name>.setter`: Defines a SETTER method with validation.

THE PYTHON PHILOSOPHY:
In Java or older languages, you wrote `product.getPrice()` and `product.setPrice(10)`.
In Python, start with public attributes `product.price`.
If you later need validation, convert it to a `@property` WITHOUT breaking existing code!
"""

class Product:
    def __init__(self, name: str, price: float, stock: int):
        self.name = name
        # Using the property setters to validate on initialization:
        self.price = price      # Calls @price.setter below!
        self.stock = stock      # Calls @stock.setter below!

    # --------------------------------------------------------------------------
    # Property: price (Getter)
    # --------------------------------------------------------------------------
    # JS: get price() { return this.#price; }
    @property
    def price(self) -> float:
        """The price property getter."""
        return self._price

    # --------------------------------------------------------------------------
    # Property: price (Setter with Validation)
    # --------------------------------------------------------------------------
    # JS: set price(value) { ... }
    @price.setter
    def price(self, value: float):
        if not isinstance(value, (int, float)):
            raise TypeError("Price must be a number!")
        if value < 0:
            raise ValueError("Price cannot be negative!")
        self._price = float(value)

    # --------------------------------------------------------------------------
    # Property: stock (Getter and Setter)
    # --------------------------------------------------------------------------
    @property
    def stock(self) -> int:
        return self._stock

    @stock.setter
    def stock(self, count: int):
        if not isinstance(count, int) or count < 0:
            raise ValueError("Stock must be a non-negative integer!")
        self._stock = count

    # --------------------------------------------------------------------------
    # Computed Read-Only Property (No setter defined)
    # --------------------------------------------------------------------------
    # JS: get totalValue() { return this.price * this.stock; }
    @property
    def total_inventory_value(self) -> float:
        """Read-only property: calculated dynamically on access."""
        return self.price * self.stock


# ==============================================================================
# DEMONSTRATION & PRACTICE
# ==============================================================================
item = Product("Ergonomic Keyboard", price=129.99, stock=50)

# Accessed like a regular attribute (NO parenthesis `()` needed!):
print(f"Product: {item.name}")
print(f"Price: ${item.price}")
print(f"Total Inventory Value: ${item.total_inventory_value:,.2f}")

# Updating via setter:
item.price = 109.99
print(f"Discounted Price: ${item.price}")

# Validation in action:
print("\nTesting validation errors:")
try:
    item.price = -25.0  # Will trigger ValueError!
except ValueError as e:
    print(f"Caught expected error: {e}")

try:
    item.stock = -5     # Will trigger ValueError!
except ValueError as e:
    print(f"Caught expected error: {e}")

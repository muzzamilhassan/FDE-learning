# In JS: get price() { return this._price; }
# In JS: set price(val) { if (val < 0) throw Error(); this._price = val; }
# In Python: @property lets you use getter and setter methods like normal attributes!

class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price  # This triggers the setter below!

    @property
    def price(self) -> float:
        return self._price  # '_price' is the internal protected variable

    @price.setter
    def price(self, value: float):
        if value < 0:
            raise ValueError("Price cannot be negative!")
        self._price = value

# Usage
item = Product("Laptop", 999.99)
print(f"Product: {item.name}, Price: ${item.price}")

item.price = 899.99  # Calls setter
print(f"Discounted Price: ${item.price}")

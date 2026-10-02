# In JS: class User { constructor(name, age) { this.name = name; this.age = age; } }
# In Python: 'self' refers to the current instance (like 'this' in JS).
# You must write 'self' as the first parameter of every instance method.

class User:
    def __init__(self, name: str, age: int):
        self.name = name       # Instance attribute
        self.age = age

    # In JS: greet() { return `Hi, I am ${this.name}`; }
    def greet(self):
        return f"Hi, I am {self.name} and I am {self.age} years old."

# In JS: const user1 = new User("Alice", 25); (Python does NOT use 'new')
user1 = User("Alice", 25)
user2 = User("Bob", 30)

print(user1.greet())
print(user2.greet())

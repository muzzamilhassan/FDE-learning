# In JS: class Animal { constructor(name) { this.name = name; } }
class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

# In JS: class Dog extends Animal { constructor(name, breed) { super(name); this.breed = breed; } }
class Dog(Animal):
    def __init__(self, name: str, breed: str):
        super().__init__(name)  # Call parent constructor
        self.breed = breed

    # Overriding parent method (In JS: speak() { ... })
    def speak(self):
        return f"{self.name} ({self.breed}) barks: Woof!"

# Usage
generic_animal = Animal("Creature")
my_dog = Dog("Buddy", "Golden Retriever")

print(generic_animal.speak())
print(my_dog.speak())

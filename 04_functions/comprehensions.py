# List Comprehensions replace .map() and .filter() in Python
numbers = [1, 2, 3, 4, 5, 6]

# In JS: numbers.filter(x => x % 2 === 0)
evens = [x for x in numbers if x % 2 == 0]
print("Filtered evens:", evens)

# In JS: numbers.map(x => x * 10)
tens = [x * 10 for x in numbers]
print("Mapped tens:", tens)

# In JS: numbers.filter(x => x % 2 === 0).map(x => x * 10)
even_tens = [x * 10 for x in numbers if x % 2 == 0]
print("Filter + Map:", even_tens)

# Dict Comprehension:
# In JS: Object.fromEntries(names.map(n => [n, n.length]))
names = ["Alice", "Bob", "Charlie"]
lengths = {name: len(name) for name in names}
print("Name lengths dict:", lengths)

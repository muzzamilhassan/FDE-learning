# Lambda: Short one-line anonymous function
# In JS: const add = (a, b) => a + b;
# Note: Python lambdas can only have a SINGLE expression (no multi-line blocks).
add = lambda a, b: a + b
print("Lambda add(3, 4):", add(3, 4))

# Common use case: Custom sorting key
# In JS: users.sort((a, b) => a.age - b.age);
users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 20},
    {"name": "Charlie", "age": 30}
]

by_age = sorted(users, key=lambda u: u["age"])
print("Sorted by age:", [u["name"] for u in by_age])

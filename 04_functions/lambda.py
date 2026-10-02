"""
04_functions / lambda.py
Topic: Anonymous Inline Functions (lambda)

JAVASCRIPT ARROW FUNCTIONS vs PYTHON LAMBDA:
--------------------------------------------
JS Arrow Functions:
    const add = (a, b) => a + b;
    // JS arrow functions can have curly-brace bodies with multiple statements:
    const complex = (a, b) => {
        const sum = a + b;
        return sum * 2;
    };

Python Lambda Functions:
    add = lambda a, b: a + b
    // CRITICAL LIMITATION: A Python lambda can ONLY contain a single expression!
    // It CANNOT contain statements, loops, assignments, or multiline blocks.
    // If you need multiple statements, simply define a standard function with `def`.
"""

# ------------------------------------------------------------------------------
# 1. Basic Lambda Syntax: lambda arguments: expression
# ------------------------------------------------------------------------------
# JS: const multiply = (x, y) => x * y;
multiply = lambda x, y: x * y
print("Lambda multiply(6, 7):", multiply(6, 7))


# ------------------------------------------------------------------------------
# 2. Main Use Case: Custom Sorting Keys
# ------------------------------------------------------------------------------
# In JS: users.sort((a, b) => a.age - b.age);
# In Python: Pass a key function that extracts the comparison value!
users = [
    {"name": "Alice", "age": 30, "salary": 75000},
    {"name": "Bob", "age": 22, "salary": 50000},
    {"name": "Charlie", "age": 28, "salary": 90000},
]

# Sort by age ascending:
by_age = sorted(users, key=lambda user: user["age"])
print("Sorted by age:", [u["name"] for u in by_age])

# Sort by salary descending:
by_salary = sorted(users, key=lambda user: user["salary"], reverse=True)
print("Sorted by salary desc:", [u["name"] for u in by_salary])


# ------------------------------------------------------------------------------
# 3. Sorting by String Length
# ------------------------------------------------------------------------------
# JS: words.sort((a, b) => a.length - b.length)
words = ["python", "go", "javascript", "rust", "c"]
sorted_words = sorted(words, key=lambda word: len(word))
print("Sorted by length:", sorted_words)

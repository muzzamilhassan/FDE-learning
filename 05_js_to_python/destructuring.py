"""
05_js_to_python / destructuring.py
Topic: JavaScript Destructuring vs Python Sequence Unpacking

JAVASCRIPT vs PYTHON:
---------------------
JS Array Destructuring:
    const [first, second, ...rest] = [10, 20, 30, 40];
    const [head, , tail] = [1, 2, 3]; // skipping elements

Python Sequence Unpacking:
    first, second, *rest = [10, 20, 30, 40]
    head, _, tail = [1, 2, 3]         # `_` is standard convention for unused value

JS Object Destructuring:
    const { name, role = "user" } = user;

Python Dictionary Extraction:
    name = user["name"]
    role = user.get("role", "user")
"""

# ------------------------------------------------------------------------------
# 1. Array / List Destructuring
# ------------------------------------------------------------------------------
scores = [100, 85, 72, 64, 50]

# JS: const [first, second] = scores;
first, second = scores[0], scores[1]

# Using rest pattern:
# JS: const [gold, silver, ...others] = scores;
gold, silver, *others = scores
print(f"Gold: {gold}, Silver: {silver}, Others: {others}")

# Skipping items with underscore `_`:
# JS: const [firstItem, , thirdItem] = scores;
first_item, _, third_item, *remainder = scores
print(f"First: {first_item}, Third: {third_item}")


# ------------------------------------------------------------------------------
# 2. Object vs Dictionary Destructuring
# ------------------------------------------------------------------------------
user_data = {
    "username": "coder_alex",
    "email": "alex@dev.to",
    "status": "active"
}

# JS: const { username, email } = userData;
username = user_data["username"]
email = user_data["email"]

# JS: const { plan = "free" } = userData;
plan = user_data.get("plan", "free")
print(f"Extracted: user={username}, email={email}, plan={plan}")


# ------------------------------------------------------------------------------
# 3. Swapping Variables
# ------------------------------------------------------------------------------
# JS: [a, b] = [b, a];
a, b = "apple", "banana"
a, b = b, a
print(f"Swapped: a={a}, b={b}")

"""
=====================================================================
TOPIC: Dictionaries - Key to Value Lookups
=====================================================================

SCENARIO
--------
You are storing user profiles: name, age, role, email. You want to
fetch any field instantly by name, add fields over time, and handle
missing ones gracefully instead of crashing. Dictionaries map keys
to values and do that in one fast step.

TOPIC
-----
- {key: value} pairs; keys are unique, values can repeat.
- dict[key] reads and writes - but a MISSING key raises KeyError.
- dict.get(key, default) returns the default instead of crashing.
- Assigning to a key adds it or overwrites it; dict.pop(k) removes.
- Loop pairs with: for key, value in dict.items().
- "key in dict" tests keys only - the safe pre-check before reading.

QUESTIONS
---------
Q1. Predict: print(stock.get("banana", 0) + stock["apple"])
Q2. Spot the bug: "if stock['banana'] > 0:" when banana may be absent
Q3. Write code: count how many times each letter appears in
    "banana" and store the result in a dictionary.
Q4. Predict: print({"a": 1, "b": 2} | {"b": 9, "c": 3})

Run: python 02_collections/dictionaries.py
Answers: answers/02_collections.py
"""

# ------------------------------------------------------------------
# TOPIC EXAMPLES
# ------------------------------------------------------------------

user = {"name": "Alice", "age": 25, "role": "Developer"}

# Square brackets read by key - but crash if the key is missing.
print("Name:", user["name"])

# .get() returns a default for missing keys instead of raising.
print("Email:", user.get("email", "not provided"))
print("Is 'email' a key?", "email" in user)

# Assigning to a key adds it if new, or overwrites if it exists.
user["email"] = "alice@example.com"     # new key
user["age"] = 26                        # existing key updated
print("Updated:", user)

# .pop() removes a key AND returns its value.
old_role = user.pop("role")
print(f"Popped role '{old_role}', keys now:", list(user.keys()))

# Looping over pairs with .items() - the most common dict loop.
for key, value in user.items():
    print(f"  {key}: {value}")

# A practical pattern: counting things safely.
word = "level"
counts = {}
for letter in word:
    counts[letter] = counts.get(letter, 0) + 1
print("Letter counts:", counts)

# Merging with |: the right-hand dict wins on duplicate keys.
base = {"theme": "light", "font": 12}
local = {"font": 14}
print("Merged:", base | local)

# ------------------------------------------------------------------
# QUESTIONS - try them yourself, then check answers/02_collections.py
# ------------------------------------------------------------------
# Q1: With stock = {"apple": 3, "pear": 0}, predict the output:
#     print(stock.get("banana", 0) + stock["apple"])
#
# Q2: This crashes whenever "banana" is not in stock. Fix it:
#     if stock["banana"] > 0:
#         print("We have bananas")
#
# Q3: Write code: loop over the word "banana" and build a dictionary
#     mapping each letter to how many times it appears.
#
# Q4: Predict the output:
#     print({"a": 1, "b": 2} | {"b": 9, "c": 3})

"""
02_collections / dictionaries.py
Topic: Python Dictionaries (Equivalent to JavaScript Objects / HashMaps)

JAVASCRIPT OBJECT/MAP vs PYTHON DICTIONARY:
-------------------------------------------
JS Object:
    const user = { name: "Alice", age: 25 };
    console.log(user.name);         // Dot notation works
    console.log(user["age"]);       // Bracket notation works
    console.log(user.missing);      // Returns `undefined` (No error!)

Python Dict:
    user = {"name": "Alice", "age": 25}
    # BIG DIFFERENCE 1: In Python, string keys MUST be quoted: {"name": "Alice"}
    # {"name": "Alice"} in JS allows omitting quotes {name: "Alice"}. Python DOES NOT!
    # BIG DIFFERENCE 2: No dot notation! user.name will raise AttributeError.
    # BIG DIFFERENCE 3: Missing key user["missing"] raises a KeyError!
    #                   Use user.get("missing", default_val) for safe access!
"""

# ------------------------------------------------------------------------------
# 1. Dictionary Creation
# ------------------------------------------------------------------------------
developer = {
    "name": "Sarah Connor",
    "role": "Backend Engineer",
    "experience_years": 5,
    "skills": ["Python", "Docker", "PostgreSQL"],
    "is_remote": True,
}

print("Developer:", developer)


# ------------------------------------------------------------------------------
# 2. Accessing Values: Bracket vs .get()
# ------------------------------------------------------------------------------
# Direct bracket access:
print("Name:", developer["name"])

# Safely accessing non-existent keys (avoiding KeyError):
# JS: developer.github ?? "Not Provided"
github_handle = developer.get("github", "Not Provided")
print("GitHub handle (safe get):", github_handle)


# ------------------------------------------------------------------------------
# 3. Adding and Updating Entries
# ------------------------------------------------------------------------------
# JS: developer.location = "Berlin";
developer["location"] = "Berlin"

# JS: Object.assign(developer, { team: "Platform", level: "Senior" });
developer.update({"team": "Platform", "level": "Senior"})
print("Updated developer:", developer)


# ------------------------------------------------------------------------------
# 4. Deleting Entries
# ------------------------------------------------------------------------------
# JS: delete developer.is_remote;
# In Python:
del developer["is_remote"]
# Or .pop() which returns the deleted value:
removed_level = developer.pop("level", None)
print(f"Popped level: {removed_level}")


# ------------------------------------------------------------------------------
# 5. Iterating Over Dictionaries
# ------------------------------------------------------------------------------
# In JS:
#   Object.keys(obj)    -> Python: dict.keys()
#   Object.values(obj)  -> Python: dict.values()
#   Object.entries(obj) -> Python: dict.items()

print("\n--- Iterating with .items() (like Object.entries) ---")
for key, value in developer.items():
    print(f"  {key}: {value}")


# ------------------------------------------------------------------------------
# 6. Dictionary Comprehension (Creating dicts dynamically)
# ------------------------------------------------------------------------------
# JS: Object.fromEntries([1, 2, 3].map(n => [`num_${n}`, n * 10]))
number_map = {f"num_{n}": n * 10 for n in range(1, 5)}
print("Dict comprehension result:", number_map)

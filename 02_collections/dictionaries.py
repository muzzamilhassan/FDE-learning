# In JS: const user = { name: "Alice", age: 25 }; (Object / Map)
# NOTE: In Python, string keys MUST have quotes!
user = {
    "name": "Alice",
    "age": 25,
    "role": "Developer"
}

# Accessing:
print("Name:", user["name"])

# In JS: user.missing ?? "Default"
# If key is missing, user["missing"] throws KeyError! Use .get() instead:
email = user.get("email", "Not provided")
print("Email:", email)

# Adding / Updating:
user["email"] = "alice@example.com"

# In JS: Object.keys(), Object.values(), Object.entries()
print("Keys:", list(user.keys()))
print("Values:", list(user.values()))

# Looping over key-value pairs:
for key, value in user.items():
    print(f"  {key}: {value}")

"""
01_basics / strings.py
Topic: String Formatting, Slicing, and Essential Methods

JAVASCRIPT vs PYTHON STRINGS:
-----------------------------
JS Template Literals:  `Hello, ${name}! Price: $${price.toFixed(2)}`
Python f-strings:      f"Hello, {name}! Price: ${price:.2f}"

JS Slicing:            str.slice(0, 5)  (no step support)
Python Slicing:        str[0:5] or str[start:stop:step] (supports negative indices and step)
"""

# ------------------------------------------------------------------------------
# 1. f-Strings (The Python equivalent to JS Template Literals)
# ------------------------------------------------------------------------------
# JS: const user = "Sarah"; const role = "Fullstack Developer";
# JS: console.log(`User ${user} is a ${role}`);
user = "Sarah"
role = "Fullstack Developer"
salary = 95000.50

# Python f-strings start with an 'f' before the quotes:
print(f"User {user} is a {role}.")
# In-line expressions work just like JS ${}:
print(f"Salary with 2 decimals: ${salary:.2f}")
print(f"Calculation: 10 * 5 = {10 * 5}")


# ------------------------------------------------------------------------------
# 2. String Indexing and Slicing [start:stop:step]
# ------------------------------------------------------------------------------
# JS: const text = "JavaScript";
# JS: text.charAt(0) or text[0]
# JS: text.slice(0, 4) // "Java"
text = "Python Programming"

print("First char text[0]:", text[0])
print("Last char text[-1]:", text[-1])      # Negative index = count from end (JS: text.at(-1))
print("Slice [0:6]:", text[0:6])            # From index 0 up to (not including) 6 -> "Python"
print("Slice [:6]:", text[:6])              # Omit start -> starts at 0
print("Slice [7:]:", text[7:])              # Omit stop -> goes to the end -> "Programming"
print("Step slice [::2]:", text[::2])       # Every 2nd character
print("Reverse string [::-1]:", text[::-1]) # Cleanest way to reverse a string in Python!


# ------------------------------------------------------------------------------
# 3. Common String Methods
# ------------------------------------------------------------------------------
# JS: str.toUpperCase()   -> Python: str.upper()
# JS: str.toLowerCase()   -> Python: str.lower()
# JS: str.trim()          -> Python: str.strip()
# JS: str.replace(a, b)   -> Python: str.replace(a, b)
# JS: str.startsWith("P") -> Python: str.startswith("P")
# JS: str.includes("on")  -> Python: "on" in str  (or str.find("on") != -1)

raw_input_data = "   hello python world   "
print("Strip whitespace:", repr(raw_input_data.strip()))
print("Upper:", text.upper())
print("Lower:", text.lower())
print("Title Case:", text.title())
print("Contains 'on'?:", "on" in text)


# ------------------------------------------------------------------------------
# 4. Split and Join (BIG SYNTAX DIFFERENCE!)
# ------------------------------------------------------------------------------
# In JS:
#   const arr = "apple,banana,orange".split(",");
#   const str = arr.join(" - ");  // Array method in JS!
#
# In Python:
#   lst = "apple,banana,orange".split(",")
#   str = " - ".join(lst)         // String method in Python! (separator.join(list))

csv_data = "apple,banana,orange,grape"
fruit_list = csv_data.split(",")
print("Split into list:", fruit_list)

# Notice: In Python, you call .join() ON THE SEPARATOR STRING, passing the list:
joined_string = " | ".join(fruit_list)
print("Joined back:", joined_string)

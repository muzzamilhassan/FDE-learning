# In JS: `Hello, ${name}!` (template literal)
name = "Sarah"
role = "Developer"
print(f"Hello, {name}! You are a {role}.")  # f-string

# In JS: text.slice(0, 4)
text = "Python"
print("First char text[0]:", text[0])
print("Last char text[-1]:", text[-1])       # In JS: text.at(-1)
print("Slice text[0:2]:", text[0:2])         # "Py"
print("Reverse text[::-1]:", text[::-1])     # Reverse string

# In JS: text.toUpperCase(), text.toLowerCase(), text.trim()
sample = "  hello world  "
print("Cleaned:", sample.strip().title())

# In JS: "a,b,c".split(",") -> ["a","b","c"].join("-")
items = "apple,banana,orange".split(",")
print("Joined back:", " - ".join(items))     # Note: separator.join(list)

# Output: print()
# In JS: console.log("Hello", "World")
print("Hello", "World", sep=" - ")           # Custom separator
print("No newline", end=" -> ")              # Custom line ending
print("Next text")

# Format numbers
price = 1234.567
print(f"Price formatted: ${price:,.2f}")

# Input: input()
# In JS (browser): prompt("Enter name: ")
# Note: input() always returns a string (str)
user_name = input("Enter your name (or press enter): ") or "Guest"
print(f"Welcome, {user_name}!")

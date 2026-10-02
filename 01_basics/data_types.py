# In JS: typeof x === "number", "string", "boolean", null, undefined
# Python core types: int, float, str, bool, None (Python has NO undefined)

count = 42                 # int (integers have unlimited size in Python)
price = 19.99              # float
message = "Hello"          # str
is_valid = True            # bool
empty_val = None           # In JS: null

# In JS: typeof count === "number"
print("Type of count:", type(count).__name__)
print("Is count an int?:", isinstance(count, int))

# In JS: Number("123"), String(123), Boolean(1)
num = int("123")
text = str(456)
flag = bool(1)

print(f"Converted: num={num}, text='{text}', flag={flag}")

# Arithmetic
# In JS: Math.floor(15 / 4) === 3
print("Float division (15 / 4):", 15 / 4)    # 3.75
print("Floor division (15 // 4):", 15 // 4)  # 3
print("Power (2 ** 3):", 2 ** 3)             # 8

# Logical: and, or, not (In JS: &&, ||, !)
is_admin = True
is_logged_in = False
print("and:", is_admin and is_logged_in)
print("or:", is_admin or is_logged_in)
print("not:", not is_logged_in)

# Membership: in (In JS: [1, 2].includes(1))
numbers = [1, 2, 3]
print("Is 2 in numbers?:", 2 in numbers)

# Identity: is (checks memory address) vs == (checks values)
# In JS: [1] === [1] is false; in Python: [1] == [1] is True
a = [1, 2]
b = [1, 2]
print("a == b (same values):", a == b)       # True
print("a is b (same memory):", a is b)       # False

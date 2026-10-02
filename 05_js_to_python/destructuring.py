# 1. Array Destructuring -> Unpacking
# In JS: const [first, second, ...rest] = [10, 20, 30, 40];
first, second, *rest = [10, 20, 30, 40]
print(f"first={first}, second={second}, rest={rest}")

# In JS: const [head, , tail] = [1, 2, 3]; (skip item with _)
head, _, tail = [1, 2, 3]
print(f"head={head}, tail={tail}")

# 2. Object Destructuring -> Dict Access
# In JS: const { name, role = "user" } = userData;
user_data = {"name": "Alex", "email": "alex@dev.to"}
name = user_data["name"]
role = user_data.get("role", "user")
print(f"name={name}, role={role}")

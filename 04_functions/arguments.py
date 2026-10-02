# *args: Arbitrary positional arguments (packed into a tuple)
# In JS: function sumAll(...numbers) { ... }
def sum_all(*numbers: float) -> float:
    return sum(numbers)

print("Sum with *args:", sum_all(10, 20, 30))

# **kwargs: Arbitrary keyword arguments (packed into a dict)
# In JS: function makeUser(options) { ... }
def make_user(username: str, **details):
    print(f"Username: {username}")
    for key, value in details.items():
        print(f"  {key}: {value}")

make_user("coder_alex", role="Admin", department="Engineering")

# In JS: function greet(name) { return `Hello, ${name}`; }
def greet(name: str) -> str:
    """Return a friendly greeting."""
    return f"Hello, {name}!"

print(greet("Sarah"))

# Returning multiple values (packed into a tuple):
# In JS: return [min, max] or return { min, max }
def get_min_max(numbers: list[int]):
    return min(numbers), max(numbers)

minimum, maximum = get_min_max([5, 2, 9, 1, 7])
print(f"Min: {minimum}, Max: {maximum}")

# Default parameters:
def connect(host="localhost", port=5432):
    return f"Connecting to {host}:{port}"

print(connect())
print(connect(port=8000))  # Named / keyword arguments!

# Tuples are IMMUTABLE lists: cannot be changed after creation.
# JS has no built-in tuple (like Object.freeze([10, 20])).
point = (10, 20)

# In JS: const [x, y] = point; (destructuring / unpacking)
x, y = point
print(f"x={x}, y={y}")

# Single element tuple MUST have a comma!
single = (42,)

# Why tuples? They can be used as dictionary keys because they are immutable:
locations = {
    (40.71, -74.00): "New York",
    (51.50, -0.12): "London"
}
print("Location at coords:", locations[(40.71, -74.00)])

# 1. List / Array Spread (...) -> *
# In JS: const combined = [...listA, ...listB];
list_a = [1, 2]
list_b = [3, 4]
combined = [*list_a, *list_b]
print("Spread lists:", combined)

# 2. Object / Dict Spread (...) -> ** or |
# In JS: const config = { ...defaults, ...overrides };
defaults = {"theme": "light", "lang": "en"}
overrides = {"theme": "dark"}
config = {**defaults, **overrides}      # or: defaults | overrides
print("Merged dict:", config)

# 3. Spread arguments into a function call
# In JS: fn(...args)
def add(a, b):
    return a + b

args = [5, 10]
print("Function spread:", add(*args))

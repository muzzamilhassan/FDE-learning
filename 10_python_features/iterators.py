# In JS: [Symbol.iterator]() and .next()
# In Python: iter() and next()

items = ["apple", "banana"]
it = iter(items)

print(next(it))  # "apple"
print(next(it))  # "banana"
# Calling next(it) again raises StopIteration (in JS: { done: true })

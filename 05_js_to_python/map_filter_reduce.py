from functools import reduce

numbers = [1, 2, 3, 4, 5]

# 1. Array.map() -> List Comprehension
# In JS: numbers.map(x => x * 2)
doubled = [x * 2 for x in numbers]
print("Map (doubled):", doubled)

# 2. Array.filter() -> List Comprehension
# In JS: numbers.filter(x => x > 2)
greater_than_two = [x for x in numbers if x > 2]
print("Filter (>2):", greater_than_two)

# 3. Array.reduce() -> sum() or functools.reduce()
# In JS: numbers.reduce((acc, curr) => acc + curr, 0)
total = sum(numbers)
# In JS: numbers.reduce((acc, curr) => acc * curr, 1)
product = reduce(lambda acc, curr: acc * curr, numbers, 1)
print(f"Reduce: sum={total}, product={product}")

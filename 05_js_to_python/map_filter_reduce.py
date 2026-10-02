"""
05_js_to_python / map_filter_reduce.py
Topic: JavaScript Array Functional Methods vs Python Equivalents

SUMMARY TABLE:
--------------
JS Method                 Python Functional             Idiomatic Python (Preferred)
------------------------------------------------------------------------------------
arr.map(fn)               map(fn, arr)                  [fn(x) for x in arr]
arr.filter(fn)            filter(fn, arr)               [x for x in arr if fn(x)]
arr.reduce(fn, init)      functools.reduce(fn, arr)     sum() built-in or loop
arr.every(fn)             all(fn(x) for x in arr)       all(...)
arr.some(fn)              any(fn(x) for x in arr)       any(...)
arr.find(fn)              next(x for x in arr if fn)    next(...)
"""
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

# ------------------------------------------------------------------------------
# 1. Array.prototype.map()
# ------------------------------------------------------------------------------
# JS: const doubled = numbers.map(x => x * 2);

# Approach A: Built-in map() function (returns an iterator, must convert to list)
doubled_via_map = list(map(lambda x: x * 2, numbers))

# Approach B: List Comprehension (Idiomatic Python - much preferred!)
doubled_via_comp = [x * 2 for x in numbers]

print("Map results match?:", doubled_via_map == doubled_via_comp)
print("Doubled:", doubled_via_comp)


# ------------------------------------------------------------------------------
# 2. Array.prototype.filter()
# ------------------------------------------------------------------------------
# JS: const evens = numbers.filter(x => x % 2 === 0);

# Approach A: Built-in filter() function
evens_via_filter = list(filter(lambda x: x % 2 == 0, numbers))

# Approach B: List Comprehension (Idiomatic Python)
evens_via_comp = [x for x in numbers if x % 2 == 0]

print("Filter results match?:", evens_via_filter == evens_via_comp)
print("Evens:", evens_via_comp)


# ------------------------------------------------------------------------------
# 3. Array.prototype.reduce()
# ------------------------------------------------------------------------------
# JS: const total = numbers.reduce((acc, curr) => acc + curr, 0);

# Approach A: For additions, use Python's built-in sum()!
total_sum = sum(numbers)

# Approach B: For general accumulations, use functools.reduce:
# JS: const product = numbers.reduce((acc, curr) => acc * curr, 1);
product = reduce(lambda acc, curr: acc * curr, numbers, 1)

print(f"Sum (reduce): {total_sum}, Product (reduce): {product}")


# ------------------------------------------------------------------------------
# 4. Array.prototype.every() and some()
# ------------------------------------------------------------------------------
# JS: const allPositive = numbers.every(x => x > 0);
# JS: const hasGreaterThanFive = numbers.some(x => x > 5);
all_positive = all(x > 0 for x in numbers)
has_greater_than_five = any(x > 5 for x in numbers)

print("all() -> every:", all_positive)
print("any() -> some:", has_greater_than_five)

"""
02_collections / lists.py
Topic: Python Lists (Equivalent to JavaScript Arrays)

JAVASCRIPT ARRAY vs PYTHON LIST:
--------------------------------
JS:     const arr = [1, 2, 3];
Python: lst = [1, 2, 3]

Method Mapping:
  JS: arr.push(4)          -> Python: lst.append(4)
  JS: arr.pop()            -> Python: lst.pop()
  JS: arr.unshift(0)       -> Python: lst.insert(0, 0)
  JS: arr.shift()          -> Python: lst.pop(0)
  JS: arr.concat([4, 5])   -> Python: lst.extend([4, 5]) or lst + [4, 5]
  JS: arr.length           -> Python: len(lst)
  JS: arr.slice(1, 3)      -> Python: lst[1:3]
  JS: arr.indexOf(2)       -> Python: lst.index(2)
  JS: arr.includes(2)      -> Python: 2 in lst
  JS: arr.sort()           -> Python: lst.sort() (in-place) or sorted(lst) (returns new)
"""

# ------------------------------------------------------------------------------
# 1. Creation and Indexing
# ------------------------------------------------------------------------------
fruits = ["apple", "banana", "cherry", "date"]

# JS: fruits.length
print("Length:", len(fruits))

# JS: fruits[0], fruits[fruits.length - 1] (or fruits.at(-1))
print("First element:", fruits[0])
print("Last element:", fruits[-1])


# ------------------------------------------------------------------------------
# 2. Mutability (Modifying, Adding, Removing)
# ------------------------------------------------------------------------------
# Lists are mutable (can be changed in-place)
fruits[1] = "blueberry"
print("After update:", fruits)

# JS: fruits.push("elderberry")
fruits.append("elderberry")
print("After append:", fruits)

# JS: fruits.unshift("avocado") (insert at beginning)
fruits.insert(0, "avocado")
print("After insert at 0:", fruits)

# JS: fruits.push(...["fig", "grape"])
fruits.extend(["fig", "grape"])
print("After extend:", fruits)

# Removing:
# JS: const removed = fruits.pop()
last_fruit = fruits.pop()
print(f"Popped last item: {last_fruit}")

# Remove by value (removes first occurrence):
fruits.remove("blueberry")
print("After removing 'blueberry':", fruits)


# ------------------------------------------------------------------------------
# 3. Sorting: in-place .sort() vs sorted()
# ------------------------------------------------------------------------------
# In JS:
#   arr.sort() mutates in-place (and converts items to strings by default!).
# In Python:
#   lst.sort() sorts numerically/alphabetically in-place.
#   sorted(lst) returns a brand new sorted list (leaves original untouched).

scores = [88, 42, 99, 73, 61]

# Non-mutating sort:
sorted_scores = sorted(scores)
print("Original scores:", scores)
print("sorted() new list:", sorted_scores)

# In-place mutating sort:
scores.sort(reverse=True)
print("scores.sort(reverse=True) in-place:", scores)

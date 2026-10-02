# In JS: const items = [1, 2, 3]; (Array)
items = [10, 20, 30]

# In JS: items.push(40)
items.append(40)

# In JS: items.pop()
last_item = items.pop()

# In JS: items.unshift(0) (insert at start)
items.insert(0, 0)

# In JS: items.length
print("Length:", len(items))
print("Items:", items)

# Slicing: [start:stop]
# In JS: items.slice(1, 3)
print("Slice [1:3]:", items[1:3])

# Sorting: in-place .sort() vs sorted()
# In JS: [...items].sort()
numbers = [5, 2, 9, 1]
print("sorted() new list:", sorted(numbers))
numbers.sort()
print("numbers.sort() in-place:", numbers)

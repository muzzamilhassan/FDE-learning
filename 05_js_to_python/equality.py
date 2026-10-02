# In JS: == (loose), === (strict)
# In Python:
#   ==  checks VALUE (structural equality)
#   is  checks IDENTITY (memory address)

# 1. Value equality (==)
# In JS: [1, 2] === [1, 2] is FALSE (references differ)
# In Python: [1, 2] == [1, 2] is TRUE (values match)
list1 = [1, 2]
list2 = [1, 2]
print("list1 == list2 (values match):", list1 == list2)  # True

# 2. Identity (is)
print("list1 is list2 (same memory):", list1 is list2)   # False

# 3. Always use 'is None' instead of '== None'
# In JS: val === null || val === undefined
val = None
if val is None:
    print("val is None (Correct Python idiom!)")

# BIG DIFFERENCE FROM JS:
# In JS: Boolean([]) === true and Boolean({}) === true
# In Python: Empty lists [] and dicts {} are FALSY!

print("Is [] truthy in Python?:", bool([]))         # False!
print("Is {} truthy in Python?:", bool({}))         # False!
print("Is '' truthy in Python?:", bool(""))         # False!
print("Is 0 truthy in Python?:", bool(0))           # False!
print("Is None truthy in Python?:", bool(None))     # False!

# Pythonic way to check if a list has items:
# In JS: if (items.length > 0)
items = []
if not items:
    print("List is empty! (Checked with 'if not items:')")

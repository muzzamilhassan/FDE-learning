"""
05_js_to_python / truthy_falsy.py
Topic: Truthy and Falsy Differences between JavaScript and Python

THE SINGLE BIGGEST TRAP FOR JAVASCRIPT DEVELOPERS IN PYTHON:
------------------------------------------------------------
In JavaScript:
    Boolean([]) === true    <-- Empty array is TRUTHY!
    Boolean({}) === true    <-- Empty object is TRUTHY!

In Python:
    bool([]) == False       <-- Empty list is FALSY!
    bool({}) == False       <-- Empty dict is FALSY!
    bool(set()) == False    <-- Empty set is FALSY!
"""

# ------------------------------------------------------------------------------
# 1. Complete Python Falsy Reference
# ------------------------------------------------------------------------------
# In Python, exactly these evaluate to False:
#   1. None
#   2. False
#   3. Zero numbers: 0, 0.0, 0j
#   4. Empty sequences: "" (empty string), [] (empty list), () (empty tuple), range(0)
#   5. Empty mappings / sets: {} (empty dict), set() (empty set)

falsy_values = [
    ("None", None),
    ("False", False),
    ("Zero int: 0", 0),
    ("Zero float: 0.0", 0.0),
    ("Empty str: ''", ""),
    ("Empty list: []", []),
    ("Empty tuple: ()", ()),
    ("Empty dict: {}", {}),
    ("Empty set: set()", set()),
]

print("=== Python FALSY Values ===")
for label, val in falsy_values:
    print(f"{label:22} -> bool() is: {bool(val)}")


# ------------------------------------------------------------------------------
# 2. Python Truthy Examples
# ------------------------------------------------------------------------------
truthy_values = [
    ("Non-empty str: 'hello'", "hello"),
    ("List with 0: [0]", [0]),          # List with items is truthy, even if item is 0!
    ("Dict with key: {'a': 1}", {"a": 1}),
    ("Non-zero number: -1", -1),
    ("True", True),
]

print("\n=== Python TRUTHY Values ===")
for label, val in truthy_values:
    print(f"{label:25} -> bool() is: {bool(val)}")


# ------------------------------------------------------------------------------
# 3. Practical Idiom: Checking for Empty Collections
# ------------------------------------------------------------------------------
# In JS:
#   if (users.length === 0) { ... }
#   if (Object.keys(config).length === 0) { ... }
#
# In Python:
#   Simply use `if not items:` !
users_list = []
if not users_list:
    print("\n[Pythonic Idiom]: 'if not users_list:' checks if collection is empty!")

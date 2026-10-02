"""
01_basics / data_types.py
Topic: Core Data Types, Type Checking, and Type Conversion

JAVASCRIPT vs PYTHON DATA TYPES:
--------------------------------
JavaScript Types:
  - number (handles BOTH integers and floating-point: 42 and 3.14 are both 'number')
  - bigint (for arbitrarily large numbers)
  - string ("hello" or 'hello')
  - boolean (true / false)
  - null (represents explicit absence of an object)
  - undefined (variable declared but not assigned a value)
  - symbol, object

Python Types:
  - int (integers have ARBITRARY precision built-in! No overflow, no separate BigInt)
  - float (double-precision floating-point)
  - str (Unicode strings)
  - bool (True / False - sub-type of int where True == 1 and False == 0)
  - NoneType (None - ONLY one empty value! Python does NOT have 'undefined')
"""

# ------------------------------------------------------------------------------
# 1. Primitive Type Overview
# ------------------------------------------------------------------------------
# JS: const count = 42;
count = 42                             # int (can grow infinitely large!)

# JS: const temperature = 98.6;
temperature = 98.6                     # float

# JS: const greeting = "Hello, Python!";
greeting = "Hello, Python!"            # str

# JS: const isVerified = false;
is_verified = False                    # bool (Capital T and F!)

# JS: const emptyValue = null; (Note: JS also has undefined, Python only has None)
empty_value = None                     # NoneType

print("count:", count, type(count))
print("temperature:", temperature, type(temperature))
print("greeting:", greeting, type(greeting))
print("is_verified:", is_verified, type(is_verified))
print("empty_value:", empty_value, type(empty_value))


# ------------------------------------------------------------------------------
# 2. Type Checking (typeof vs isinstance)
# ------------------------------------------------------------------------------
# In JS:
#   typeof count === "number"
#   count instanceof Number (only for wrapped objects)
#
# In Python:
#   type(x) -> returns the exact class type
#   isinstance(x, Type) -> checks type AND inheritance (recommended best practice)

print("Is count an int?", isinstance(count, int))
print("Is count a float?", isinstance(count, float))

# Check multiple allowable types (tuple of types):
# JS: typeof count === "number"
print("Is count numeric (int or float)?", isinstance(count, (int, float)))


# ------------------------------------------------------------------------------
# 3. Type Conversion (Casting)
# ------------------------------------------------------------------------------
# In JS:
#   Number("123")  or parseInt("123")  -> 123
#   parseFloat("123.45")               -> 123.45
#   String(123)                        -> "123"
#   Boolean(1)                         -> true
#
# In Python:
#   Use constructor functions: int(), float(), str(), bool()

str_number = "123"
converted_int = int(str_number)
converted_float = float(str_number)
back_to_str = str(converted_int)
bool_from_num = bool(1)   # 0 is False, any non-zero number is True

print("Converted Int:", converted_int, type(converted_int))
print("Converted Float:", converted_float, type(converted_float))
print("Back to String:", repr(back_to_str), type(back_to_str))
print("Bool from 1:", bool_from_num, type(bool_from_num))

"""
Answers for 01_basics - try the questions first!
"""

# ------------------------------------------------------------------
# variables.py
# ------------------------------------------------------------------

# Q1: score = score * 2 reuses the old value, so 10 becomes 20.
score = 10
score = score * 2
print(f"score is {score}")                 # score is 20

# Q2: Reading a name that was never assigned raises NameError -
#     Python does not guess what `location` should be.
location = "Lahore"
print(location)                            # works only AFTER assignment

# Q3: Three variables, one f-string sentence that uses all three.
title = "The Pragmatic Learner"
price = 12.99
in_stock = True
print(f"{title} costs ${price}. In stock: {in_stock}")

# Q4: The right side (b, a) is packed into the pair (2, 1) FIRST,
#     then unpacked into a and b - so the values trade places.
a, b = 1, 2
a, b = b, a
print(a, b)                                # 2 1

# ------------------------------------------------------------------
# data_types.py
# ------------------------------------------------------------------

# Q1: 7 is an int, but the / operator ALWAYS produces a float,
#     even when the division is exact.
print(type(7).__name__, type(7 / 1).__name__)   # int float

# Q2: "19.99" is not a whole number, so int() raises ValueError -
#     convert with float() instead (or int(float(text)) to truncate).
price_text = "19.99"
price = float(price_text)
print(price, type(price).__name__)              # 19.99 float

# Q3: Convert once, then normal maths works on the int.
number = int("42") * 2
print(number, type(number).__name__)            # 84 int

# Q4: bool() follows the emptiness rule: 0 and "" are empty ->
#     False, but "0" is a non-empty STRING, so it is True.
print(bool(0), bool(""), bool("0"))             # False False True

# ------------------------------------------------------------------
# strings.py
# ------------------------------------------------------------------

# Q1: Slices include the start index but EXCLUDE the stop index,
#     so [1:4] takes indexes 1, 2 and 3 -> "yth".
print("Python"[1:4])                       # yth

# Q2: Strings are immutable - .upper() returns a NEW string and
#     throws it away unless you assign it back to the name.
shout = "hey"
shout = shout.upper()                      # capture the new string
print(shout)                               # HEY

# Q3: Chain .strip() (spaces) with .title() (capitalisation).
display_name = "  ada LOVELACE  ".strip().title()
print(display_name)                        # Ada Lovelace

# Q4: split() cuts on the comma, join() glues with the separator.
colours = "red,green,blue".split(",")
print(" | ".join(colours))                 # red | green | blue

# ------------------------------------------------------------------
# operators.py
# ------------------------------------------------------------------

# Q1: // counts how many whole 2s fit in 7 (3) and % gives the
#     leftover remainder (1).
print(7 // 2, 7 % 2)                       # 3 1

# Q2: / always returns a float (4.5); use // for the whole-number
#     floor when you are counting indivisible things.
items = 9
print(items // 2)                          # 4

# Q3: `and` is True only when BOTH sides are True - exactly the
#     rule for entering.
age = 20
has_ticket = True
print(age >= 18 and has_ticket)            # True

# Q4: `in` checks substrings in strings and members in lists, so
#     the substring is found but 3 is not an element of [1, 2].
print("py" in "python", 3 in [1, 2])       # True False

# ------------------------------------------------------------------
# input_output.py
# ------------------------------------------------------------------

# Q1: sep= replaces the space between values and end= replaces the
#     newline, so the second print continues on the same line.
print("a", "b", sep="-", end="!")
print("c")                                 # a-b!c

# Q2: input() ALWAYS returns str, so + glues text together instead
#     of adding numbers; int(nums) * 10 or int(nums + "0") gets 50.
nums = "5"                                 # what input() gave back
print(nums + "0", type(nums).__name__)     # 50 str

# Q3: Convert immediately with int(); `or` handles an empty answer.
#     (try/except just keeps this file runnable without a keyboard.)
try:
    name = input("Name: ") or "Guest"
    age_text = input("Age: ")
    age = int(age_text) if age_text else 0
    print(f"{name} will be {age + 1} next year.")
except EOFError:
    print("(no input available - run me in a terminal)")

# ------------------------------------------------------------------
# equality.py
# ------------------------------------------------------------------

# Q1: == compares contents (equal) while is compares identity, and
#     two separately written lists are two different objects.
print([1, 2] == [1, 2], [1, 2] is [1, 2])  # True False

# Q2: There is exactly one None object, so `is None` asks the
#     identity question directly and can never be tricked by a
#     custom __eq__ (which == would call).
x = None
print(x is None)                           # True

# Q3: True and False ARE the numbers 1 and 0 in Python, so the
#     first two match; a str never equals an int.
print(1 == True, 0 == False, "1" == 1)     # True True False

# Q4: `is` asks "is this the single None object?", which is exactly
#     the question - == would run the value's own comparison and
#     can give surprising answers.
saved = None
if saved is None:
    print("nothing saved yet")

# Q5: == fires on equal contents; `is` fires only for one shared
#     object (make b a copy to see them differ).
items_a = ["pen"]
items_b = ["pen"]
if items_a == items_b:
    print("same contents")
if items_a is items_b:
    print("same object")                   # never prints here

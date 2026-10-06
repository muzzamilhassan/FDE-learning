"""
=====================================================================
TOPIC: Variables
=====================================================================

SCENARIO
--------
You are building the sign-up page for a small library app. You need
to store a reader's name, age, and membership status, and you want
to swap two shelf labels around when the shelves get reorganised.
Variables are how data stays alive between lines of code.

TOPIC
-----
- Assignment: name = value. No keyword needed in front of the name.
- Names use snake_case; ALL_CAPS means "please do not change me".
- Multiple assignment: x, y = 1, 2. Swap: x, y = y, x.
- Reassigning is allowed any time, even to a different type.
- Gotcha: reading a name before assigning it raises NameError.

QUESTIONS
---------
Q1. (predict) What does the final print show?
Q2. (bug spot) Why does print(city) crash before city = "Paris"?
Q3. (write code) Store a book title, price, and availability flag,
    then print one sentence that uses all three.
Q4. (predict) After a, b = 1, 2 and a, b = b, a, what are a and b?

Run: python 01_basics/variables.py
Answers: answers/01_basics.py
=====================================================================
"""

# ------------------------------------------------------------------
# TOPIC EXAMPLES
# ------------------------------------------------------------------

reader_name = "Aisha"        # snake_case is the normal style
reader_age = 27
has_membership = True        # booleans are capitalised True / False

# Multiple assignment: create two names in one line
shelf_a, shelf_b = "Cookbooks", "Sci-Fi"

# The swap needs no temp variable: the right side packs the pair
# first, then unpacks it into the names on the left.
shelf_a, shelf_b = shelf_b, shelf_a

# ALL_CAPS marks a value you promise not to reassign
MAX_BOOKS = 5

# Reassignment simply replaces the old value
books_borrowed = 2
books_borrowed = books_borrowed + 3   # now 5
books_borrowed += 1                   # shortcut: now 6

print(f"Reader: {reader_name}, age {reader_age}, member: {has_membership}")
print(f"Shelves: {shelf_a} / {shelf_b}")
print(f"Max books per visit: {MAX_BOOKS}")
print(f"Borrowed so far: {books_borrowed}")

# ------------------------------------------------------------------
# QUESTIONS - try them yourself, then check answers/01_basics.py
# ------------------------------------------------------------------
# Q1: Predict the output of:
#       score = 10
#       score = score * 2
#       print(f"score is {score}")
# Q2: Spot the bug - what error does this raise, and why?
#       print(location)
#       location = "Lahore"
# Q3: Write code: create `title`, `price`, and `in_stock` variables
#     for one book, then print a single sentence using all three.
# Q4: Predict the values of a and b after:
#       a, b = 1, 2
#       a, b = b, a

"""
=====================================================================
TOPIC: Equality (== vs is)
=====================================================================

SCENARIO
--------
Your bookmark app saves a list of links, then later asks two
questions: "did the user already save this list?" and "is this
field empty?". Mixing up == and is makes both checks lie to you,
so it pays to know exactly what each one tests.

TOPIC
-----
- == asks: do these two values LOOK the same? (value equality)
- is asks: are these literally the same object in memory?
- Collections compare by value: [1, 2] == [1, 2] is True.
- Two separately created lists are never `is` each other.
- Bools count as numbers: True == 1 and False == 0.
- Different types usually differ: "1" == 1 is False.
- Rule of thumb: `is` only for None (and sentinels), == for data.

QUESTIONS
---------
Q1. (predict) What do these two lines print?
      print([1, 2] == [1, 2])
      print([1, 2] is [1, 2])
Q2. (concept) Why does the style guide say `if x is None:` instead
    of `if x == None:`?
Q3. (predict) What do 1 == True, 0 == False, and "1" == 1 return?
Q4. (bug spot) A teammate wrote `if saved == None:` to detect
    "nothing saved yet" - why is `is` the right tool here?
Q5. (write code) For items_a = ["pen"] and items_b = ["pen"],
    write two ifs: one that fires on equal CONTENTS and one that
    fires only when they are the SAME object.

Run: python 01_basics/equality.py
Answers: answers/01_basics.py
=====================================================================
"""

# ------------------------------------------------------------------
# TOPIC EXAMPLES
# ------------------------------------------------------------------

# == compares what is INSIDE, so copies of a list count as equal
list1 = [1, 2]
list2 = [1, 2]
print("list1 == list2:", list1 == list2)    # True  - same contents
print("list1 is list2:", list1 is list2)    # False - two objects

# is compares identity: one object with two names
alias = list1
print("alias is list1:", alias is list1)    # True

# The Python idiom for "is it nothing?" is `is None`
bookmarks = None
print("bookmarks is None:", bookmarks is None)

# == surprises worth knowing
print("1 == True:", 1 == True)              # True - bool IS a number
print("0 == False:", 0 == False)            # True - same reason
print('"1" == 1:', "1" == 1)                # False - str vs int
print('"a" == "a":', "a" == "a")            # True - str compares by value

# ------------------------------------------------------------------
# QUESTIONS - try them yourself, then check answers/01_basics.py
# ------------------------------------------------------------------
# Q1: Predict the output of:
#       print([1, 2] == [1, 2], [1, 2] is [1, 2])
# Q2: Concept: why `if x is None:` rather than `if x == None:`?
# Q3: Predict the output of:
#       print(1 == True, 0 == False, "1" == 1)
# Q4: Spot the bug: `if saved == None:` should detect "nothing
#     saved yet". Why is `is` the better choice?
# Q5: Write code: with items_a = ["pen"] and items_b = ["pen"],
#     print "same contents" when == is True and "same object"
#     only when `is` is True.

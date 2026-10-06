"""
Answers for 03_control_flow - try the questions first!
"""

# ------------------------------------------------------------------
# conditions.py
# ------------------------------------------------------------------

# Q1: Output is "True Hot".
# Why: 10 < 25 < 30 is a True chained comparison, and temp > 20
# picks the "Hot" branch of the conditional expression.
temp = 25
label = "Hot" if temp > 20 else "Cold"
print(10 < temp < 30, label)       # True Hot

# Q2: Bug: conditions are checked top to bottom, and 95 is >= 60,
# so the first branch wins and the elif is never reached.
# Why it works after the fix: put the most specific condition first.
score = 95
if score >= 90:
    grade = "Distinction"
elif score >= 60:
    grade = "Pass"
else:
    grade = "Fail"
print(grade)                       # Distinction

# Q3: A conditional expression returns the value in one line.
# Why: "0 if total >= 50 else 4.99" reads as the whole pricing rule.
def shipping_cost(total):
    return 0 if total >= 50 else 4.99

print(shipping_cost(75), shipping_cost(30))   # 0 4.99

# ------------------------------------------------------------------
# truthy_falsy.py
# ------------------------------------------------------------------

# Q1: Output is "True True False False".
# Why: "0" is a non-empty string and [0] is a non-empty list (both
# truthy); "" and set() are empty (both falsy).
print(bool("0"), bool([0]), bool(""), bool(set()))

# Q2: Falsy: 0.0, {}, None.
# Why: "False" is a non-empty string and [""] is a non-empty list,
# so both are truthy despite looking like "nothing".
for value in ["False", 0.0, [""], {}, None]:
    print(repr(value), bool(value))

# Q3: Bug: 0 is a falsy value, so "if items_left:" treats a real
# zero as "nothing to show" and skips the print.
# Why the fix works: "is not None" asks "do we have a value at all".
items_left = 0
if items_left is not None:
    print(f"{items_left} items left")          # 0 items left

# Q4: An empty cart is falsy, so truthiness replaces a length check.
# Why: "if cart:" is True only when the cart has at least one item.
def first_item(cart):
    if cart:
        return cart[0]
    return "Cart is empty"

print(first_item(["apple"]))       # apple
print(first_item([]))              # Cart is empty

# ------------------------------------------------------------------
# loops.py
# ------------------------------------------------------------------

# Q1: Output is "7".
# Why: range(1, 5) gives 1, 2, 3, 4; continue skips 3, so
# 1 + 2 + 4 = 7.
total = 0
for n in range(1, 5):
    if n == 3:
        continue
    total += n
print(total)                       # 7

# Q2: Bug: nothing inside the loop ever decreases count, so
# "count > 0" stays True forever (an infinite loop).
# Why the fix works: each pass moves the condition toward False.
count = 3
while count > 0:
    print(count)
    count -= 1                     # the missing line

# Q3: enumerate hands you the position and the dish together.
# Why: start=1 makes the numbering human-friendly (menus start at 1).
dishes = ["Pizza", "Salad", "Soup"]
for number, dish in enumerate(dishes, start=1):
    print(f"{number}. {dish}")

# Q4: range(5, 0, -1) produces 5 4 3 2 1.
# Why: it starts at 5, steps down by 1, and stops before reaching 0.
print(list(range(5, 0, -1)))       # [5, 4, 3, 2, 1]

# ------------------------------------------------------------------
# match.py
# ------------------------------------------------------------------

# Q1: Output is "small medium large".
# Why: 2 matches the or-pattern; 5 fails it but passes the guard
# n <= 6; 9 matches nothing except the wildcard.
def size(n):
    match n:
        case 1 | 2 | 3:
            return "small"
        case n if n <= 6:
            return "medium"
        case _:
            return "large"

print(size(2), size(5), size(9))   # small medium large

# Q2: Bug: "case OFF:" is a capture pattern -- a bare name matches
# ANY value, so the case grabs the first command and never compares.
# Why the fix works: a dotted name (attribute access) is treated as
# a value to compare against, so the match behaves as intended.
class Commands:
    OFF = "off"

command = "off"
match command:
    case Commands.OFF:             # dotted name -> real comparison
        print("Powering down")     # prints now

# Q3: The wildcard case _ is the catch-all for unknown commands.
# Why: match always picks the first matching case, so specific
# commands are handled above and everything else falls through.
def respond(command):
    match command:
        case "start":
            return "Running"
        case "stop":
            return "Stopped"
        case _:
            return "Unknown command"

print(respond("start"))            # Running
print(respond("stop"))             # Stopped
print(respond("dance"))            # Unknown command

# Q4: A bare name like "case mode:" is a capture pattern: it binds
# the matched value to that name and therefore matches everything.
# Why: only dotted names (Mode.OFF) or literals compare; to compare
# with a plain variable, use a guard such as "case m if m == mode:".
mode = "dark"
for candidate in ("dark", "light"):
    match candidate:
        case m if m == mode:       # guard compares, no capture trap
            print(f"{candidate} is the active mode")
        case _:
            print(f"{candidate} is not active")

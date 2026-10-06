"""
=====================================================================
TOPIC: Arguments
=====================================================================

SCENARIO
--------
Your hotel-booking app has one book_room() function, but calls come
from everywhere: a web form, a CLI, a test. Some callers pass every
option; most pass just a name. Python's argument kinds let one
function serve all of them without a pile of if-statements.

TOPIC
-----
Positional args match by order; keyword args match by name.
Defaults (`nights=1`) are created ONCE when the def line runs - so a
mutable default like [] is shared across every call. Classic bug!
*args packs extra positional args into a tuple, **kwargs packs extra
keyword args into a dict. Params after a bare * are keyword-only.

QUESTIONS
---------
Q1. Predict the output of the two order() calls.
Q2. Spot the bug in add_tag(): what does the second call print?
Q3. Predict what show(1, 2, x=3) prints.
Q4. Write summary(title, *points, shout=False) - details below.

Run: python 04_functions/arguments.py
Answers: answers/04_functions.py
=====================================================================
"""

# ------------------------------------------------------------------
# TOPIC EXAMPLES
# ------------------------------------------------------------------

def book_room(guest, nights=1, breakfast=False):
    plan = "breakfast included" if breakfast else "room only"
    return f"{guest}: {nights} night(s), {plan}"


print(book_room("Aisha", 3))               # positional: order matters
print(book_room(nights=2, guest="Ben"))    # keywords: any order works
print(book_room("Chen", breakfast=True))   # mix: positionals come first

# GOTCHA: a mutable default is built ONCE and shared by all calls.
def add_tag(tag, tags=[]):   # every call mutates the SAME list
    tags.append(tag)
    return tags


print(add_tag("urgent"))     # ['urgent']
print(add_tag("later"))      # ['urgent', 'later'] - surprise!

# *args: extra positional values arrive as a TUPLE.
def total(*prices):
    return sum(prices)


print(total(10, 20, 5))      # 35

# **kwargs: extra keyword values arrive as a DICT.
def profile(name, **details):
    print(name, details)


profile("Ravi", city="Pune", age=30)       # Ravi {'city': 'Pune', 'age': 30}

# A bare * makes later parameters keyword-only: callers MUST name them.
def retry(attempts=3, *, timeout=5):
    return f"{attempts} tries, timeout={timeout}s"


print(retry(timeout=10))     # retry(10) alone would be a TypeError

# ------------------------------------------------------------------
# QUESTIONS - try them yourself, then check answers/04_functions.py
# ------------------------------------------------------------------
# Q1: Predict the output:
#     def order(drink, size): return f"{size} {drink}"
#     print(order("latte", size="large"))
#     print(order(size="small", drink="tea"))
#
# Q2: The add_tag example above: what do its two prints show, and why
#     is the second one a bug? Fix it so each call starts fresh.
#
# Q3: Predict the output:
#     def show(*args, **kwargs): print(args, kwargs)
#     show(1, 2, x=3)
#
# Q4: Write summary(title, *points, shout=False) that returns the
#     title then each point on its own "- " line; if shout=True the
#     whole text is uppercased. shout may only be passed by keyword.

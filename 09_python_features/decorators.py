"""
=====================================================================
TOPIC: Decorators
=====================================================================

SCENARIO
--------
You keep copy-pasting the same "started / finished" log lines into a
dozen functions. A decorator lets you write that logging once and bolt
it onto any function with a single @ line.

TOPIC
-----
A decorator is a function that takes a function and returns a new one.
@my_decorator above `def` is shorthand for: func = my_decorator(func).
The inner wrapper(*args, **kwargs) passes any arguments straight through.
Always return the result inside the wrapper, and return the wrapper.
@functools.wraps(func) keeps the original name and docstring.
Gotcha: the decorator itself runs once, at definition time.

QUESTIONS
---------
Q1. Predict the output: a decorator that upper-cases a return value.
Q2. Concept check: what does @tag_star mean without the @ symbol?
Q3. Spot the bug: a decorated function that returns None.
Q4. Write code: a count_calls decorator that reports the call count.

Run: python 09_python_features/decorators.py
Answers: answers/09_python_features.py
=====================================================================
"""

# ------------------------------------------------------------------
# TOPIC EXAMPLES
# ------------------------------------------------------------------
import functools

def log_call(func):
    @functools.wraps(func)  # keeps func's name and docstring alive
    def wrapper(*args, **kwargs):
        print(f"-> calling {func.__name__}{args}")
        result = func(*args, **kwargs)
        print(f"<- {func.__name__} returned {result}")
        return result  # forget this and every caller gets None
    return wrapper

@log_call
def add(a, b):
    return a + b

print(add(2, 3))

def loud(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

@loud
def greet(name):
    return f"hi {name}"

print(greet("sam"))   # HI SAM

# ------------------------------------------------------------------
# QUESTIONS - try them yourself, then check answers/09_python_features.py
# ------------------------------------------------------------------
# Q1: Predict the output:
#         def shout(func):
#             def wrapper():
#                 return func().upper()
#             return wrapper
#         @shout
#         def greet():
#             return "hello"
#         print(greet())
#
# Q2: Rewrite this WITHOUT the @ syntax. Which single line of code
#     means the same thing as putting @tag_star above `def cheer():`?
#
# Q3: Spot the bug -- get_price() prints None instead of 20:
#         def double(func):
#             def wrapper(*args, **kwargs):
#                 func(*args, **kwargs) * 2
#             return wrapper
#         @double
#         def get_price():
#             return 10
#
# Q4: Write code: a count_calls decorator that, on every call, prints
#     how many times the decorated function has run so far.

"""
Answers for 09_python_features - try the questions first!
"""

import functools
import time
from contextlib import contextmanager

# ------------------------------------------------------------------
# iterators.py
# ------------------------------------------------------------------
# Q1: Prints "h" then "i", then StopIteration crashes -- strings iterate
#     one character at a time, and the third next() is one too many.
it = iter("hi")
print("iter Q1:", next(it), next(it))
try:
    next(it)
except StopIteration:
    print("iter Q1: StopIteration raised (caught here so the file runs)")

# Q2: A for loop calls iter() once, then next() repeatedly, and stops
#     silently when StopIteration appears. The manual version:
hidden = iter(["k", "e", "y"])
while True:
    try:
        print("iter Q2:", next(hidden))
    except StopIteration:
        break  # exactly where a for loop would stop

# Q3: An iterator is one-way: the first sum(it) consumed it, so the
#     second call sees an empty iterator and returns 0. Use iter(nums)
#     again, or simply call sum(nums) which makes a fresh one each time.
nums = [1, 2, 3]
print("iter Q3:", sum(nums), sum(nums))  # 6 6

# Q4: The protocol is: __iter__ returns the iterator (self) and
#     __next__ gives the next value or raises StopIteration.
class Countdown:
    def __init__(self, start):
        self.n = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.n == 0:
            raise StopIteration
        value = self.n
        self.n -= 1
        return value

print("iter Q4:", list(Countdown(3)))  # [3, 2, 1]

# ------------------------------------------------------------------
# generators.py
# ------------------------------------------------------------------
# Q1: "[1, 2]" then "[]" -- a generator is consumed once; the second
#     list() finds it already exhausted and empty.
def pair():
    yield 1
    yield 2

g = pair()
print("gen Q1:", list(g), list(g))

# Q2: Calling a generator function runs no body code -- it returns a
#     generator. The body starts at the first next() and pauses at each
#     yield, keeping its local variables until the next request.
def who():
    print("gen Q2: body only runs when iterated")
    yield 1

w = who()
print("gen Q2: created, nothing printed yet")
print("gen Q2:", next(w))  # now the body runs up to the yield

# Q3: `return i * 2` exits the function on the very first loop pass, so
#     only 0 ever comes out. Replace return with yield to emit a value
#     per iteration and keep looping.
def doubles(n):
    for i in range(n):
        yield i * 2  # fix: yield, not return

print("gen Q3:", list(doubles(3)))  # [0, 2, 4]

# Q4: Yield inside a loop produces one Fibonacci number per request.
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print("gen Q4:", list(fibonacci(7)))  # [0, 1, 1, 2, 3, 5, 8]

# ------------------------------------------------------------------
# decorators.py
# ------------------------------------------------------------------
# Q1: "HELLO" -- @shout replaces greet with wrapper, which calls the
#     original greet and upper-cases whatever it returns.
def shout(func):
    def wrapper():
        return func().upper()
    return wrapper

@shout
def greet():
    return "hello"

print("dec Q1:", greet())

# Q2: @tag_star above `def cheer():` is exactly cheer = tag_star(cheer):
#     pass the function in, store the wrapper back under the same name.
def tag_star(func):
    def wrapper(*args, **kwargs):
        return f"*{func(*args, **kwargs)}*"
    return wrapper

def cheer():
    return "go"

cheer = tag_star(cheer)  # the manual equivalent of @tag_star
print("dec Q2:", cheer())

# Q3: The wrapper computes func(...) * 2 but never returns it, so the
#     function falls off the end and returns None. Add `return`.
def double(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) * 2  # fix: return the result
    return wrapper

@double
def get_price():
    return 10

print("dec Q3:", get_price())  # 20

# Q4: Keep the count in the enclosing scope; bump it on every call.
def count_calls(func):
    calls = 0

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal calls
        calls += 1
        result = func(*args, **kwargs)
        print(f"dec Q4: {func.__name__} called {calls} time(s)")
        return result

    return wrapper

@count_calls
def ping():
    return "pong"

ping()
ping()

# ------------------------------------------------------------------
# context_managers.py
# ------------------------------------------------------------------
# Q1: "<b>", "bold text", "</b>" -- setup runs on entering, the with
#     body runs at the yield, cleanup runs on leaving.
@contextmanager
def tag(name):
    print(f"<{name}>")
    yield
    print(f"</{name}>")

with tag("b"):
    print("bold text")

# Q2: __exit__ runs even when the block raises, so the file can never
#     stay open and leak resources; a manual close() is skipped on any
#     error path.
print("cm Q2: with guarantees cleanup even when errors happen")

# Q3: The lines are swapped. Everything BEFORE the yield is setup (runs
#     when entering); everything AFTER is cleanup (runs when leaving).
@contextmanager
def tracker_fixed():
    print("start")  # setup goes before the yield
    yield
    print("done")   # cleanup goes after the yield

with tracker_fixed():
    print("  work")

# Q4: __enter__ saves the start time and returns self; __exit__ always
#     runs, so the elapsed time prints even if the block crashes.
class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc, tb):
        elapsed = time.perf_counter() - self.start
        print(f"cm Q4: block took {elapsed:.4f}s")
        return False  # never hide exceptions

with Timer():
    total = sum(range(200_000))
    print(f"cm Q4: summed to {total}")

"""
10_python_features / iterators.py
Topic: The Iterator Protocol in Python vs JavaScript

JAVASCRIPT vs PYTHON ITERATOR PROTOCOL:
---------------------------------------
JavaScript:
    - An iterable implements `[Symbol.iterator]()`.
    - Returns an iterator with a `.next()` method.
    - `.next()` returns `{ value: any, done: boolean }`.

Python:
    - An iterable implements `__iter__()`.
    - Returns an iterator object that implements `__next__()`.
    - `__next__()` returns the next item directly.
    - When exhausted, `__next__()` raises the `StopIteration` exception!
"""

# ------------------------------------------------------------------------------
# 1. Built-in iter() and next()
# ------------------------------------------------------------------------------
# JS: const iterator = items[Symbol.iterator](); iterator.next();
fruits = ["apple", "banana", "cherry"]
fruit_iterator = iter(fruits)

print(next(fruit_iterator))  # "apple"
print(next(fruit_iterator))  # "banana"
print(next(fruit_iterator))  # "cherry"
# next(fruit_iterator)       # Raises StopIteration exception!


# ------------------------------------------------------------------------------
# 2. Building a Custom Iterator Class
# ------------------------------------------------------------------------------
class StepCounter:
    """Iterator that steps from `start` to `stop` by `step` amount."""
    def __init__(self, start: int, stop: int, step: int = 1):
        self.current = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        # Must return the iterator object itself
        return self

    def __next__(self) -> int:
        if self.current >= self.stop:
            # Signal termination (equivalent to `{ done: true }` in JS)
            raise StopIteration
        val = self.current
        self.current += self.step
        return val

print("\nCustom StepCounter Iterator:")
for n in StepCounter(start=10, stop=50, step=10):
    print(n, end=" ")
print()

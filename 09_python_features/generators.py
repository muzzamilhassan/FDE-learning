"""
=====================================================================
TOPIC: Generators
=====================================================================

SCENARIO
--------
Your sensor app collects thousands of readings per hour. Holding them
all in a list eats memory, so instead you write a generator that hands
you one reading at a time, exactly when you ask for it.

TOPIC
-----
A function containing `yield` is a generator function.
Calling it runs NO body code -- it just returns a generator object.
Each next() runs the body until the next yield, then pauses there,
remembering all local variables for next time.
Lazy and memory friendly: values appear one at a time, never stored.
Gotcha: a generator can be consumed only ONCE; after that it is empty.

QUESTIONS
---------
Q1. Predict the output: list(g) called twice on the same generator.
Q2. Concept check: why does nothing run when you call it?
Q3. Spot the bug: a function that returns only its first result.
Q4. Write code: a fibonacci(n) generator.

Run: python 09_python_features/generators.py
Answers: answers/09_python_features.py
=====================================================================
"""

# ------------------------------------------------------------------
# TOPIC EXAMPLES
# ------------------------------------------------------------------

def count_up(limit):
    n = 1
    while n <= limit:
        yield n  # pause here, hand out n, resume when asked again
        n += 1

gen = count_up(3)
print(next(gen))   # 1 -- the body starts at the first next()
print(next(gen))   # 2 -- resumes right after the last yield
print(list(gen))   # [3] -- whatever is left of THIS generator

# Generators shine for big or endless data: nothing exists until asked
def even_squares(max_n):
    for n in range(max_n):
        if n % 2 == 0:
            yield n * n

print(list(even_squares(6)))  # [0, 4, 16]

# A generator expression looks like a list comprehension but stays
# lazy: parentheses instead of square brackets.
squares = (n * n for n in range(4))
print(sum(squares))  # 14 -- created one at a time, never stored

# ------------------------------------------------------------------
# QUESTIONS - try them yourself, then check answers/09_python_features.py
# ------------------------------------------------------------------
# Q1: Predict the output:
#         def pair():
#             yield 1
#             yield 2
#         g = pair()
#         print(list(g))
#         print(list(g))
#
# Q2: Why does calling pair() not run the body? When does the body
#     actually start, and where does it pause between values?
#
# Q3: Spot the bug -- doubles(3) should give [0, 2, 4] but gives only 0:
#         def doubles(n):
#             for i in range(n):
#                 return i * 2
#
# Q4: Write code: a fibonacci(n) generator yielding the first n
#     Fibonacci numbers, so list(fibonacci(7)) == [0, 1, 1, 2, 3, 5, 8].

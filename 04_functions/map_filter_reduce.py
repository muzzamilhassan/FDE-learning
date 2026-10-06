"""
=====================================================================
TOPIC: map, filter, reduce
=====================================================================

SCENARIO
--------
Your orders report receives raw rows: amounts as strings, plus a few
negatives from refunds that went wrong. You need to convert, clean,
then total them - a classic data pipeline. map, filter, and reduce
are the three building blocks designed for exactly this.

TOPIC
-----
map(fn, it) applies fn to every item; filter(fn, it) keeps items
where fn is truthy. Both return LAZY iterators: wrap in list() to
see contents, and they are used up after a single pass.
functools.reduce(fn, it, initializer) folds everything to one value.
A comprehension is often cleaner - learn all three, then choose.

QUESTIONS
---------
Q1. Predict the output of the list(map(...)) call.
Q2. Spot the bug: why is the second list(totals) empty?
Q3. Build a pipeline: convert strings to ints, keep >= 10, then sum.
Q4. Rewrite a map+filter chain as one comprehension.

Run: python 04_functions/map_filter_reduce.py
Answers: answers/04_functions.py
=====================================================================
"""

# ------------------------------------------------------------------
# TOPIC EXAMPLES
# ------------------------------------------------------------------
from functools import reduce

raw = ["12", "7", "30", "5"]

# map: apply one function to every item (here: str -> int).
amounts = list(map(int, raw))
print(amounts)                     # [12, 7, 30, 5]

# filter: keep items where the function returns something truthy.
big = list(filter(lambda a: a >= 10, amounts))
print(big)                         # [12, 30]

# map is LAZY: one pass only, then the iterator is spent.
lazy = map(lambda n: n * 2, [1, 2, 3])
print(list(lazy))                  # [2, 4, 6]
print(list(lazy))                  # [] - already consumed!

# reduce folds a sequence down to ONE value, left to right.
# The initializer is the starting accumulator (start at 1 for products).
product = reduce(lambda acc, n: acc * n, [1, 2, 3, 4], 1)
print(product)                     # 24

# Often a built-in or a comprehension says the same thing more clearly.
print(sum([1, 2, 3, 4]))                   # instead of reduce
print([n * 2 for n in [1, 2, 3]])          # instead of map
print([n for n in amounts if n >= 10])     # instead of filter

# ------------------------------------------------------------------
# QUESTIONS - try them yourself, then check answers/04_functions.py
# ------------------------------------------------------------------
# Q1: Predict the output:
#     nums = [1, 2, 3, 4]
#     print(list(map(lambda n: n * n, nums)))
#
# Q2: What does each line print, and why is the last one empty?
#     totals = map(lambda n: n + 1, [10, 20])
#     print(list(totals))
#     print(list(totals))
#
# Q3: Given raw = ["3", "15", "8", "22", "10"], use map to convert to
#     ints, filter to keep values >= 10, then sum() the result.
#     (Expected total: 47.)
#
# Q4: Rewrite this chain as ONE comprehension:
#     list(map(lambda n: n * 3, filter(lambda n: n % 2 == 0, nums)))
#     Which version would you rather read in six months?

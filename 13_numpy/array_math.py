"""
=====================================================================
TOPIC: NumPy Math - Vectorization, Broadcasting, and Dot Products
=====================================================================

SCENARIO
--------
Time to compute a model's output. A single neuron calculates
z = w.x + b from a feature vector, and a real layer repeats that
for thousands of samples at once. Doing that with Python loops is
painfully slow; NumPy applies math to whole arrays in one shot.

TOPIC
-----
- Arithmetic (+ - * / **) works ELEMENTWISE: shapes must match, or
  one side must be broadcastable (see below).
- Loops over arrays are slow; whole-array expressions are vectorized
  and run in compiled code -- often 10-100x faster.
- Broadcasting stretches sizes of 1 to match: array + scalar, or a
  (3, 1) column plus a (1, 4) row gives a (3, 4) result.
- Aggregations take an axis: axis=0 collapses ROWS (one result per
  column), axis=1 collapses COLUMNS (one result per row).
- w @ x is the dot product: multiply pairwise, then sum -- exactly
  what a neuron does with its weights and inputs.
- A plain np.mean returns np.nan if ANY value is nan; use
  np.nanmean / np.nansum to skip missing values.

QUESTIONS
---------
Q1. Predict the printed matrix and its shape:
    np.arange(3).reshape(3, 1) + np.arange(3)
Q2. Spot the bug: np.mean(daily_sales) prints nan on real data
    with one missing value. Why, and what is the fix?
Q3. Write code: for weights w = [0.4, -0.2, 0.7], bias b = 0.1 and
    the (4, 3) matrix X from array_basics, compute every sample's
    neuron output z = X @ w + b, then apply ReLU (max(z, 0)).
Q4. Predict both results for a (2, 3) array X:
    X.sum(axis=0) and X.sum(axis=1).

Run: python 13_numpy/array_math.py
Answers: answers/13_numpy.py
=====================================================================
"""

import time

import numpy as np

# ------------------------------------------------------------------
# TOPIC EXAMPLES
# ------------------------------------------------------------------

# Elementwise: the operation hits every cell, no loop needed.
prices = np.array([10.0, 20.0, 30.0])
quantities = np.array([2, 1, 4])
print("totals :", prices * quantities)        # [20. 20. 120.]

# Vectorized vs loop: the SAME 100k-element job, two styles.
big = np.arange(100_000, dtype=np.float64)
start = time.perf_counter()
slow = [x * 2 + 1 for x in big]               # Python loop
loop_time = time.perf_counter() - start
start = time.perf_counter()
fast = big * 2 + 1                            # one array expression
vec_time = time.perf_counter() - start
print(f"loop {loop_time * 1000:.1f} ms vs vectorized "
      f"{vec_time * 1000:.2f} ms "
      f"(~{loop_time / max(vec_time, 1e-9):.0f}x faster)")
print("both give the same result:", np.array_equal(slow, fast))

# Broadcasting: a scalar reaches every cell...
print("shifted:", prices + 5)                 # each price + 5
# ...and a (3, 1) column + a (1, 3) row stretch both to (3, 3).
col = np.array([[10], [20], [30]])            # shape (3, 1)
row = np.array([1, 2, 3])                     # shape (3,)
print("col + row:\n", col + row)              # cell (i, j) = col_i + row_j

# Classic AI use: normalize features so each column has mean 0.
X = np.array([[850.0, 2.0, 15.0],
              [1200.0, 3.0, 8.0],
              [950.0, 2.0, 40.0]])
print("column means:", X.mean(axis=0))        # one mean per FEATURE
print("centered:\n", X - X.mean(axis=0))      # subtracted per column

# axis=0 collapses rows -> per-column stats; axis=1 -> per-row stats.
print("sum axis=0:", X.sum(axis=0))           # one total per feature
print("sum axis=1:", X.sum(axis=1))           # one total per sample
print("max axis=0:", X.max(axis=0), "| max axis=1:", X.max(axis=1))

# The dot product w @ x multiplies pairwise and sums -- exactly what
# a neuron does with its weights and inputs. Raw features are huge,
# so z is huge too; models normalize inputs first (see above).
w = np.array([0.5, -1.0, 2.0])
b = 0.1
z = w @ X[0] + b                              # one sample -> one output
print("z for sample 0:", round(z, 2))

# @ also works on a whole batch: (3 samples, 3 features) @
# (3 features, 2 neurons) -> (3 samples, 2 neurons), in one line.
W = np.array([[0.5, -1.0], [-1.0, 0.5], [2.0, 1.0]])
print("all samples x 2 neurons:\n", X @ W + b)

# Real data has holes: one nan poisons a normal aggregation.
sales = np.array([120.0, np.nan, 90.0, 140.0])
print("mean   :", np.mean(sales))             # nan -- nan infects it
print("nanmean:", np.nanmean(sales))          # skips the missing day

# ------------------------------------------------------------------
# QUESTIONS - try them yourself, then check answers/13_numpy.py
# ------------------------------------------------------------------
# Q1: Predict the printed matrix AND its shape, and explain how the
#     two operands were stretched:
#     print(np.arange(3).reshape(3, 1) + np.arange(3))
#
# Q2: np.mean(daily_sales) prints nan because one day is np.nan.
#     Why does one missing value ruin the whole mean, and which
#     function fixes it?
#
# Q3: Write code: with w = np.array([0.4, -0.2, 0.7]), b = 0.1, and
#     a (4, 3) feature matrix X, compute every sample's neuron
#     output z = X @ w + b, then apply ReLU: np.maximum(z, 0).
#
# Q4: Predict both outputs for X = [[1, 2, 3], [4, 5, 6]]:
#     X.sum(axis=0) and X.sum(axis=1). Which axis gives one number
#     per feature?

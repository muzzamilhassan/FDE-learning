"""
=====================================================================
TOPIC: NumPy Array Basics - The Data Structure Behind AI
=====================================================================

SCENARIO
--------
You just received a tiny dataset: 4 houses, each described by 3
numbers (size, bedrooms, age). A model wants this as ONE table of
numbers where rows are samples and columns are features. NumPy's
ndarray is that table -- it is the input format nearly every AI
library expects, and one array can hold millions of samples.

TOPIC
-----
- An ndarray is a grid of numbers with ONE dtype; operating on the
  whole grid runs in compiled C-speed loops, not per-item Python.
- np.array([[...], [...]]) builds a 2-D array from nested lists
  (inner lists = rows, and every row must have the same length).
- Inspect with .shape (rows, cols), .ndim, and .dtype.
- Index and slice per axis: a[row, col], a[:2], a[:, 1].
- Boolean masks filter data: a[a > 0.5] keeps the True cells; use a
  row mask like X[X[:, 0] > 1000] to keep whole rows.
- .reshape() changes the shape, not the data; -1 means "infer this
  dimension so the element count fits".
- np.arange, np.linspace, np.zeros, np.ones generate arrays fast.
- Gotcha: a[0] on a 2-D array is a VIEW of the row, not a copy --
  editing it edits the original array too.

QUESTIONS
---------
Q1. Predict: X.shape, X.ndim, X.dtype for X built from
    [[1, 2, 3], [4, 5, 6]].
Q2. Spot the bug: row = X[0]; row[0] = 999 -- what happened to X?
Q3. Write code: from a (4, 3) feature matrix, keep only the rows
    whose age column (column 2) is greater than 10.
Q4. Predict: X[:, 0] for a (2, 3) array, and the shape of
    np.arange(6).reshape(3, -1).

Run: python 13_numpy/array_basics.py
Answers: answers/13_numpy.py
=====================================================================
"""

import numpy as np

# ------------------------------------------------------------------
# TOPIC EXAMPLES
# ------------------------------------------------------------------

# One array does the work of thousands of Python-level number boxes,
# which is why AI code passes arrays around instead of nested lists.
X = np.array([[850, 2, 15], [1200, 3, 8],      # rows = samples
              [950, 2, 40], [1400, 4, 5]])     # cols = features

# The three "what am I holding?" attributes you check first.
print("X:\n", X)
print("shape:", X.shape)     # (4, 3) -> 4 samples, 3 features
print("ndim  :", X.ndim)     # 2 -> a 2-D grid
print("dtype :", X.dtype)    # int64 -> every cell is a 64-bit int

# Indexing: one index picks a ROW, [row, col] picks a single cell.
print("first sample :", X[0])        # [850  2 15]
print("last sample  :", X[-1])       # negative counts from the end
print("first age    :", X[0, 2])     # row 0, column 2 -> 15

# Slicing: [start:stop] per axis, stop excluded; : means "all of it".
print("size column  :", X[:, 0])     # every row, column 0
print("first 2 rows, last 2 cols:\n", X[:2, 1:])

# Boolean masks: compare the whole array at once to get True/False,
# then use the mask to filter. This is how you clean and slice data.
scores = np.array([0.2, 0.9, 0.5, 0.7])
print("mask        :", scores > 0.5)
print("kept values :", scores[scores > 0.5])   # only the True cells
big = X[X[:, 0] > 1000]     # keep ROWS where the size feature > 1000
print("rows matching mask:\n", big)

# reshape: same numbers, new shape. -1 = "infer this dimension".
six = np.arange(6)                  # [0 1 2 3 4 5]
print("as (2, 3) grid:\n", six.reshape(2, 3))
print("as (3, 2) grid:\n", six.reshape(3, -1))   # -1 -> 2 automatically
col = six.reshape(-1, 1)            # (-1, 1) = one value per row
print("column vector shape:", col.shape)        # (6, 1)

# Common generators for quick data and placeholders.
print("arange :", np.arange(0, 10, 2))        # like range(): step 2
print("linspace:", np.linspace(0, 1, 5))      # 5 evenly spaced points
print("zeros  :\n", np.zeros((2, 3)))         # placeholder grid of 0.0
print("ones   :", np.ones(4))                 # placeholder row of 1.0

# ------------------------------------------------------------------
# QUESTIONS - try them yourself, then check answers/13_numpy.py
# ------------------------------------------------------------------
# Q1: Predict the output (and explain WHY each value is what it is):
#     X = np.array([[1, 2, 3], [4, 5, 6]])
#     print(X.shape, X.ndim, X.dtype)
#
# Q2: A teammate ran this and their dataset changed. What went wrong?
#     row = X[0]
#     row[0] = 999      # X is now different -- why?
#
# Q3: Write code: using the (4, 3) matrix X above (size, bedrooms,
#     age), create `older` containing only the rows where the age
#     column is greater than 10.
#
# Q4: Predict the output / shape:
#     X = np.array([[1, 2, 3], [4, 5, 6]])
#     print(X[:, 0])
#     print(np.arange(6).reshape(3, -1).shape)

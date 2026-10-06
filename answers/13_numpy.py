"""
Answers for 13_numpy - try the questions first!

Every answer below is runnable code, so you can execute this file
and see each output for yourself.
"""

import numpy as np

# ------------------------------------------------------------------
# array_basics.py
# ------------------------------------------------------------------
# Q1: (2, 3) 2 int64. Two inner lists = 2 rows, each with 3 numbers
#     = (2, 3); a table has ndim 2; whole numbers default to int64.
X = np.array([[1, 2, 3], [4, 5, 6]])
print("basics Q1 ->", X.shape, X.ndim, X.dtype)

# Q2: X[0] returns a VIEW of the row, not a copy, so writing to
#     `row` writes straight into X. Use .copy() when you want an
#     independent array.
X = np.array([[1, 2, 3], [4, 5, 6]])
row = X[0].copy()          # the fix: copy() breaks the link
row[0] = 999
print("basics Q2 -> X untouched:", X.tolist(), "| row:", row)

# Q3: Build the mask on the age COLUMN (X[:, 2]) and use it to keep
#     whole rows -- houses with ages 15 and 40 survive.
X = np.array([
    [850, 2, 15],
    [1200, 3, 8],
    [950, 2, 40],
    [1400, 4, 5],
])
older = X[X[:, 2] > 10]
print("basics Q3 ->\n", older)

# Q4: [1 4] -- ': ' takes every row, ', 0' takes column 0 only.
#     (3, 2) -- six values reshaped into 3 rows means 2 columns, so
#     -1 is inferred as 2.
X = np.array([[1, 2, 3], [4, 5, 6]])
print("basics Q4 ->", X[:, 0], "|", np.arange(6).reshape(3, -1).shape)
# -> [1 4] | (3, 2)

# ------------------------------------------------------------------
# array_math.py
# ------------------------------------------------------------------
# Q1: [[0 1 2] [1 2 3] [2 3 4]], shape (3, 3). The (3, 1) column is
#     stretched across 3 columns and the (3,) row down 3 rows, so
#     each cell gets col_i + row_j.
print("math Q1 ->\n", np.arange(3).reshape(3, 1) + np.arange(3))

# Q2: nan + anything is nan, so ONE missing value poisons the total
#     and the mean comes out nan. np.nanmean ignores nan values.
daily_sales = np.array([120.0, np.nan, 90.0, 140.0])
print("math Q2 ->", np.mean(daily_sales), "vs", np.nanmean(daily_sales))
# -> nan vs 116.66...

# Q3: X @ w multiplies each sample's 3 features by the 3 weights and
#     sums (a dot product per row), + b shifts, np.maximum(z, 0) is
#     ReLU. All outputs happen to be positive here, so ReLU keeps
#     every value unchanged.
X = np.array([
    [850, 2, 15],
    [1200, 3, 8],
    [950, 2, 40],
    [1400, 4, 5],
])
w = np.array([0.4, -0.2, 0.7])
b = 0.1
z = X @ w + b
relu = np.maximum(z, 0)
print("math Q3 -> z:", np.round(z, 1), "| relu:", np.round(relu, 1))
# -> [350.2 485.1 407.7 562.8] for both

# Q4: axis=0 -> [5 7 9] (one number per COLUMN/feature, rows
#     collapsed); axis=1 -> [ 6 15] (one number per row/sample).
#     axis=0 is the one that gives one number per feature.
X = np.array([[1, 2, 3], [4, 5, 6]])
print("math Q4 ->", X.sum(axis=0), "|", X.sum(axis=1))

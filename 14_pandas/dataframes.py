"""
=====================================================================
TOPIC: DataFrames - Loading and Exploring Data
=====================================================================

SCENARIO
--------
You just joined the data team at a cafe chain. The app exports every
order to a CSV, and before anyone trains a model or builds a report,
somebody has to actually look at the data. That somebody is you.

TOPIC
-----
A Series is one labeled column; a DataFrame is a table of Series.
pd.DataFrame(dict_of_lists) builds a table; pd.read_csv(path) is how
real data arrives. First-look ritual: .head(), .info(), .describe().
df["col"] -> Series; df[["a", "b"]] -> DataFrame (double brackets!).
Filter rows with a boolean mask: df[df["price"] > 4]. Combine masks
with & and | -- each condition needs its own parentheses.

QUESTIONS
---------
Q1. Predict the output: the type of df["drink"] vs df[["drink"]].
Q2. Spot the bug: combining two filters with `and` crashes. Why, and what are the two fixes?
Q3. Write code: print the large (size "L") orders that took at most 6 minutes, showing drink, price and minutes.
Q4. Write code: print how many orders each drink received, most popular first.

Run: python 14_pandas/dataframes.py
Answers: answers/14_pandas.py
=====================================================================
"""

# ------------------------------------------------------------------
# TOPIC EXAMPLES
# ------------------------------------------------------------------
from pathlib import Path

import pandas as pd

# Every run regenerates its own data, so the lesson is self-contained.
DEMO_DIR = Path(__file__).parent / "demo_data"
DEMO_DIR.mkdir(exist_ok=True)
CSV_PATH = DEMO_DIR / "cafe_orders.csv"

# Series = ONE labeled column; DataFrame = a table of such columns.
print(pd.Series({"Mon": 32, "Tue": 41, "Wed": 38}))              # 1-D
print(pd.DataFrame({"drink": ["latte", "mocha"],
                    "price": [4.50, 5.50]}))                     # 2-D

# Build a small CSV once, then read it back the way real data arrives.
orders = pd.DataFrame({
    "order_id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    "drink": ["latte", "latte", "espresso", "cappuccino", "latte",
              "mocha", "espresso", "cappuccino", "latte", "mocha",
              "flat_white", "espresso"],
    "size": ["M", "L", "S", "M", "M", "L", "S", "L", "L", "M", "M", "M"],
    "price": [4.50, 5.00, 2.50, 4.00, 4.50, 5.50, 2.50, 4.75, 5.00, 5.00, 4.25, 3.00],
    "minutes": [4, 5, 2, 4, 6, 7, 1, 5, 8, 6, 3, 2],
})
orders.to_csv(CSV_PATH, index=False)  # index=False: no extra unnamed column
df = pd.read_csv(CSV_PATH)  # the usual first line of any data script

# The first-look ritual: rows that look right, then types, then stats.
print("--- head ---")
print(df.head(3))       # eye check: did the columns land as expected?
print("--- info ---")
df.info()               # row count, dtypes, missing values per column
print("--- describe ---")
print(df.describe())    # count/mean/std/quartiles of numeric columns

# One column is a Series (it keeps its name); two or more is a DataFrame.
print("--- selecting columns ---")
print(type(df["drink"]).__name__,             # Series
      type(df[["drink", "price"]]).__name__)  # DataFrame: [[column list]]

# Filtering: a comparison makes a boolean mask; df[mask] keeps True rows.
print(df[df["price"] > 4.5][["drink", "price"]])

# Combine masks with & / |. Parentheses are REQUIRED: & binds tighter
# than >, so without them Python parses nonsense.
busy = df[(df["price"] > 4.5) & (df["minutes"] >= 5)]
print("--- pricey AND slow ---")
print(busy[["drink", "size", "price", "minutes"]])

# value_counts: how often does each value appear? An instant report.
print("--- value_counts ---")
print(df["size"].value_counts())

# ------------------------------------------------------------------
# QUESTIONS - try them yourself, then check answers/14_pandas.py
# ------------------------------------------------------------------
# Q1: Using `df` from the examples, predict the output:
#         print(type(df["drink"]).__name__)
#         print(type(df[["drink"]]).__name__)
#
# Q2: Spot the bug -- this line raises an error. What does Python
#     complain about, and which two fixes does it need?
#         df[df["price"] > 4.5 and df["size"] == "L"]
#
# Q3: Write code: print the large (size "L") orders that took at most
#     6 minutes, showing only drink, price and minutes.
#
# Q4: Write code: print how many orders each drink received, most
#     popular first.

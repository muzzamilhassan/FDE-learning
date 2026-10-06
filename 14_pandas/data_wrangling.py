"""
=====================================================================
TOPIC: Data Wrangling - From Messy Export to Report
=====================================================================

SCENARIO
--------
The app team sends over their "final" sales export. Of course it is
messy: cryptic column names, empty cells where the logging pipeline
hiccuped, and no totals. Your job: clean it up and hand back a
per-drink revenue report the team can actually open.

TOPIC
-----
df.isna().sum() counts missing values per column -- always look first.
fillna(value) fills gaps; dropna() deletes rows; both return NEW objects.
Gotcha: neither changes df by itself -- you must assign the result back!
Derived column: df["revenue"] = df["qty"] * df["price"] (row-wise math).
groupby("col").agg(name=("other", "func")) averages/counts per group.
sort_values("col", ascending=False); pass lists to sort by several keys.

QUESTIONS
---------
Q1. Predict the output: what does isna().sum() print for a frame with gaps?
Q2. Spot the bug: df["minutes"].fillna(0) runs fine, but nothing changes. Why?
Q3. Write code: print the average revenue per cup size, biggest first.
Q4. Write code: save the report to CSV so the item names survive as a real column.

Run: python 14_pandas/data_wrangling.py
Answers: answers/14_pandas.py
=====================================================================
"""

# ------------------------------------------------------------------
# TOPIC EXAMPLES
# ------------------------------------------------------------------
from pathlib import Path

import pandas as pd

DEMO_DIR = Path(__file__).parent / "demo_data"
DEMO_DIR.mkdir(exist_ok=True)

# The "messy export": ugly names and empty cells (read back as NaN).
RAW_PATH = DEMO_DIR / "app_export.csv"
pd.DataFrame({
    "item": ["latte", "latte", "espresso", "cappuccino", "latte", "mocha",
             "espresso", "cappuccino", "latte", "mocha", "flat white", "espresso"],
    "cup_size": ["M", "L", "S", "M", "M", "L", "S", "L", "L", "M", "M", "M"],
    "qty": [2, 1, 1, 1, 1, 2, 1, 1, 3, 1, 1, 1],
    "unit_price": [4.5, 5.0, 2.5, 4.0, None, 5.5, 2.5, 4.75, 5.0, 5.0, 4.25, 3.0],
    "prep_min": [4, None, 2, 4, 6, 7, None, 5, 8, 6, None, 2],
}).to_csv(RAW_PATH, index=False)
df = pd.read_csv(RAW_PATH)

# Step 1: look before you clean -- missing count per column, at a glance.
print("--- missing values ---")
print(df.isna().sum())

# Step 2: friendly names (rename also returns a NEW frame).
df = df.rename(columns={"cup_size": "size", "unit_price": "price",
                        "prep_min": "minutes"})

# Step 3: "missing" means different things per column. No price -> the
# row can never become revenue, drop it. No prep time -> just guess it
# with the median.
df = df.dropna(subset=["price"])
df["minutes"] = df["minutes"].fillna(df["minutes"].median())

# Step 4: a derived column -- the math runs on whole columns at once.
df["revenue"] = df["qty"] * df["price"]

# Step 5: named aggregation -- name=("col", "func") reads like a
# sentence instead of a pile of same-named columns.
report = df.groupby("item").agg(
    orders=("item", "count"), cups=("qty", "sum"), revenue=("revenue", "sum"),
)
print("--- per-drink report ---")
print(report)

# sort_values: one key (revenue high-low), or lists of keys (size
# A-Z, then revenue high-low within each size).
report = report.sort_values("revenue", ascending=False)
print(report.head(3))
by_size = df.sort_values(["size", "revenue"], ascending=[True, False])
print(by_size[["size", "item", "revenue"]].head(5))

# Step 6: save the report. groupby() parked the item names in the
# INDEX, so reset_index() must promote them back to a real column
# before index=False -- or the CSV would hold numbers but no names.
OUT_PATH = DEMO_DIR / "drink_report.csv"
report.reset_index().to_csv(OUT_PATH, index=False)

# ------------------------------------------------------------------
# QUESTIONS - try them yourself, then check answers/14_pandas.py
# ------------------------------------------------------------------
# Q1: Predict the output:
#         x = pd.DataFrame({"a": [1, None], "b": [None, None]})
#         print(x.isna().sum())
#
# Q2: Spot the bug -- the export had gaps in prep_min, but this fix
#     silently does nothing. What is missing?
#         df["minutes"].fillna(0)
#
# Q3: Write code: using `df` from the examples (it has a revenue
#     column), print the average revenue per cup size, biggest first.
#
# Q4: Write code: save the report DataFrame to "drink_report.csv" so
#     the item names come back as a real column when reopened.

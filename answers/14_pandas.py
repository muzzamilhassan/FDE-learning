"""
Answers for 14_pandas - try the questions first!
"""

import tempfile
from pathlib import Path

import pandas as pd

# ------------------------------------------------------------------
# dataframes.py
# ------------------------------------------------------------------

# The same 12-row cafe dataset the lesson generates on each run.
df = pd.DataFrame({
    "order_id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    "drink": ["latte", "latte", "espresso", "cappuccino", "latte", "mocha",
              "espresso", "cappuccino", "latte", "mocha", "flat_white", "espresso"],
    "size": ["M", "L", "S", "M", "M", "L", "S", "L", "L", "M", "M", "M"],
    "price": [4.50, 5.00, 2.50, 4.00, 4.50, 5.50, 2.50, 4.75, 5.00, 5.00, 4.25, 3.00],
    "minutes": [4, 5, 2, 4, 6, 7, 1, 5, 8, 6, 3, 2],
})

# Q1: "Series" then "DataFrame". One bracket pair asks for ONE column
#     (a Series); the inner [...] is a LIST of columns, so pandas
#     builds a DataFrame even when the list holds a single name.
print("dataframes Q1:", type(df["drink"]).__name__,
      "/", type(df[["drink"]]).__name__)  # Series / DataFrame

# Q2: `and` calls bool() on a whole Series, and "is this Series true?"
#     is ambiguous -> ValueError. Two fixes: use the element-wise &
#     operator, and wrap EACH condition in parentheses (it matters).
try:
    df[df["price"] > 4.5 and df["size"] == "L"]
except ValueError as err:
    print("dataframes Q2:", type(err).__name__, "->", str(err).splitlines()[0][:55])

fixed = df[(df["price"] > 4.5) & (df["size"] == "L")]
print("dataframes Q2 fixed rows:", len(fixed))  # 4: every large cup over 4.50

# Q3: Build the mask, then index the frame AND the column list with it.
#     Result: orders 2 (latte, 5.00) and 8 (cappuccino, 4.75).
slow_larges = df[(df["size"] == "L") & (df["minutes"] <= 6)]
print("dataframes Q3:")
print(slow_larges[["drink", "price", "minutes"]])

# Q4: value_counts() counts each distinct value, sorted most common
#     first. latte 4, espresso 3, mocha 2, cappuccino 2, flat_white 1.
print("dataframes Q4:")
print(df["drink"].value_counts())

# ------------------------------------------------------------------
# data_wrangling.py
# ------------------------------------------------------------------

# Q1: a    1 / b    2 (with "dtype: int64"). isna() makes a boolean
#     frame and sum() counts the True values down each column, giving
#     back a Series indexed by column name.
x = pd.DataFrame({"a": [1, None], "b": [None, None]})
print("wrangling Q1:")
print(x.isna().sum())

# Q2: fillna() RETURNS a new Series and never edits the original --
#     the cleaned copy was thrown away. Assign it back to the column.
y = pd.DataFrame({"minutes": [4.0, None, 6.0]})
y["minutes"].fillna(0)  # the bug: result not stored
print("wrangling Q2 before fix, still missing:", y["minutes"].isna().sum())  # 1
y["minutes"] = y["minutes"].fillna(0)  # fix: assign the result back
print("wrangling Q2 after fix, missing:", y["minutes"].isna().sum())  # 0

# Q3: groupby splits by size, ["revenue"].mean() averages each group's
#     revenue, sort_values(ascending=False) puts the biggest cup first.
z = pd.DataFrame({
    "size": ["M", "L", "M", "L", "M"],
    "revenue": [9.0, 5.0, 4.5, 16.5, 5.0],
})
print("wrangling Q3:")
print(z.groupby("size")["revenue"].mean().sort_values(ascending=False))

# Q4: After a groupby, the item names live in the INDEX, not in a
#     column -- so reset_index() must promote them back before
#     index=False, or the CSV would hold numbers but no item names.
with tempfile.TemporaryDirectory() as tmp:
    out = Path(tmp) / "drink_report.csv"
    report = pd.DataFrame({"orders": [4, 3], "revenue": [29.0, 13.0]},
                          index=pd.Index(["latte", "espresso"], name="item"))
    report.reset_index().to_csv(out, index=False)
    saved = pd.read_csv(out)
    print("wrangling Q4 columns:", list(saved.columns))  # item, orders, revenue

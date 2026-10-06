"""
=====================================================================
PROJECT: Data Explorer  (Difficulty: intermediate)
=====================================================================

SCENARIO
--------
You are the first data hire at "Bean There", a small cafe chain.
Management exported 200 cafe orders to a CSV that nobody has looked
at -- and of course some customer ratings were never recorded. They
want a repeatable script that checks data quality, cleans it up, and
answers five concrete business questions, ending with a small summary
CSV the team can open in a spreadsheet.

WHAT YOU WILL PRACTICE
----------------------
- pd.read_csv and the first-look ritual: .head()/.info()/.describe() (module 14)
- Counting missing values with .isna().sum() (module 14)
- Filling missing values with .fillna(median) (module 14)
- Creating a new column from other columns (module 14)
- groupby(...) + sum/mean, .nlargest and sorting (module 14)
- Saving a result with .to_csv (module 14)
- Module 15 flavor: turning a fuzzy business question into ONE number

YOUR TASKS
----------
1. load_cafe_data(): read the CSV, parsing `date` as real dates.
2. first_look(df): print .head(), .info() and .describe(). Do this
   ritual EVERY time you meet a new dataset -- no exceptions.
3. missing_report(df): count missing values per column; print only
   the columns that actually have some.
4. clean_ratings(df): return a COPY with missing ratings filled by
   the median rating. (Think: why the median and not the mean?)
5. add_revenue(df): add a revenue column = quantity * unit_price.
6. revenue_by_category(df): total revenue per category, biggest first.
7. top_products(df, n=3): the n products with the highest total revenue.
8. answer_questions(df): print one-line answers to the cafe's five
   questions (listed in its docstring) and save the per-category
   totals to sample_data/revenue_summary.csv.
   Stretch: which weekday earns the most, and is it a big deal?

STARTER CODE
------------
Complete the TODOs below. Run with:
    python 99_projects/project_06_data_explorer.py

The dataset is generated for you on first run
(99_projects/sample_data/cafe_orders.csv) and reused afterwards.
Hints are inline. A full solution is in answers/projects/.
=====================================================================
"""

from __future__ import annotations

import random
from datetime import date, timedelta
from pathlib import Path

import pandas as pd

SAMPLE_DIR = Path(__file__).parent / "sample_data"
DATA_FILE = SAMPLE_DIR / "cafe_orders.csv"
SUMMARY_FILE = SAMPLE_DIR / "revenue_summary.csv"

MENU: list[tuple[str, str, float]] = [
    ("Latte", "drinks", 4.50),
    ("Cappuccino", "drinks", 4.00),
    ("Flat White", "drinks", 4.25),
    ("Chai Tea", "drinks", 3.75),
    ("Blueberry Muffin", "bakery", 3.25),
    ("Butter Croissant", "bakery", 3.50),
    ("Chocolate Cookie", "bakery", 2.75),
    ("Cinnamon Bagel", "bakery", 3.00),
]


def generate_cafe_data(rows: int = 200, path: Path = DATA_FILE) -> None:
    """Done for you: create a messy-but-realistic cafe_orders.csv once.

    Later runs reuse the same file. customer_rating is left empty on
    roughly 10% of rows, just like a real cafe export.
    """
    if path.exists():
        print(f"  {path.name} already exists -- reusing it.")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    rng = random.Random(42)  # seeded, so everyone gets the same data
    lines = ["order_id,date,product,category,quantity,unit_price,"
             "customer_rating"]
    for order_id in range(1, rows + 1):
        product, category, price = rng.choice(MENU)
        day = date.today() - timedelta(days=rng.randint(0, 89))
        rating = "" if rng.random() < 0.10 else f"{rng.uniform(3.0, 5.0):.1f}"
        lines.append(
            f"{order_id},{day.isoformat()},{product},{category},"
            f"{rng.randint(1, 4)},{price:.2f},{rating}"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"  Generated {rows} rows in {path}.")


# ------------------------------------------------------------------
# TODOs -- everything below is yours
# ------------------------------------------------------------------

def load_cafe_data(path: Path = DATA_FILE) -> pd.DataFrame:
    """TODO 1: return the DataFrame from pd.read_csv(path, parse_dates=["date"]).

    parse_dates turns the date strings into real datetimes so that
    .dt.day_name() works later. One line is enough.
    """
    print("TODO: implement load_cafe_data()")
    return pd.DataFrame()


def first_look(df: pd.DataFrame) -> None:
    """TODO 2: print df.head(), then df.info(), then df.describe().

    Ask yourself at each step: how many rows? which columns exist?
    what are the dtypes? any suspicious min/max already?
    """
    print("TODO: implement first_look()")


def missing_report(df: pd.DataFrame) -> pd.Series:
    """TODO 3: count missing values per column.

    report = df.isna().sum()          # one count per column
    print only the columns with report > 0 (a boolean mask selects them).
    Return the full report.
    """
    print("TODO: implement missing_report()")
    return pd.Series(dtype=int)


def clean_ratings(df: pd.DataFrame) -> pd.DataFrame:
    """TODO 4: return a COPY with missing ratings filled by the median.

    median = df["customer_rating"].median()   # skips NaN for you
    then .fillna(median) and assign it back -- on a copy, never the
    caller's original. Bonus thought: why is the median safer than
    the mean when a few customers left angry 1-star ratings?
    """
    print("TODO: implement clean_ratings()")
    return df.copy()


def add_revenue(df: pd.DataFrame) -> pd.DataFrame:
    """TODO 5: on a copy, add column `revenue` = quantity * unit_price."""
    print("TODO: implement add_revenue()")
    return df.copy()


def revenue_by_category(df: pd.DataFrame) -> pd.Series:
    """TODO 6: total revenue per category, biggest first.

    Hint: df.groupby("category")["revenue"].sum().sort_values(ascending=False)
    """
    print("TODO: implement revenue_by_category()")
    return pd.Series(dtype=float)


def top_products(df: pd.DataFrame, n: int = 3) -> pd.Series:
    """TODO 7: group by product, sum revenue, keep the top n with .nlargest."""
    print("TODO: implement top_products()")
    return pd.Series(dtype=float)


def answer_questions(df: pd.DataFrame) -> None:
    """TODO 8: print a short one-line answer to each question:

    Q1. Which category earns more: drinks or bakery?
    Q2. Which 3 products bring in the most revenue? (use top_products)
    Q3. What is the average customer rating per category (after cleaning)?
    Q4. Which weekday has the highest total revenue?
        Hint: df["date"].dt.day_name() gives you a grouping column.
    Q5. What share of total revenue comes from orders of 3+ items?
        Hint: a boolean mask filters, mask.mean() gives a share.

    Then save revenue_by_category(df) to SUMMARY_FILE. Hint: a groupby
    result keeps its group names in the INDEX, so write it with
    by_cat.reset_index().to_csv(SUMMARY_FILE, index=False) -- otherwise
    the category names silently vanish from the CSV.
    """
    print("TODO: implement answer_questions()")


def main() -> None:
    print("=" * 58)
    print("  DATA EXPLORER -- starter")
    print("  Fill in the TODOs to answer the cafe's five questions.")
    print("=" * 58)

    print("\nStep 0: sample data")
    generate_cafe_data()

    print("\nStep 1: load + first look")
    df = load_cafe_data()
    if df.empty:
        print("  df is empty -- implement load_cafe_data(), then rerun.")
        return
    first_look(df)

    print("\nStep 2: data quality")
    missing_report(df)
    df = clean_ratings(df)

    print("\nStep 3: revenue math")
    df = add_revenue(df)
    if "revenue" in df.columns:
        print(f"  total revenue: {df['revenue'].sum():,.2f}")
    else:
        print("  (implement add_revenue() to see the total)")

    print("\nStep 4: the five answers")
    answer_questions(df)

    print("\nHappy exploring!")


if __name__ == "__main__":
    main()

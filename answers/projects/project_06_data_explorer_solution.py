"""
Solution for Project 06 - Data Explorer (pandas capstone-lite).

Run it with:
    python answers/projects/project_06_data_explorer_solution.py

On the first run it generates 99_projects/sample_data/cafe_orders.csv
(200 rows, ~10% of ratings missing); later runs reuse that file, so
answers are identical every time. It walks the first-look ritual,
cleans the ratings, computes revenue, prints answers to the cafe's
five business questions and saves revenue_summary.csv.
"""

from __future__ import annotations

import random
from datetime import date, timedelta
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[2]  # answers/projects/ -> repo root
SAMPLE_DIR = ROOT / "99_projects" / "sample_data"
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
    """Create the sample CSV once; later runs keep the same data."""
    if path.exists():
        print(f"  {path.name} already exists -- reusing it.")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    rng = random.Random(42)
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


def load_cafe_data(path: Path = DATA_FILE) -> pd.DataFrame:
    """Task 1: read the CSV; parse_dates gives real datetimes."""
    return pd.read_csv(path, parse_dates=["date"])


def first_look(df: pd.DataFrame) -> None:
    """Task 2: the ritual -- never skip it."""
    print("\n  --- head() ---")
    print(df.head().to_string(index=False))
    print("\n  --- info() ---")
    df.info()
    print("\n  --- describe() ---")
    print(df.describe().round(2).to_string())


def missing_report(df: pd.DataFrame) -> pd.Series:
    """Task 3: count NaNs per column; show only the dirty ones."""
    report = df.isna().sum()
    holes = report[report > 0]
    if holes.empty:
        print("  no missing values -- suspiciously clean data")
    else:
        print("  missing values per column:")
        for column, count in holes.items():
            share = count / len(df) * 100
            print(f"    {column:<16} {count:>3}  ({share:.1f}% of rows)")
    return report


def clean_ratings(df: pd.DataFrame) -> pd.DataFrame:
    """Task 4: fill missing ratings with the median, on a copy.

    Median, not mean: one angry 3.0 when everyone else is 4.5-5.0
    drags the mean but barely moves the median.
    """
    cleaned = df.copy()
    median = cleaned["customer_rating"].median()
    filled = int(cleaned["customer_rating"].isna().sum())
    cleaned["customer_rating"] = cleaned["customer_rating"].fillna(median)
    print(f"  filled {filled} missing ratings with the median ({median:.2f}).")
    print("  (median: robust to the odd harsh rating, unlike the mean.)")
    return cleaned


def add_revenue(df: pd.DataFrame) -> pd.DataFrame:
    """Task 5: revenue = quantity * unit_price, as a new column."""
    result = df.copy()
    result["revenue"] = result["quantity"] * result["unit_price"]
    return result


def revenue_by_category(df: pd.DataFrame) -> pd.Series:
    """Task 6: groupby + sum, biggest first."""
    return df.groupby("category")["revenue"].sum().sort_values(ascending=False)


def top_products(df: pd.DataFrame, n: int = 3) -> pd.Series:
    """Task 7: products ranked by total revenue."""
    return df.groupby("product")["revenue"].sum().nlargest(n)


def answer_questions(df: pd.DataFrame) -> None:
    """Task 8: the cafe's five questions, one printed answer each."""
    by_cat = revenue_by_category(df)
    winner = by_cat.idxmax()
    loser = by_cat.drop(winner).index[0]

    print(f"\n  Q1. Which category earns more?")
    print(f"      {winner.capitalize()} ({by_cat[winner]:,.2f}) beat "
          f"{loser} ({by_cat[loser]:,.2f}).")

    print("\n  Q2. Top 3 products by revenue:")
    for product, revenue in top_products(df).items():
        print(f"      {product:<18} {revenue:>9,.2f}")

    print("\n  Q3. Average customer rating per category:")
    for category, rating in df.groupby("category")["customer_rating"].mean().items():
        print(f"      {category:<10} {rating:.2f} / 5.0")

    by_day = df.groupby(df["date"].dt.day_name())["revenue"].sum()
    print(f"\n  Q4. Best weekday: {by_day.idxmax()} "
          f"({by_day.max():,.2f} total revenue).")

    total = df["revenue"].sum()
    big = df.loc[df["quantity"] >= 3, "revenue"].sum()
    print(f"\n  Q5. Orders of 3+ items: {big:,.2f} of {total:,.2f} "
          f"= {big / total:.1%} of revenue.")

    # groupby keeps the group names in the INDEX: reset_index() promotes
    # them to a real column, otherwise index=False would drop them.
    by_cat.reset_index().to_csv(SUMMARY_FILE, index=False)
    print(f"\n  Summary saved to {SUMMARY_FILE}")


def main() -> None:
    print("DATA EXPLORER -- solution")

    print("\nStep 0: sample data")
    generate_cafe_data()

    print("\nStep 1: load + first look")
    df = load_cafe_data()
    print(f"  loaded {len(df)} rows x {len(df.columns)} columns")
    first_look(df)

    print("\nStep 2: data quality")
    missing_report(df)
    df = clean_ratings(df)

    print("\nStep 3: revenue math")
    df = add_revenue(df)
    print(f"  total revenue: {df['revenue'].sum():,.2f} "
          f"across {df['order_id'].nunique()} orders")

    print("\nStep 4: the cafe's five questions")
    answer_questions(df)

    print("\nDone -- run it again: the CSV is reused, the answers match.")


if __name__ == "__main__":
    main()

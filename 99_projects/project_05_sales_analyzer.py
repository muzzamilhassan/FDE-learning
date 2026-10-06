"""
=====================================================================
PROJECT: Sales Data Analyzer  (Difficulty: capstone)
=====================================================================

SCENARIO
--------
You just joined a two-person online shop as "the data person". The
orders live in a plain CSV export and the founders want answers on
one screen: how much did we sell, which category carries the shop,
what is our best product, and what were the biggest single orders?
On the very first run your program even creates realistic sample
data, so the tool works out of the box.

WHAT YOU WILL PRACTICE
----------------------
- CSV reading and writing (from module 08)
- Comprehensions and sorting with key= (from module 02)
- Generators for lazy row-by-row reading (from module 09)
- Context managers: with open(...) (from module 09)
- Writing a decorator (from module 09)
- collections.Counter and defaultdict (module 02/09 territory)
- Type hints and a dataclass (from module 11)
- Bonus: asyncio.gather (from module 10)

YOUR TASKS
----------
1. Give the Sale dataclass its five fields (date, product, category,
   quantity, unit_price) and a @property revenue -> quantity *
   unit_price.
2. Turn timing() into a real decorator that prints how long the
   function took (time.perf_counter() before and after).
3. generate_csv(): skip when the file exists; otherwise create the
   folder and, inside `with path.open(...)`, write a header plus 50
   random rows (products from PRODUCTS, dates in the last 60 days).
4. read_sales(): a GENERATOR that yields one Sale per CSV row -- one
   row in memory at a time, file opened with `with`.
5. total_revenue(sales): one sum() over a generator expression.
6. revenue_by_category(sales): a defaultdict(float) turned into a
   dict sorted by amount (biggest first).
7. best_selling_product(sales): a Counter of units per product and
   most_common(1).
8. top_sales(sales, n=3): sorted(...) with key=, sliced to the top n.
   And average_order_value(sales): total / count (guard against an
   empty list).
9. Stretch: finish print_report() so the numbers look like a report,
   and check out the asyncio.gather bonus in the solution.

STARTER CODE
------------
Run with:
    python 99_projects/project_05_sales_analyzer.py

The data file is created at sample_data/ next to this script.
A full solution is in answers/projects/.
=====================================================================
"""

from __future__ import annotations

import csv
import random
import time
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path
from typing import Iterator
# (every import above becomes useful as you complete the TODOs)

DATA_DIR = Path(__file__).parent / "sample_data"
SALES_FILE = DATA_DIR / "sales.csv"

PRODUCTS: list[tuple[str, str, float]] = [
    ("Laptop", "electronics", 999.00),
    ("Headphones", "electronics", 149.50),
    ("Desk Chair", "furniture", 175.00),
    ("Bookshelf", "furniture", 89.99),
    ("Notebook", "stationery", 3.50),
    ("Fancy Pen", "stationery", 12.25),
    ("Coffee Mug", "kitchen", 9.99),
    ("French Press", "kitchen", 42.00),
]


def timing(func):
    """
    TODO 2: a decorator. Inside, define wrapper(*args, **kwargs) that
    notes time.perf_counter(), calls func, prints
        f"[timing] {func.__name__}: {elapsed:.4f}s"
    and returns the result. Then `return wrapper`.
    (For now it is a pass-through so the file runs.)
    """
    return func


@dataclass
class Sale:
    """One row of the sales file."""
    # TODO 1: add the five fields with type hints:
    #   date: str, product: str, category: str, quantity: int, unit_price: float

    @property
    def revenue(self) -> float:
        """TODO 1: quantity * unit_price"""
        print("TODO: implement Sale.revenue")
        return 0.0


def generate_csv(rows: int = 50, path: Path = SALES_FILE) -> None:
    """
    TODO 3:
    1. if path.exists(): print "reusing existing file" and return
    2. path.parent.mkdir(parents=True, exist_ok=True)
    3. inside `with path.open("w", newline="", encoding="utf-8") as f:`
       write the header row, then `rows` random rows:
       product/category/price = random.choice(PRODUCTS),
       day = date.today() - timedelta(days=random.randint(0, 59)),
       quantity = random.randint(1, 5), price formatted "%.2f"
    """
    print("TODO: implement generate_csv()")


def read_sales(path: Path = SALES_FILE) -> Iterator[Sale]:
    """
    TODO 4: a GENERATOR. Open the file with `with`, use csv.DictReader,
    and `yield Sale(...)` for every row (cast quantity to int and
    unit_price to float). Lazy: one row in memory at a time.
    """
    print("TODO: implement read_sales()")
    return
    yield  # unreachable -- it just makes this function a generator


@timing
def total_revenue(sales: list[Sale]) -> float:
    """TODO 5: sum(sale.revenue for sale in sales)"""
    print("TODO: implement total_revenue()")
    return 0.0


@timing
def revenue_by_category(sales: list[Sale]) -> dict[str, float]:
    """
    TODO 6: totals = defaultdict(float); add sale.revenue per category;
    return dict(sorted(totals.items(), key=lambda item: item[1],
                       reverse=True))
    """
    print("TODO: implement revenue_by_category()")
    return {}


@timing
def best_selling_product(sales: list[Sale]) -> tuple[str, int]:
    """
    TODO 7: units = Counter(); units[sale.product] += sale.quantity;
    return units.most_common(1)[0]  ->  (product, units_sold)
    """
    print("TODO: implement best_selling_product()")
    return ("nobody", 0)


@timing
def top_sales(sales: list[Sale], n: int = 3) -> list[Sale]:
    """TODO 8: the n sales with the biggest revenue."""
    print("TODO: implement top_sales()")
    return []


@timing
def average_order_value(sales: list[Sale]) -> float:
    """TODO 8: total revenue / number of sales (return 0.0 when empty)."""
    print("TODO: implement average_order_value()")
    return 0.0


def print_report(sales: list[Sale]) -> None:
    """
    Stretch: print a tidy report. Suggested layout:
      rows analyzed / total revenue / average order value, then
      revenue by category (with a % share), the best-selling product
      and the top 3 sales.
    """
    print("TODO: implement print_report()")


def main():
    print("=" * 52)
    print("  SALES DATA ANALYZER -- starter")
    print("  Fill in the TODOs to turn this into a real report.")
    print("=" * 52)
    print("(Note: timing() is still a pass-through -- that is task 2.)")

    print("\nStep 1: data file")
    generate_csv()

    print("\nStep 2: reading rows")
    sales = list(read_sales())  # a generator can be walked only once:
    print(f"  Loaded {len(sales)} row(s).")  # collect it into a list.

    print("\nStep 3: the numbers")
    print(f"  total revenue       : {total_revenue(sales)}")
    print(f"  revenue by category : {revenue_by_category(sales)}")
    print(f"  best-selling product: {best_selling_product(sales)}")
    print(f"  top 3 sales         : {top_sales(sales)}")
    print(f"  average order value : {average_order_value(sales)}")

    print("\nStep 4: the report")
    print_report(sales)

    print("\nHappy analyzing!")


if __name__ == "__main__":
    main()

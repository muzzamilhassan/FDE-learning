"""
Solution for Project 05 - Sales Data Analyzer (capstone).

Run it with:
    python answers/projects/project_05_sales_analyzer_solution.py

On the first run it generates 99_projects/sample_data/sales.csv
(50 rows); later runs reuse that file. Then it prints a small
report: total revenue, revenue per category, best-selling product,
top 3 sales and the average order value -- plus a bonus section
that fetches pretend exchange rates concurrently with asyncio.gather.
"""

from __future__ import annotations

import asyncio
import csv
import random
import time
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path
from typing import Iterator

ROOT = Path(__file__).resolve().parents[2]  # answers/projects/ -> repo root
DATA_DIR = ROOT / "99_projects" / "sample_data"
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
    """Decorator that reports how long the call took."""
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"  [timing] {func.__name__}: {elapsed:.4f}s")
        return result
    return wrapper


@dataclass
class Sale:
    """One row of the sales file."""
    date: str
    product: str
    category: str
    quantity: int
    unit_price: float

    @property
    def revenue(self) -> float:
        return self.quantity * self.unit_price


def generate_csv(rows: int = 50, path: Path = SALES_FILE) -> None:
    """Create the sample CSV once; later runs keep the same data."""
    if path.exists():
        print(f"  {path.name} already exists -- reusing it.")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    today = date.today()
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["date", "product", "category", "quantity",
                         "unit_price"])
        for _ in range(rows):
            product, category, price = random.choice(PRODUCTS)
            day = today - timedelta(days=random.randint(0, 59))
            writer.writerow([
                day.isoformat(),
                product,
                category,
                random.randint(1, 5),
                f"{price:.2f}",
            ])
    print(f"  Generated {rows} rows in {path}.")


def read_sales(path: Path = SALES_FILE) -> Iterator[Sale]:
    """Lazy generator: yield one Sale at a time, never the whole file."""
    with path.open("r", newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            yield Sale(
                date=row["date"],
                product=row["product"],
                category=row["category"],
                quantity=int(row["quantity"]),
                unit_price=float(row["unit_price"]),
            )


@timing
def total_revenue(sales: list[Sale]) -> float:
    return sum(sale.revenue for sale in sales)


@timing
def revenue_by_category(sales: list[Sale]) -> dict[str, float]:
    totals: defaultdict[str, float] = defaultdict(float)
    for sale in sales:
        totals[sale.category] += sale.revenue
    return dict(sorted(totals.items(), key=lambda item: item[1], reverse=True))


@timing
def best_selling_product(sales: list[Sale]) -> tuple[str, int]:
    units: Counter[str] = Counter()
    for sale in sales:
        units[sale.product] += sale.quantity
    return units.most_common(1)[0]  # -> (product, units sold)


@timing
def top_sales(sales: list[Sale], n: int = 3) -> list[Sale]:
    return sorted(sales, key=lambda sale: sale.revenue, reverse=True)[:n]


@timing
def average_order_value(sales: list[Sale]) -> float:
    if not sales:
        return 0.0
    return sum(sale.revenue for sale in sales) / len(sales)


# ---------------------------------------------------------------- bonus --
async def fetch_rate(currency: str, rate: float, delay: float):
    """Pretend to call a slow exchange-rate API."""
    await asyncio.sleep(delay)
    return currency, rate


async def currency_board(total: float) -> list[tuple[str, float]]:
    """Fetch three 'APIs' at the same time with asyncio.gather."""
    rates = await asyncio.gather(
        fetch_rate("EUR", 0.92, 0.05),
        fetch_rate("GBP", 0.79, 0.03),
        fetch_rate("JPY", 155.0, 0.04),
    )
    return [(currency, total * rate) for currency, rate in rates]


# ----------------------------------------------------------------- main --
def print_report(sales: list[Sale]) -> None:
    revenue = total_revenue(sales)
    best_product, best_units = best_selling_product(sales)

    print("=" * 54)
    print("                SALES REPORT")
    print("=" * 54)
    print(f"  Rows analyzed      : {len(sales)}")
    print(f"  Total revenue      : ${revenue:,.2f}")
    print(f"  Average order value: ${average_order_value(sales):,.2f}")

    print("\n  Revenue by category:")
    for category, amount in revenue_by_category(sales).items():
        share = amount / revenue * 100 if revenue else 0.0
        bar = "#" * int(share // 5)
        print(f"    {category:<12} ${amount:>9,.2f}  {share:5.1f}% {bar}")

    print(f"\n  Best-selling product: {best_product} ({best_units} units)")

    print("\n  Top 3 biggest sales:")
    for sale in top_sales(sales):
        print(f"    {sale.date}  {sale.product:<12} x{sale.quantity}"
              f"   ${sale.revenue:,.2f}")


def main() -> None:
    print("SALES ANALYZER -- solution")

    print("\nStep 1: data file")
    generate_csv()

    print("\nStep 2: reading rows lazily")
    started = time.perf_counter()
    sales = list(read_sales())  # a generator can be walked only once
    print(f"  Loaded {len(sales)} rows in "
          f"{time.perf_counter() - started:.4f}s.")
    if not sales:
        print(f"  No data at {SALES_FILE} -- delete it and rerun.")
        return

    print("\nStep 3: the report")
    print_report(sales)

    print("\nBonus: exchange rates fetched concurrently (asyncio.gather)")
    revenue = total_revenue(sales)
    for currency, amount in asyncio.run(currency_board(revenue)):
        print(f"    {revenue:>12,.2f} USD = {amount:>13,.2f} {currency}")


if __name__ == "__main__":
    main()

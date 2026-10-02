import csv
from pathlib import Path

# Built-in csv module in Python
csv_path = Path("data.csv")

# Writing CSV using DictWriter
data = [{"name": "Alice", "role": "Dev"}, {"name": "Bob", "role": "Designer"}]
with open(csv_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "role"])
    writer.writeheader()
    writer.writerows(data)

# Reading CSV using DictReader
with open(csv_path, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"User: {row['name']} -> {row['role']}")

# Clean up
if csv_path.exists():
    csv_path.unlink()

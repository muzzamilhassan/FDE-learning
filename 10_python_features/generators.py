"""
10_python_features / generators.py
Topic: Generators and the `yield` Keyword

JAVASCRIPT vs PYTHON GENERATORS:
--------------------------------
JavaScript:
    function* idMaker() {
        let index = 0;
        while (true) {
            yield index++;
        }
    }
    const gen = idMaker();
    gen.next().value; // 0

Python:
    def id_maker():
        index = 0
        while True:
            yield index
            index += 1

    gen = id_maker()
    next(gen) # 0

WHY GENERATORS ARE A GAME CHANGER:
- Memory Efficiency: They generate items LAZILY on-demand one by one.
- Processing a 10 GB log file? A list loads all 10 GB into RAM (crash!).
  A generator streams line by line using negligible memory (~a few KB).
"""

# ------------------------------------------------------------------------------
# 1. Fibonacci Generator
# ------------------------------------------------------------------------------
def fibonacci_stream(max_count: int):
    """Generates Fibonacci numbers lazily up to max_count."""
    a, b = 0, 1
    count = 0
    while count < max_count:
        yield a
        a, b = b, a + b
        count += 1

print("Fibonacci first 7 numbers:")
for num in fibonacci_stream(7):
    print(num, end=" ")
print()


# ------------------------------------------------------------------------------
# 2. Infinite Stream Generator
# ------------------------------------------------------------------------------
def generate_order_ids(prefix="ORD"):
    order_num = 1001
    while True:
        yield f"{prefix}-{order_num}"
        order_num += 1

order_gen = generate_order_ids()

# Grabbing individual items with next():
print("\nGenerated IDs on demand:")
print(next(order_gen))
print(next(order_gen))
print(next(order_gen))

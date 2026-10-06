"""
Answers for 04_functions - try the questions first!

Scroll to a topic section, compare with your attempt, then tweak and
re-run until every output makes sense.
"""

# ------------------------------------------------------------------
# functions.py
# ------------------------------------------------------------------
# Q1: "B" - classify(85) fails the first check (85 < 90), passes the
# second (85 >= 80), and `return` exits before "C" is ever reached.
def classify(score):
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    return "C"


print("functions Q1:", classify(85))          # B

# Q2: double() only PRINTS; with no return it hands back None, and
# None * 10 raises TypeError. Fix: return the value instead.
def double(n):
    return n * 2


print("functions Q2:", double(4) * 10)        # 80

# Q3: return both values as a tuple, then unpack in one line.
def min_max(numbers):
    return min(numbers), max(numbers)


smallest, largest = min_max([4, 11, 7, 2])
print("functions Q3:", smallest, largest)     # 2 11

# Q4: "12 3 4.0" - the tuple (12, 3) unpacks into total and count,
# and 12 / 3 is true division, so the result is the float 4.0.

# ------------------------------------------------------------------
# arguments.py
# ------------------------------------------------------------------
# Q1: "large latte" then "small tea". Positionals match by order;
# keywords match by NAME, so even swapped order lines up correctly.
def order(drink, size):
    return f"{size} {drink}"


print("arguments Q1:", order("latte", size="large"),
      "|", order(size="small", drink="tea"))

# Q2: ['urgent'] then ['urgent', 'later']. The default list is created
# ONCE when the def line runs, so every call mutates the same list.
# Fix: default to None and build a fresh list inside the function.
def add_tag(tag, tags=None):
    if tags is None:
        tags = []
    tags.append(tag)
    return tags


print("arguments Q2:", add_tag("urgent"), add_tag("later"))

# Q3: "(1, 2) {'x': 3}" - *args collects into a tuple,
# **kwargs collects into a dict.
def show(*args, **kwargs):
    print("arguments Q3:", args, kwargs)


show(1, 2, x=3)

# Q4: *points gathers any number of bullets; the bare * before shout
# makes it keyword-only, so callers must write shout=True.
def summary(title, *points, shout=False):
    text = title + "\n" + "\n".join(f"- {p}" for p in points)
    return text.upper() if shout else text


print("arguments Q4:")
print(summary("Sprint notes", "shipped login", "fixed nav", shout=True))

# ------------------------------------------------------------------
# lambda.py
# ------------------------------------------------------------------
# Q1: ['fig', 'pear', 'banana'] - sorted by length 3, 4, 6.
words = ["banana", "fig", "pear"]
print("lambda Q1:", sorted(words, key=lambda w: len(w)))

# Q2: dicts have no < ordering, so sorting them directly crashes.
# Give sorted a key so it compares the "age" values instead.
users = [{"name": "Ann", "age": 30}, {"name": "Bo", "age": 25}]
print("lambda Q2:", [u["name"] for u in sorted(users, key=lambda u: u["age"])])

# Q3: key= works in sorted and max alike; the lambda picks the field.
products = [
    {"name": "pen", "price": 3},
    {"name": "bag", "price": 25},
    {"name": "cup", "price": 9},
]
cheapest_first = [p["name"] for p in sorted(products, key=lambda p: p["price"])]
priciest = max(products, key=lambda p: p["price"])["name"]
print("lambda Q3:", cheapest_first, "/", priciest)   # pen, cup, bag / bag

# Q4: "15 6" - lambdas take defaults like def does: add(5) uses b=10,
# the second call overrides it with b=1.
add = lambda a, b=10: a + b
print("lambda Q4:", add(5), add(5, b=1))

# ------------------------------------------------------------------
# map_filter_reduce.py
# ------------------------------------------------------------------
# Q1: [1, 4, 9, 16] - map squares every item, list() collects them.
nums = [1, 2, 3, 4]
print("map_filter_reduce Q1:", list(map(lambda n: n * n, nums)))

# Q2: first call [11, 21]; second []. A map object is a lazy
# one-pass iterator: after the first list() it is exhausted.
totals = map(lambda n: n + 1, [10, 20])
print("map_filter_reduce Q2:", list(totals), list(totals))

# Q3: chain the steps; sum() is the friendlier reduce for totals.
raw = ["3", "15", "8", "22", "10"]
amounts = map(int, raw)
big = filter(lambda a: a >= 10, amounts)
print("map_filter_reduce Q3:", sum(big))      # 47

# Q4: [n * 3 for n in nums if n % 2 == 0] - same job, no lambdas,
# far easier to read. Prefer comprehensions for transform+filter;
# reach for reduce only when no built-in like sum() or max() fits.
print("map_filter_reduce Q4:", [n * 3 for n in nums if n % 2 == 0])

# ------------------------------------------------------------------
# comprehensions.py
# ------------------------------------------------------------------
# Q1: [1, 9, 25] - odd numbers 1, 3, 5 pass the filter, then square.
nums = [1, 2, 3, 4, 5]
print("comprehensions Q1:", [n * n for n in nums if n % 2 == 1])

# Q2: n.upper (no parentheses) references the method without CALLING
# it, so the list fills with method objects. Add the () - n.upper().
names = ["ada", "bo"]
caps = [n.upper() for n in names]
print("comprehensions Q2:", caps)             # ['ADA', 'BO']

# Q3: loop over the tuples, keep score >= 60, build name -> score.
scores = [("ada", 90), ("bo", 55), ("cy", 72)]
passed = {name: score for name, score in scores if score >= 60}
print("comprehensions Q3:", passed)           # {'ada': 90, 'cy': 72}

# Q4: {'a', 'b'} - sets keep one copy of each letter (the repeated
# 'bee' still adds just one 'b'). Sets are unordered, so never rely
# on their print order.
words = ["ant", "bee", "ape", "bee"]
print("comprehensions Q4:", {w[0] for w in words})

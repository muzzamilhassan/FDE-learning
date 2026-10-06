"""
Answers for 02_collections - try the questions first!

Every answer below is runnable code, so you can execute this file
and see each output for yourself.
"""

# ------------------------------------------------------------------
# lists.py
# ------------------------------------------------------------------
# Q1: 4. append() adds the WHOLE list [4, 5] as ONE item, so nums
#     becomes [1, 2, 3, [4, 5]]. Use extend() to add each item.
nums = [1, 2, 3]
nums.append([4, 5])
print("lists Q1 ->", len(nums), nums)

# Q2: It prints None. .sort() reorders the list IN PLACE and returns
#     None. Call sorted(numbers) when you want a new sorted copy.
numbers = [3, 1, 2]
result = numbers.sort()
print("lists Q2 ->", result, numbers)

# Q3: sorted(scores, reverse=True) builds a new descending list
#     without touching the original, then [:3] keeps the top three.
scores = [88, 45, 92, 67, 74]
top3 = sorted(scores, reverse=True)[:3]
print("lists Q3 ->", top3, "(scores unchanged:", scores, ")")

# Q4: [2:] drops the first two items, [-3:] keeps the last three,
#     and [::2] takes every second item starting at index 0.
letters = ["a", "b", "c", "d", "e", "f"]
print("lists Q4 ->", letters[2:], "|", letters[-3:], "|", letters[::2])
# -> ['c', 'd', 'e', 'f'] | ['d', 'e', 'f'] | ['a', 'c', 'e']

# ------------------------------------------------------------------
# tuples.py
# ------------------------------------------------------------------
# Q1: <class 'int'> then <class 'tuple'>. The comma makes the tuple;
#     without it the parentheses are just grouping around the number.
print("tuples Q1 ->", type((5)), type((5,)))

# Q2: TypeError: 'tuple' object does not support item assignment.
#     Tuples are immutable - build a NEW tuple instead.
coords = (10, 20)
coords = (99,) + coords[1:]
print("tuples Q2 ->", coords)

# Q3: Returning two values packs them into a tuple; unpacking in the
#     call pulls them straight back apart.
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([4, 11, 7, 2, 19])
print("tuples Q3 ->", low, high)

# Q4: Dict keys must be hashable. Tuples are immutable, so their
#     hash never changes; a mutable list has no stable hash.
ok = {(1, 2): "ok"}
print("tuples Q4 ->", ok[(1, 2)])
# bad = {[1, 2]: "no"}   # TypeError: unhashable type: 'list'

# ------------------------------------------------------------------
# dictionaries.py
# ------------------------------------------------------------------
# Q1: 3. get("banana", 0) finds no key and returns the default 0,
#     then 0 + stock["apple"] equals 3 - no KeyError anywhere.
stock = {"apple": 3, "pear": 0}
print("dictionaries Q1 ->", stock.get("banana", 0) + stock["apple"])

# Q2: stock["banana"] raises KeyError on a missing key. Guard with
#     "in", or read through .get() with a default.
stock = {"apple": 3}
if stock.get("banana", 0) > 0:
    print("dictionaries Q2 -> We have bananas")
else:
    print("dictionaries Q2 -> no bananas, and no crash")

# Q3: Seed each letter with .get(letter, 0) so the first sighting
#     starts the count at 1 instead of raising KeyError.
word = "banana"
counts = {}
for letter in word:
    counts[letter] = counts.get(letter, 0) + 1
print("dictionaries Q3 ->", counts)

# Q4: {'a': 1, 'b': 9, 'c': 3}. | merges the right dict into the
#     left one, and RIGHT-hand values win on duplicate keys.
print("dictionaries Q4 ->", {"a": 1, "b": 2} | {"b": 9, "c": 3})

# ------------------------------------------------------------------
# sets.py
# ------------------------------------------------------------------
# Q1: 3. Sets keep only unique values, so the duplicate 2s and 3s
#     collapse into {1, 2, 3}.
print("sets Q1 ->", len({1, 2, 2, 3, 3, 3}))

# Q2: AttributeError - {} builds an empty DICT, and dicts have no
#     .add(). Build an empty set with set() instead.
empty = set()
empty.add(1)
print("sets Q2 ->", empty)

# Q3: Turn both lists into sets and intersect with & - it keeps
#     exactly the names present in both days.
saturday = ["ana", "raj", "mia"]
sunday = ["raj", "mia", "tom"]
both = set(saturday) & set(sunday)
print("sets Q3 ->", both)

# Q4: discard() when a missing item is normal business; remove()
#     when absence means something went wrong and you want to know.
s = {"a"}
s.discard("zzz")        # silent - carries on
print("sets Q4 -> discard stays silent; remove('zzz') would raise KeyError")

# ------------------------------------------------------------------
# unpacking.py
# ------------------------------------------------------------------
# Q1: [2, 3, 4]. The star grabs everything BETWEEN the first and
#     last captured values.
a, *b, c = [1, 2, 3, 4, 5]
print("unpacking Q1 ->", a, b, c)

# Q2: ValueError: too many values to unpack. Fix with a star
#     (first, *rest = ...) or slice first (first, second = ...[:2]).
first, *rest = [1, 2, 3]
print("unpacking Q2 ->", first, rest)

# Q3: {'volume': 5, 'quality': 'high'} - user comes AFTER base, so
#     its "quality" value overwrites the default.
base = {"volume": 5, "quality": "low"}
user = {"quality": "high"}
print("unpacking Q3 ->", {**base, **user})

# Q4: * spreads the list into positional args, ** spreads the dict
#     into keyword args - one flexible signature, no manual indexing.
def report(*names, **details):
    for name in names:
        print(" -", name)
    for key, value in details.items():
        print(f"   {key}: {value}")

report(*["Ana", "Raj"], topic="sets", level=1)

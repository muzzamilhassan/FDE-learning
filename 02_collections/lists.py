"""
=====================================================================
TOPIC: Lists - Your Ordered, Editable Collection
=====================================================================

SCENARIO
--------
You are building the playlist feature of a music app. Songs get
added, skipped, and reordered all the time. A list is Python's go-to
structure for ordered data you can change in place.

TOPIC
-----
- Ordered and mutable: items keep their order and can be replaced.
- Grow with .append(x) / .insert(i, x); shrink with .pop() / .remove(x).
- Slice with items[start:stop] - the stop index is NOT included.
- sorted(items) returns a NEW list; .sort() reorders IN PLACE.
- Gotcha: .sort() returns None, so "x = items.sort()" loses your data.
- Gotcha: .append([1, 2]) adds the whole list as ONE item; use
  .extend() to add each item individually.

QUESTIONS
---------
Q1. Predict: nums = [1, 2, 3]; nums.append([4, 5]); print(len(nums))
Q2. Spot the bug: result = numbers.sort(), then print(result)
Q3. Write code: from scores, build top3 = the three highest scores,
    highest first, WITHOUT changing the original list.
Q4. Predict the three prints using slicing on ["a" .. "f"].

Run: python 02_collections/lists.py
Answers: answers/02_collections.py
"""

# ------------------------------------------------------------------
# TOPIC EXAMPLES
# ------------------------------------------------------------------

# A list keeps items in order; indexes start at 0.
playlist = ["aphelion", "bloom", "cascade"]
print("First song:", playlist[0])
print("Last song :", playlist[-1])      # negative index = from the end

# .append adds ONE item to the end; .insert places it at an index.
playlist.append("daylight")
playlist.insert(0, "aurora")            # everything else shifts right
print("Playlist  :", playlist)

# .pop removes AND returns an item (the last one by default).
skipped = playlist.pop(1)
print(f"Removed '{skipped}', now:", playlist)

# .remove deletes the FIRST match by value and returns nothing.
playlist.remove("cascade")
print("After remove:", playlist)

# Slicing: [start:stop:step], stop excluded. Slices return NEW lists.
songs = ["a", "b", "c", "d", "e", "f"]
print("songs[1:4] :", songs[1:4])       # b, c, d
print("songs[:2]  :", songs[:2])        # start defaults to 0
print("songs[-2:]  :", songs[-2:])      # last two items
print("songs[::-1] :", songs[::-1])     # reversed copy

# sorted() leaves the original alone; .sort() changes it for real.
numbers = [5, 2, 9, 1]
print("sorted()   :", sorted(numbers))
numbers.sort(reverse=True)
print(".sort()    :", numbers)          # numbers itself is now ordered

# ------------------------------------------------------------------
# QUESTIONS - try them yourself, then check answers/02_collections.py
# ------------------------------------------------------------------
# Q1: Predict the output:
#     nums = [1, 2, 3]
#     nums.append([4, 5])
#     print(len(nums))
#
# Q2: This code prints something surprising. What, and why?
#     numbers = [3, 1, 2]
#     result = numbers.sort()
#     print(result)
#
# Q3: Write code: given scores = [88, 45, 92, 67, 74], create top3:
#     the three highest scores, highest first, WITHOUT changing
#     scores itself.
#
# Q4: Predict all three outputs:
#     letters = ["a", "b", "c", "d", "e", "f"]
#     print(letters[2:])
#     print(letters[-3:])
#     print(letters[::2])

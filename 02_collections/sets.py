"""
=====================================================================
TOPIC: Sets - Unique Items and Fast Membership
=====================================================================

SCENARIO
--------
You are tagging articles and comparing the skill lists of two
candidates. Duplicates should never show up twice, and you keep
asking "does this include X?" or "what do these two lists share?".
Sets answer both questions in one readable expression.

TOPIC
-----
- An unordered collection of UNIQUE values: {"a", "b"}.
- Build one from a list with set(my_list); duplicates vanish.
- Add with .add(x); remove with .discard(x) or .remove(x).
- Math operators: | union, & intersection, - difference.
- "x in s" is the idiomatic membership test - and very fast.
- Gotcha: an empty set is set(), because {} creates an empty DICT.

QUESTIONS
---------
Q1. Predict: print(len({1, 2, 2, 3, 3, 3}))
Q2. Spot the bug: empty = {} followed by empty.add(1)
Q3. Write code: given attendee name lists for two days, print who
    attended BOTH days, using sets.
Q4. Concept: .remove() raises KeyError on a missing item while
    .discard() does not - when is each the better choice?

Run: python 02_collections/sets.py
Answers: answers/02_collections.py
"""

# ------------------------------------------------------------------
# TOPIC EXAMPLES
# ------------------------------------------------------------------

# Duplicate entries collapse; order is not guaranteed.
tags = {"python", "web", "python", "tutorial"}
print("Tags:", tags)
print("Unique tag count:", len(tags))

# De-duplicating a list: convert to a set (and back if you need a list).
raw = ["css", "html", "css", "sql"]
unique = list(set(raw))
print("Raw:", raw)
print("Unique:", unique)

# .add inserts one item; .discard and .remove take one out.
tags.add("docker")
tags.discard("web")             # gone - and no error if it was absent
tags.discard("web")             # safe to call again
print("Tags now:", tags)

# Set math reads like plain English.
frontend = {"html", "css", "python"}
backend = {"python", "sql", "css"}

print("Union        | :", frontend | backend)   # everything, once
print("Intersection & :", frontend & backend)   # in both
print("Difference   - :", frontend - backend)   # only in frontend

# Membership checks: the clean way to ask "is it there?".
print("'sql' in backend?", "sql" in backend)

# ------------------------------------------------------------------
# QUESTIONS - try them yourself, then check answers/02_collections.py
# ------------------------------------------------------------------
# Q1: Predict the output:
#     print(len({1, 2, 2, 3, 3, 3}))
#
# Q2: This code crashes. Why, and what is the fix?
#     empty = {}
#     empty.add(1)
#
# Q3: Write code: saturday = ["ana", "raj", "mia"] and
#     sunday = ["raj", "mia", "tom"]. Print everyone who attended
#     BOTH days, using sets.
#
# Q4: Concept: .remove() raises KeyError on a missing item while
#     .discard() stays silent. Describe one situation where each is
#     the better choice.

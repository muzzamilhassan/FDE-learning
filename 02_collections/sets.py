"""
02_collections / sets.py
Topic: Python Sets (Equivalent to JavaScript Set)

JAVASCRIPT Set vs PYTHON set:
-----------------------------
JS:
    const s = new Set([1, 2, 2, 3]);
    s.add(4);
    s.delete(2);
    s.has(1); // true

Python:
    s = {1, 2, 2, 3}  # Syntax literal using curly braces!
    s.add(4)
    s.discard(2)      # Or s.remove(2)
    1 in s            # True

CRITICAL GOTCHA:
In Python:
    {}        creates an EMPTY DICT (not a set!)
    set()     creates an EMPTY SET!
"""

# ------------------------------------------------------------------------------
# 1. Set Creation & Automatic Deduplication
# ------------------------------------------------------------------------------
# JS: const tags = new Set(["python", "backend", "python", "api"]);
tags = {"python", "backend", "python", "api"}
print("Unique tags:", tags)

# Creating empty set:
empty_set = set()   # Note: {} would be a dict!
print("Empty set type:", type(empty_set))

# Deduplicating a list (very common pattern):
# JS: const uniqueList = [...new Set([1, 2, 2, 3])];
numbers_with_duplicates = [1, 2, 2, 3, 4, 4, 4, 5]
unique_numbers = list(set(numbers_with_duplicates))
print("Deduplicated list:", unique_numbers)


# ------------------------------------------------------------------------------
# 2. Adding & Removing
# ------------------------------------------------------------------------------
tags.add("docker")

# .remove() raises KeyError if item is missing;
# .discard() safely removes without error if missing (like JS set.delete()):
tags.discard("not_existing_tag")
print("After modifications:", tags)


# ------------------------------------------------------------------------------
# 3. Powerful Mathematical Set Operations
# ------------------------------------------------------------------------------
# Python has native operators for mathematical set operations:
frontend_skills = {"HTML", "CSS", "JavaScript", "TypeScript", "React"}
backend_skills = {"Python", "JavaScript", "TypeScript", "Docker", "SQL"}

# UNION: All skills combined (|)
# JS: new Set([...frontend_skills, ...backend_skills])
all_skills = frontend_skills | backend_skills
print("Union (|):", all_skills)

# INTERSECTION: Shared skills in both sets (&)
# JS: new Set([...frontend_skills].filter(x => backend_skills.has(x)))
shared_skills = frontend_skills & backend_skills
print("Intersection (&):", shared_skills)

# DIFFERENCE: Skills in frontend but NOT in backend (-)
frontend_only = frontend_skills - backend_skills
print("Difference (-):", frontend_only)

# SYMMETRIC DIFFERENCE: In either, but NOT in both (^)
exclusive_skills = frontend_skills ^ backend_skills
print("Symmetric Difference (^):", exclusive_skills)

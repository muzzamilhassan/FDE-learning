"""
03_control_flow / loops.py
Topic: Loops (for, while), range(), enumerate(), zip(), and Loop-Else

JAVASCRIPT vs PYTHON LOOPS:
---------------------------
JS for loops:
    for (let i = 0; i < 5; i++) { ... }       // C-style index loop
    for (const item of items) { ... }          // for..of loop (iterates values)
    for (const key in object) { ... }          // for..in loop (iterates keys)
    items.forEach((item, index) => { ... })   // Array method

Python for loops:
    for i in range(5):                         // generates 0, 1, 2, 3, 4
    for item in items:                         // directly iterates values (like for..of)
    for index, item in enumerate(items):       // iterates index AND value together!
    for a, b in zip(list_a, list_b):           // iterates multiple lists simultaneously!
"""

# ------------------------------------------------------------------------------
# 1. for loop with range(start, stop, step)
# ------------------------------------------------------------------------------
# JS: for (let i = 0; i < 5; i++)
print("Range 0 to 4:")
for i in range(5):
    print(i, end=" ")
print()

# JS: for (let i = 2; i <= 10; i += 2)
print("Even numbers 2 to 10:")
for num in range(2, 11, 2):
    print(num, end=" ")
print()


# ------------------------------------------------------------------------------
# 2. enumerate() - Getting Index and Value together
# ------------------------------------------------------------------------------
# JS: frameworks.forEach((fw, idx) => console.log(`${idx + 1}: ${fw}`));
frameworks = ["React", "FastAPI", "Next.js", "Django"]

print("\nEnumerate (index + value):")
for index, fw in enumerate(frameworks, start=1):
    print(f"  {index}. {fw}")


# ------------------------------------------------------------------------------
# 3. zip() - Looping multiple lists in parallel
# ------------------------------------------------------------------------------
# In JS, to loop over 2 arrays at once, you index manually:
#   names.forEach((name, i) => console.log(`${name}: ${scores[i]}`));
names = ["Alice", "Bob", "Charlie"]
scores = [95, 88, 92]

print("\nZip (parallel iteration):")
for name, score in zip(names, scores):
    print(f"  {name} scored {score}")


# ------------------------------------------------------------------------------
# 4. while loop
# ------------------------------------------------------------------------------
count = 3
while count > 0:
    print(f"Countdown: {count}")
    count -= 1


# ------------------------------------------------------------------------------
# 5. The Unique for...else Clause (No JS Equivalent!)
# ------------------------------------------------------------------------------
# In Python, a loop can have an `else` block!
# The `else` block executes ONLY IF the loop finished naturally WITHOUT hitting `break`.
target = 7
search_list = [1, 3, 5, 7, 9]

for num in search_list:
    if num == target:
        print(f"Found target {target}!")
        break
else:
    print("Target was not found in the list.")

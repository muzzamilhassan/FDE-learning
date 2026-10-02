# In JS: for (let i = 0; i < 4; i++)
print("for loop with range(4):")
for i in range(4):
    print(i, end=" ")
print()

# In JS: for (const item of items)
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"Fruit: {fruit}")

# In JS: items.forEach((item, index) => ...)
print("enumerate (index + item):")
for index, fruit in enumerate(fruits, start=1):
    print(f"  {index}. {fruit}")

# while loop
count = 3
while count > 0:
    print(f"Countdown: {count}")
    count -= 1

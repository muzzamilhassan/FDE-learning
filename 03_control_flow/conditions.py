# In JS: if (score >= 90) { ... } else if (score >= 80) { ... } else { ... }
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:     # Note: elif, not else if
    grade = "B"
else:
    grade = "C"

print(f"Score: {score} -> Grade: {grade}")

# Ternary operator:
# In JS: const status = age >= 18 ? "Adult" : "Minor";
age = 20
status = "Adult" if age >= 18 else "Minor"
print(f"Status: {status}")

# Chained comparison (In JS: x > 10 && x < 20)
x = 15
if 10 < x < 20:
    print("x is between 10 and 20!")

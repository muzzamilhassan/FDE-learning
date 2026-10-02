# In JS: export function add(a, b) { ... }
# In Python: Every function in a file is automatically exported!

def add(a: float, b: float) -> float:
    return a + b

def multiply(a: float, b: float) -> float:
    return a * b

# if __name__ == "__main__":
# Runs only when this file is executed directly (not when imported)
if __name__ == "__main__":
    print("Testing math_utils locally: 5 + 5 =", add(5, 5))

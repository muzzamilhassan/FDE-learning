"""
04_functions / functions.py
Topic: Defining Functions, Scope, and Returning Values

JAVASCRIPT vs PYTHON FUNCTIONS:
-------------------------------
JS Functions:
    function greet(name) {
        return `Hello, ${name}`;
    }
    const greetArrow = (name) => `Hello, ${name}`;

Python Functions:
    def greet(name: str) -> str:
        """Docstring explaining what this function does."""
        return f"Hello, {name}"

KEY DIFFERENCES:
1. No `function` keyword - use `def`.
2. Indentation defines the body of the function.
3. Docstrings: Multiline strings immediately after `def` serve as built-in
   documentation (accessible via `help(func)` or `func.__doc__`).
4. Returning multiple values: In Python, `return x, y` returns a tuple.
"""

# ------------------------------------------------------------------------------
# 1. Defining a Function & Docstrings
# ------------------------------------------------------------------------------
def calculate_net_salary(gross: float, tax_rate: float = 0.2) -> float:
    """Calculate the net salary after applying tax deductions.
    
    Args:
        gross: Total gross salary before taxes.
        tax_rate: Tax percentage (default: 0.2 / 20%).
    Returns:
        Net salary amount.
    """
    return gross * (1 - tax_rate)

net = calculate_net_salary(100000)
print(f"Net salary: ${net:,.2f}")
print("Function docstring:", calculate_net_salary.__doc__.strip().split("\n")[0])


# ------------------------------------------------------------------------------
# 2. Returning Multiple Values (Packed into a Tuple)
# ------------------------------------------------------------------------------
# In JS, to return multiple values, you must return an array or object:
#   function getMinMax(arr) { return { min: Math.min(...arr), max: Math.max(...arr) }; }
#   const { min, max } = getMinMax([1, 5, 2]);
#
# In Python, comma-separated return automatically packs into a tuple:
def get_min_and_max(numbers: list[int]) -> tuple[int, int]:
    return min(numbers), max(numbers)

min_val, max_val = get_min_and_max([12, 45, 2, 89, 34])
print(f"Min: {min_val}, Max: {max_val}")


# ------------------------------------------------------------------------------
# 3. Variable Scope (local, global, nonlocal)
# ------------------------------------------------------------------------------
# In JS: Outer variables can be modified inside functions directly.
# In Python: Reading an outer variable works, but ASSIGNING to it creates a LOCAL
# variable unless you explicitly declare it with `global` or `nonlocal`.
request_counter = 0

def record_request():
    global request_counter  # Explicitly tell Python to modify the global variable
    request_counter += 1

record_request()
record_request()
print("Global request counter:", request_counter)

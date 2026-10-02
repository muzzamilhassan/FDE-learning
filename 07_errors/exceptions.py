"""
07_errors / exceptions.py
Topic: Error and Exception Handling (try, except, else, finally)

JAVASCRIPT vs PYTHON ERROR HANDLING:
------------------------------------
JavaScript:
    try {
        riskyOperation();
    } catch (error) {
        // In JS, catch catches EVERYTHING.
        // You have to manually inspect: if (error instanceof TypeError) { ... }
    } finally {
        cleanup();
    }

Python:
    try:
        risky_operation()
    except ZeroDivisionError as err:      # Catch SPECIFIC exception type!
        handle_zero_div(err)
    except (ValueError, TypeError) as err:# Catch multiple specific types!
        handle_type_or_val(err)
    else:
        # PYTHON UNIQUE CLAUSE: Runs ONLY if NO exceptions occurred!
        print("Success!")
    finally:
        cleanup()                         # Always runs
"""

def safe_divide(numerator: float, denominator: float) -> float | None:
    try:
        result = numerator / denominator
    except ZeroDivisionError as err:
        print(f"[Error Handled] Cannot divide by zero: {err}")
        return None
    except TypeError as err:
        print(f"[Error Handled] Invalid operand types: {err}")
        return None
    else:
        # `else` executes ONLY when the `try` block succeeded without any errors!
        print(f"[Success] {numerator} / {denominator} = {result}")
        return result
    finally:
        # `finally` executes unconditionally (great for closing DB connections, files, etc.)
        print("[Finally] Operation cycle complete.\n")


# 1. Successful run:
safe_divide(100, 4)

# 2. ZeroDivisionError run:
safe_divide(50, 0)

# 3. TypeError run:
safe_divide(50, "two")  # type: ignore


# ------------------------------------------------------------------------------
# Raising Exceptions (Equivalent to `throw` in JS)
# ------------------------------------------------------------------------------
# JS: throw new Error("Invalid age");
# Python: raise ValueError("Invalid age")
def validate_age(age: int):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    return f"Valid age: {age}"

try:
    validate_age(-5)
except ValueError as e:
    print(f"Caught raised exception: {e}")

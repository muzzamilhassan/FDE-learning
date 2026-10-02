"""
10_python_features / decorators.py
Topic: Function Decorators (Higher-Order Function Syntactic Sugar)

JAVASCRIPT vs PYTHON DECORATORS:
--------------------------------
In JavaScript:
    Decorators (TC39 Stage 3) are used like `@autobind` or `@deprecated` on classes.
    For regular functions in JS, you write Higher-Order Functions:
    const withLogging = (fn) => (...args) => {
        console.log("Calling fn");
        return fn(...args);
    };

In Python:
    A decorator is a function that takes a function as input, wraps it,
    and returns an enhanced replacement function.
    The `@decorator_name` syntax is syntactic sugar for:
        my_func = decorator_name(my_func)
"""
import time
from functools import wraps

# ------------------------------------------------------------------------------
# 1. Performance Timing Decorator
# ------------------------------------------------------------------------------
def measure_execution_time(func):
    # @wraps(func) preserves the original function's name and __doc__ metadata:
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        
        # Execute the original function:
        result = func(*args, **kwargs)
        
        elapsed = time.perf_counter() - start_time
        print(f"[Timer] Function '{func.__name__}' executed in {elapsed:.6f} seconds")
        return result
    return wrapper


@measure_execution_time
def compute_heavy_sum(limit: int) -> int:
    """Sum numbers up to limit."""
    return sum(i for i in range(limit))

# Calling the decorated function:
result = compute_heavy_sum(1_000_000)
print(f"Result: {result} (Doc preserved: '{compute_heavy_sum.__doc__}')")


# ------------------------------------------------------------------------------
# 2. Decorators with Arguments (Decorator Factory)
# ------------------------------------------------------------------------------
def repeat(times: int):
    """Decorator factory that repeats function execution N times."""
    def decorator_repeat(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_result = None
            for i in range(1, times + 1):
                print(f"[Repeat {i}/{times}] calling {func.__name__}...")
                last_result = func(*args, **kwargs)
            return last_result
        return wrapper
    return decorator_repeat

@repeat(times=3)
def send_ping(host: str):
    print(f"  -> Ping sent to {host}")

print("\nTesting @repeat decorator:")
send_ping("192.168.1.1")

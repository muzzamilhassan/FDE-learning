# In JS: Higher-order function: const withLog = fn => (...args) => { ... }
# In Python: @decorator syntax wraps and enhances functions

def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}.")
        return result
    return wrapper

@log_call
def say_hello(name: str):
    print(f"Hello, {name}!")

say_hello("Alice")

# In JS: try { ... } catch (err) { ... } finally { ... }
# In Python: try, except, else, finally

def divide(a: float, b: float):
    try:
        result = a / b
    except ZeroDivisionError as err:
        print(f"Error caught: {err}")
    except TypeError as err:
        print(f"Type error: {err}")
    else:
        # Runs ONLY if no error occurred
        print(f"Success! {a} / {b} = {result}")
    finally:
        # Always runs
        print("Done attempt.")

divide(10, 2)
divide(10, 0)

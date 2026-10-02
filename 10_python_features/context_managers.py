"""
10_python_features / context_managers.py
Topic: Context Managers and the `with` Statement

JAVASCRIPT vs PYTHON RESOURCE MANAGEMENT:
-----------------------------------------
JavaScript:
    Recently introduced the `using` keyword (TypeScript 5.2+ / TC39 Explicit Resource Management).
    Traditionally, JS used try...finally:
    const conn = openConnection();
    try {
        doQuery(conn);
    } finally {
        conn.close();
    }

Python:
    The `with` statement encapsulates acquisition and automatic cleanup of resources.
    Guarantees cleanup even if exceptions are raised!

HOW IT WORKS INTERNALLY:
1. `__enter__()`: Called when entering the `with` block (acquires resource).
2. `__exit__()`: Called when leaving the `with` block (releases resource).
"""
from contextlib import contextmanager
import time

# ------------------------------------------------------------------------------
# 1. Class-Based Context Manager
# ------------------------------------------------------------------------------
class ManagedDatabaseConnection:
    def __init__(self, dsn: str):
        self.dsn = dsn

    def __enter__(self):
        print(f"[DB] Opening connection to {self.dsn}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f"[DB] Error occurred ({exc_val}) -> Rolling back transaction!")
        else:
            print("[DB] Transaction successful -> Committing changes.")
        print("[DB] Closed connection.")
        # Returning True suppresses the exception; False re-raises it:
        return False

# Usage:
print("--- Class Context Manager ---")
with ManagedDatabaseConnection("postgres://localhost:5432/app") as conn:
    print("  -> Executing SELECT * FROM users")


# ------------------------------------------------------------------------------
# 2. Generator-Based Context Manager (contextlib.contextmanager)
# ------------------------------------------------------------------------------
# Much simpler syntax using a generator with yield!
@contextmanager
def stopwatch(task_name: str):
    start = time.perf_counter()
    try:
        # Code before yield runs on __enter__:
        print(f"[Timer] Starting task: '{task_name}'")
        yield
    finally:
        # Code after yield runs on __exit__:
        elapsed = time.perf_counter() - start
        print(f"[Timer] Finished '{task_name}' in {elapsed:.4f}s")

print("\n--- Generator Context Manager ---")
with stopwatch("Summing 500,000 numbers"):
    sum(i ** 2 for i in range(500_000))

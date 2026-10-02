# In Python, 'with' handles setup and automatic cleanup
from contextlib import contextmanager

@contextmanager
def simple_timer(label: str):
    print(f"[{label}] Started")
    yield
    print(f"[{label}] Ended")

with simple_timer("My Task"):
    print("Doing work inside context...")

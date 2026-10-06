"""
=====================================================================
TOPIC: Context Managers
=====================================================================

SCENARIO
--------
Your backup script opens a connection, does some work, and must ALWAYS
release that connection -- even if a step crashes halfway through. A
context manager bundles the setup and the guaranteed cleanup into one
readable `with` block.

TOPIC
-----
`with obj as x:` calls __enter__(), runs the block, then ALWAYS calls __exit__().
The name after `as` receives whatever __enter__ returns.
Two styles: a class with __enter__/__exit__, or the quick
@contextmanager decorator where `yield` splits setup from cleanup.
Put cleanup AFTER the yield (inside try/finally when it matters).
Returning True from __exit__ swallows exceptions -- usually avoid it.

QUESTIONS
---------
Q1. Predict the output: a tag() context manager wrapping a print.
Q2. Concept check: why is `with open(...)` safer than manual close?
Q3. Spot the bug: setup and cleanup lines are in the wrong place.
Q4. Write code: a Timer class that times a with-block.

Run: python 09_python_features/context_managers.py
Answers: answers/09_python_features.py
=====================================================================
"""

# ------------------------------------------------------------------
# TOPIC EXAMPLES
# ------------------------------------------------------------------
import time
from contextlib import contextmanager

# Class style: __enter__ is setup, __exit__ is cleanup (always runs)
class Step:
    def __enter__(self):
        print("step: begin")
        return self  # this is what `as` would bind

    def __exit__(self, exc_type, exc, tb):
        print("step: end")  # runs even if the block raised
        return False  # False = let any exception propagate

with Step():
    print("  ...working...")

# Function style: everything before yield = setup, after = cleanup
@contextmanager
def timer(label):
    start = time.perf_counter()
    try:
        yield label  # the with-block runs right here
    finally:
        elapsed = time.perf_counter() - start
        print(f"{label} took {elapsed:.4f}s")

with timer("quick loop") as name:
    print(f"  timing: {name}")
    sum(range(100_000))

# ------------------------------------------------------------------
# QUESTIONS - try them yourself, then check answers/09_python_features.py
# ------------------------------------------------------------------
# Q1: Predict the output:
#         @contextmanager
#         def tag(name):
#             print(f"<{name}>")
#             yield
#             print(f"</{name}>")
#         with tag("b"):
#             print("bold text")
#
# Q2: Why does `with open(path) as f:` beat f = open(path) ... f.close()?
#     What exactly does __exit__ guarantee?
#
# Q3: Spot the bug -- this prints "done" before "start":
#         @contextmanager
#         def tracker():
#             print("done")
#             yield
#             print("start")
#
# Q4: Write code: a Timer class whose __enter__/__exit__ print how long
#     the with-block took, e.g.  with Timer(): sum(range(200000))

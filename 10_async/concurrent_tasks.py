"""
=====================================================================
TOPIC: Running Tasks Concurrently (asyncio.gather)
=====================================================================

SCENARIO
--------
Your gallery app downloads three images. Fetching them one by one
takes the SUM of all three delays; starting them together only takes
as long as the SLOWEST one. asyncio.gather launches several
coroutines at once and collects every result for you.

TOPIC
-----
- `await asyncio.gather(a(), b(), c())` runs the coroutines
  concurrently and waits until ALL of them finish.
- Results come back in the ORDER you passed the coroutines in --
  NOT the order they happened to finish.
- Total time is roughly the slowest task, not the sum of all waits
  (true whenever the work is mostly waiting, not computing).
- gather wraps each coroutine in a Task and starts it as soon as the
  loop gets control (at the first `await` inside any of them).
- Forgetting `await` on gather is the classic bug: you get an
  unawaited coroutine object instead of the results list.

QUESTIONS
---------
Q1. Predict the demo: which download finishes first, which result is
    listed first, and roughly how long does the run take?
Q2. Spot the bug: `results = asyncio.gather(d1, d2)` with no `await`,
    then `print(results)`. What is printed and why?
Q3. Write async `fetch(page)` that sleeps 0.2s then returns
    f"{page} fetched", and use gather on "a", "b", "c" in main().

Run: python 10_async/concurrent_tasks.py
Answers: answers/10_async.py
=====================================================================
"""

import asyncio
import time


# ------------------------------------------------------------------
# TOPIC EXAMPLES
# ------------------------------------------------------------------

async def download(name: str, seconds: float) -> str:
    await asyncio.sleep(seconds)  # pretend network wait
    print(f"  finished: {name}")
    return f"{name} ok"


async def main() -> None:
    start = time.perf_counter()
    # All three start together. cat.png sleeps least so it finishes
    # first -- yet it still lands in position 2 of the results.
    results = await asyncio.gather(
        download("dog.png", 0.4),
        download("cat.png", 0.1),
        download("bird.png", 0.3),
    )
    elapsed = time.perf_counter() - start
    print("Results:", results)
    print(f"Total: {elapsed:.2f}s (slowest task, not the 0.8s sum)")


if __name__ == "__main__":
    asyncio.run(main())


# ------------------------------------------------------------------
# QUESTIONS - try them yourself, then check answers/10_async.py
# ------------------------------------------------------------------
# Q1: Which download prints "finished" first? Which result is FIRST in
#     the results list? Roughly how long does the whole demo take?
# Q2: A teammate wrote `results = asyncio.gather(a(), b())` inside an
#     async function and printed results with no `await`. What do they
#     see, and what is the fix?
# Q3: Write async fetch(page: str) that sleeps 0.2s and returns
#     f"{page} fetched". In main(), gather it over "a", "b", "c" and
#     print the results list.

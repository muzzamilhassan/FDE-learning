"""
=====================================================================
TOPIC: Async Basics (async / await)
=====================================================================

SCENARIO
--------
You are building a small weather app that fetches live forecasts.
Each fetch takes a moment, and while waiting you do not want the
whole program frozen. Python's asyncio lets a single thread juggle
many waiting jobs by *pausing* (awaiting) instead of blocking.

TOPIC
-----
- `async def` defines a coroutine function. Calling it only CREATES
  a coroutine object -- nothing inside runs until you await it.
- `await` pauses the coroutine until the awaited thing finishes,
  freeing the event loop to run other work in the meantime.
- The event loop drives coroutines: `asyncio.run(main())` starts a
  loop, runs main() to completion, then closes the loop.
- Only `await` inside `async def`. Plain `time.sleep` blocks the
  entire loop -- use `asyncio.sleep` for non-blocking waits.

QUESTIONS
---------
Q1. Predict the output: order of the demo's printed lines, and why.
Q2. Spot the bug: a teammate calls `fetch_data("wind")` with no
    `await` inside another async function. What happens?
Q3. Write an async `greet(name)` that sleeps 0.2s then returns
    f"Hi, {name}!", plus a main() that prints it via asyncio.run.

Run: python 10_async/basic_async.py
Answers: answers/10_async.py
=====================================================================
"""

import asyncio


# ------------------------------------------------------------------
# TOPIC EXAMPLES
# ------------------------------------------------------------------

async def fetch_data(label: str) -> str:
    # asyncio.sleep is a NON-blocking wait: while this coroutine
    # pauses, the event loop is free to run other coroutines.
    print(f"{label}: starting")
    await asyncio.sleep(0.3)
    print(f"{label}: done")
    return f"{label} data"


async def main() -> None:
    # Calling fetch_data("weather") alone builds a coroutine object.
    # `await` is what actually runs it through to completion.
    result = await fetch_data("weather")
    print("Got:", result)


# asyncio.run creates the event loop, runs main(), closes the loop.
if __name__ == "__main__":
    asyncio.run(main())


# ------------------------------------------------------------------
# QUESTIONS - try them yourself, then check answers/10_async.py
# ------------------------------------------------------------------
# Q1: In what order does the demo print its lines? Explain why the
#     output is fully sequential even though the code is async.
# Q2: A teammate wrote `fetch_data("wind")` with no `await` inside an
#     async function and stored it in a variable. What do they get,
#     and what warning does Python print?
# Q3: Write an async function greet(name) that sleeps 0.2 seconds and
#     returns f"Hi, {name}!", plus an async main() that prints it,
#     launched with asyncio.run.

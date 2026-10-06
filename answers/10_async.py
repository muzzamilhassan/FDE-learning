"""
Answers for 10_async - try the questions first!
"""

import asyncio


# ------------------------------------------------------------------
# basic_async.py
# ------------------------------------------------------------------

# Q1: Output order is strictly sequential:
#         weather: starting
#         weather: done
#         Got: weather data
#     Why: `await fetch_data(...)` runs that coroutine to completion
#     before the next line of main() executes, and only one coroutine
#     exists -- async does not mean parallel by itself.

# Q2: Calling fetch_data("wind") without `await` only CREATES a
#     coroutine object; the body never runs. Python prints
#     "RuntimeWarning: coroutine 'fetch_data' was never awaited" and
#     the variable holds a coroutine, not the data. Fix:
#     `result = await fetch_data("wind")`.

# Q3: Working solution:

async def greet(name: str) -> str:
    await asyncio.sleep(0.2)  # pretend short wait
    return f"Hi, {name}!"


async def basic_main() -> None:
    print(await greet("Sam"))


# ------------------------------------------------------------------
# concurrent_tasks.py
# ------------------------------------------------------------------

# Q1: "finished" order: cat.png (0.1s), bird.png (0.3s), dog.png
#     (0.4s) -- shortest sleep wins. But the results list keeps
#     ARGUMENT order: [dog, cat, bird]. Total ~0.4s: the slowest
#     task, because all three slept at the same time.

# Q2: Without `await`, gather() is never run, so printing shows the
#     coroutine object itself, no downloads happen, and Python warns
#     it was never awaited. Fix: `results = await asyncio.gather(...)`.

# Q3: Working solution:

async def fetch(page: str) -> str:
    await asyncio.sleep(0.2)
    return f"{page} fetched"


async def concurrent_main() -> None:
    results = await asyncio.gather(fetch("a"), fetch("b"), fetch("c"))
    print(results)


if __name__ == "__main__":
    asyncio.run(basic_main())
    asyncio.run(concurrent_main())

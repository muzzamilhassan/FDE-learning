"""
11_async / basic_async.py
Topic: Asynchronous Programming with asyncio (async / await)

JAVASCRIPT PROMISES vs PYTHON ASYNCIO COROUTINES:
-------------------------------------------------
JavaScript (V8 Event Loop):
    - JS is inherently asynchronous and single-threaded.
    - Calling an async function IMMEDIATELY returns a Promise and STARTS executing (eager execution).
    - The JS event loop runs automatically in the background.

Python (asyncio Event Loop):
    - Python is synchronous by default.
    - Calling an async function DOES NOT start execution! It returns a COROUTINE object (lazy execution).
    - To start the event loop and run the coroutine, you must call `asyncio.run(main())`.
"""
import asyncio

# Defining an async function (Coroutine Function):
# JS: async function fetchUserData(userId) { ... }
async def fetch_user_data(user_id: int):
    print(f"[Async] Starting fetch for user ID {user_id}...")
    
    # asyncio.sleep simulates a non-blocking network I/O call:
    # JS: await new Promise(resolve => setTimeout(resolve, 1000));
    await asyncio.sleep(1)
    
    print(f"[Async] Received response for user ID {user_id}")
    return {"id": user_id, "username": f"user_{user_id}", "status": "active"}

async def main():
    print("--- Event Loop Starting ---")
    data = await fetch_user_data(42)
    print("Result data received:", data)
    print("--- Event Loop Finished ---")

# In Python, we must explicitly launch the event loop:
if __name__ == "__main__":
    asyncio.run(main())

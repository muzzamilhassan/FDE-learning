import asyncio

# In JS: async function fetchMessage() { await delay(); return "done"; }
async def fetch_message():
    print("Fetching...")
    await asyncio.sleep(1)  # Simulates async wait (like setTimeout in JS)
    return "Data received!"

async def main():
    result = await fetch_message()
    print("Result:", result)

# In JS: event loop runs automatically. In Python: start with asyncio.run()
if __name__ == "__main__":
    asyncio.run(main())

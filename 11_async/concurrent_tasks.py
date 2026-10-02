import asyncio
import time

# In JS: await Promise.all([task1(), task2()])
# In Python: await asyncio.gather(task1(), task2())

async def download(file_name: str, delay: float):
    await asyncio.sleep(delay)
    return f"{file_name} downloaded"

async def main():
    start = time.perf_counter()
    results = await asyncio.gather(
        download("image1.png", 0.5),
        download("image2.png", 0.5),
    )
    print("Results:", results)
    print(f"Total time: {time.perf_counter() - start:.2f}s (ran concurrently!)")

if __name__ == "__main__":
    asyncio.run(main())

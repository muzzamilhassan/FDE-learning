"""
11_async / concurrent_tasks.py
Topic: Concurrent Execution (Promise.all vs asyncio.gather)

JAVASCRIPT Promise.all vs PYTHON asyncio.gather:
------------------------------------------------
JavaScript:
    const [auth, payment, notify] = await Promise.all([
        callService("Auth", 1000),
        callService("Payment", 1500),
        callService("Notification", 800)
    ]);

Python:
    auth, payment, notify = await asyncio.gather(
        call_service("Auth", 1.0),
        call_service("Payment", 1.5),
        call_service("Notification", 0.8)
    )
"""
import asyncio
import time

async def fetch_service_status(service_name: str, latency_seconds: float) -> str:
    print(f"  [Request Sent] -> {service_name} (expects ~{latency_seconds}s latency)")
    await asyncio.sleep(latency_seconds)
    print(f"  [Response Recv] <- {service_name} ready")
    return f"{service_name}: 200 OK"

async def main():
    print("=== Launching Concurrent Async Tasks ===")
    start_time = time.perf_counter()

    # asyncio.gather schedules all 3 coroutines on the event loop concurrently:
    # In sequential code, this would take 1.0 + 1.5 + 0.8 = 3.3 seconds.
    # In concurrent async, this completes in ~1.5 seconds (the longest task)!
    results = await asyncio.gather(
        fetch_service_status("AuthService", 1.0),
        fetch_service_status("PaymentGateway", 1.5),
        fetch_service_status("EmailNotifier", 0.8),
    )

    total_time = time.perf_counter() - start_time
    print(f"\nAll Service Results: {results}")
    print(f"Total concurrent time: {total_time:.2f}s (vs ~3.3s sequential!)")

if __name__ == "__main__":
    asyncio.run(main())

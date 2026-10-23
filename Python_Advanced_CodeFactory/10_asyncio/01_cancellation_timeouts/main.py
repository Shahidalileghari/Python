import asyncio


async def worker(name: str, delay: float) -> str:
    try:
        await asyncio.sleep(delay)
        return f"{name} finished"
    finally:
        print(f"{name}: cleanup")


async def main_async() -> None:
    task = asyncio.create_task(worker("slow-worker", 2.0))
    try:
        async with asyncio.timeout(0.2):
            print(await task)
    except TimeoutError:
        print("Timed out; cancelling worker")
        task.cancel()
        try:
            await task
        except asyncio.CancelledError:
            print("Cancellation observed")


if __name__ == "__main__":
    asyncio.run(main_async())

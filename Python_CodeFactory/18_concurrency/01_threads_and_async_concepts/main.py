import asyncio


async def simulated_task(label: str, delay: float) -> None:
    print(f"Starting {label}")
    await asyncio.sleep(delay)
    print(f"Finished {label}")


async def main_async() -> None:
    await asyncio.gather(
        simulated_task("A", 1.0),
        simulated_task("B", 0.5),
    )


if __name__ == "__main__":
    asyncio.run(main_async())

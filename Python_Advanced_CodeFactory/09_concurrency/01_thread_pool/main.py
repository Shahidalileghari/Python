from concurrent.futures import ThreadPoolExecutor, as_completed
from time import sleep


def simulated_io(task_id: int) -> str:
    sleep(0.05)  # Demonstrates waiting; no network traffic is sent.
    return f"task-{task_id}-complete"


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(simulated_io, i) for i in range(1, 7)]
        for future in as_completed(futures):
            print(future.result())

# Async Tasks, Cancellation, and Timeouts

## Why this matters
Asyncio suits workloads with many I/O waits. Cancellation and timeouts are part of correct resource management. Python 3.11+ supports `asyncio.timeout`.

## Run
From the project root, run:
```bash
python 10_asyncio/01_cancellation_timeouts/main.py
```

## Teaching method
Predict the output, run the example, modify one assumption, then explain the trade-off.

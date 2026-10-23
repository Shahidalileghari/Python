# Thread Pools and Futures

## Why this matters
Thread pools can overlap blocking I/O. They do not generally speed up pure Python CPU-bound work in standard CPython because of the GIL. Bound work and handle worker failures explicitly.

## Run
From the project root, run:
```bash
python 09_concurrency/01_thread_pool/main.py
```

## Teaching method
Predict the output, run the example, modify one assumption, then explain the trade-off.

# SQLite Transactions and Repository Design

## Why this matters
Transactions group related changes so they commit together or roll back. Use parameterized SQL and constraints. A production financial system needs careful concurrency, authorization, audit, and currency design beyond this demo.

## Run
From the project root, run:
```bash
python 12_databases/01_transactions/main.py
```

## Teaching method
Predict the output, run the example, modify one assumption, then explain the trade-off.

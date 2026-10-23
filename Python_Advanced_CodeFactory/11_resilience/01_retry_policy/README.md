# Retries and Resilient Clients

## Why this matters
Remote services can fail or become slow. Use timeouts, bounded retries, and explicit retryable-error rules. In production, add jitter and a total deadline; don't blindly retry non-idempotent operations.

## Run
From the project root, run:
```bash
python 11_resilience/01_retry_policy/main.py
```

## Teaching method
Predict the output, run the example, modify one assumption, then explain the trade-off.

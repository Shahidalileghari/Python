# Advanced Capstone Projects

## 1. Async API Aggregator
Fetch multiple documented public endpoints concurrently. Add timeouts, bounded concurrency, retries for classified transient failures, schema validation, caching, and tests with fake clients.

## 2. Job Queue Simulator
Model queued/running/succeeded/failed/cancelled states, bounded workers, retry rules, SQLite persistence, duplicate-submission tests, and graceful shutdown.

## 3. ETL Data Quality Platform
Stream CSV/JSON records, validate and normalize, store valid rows in SQLite, report invalid rows, make repeated runs idempotent, and produce a run summary.

## 4. Secure Student Management API — design exercise
Separate transport, use cases, repository, and domain layers. Include input validation, authorization concepts, parameterized SQL, environment configuration, tests, request limits, and safe logging.

## 5. ML Experiment Tracker
Record dataset version, parameters, metrics, and artifact path; compare results; document leakage prevention and reproducibility. Use synthetic data only.

## Delivery checklist
- [ ] README, architecture diagram, setup steps
- [ ] Unit tests and integration test plan
- [ ] Input validation and failure behaviour
- [ ] Logging without secrets
- [ ] Dependency and version policy
- [ ] Security notes and measured performance notes

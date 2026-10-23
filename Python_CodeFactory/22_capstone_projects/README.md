# Capstone Projects

Use these projects after students have covered the preceding foundations. Each project should be planned, implemented in small increments, tested, and documented.

## Project 1 — Student Gradebook
**Skills:** functions, collections, validation, JSON/CSV, testing.
- Add, list, update, and remove student records.
- Validate marks from 0 to 100.
- Calculate averages and grade bands.
- Save/load data.
- Write unit tests.

## Project 2 — Personal Expense Tracker
**Skills:** dates, Decimal, CSV, SQLite, command-line arguments.
- Record expense date, category, amount, and note.
- Filter by date range and category.
- Show totals by category.
- Use `decimal.Decimal` for money calculations.
- Never store bank credentials.

## Project 3 — Library Inventory
**Skills:** OOP, SQLite, exceptions, tests.
- Manage books and availability.
- Check books out and return them.
- Prevent invalid state transitions.
- Use parameterized SQL.
- Test duplicate IDs and missing books.

## Project 4 — Public API Dashboard (CLI)
**Skills:** HTTP, JSON, timeouts, error handling, logging.
- Fetch public data from a documented demo API.
- Handle timeout, network errors, and unexpected payloads.
- Cache data locally.
- Respect the API's terms and rate limits.

## Project 5 — Secure Notes (local learning edition)
**Skills:** files, input validation, threat modelling, tests.
- Start with a plain-text prototype using only fake data.
- Discuss why plain text is not secure storage.
- Do not claim encryption unless using a reviewed cryptographic library correctly.
- Do not store real passwords or confidential information in the classroom project.

## Capstone delivery checklist
- [ ] README explains the purpose and setup.
- [ ] Requirements and assumptions are documented.
- [ ] Functions/classes have clear responsibilities.
- [ ] Invalid inputs are handled.
- [ ] Tests cover normal and edge cases.
- [ ] No secrets or personal data are committed.
- [ ] Git history has meaningful commits.

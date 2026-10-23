# Extending Python CodeFactory

## Add a lesson
1. Create a numbered folder using the existing naming pattern.
2. Add a `README.md` with objectives, concepts, run instructions, and teaching notes.
3. Add a small runnable `main.py`.
4. Add `exercises.md` with at least three tasks of increasing difficulty.
5. Keep examples standard-library-only where practical.
6. Check that the code runs on Python 3.10+.

## Style
- Follow PEP 8 conventions.
- Prefer descriptive names over clever abbreviations.
- Add type hints when they make the contract clearer.
- Use `if __name__ == "__main__":` for executable entry points.
- Explain why a technique is useful, not just what syntax to type.

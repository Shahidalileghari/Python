import sqlite3
from pathlib import Path


def main() -> None:
    database_path = Path(__file__).with_name("classroom.db")
    with sqlite3.connect(database_path) as connection:
        connection.execute(
            "CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT NOT NULL)"
        )
        connection.execute("INSERT INTO students (name) VALUES (?)", ("Ayesha",))
        rows = connection.execute("SELECT id, name FROM students ORDER BY id").fetchall()
        for row in rows:
            print(row)


if __name__ == "__main__":
    main()

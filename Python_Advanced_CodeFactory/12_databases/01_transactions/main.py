import sqlite3
from pathlib import Path


def transfer(db: sqlite3.Connection, sender: int, receiver: int, amount: int) -> None:
    if amount <= 0:
        raise ValueError("Amount must be positive")
    with db:
        source = db.execute("SELECT balance FROM accounts WHERE id = ?", (sender,)).fetchone()
        target = db.execute("SELECT balance FROM accounts WHERE id = ?", (receiver,)).fetchone()
        if source is None or target is None:
            raise ValueError("Account not found")
        if source[0] < amount:
            raise ValueError("Insufficient funds")
        db.execute("UPDATE accounts SET balance = balance - ? WHERE id = ?", (amount, sender))
        db.execute("UPDATE accounts SET balance = balance + ? WHERE id = ?", (amount, receiver))


if __name__ == "__main__":
    path = Path(__file__).with_name("accounts_demo.db")
    with sqlite3.connect(path) as db:
        db.execute("CREATE TABLE IF NOT EXISTS accounts (id INTEGER PRIMARY KEY, balance INTEGER NOT NULL CHECK(balance >= 0))")
        db.execute("INSERT OR IGNORE INTO accounts VALUES (1, 10000), (2, 2000)")
        transfer(db, 1, 2, 1500)
        print(db.execute("SELECT id, balance FROM accounts ORDER BY id").fetchall())

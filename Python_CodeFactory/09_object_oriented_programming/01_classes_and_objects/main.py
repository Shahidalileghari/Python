class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        if balance < 0:
            raise ValueError("Opening balance cannot be negative.")
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit must be positive.")
        self.balance += amount

    def summary(self) -> str:
        return f"{self.owner}: balance = {self.balance:.2f}"


def main() -> None:
    account = BankAccount("Ayesha", 1000)
    account.deposit(250)
    print(account.summary())


if __name__ == "__main__":
    main()

from typing import Protocol


class MessageSender(Protocol):
    def send(self, recipient: str, message: str) -> None: ...


class ConsoleSender:
    def send(self, recipient: str, message: str) -> None:
        print(f"To {recipient}: {message}")


class WelcomeService:
    def __init__(self, sender: MessageSender) -> None:
        self._sender = sender

    def welcome(self, recipient: str) -> None:
        if "@" not in recipient:
            raise ValueError("Recipient must look like an email address")
        self._sender.send(recipient, "Welcome to the course!")


if __name__ == "__main__":
    WelcomeService(ConsoleSender()).welcome("student@example.test")

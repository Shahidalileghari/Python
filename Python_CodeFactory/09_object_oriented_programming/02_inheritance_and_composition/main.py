class Notification:
    def send(self, message: str) -> str:
        return f"Notification: {message}"


class EmailNotification(Notification):
    def send(self, message: str) -> str:
        return f"Email sent: {message}"


def main() -> None:
    channels: list[Notification] = [Notification(), EmailNotification()]
    for channel in channels:
        print(channel.send("Class begins at 9 AM."))


if __name__ == "__main__":
    main()

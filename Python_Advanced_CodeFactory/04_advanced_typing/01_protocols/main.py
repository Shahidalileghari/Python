from typing import Protocol, TypeVar


class HasIdentifier(Protocol):
    @property
    def identifier(self) -> str: ...


T = TypeVar("T", bound=HasIdentifier)


def index_by_identifier(items: list[T]) -> dict[str, T]:
    return {item.identifier: item for item in items}


class User:
    def __init__(self, identifier: str, email: str) -> None:
        self.identifier = identifier
        self.email = email


if __name__ == "__main__":
    users = [User("u-1", "student@example.test")]
    print(index_by_identifier(users))

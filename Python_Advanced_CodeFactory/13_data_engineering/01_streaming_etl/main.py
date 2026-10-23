from collections.abc import Iterable, Iterator
from dataclasses import dataclass


@dataclass(frozen=True)
class Event:
    user_id: str
    amount: float


def transform(records: Iterable[dict[str, object]]) -> Iterator[Event]:
    for index, record in enumerate(records, start=1):
        user_id = str(record.get("user_id", "")).strip()
        try:
            amount = float(record["amount"])
        except (KeyError, TypeError, ValueError) as error:
            raise ValueError(f"Invalid amount at record {index}") from error
        if not user_id or amount < 0:
            raise ValueError(f"Invalid event at record {index}")
        yield Event(user_id, amount)


if __name__ == "__main__":
    for event in transform([{"user_id": "u-1", "amount": "12.5"}, {"user_id": "u-2", "amount": 7}]):
        print(event)

from typing import Protocol


class DiscountStrategy(Protocol):
    def discount(self, price: float) -> float:
        ...


class NoDiscount:
    def discount(self, price: float) -> float:
        return 0.0


class StudentDiscount:
    def discount(self, price: float) -> float:
        return price * 0.10


def final_price(price: float, strategy: DiscountStrategy) -> float:
    if price < 0:
        raise ValueError("Price cannot be negative.")
    return price - strategy.discount(price)


def main() -> None:
    print(final_price(1000, NoDiscount()))
    print(final_price(1000, StudentDiscount()))


if __name__ == "__main__":
    main()

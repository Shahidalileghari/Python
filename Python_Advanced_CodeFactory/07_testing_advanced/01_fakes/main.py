import unittest
from typing import Protocol


class PaymentGateway(Protocol):
    def charge(self, amount_cents: int) -> str: ...


class FakeGateway:
    def __init__(self) -> None:
        self.charges: list[int] = []

    def charge(self, amount_cents: int) -> str:
        self.charges.append(amount_cents)
        return "demo-payment-123"


def purchase(gateway: PaymentGateway, amount_cents: int) -> str:
    if amount_cents <= 0:
        raise ValueError("Amount must be positive")
    return gateway.charge(amount_cents)


class PurchaseTests(unittest.TestCase):
    def test_purchase_records_charge(self) -> None:
        gateway = FakeGateway()
        self.assertEqual(purchase(gateway, 2500), "demo-payment-123")
        self.assertEqual(gateway.charges, [2500])

    def test_invalid_amount_does_not_charge(self) -> None:
        gateway = FakeGateway()
        with self.assertRaises(ValueError):
            purchase(gateway, 0)
        self.assertEqual(gateway.charges, [])


if __name__ == "__main__":
    unittest.main()

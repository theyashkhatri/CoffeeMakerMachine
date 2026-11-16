import unittest
from decimal import Decimal

from coffee_maker import CoffeeMachine, Inventory


class CoffeeMachineTests(unittest.TestCase):
    def test_brews_drink_and_returns_change(self) -> None:
        machine = CoffeeMachine()

        result = machine.brew("espresso", Decimal("2.00"))

        self.assertTrue(result.success)
        self.assertEqual(result.change, Decimal("0.50"))
        self.assertEqual(machine.inventory.water, 950)
        self.assertEqual(machine.inventory.coffee, 82)

    def test_insufficient_payment_does_not_consume_resources(self) -> None:
        machine = CoffeeMachine()
        before = (machine.inventory.water, machine.inventory.coffee, machine.inventory.milk)

        result = machine.brew("latte", Decimal("2.49"))

        self.assertFalse(result.success)
        self.assertIn("Insufficient payment", result.message)
        self.assertEqual(
            (machine.inventory.water, machine.inventory.coffee, machine.inventory.milk),
            before,
        )

    def test_insufficient_ingredients_does_not_charge_or_consume(self) -> None:
        machine = CoffeeMachine(inventory=Inventory(water=49, coffee=100, milk=500))

        result = machine.brew("espresso", Decimal("5.00"))

        self.assertFalse(result.success)
        self.assertIn("water", result.message)
        self.assertEqual(machine.inventory.water, 49)

    def test_rejects_negative_payment(self) -> None:
        machine = CoffeeMachine()

        with self.assertRaises(ValueError):
            machine.brew("espresso", Decimal("-1"))

    def test_unknown_drink_is_reported(self) -> None:
        machine = CoffeeMachine()

        with self.assertRaisesRegex(ValueError, "Unknown drink"):
            machine.brew("mocha", Decimal("5.00"))


if __name__ == "__main__":
    unittest.main()

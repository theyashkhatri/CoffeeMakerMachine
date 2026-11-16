import tempfile
import unittest
from decimal import Decimal
from pathlib import Path

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

    def test_brew_normalizes_drink_names(self) -> None:
        machine = CoffeeMachine()

        result = machine.brew(" ESPRESSO ", Decimal("2.00"))

        self.assertTrue(result.success)
        self.assertEqual(result.change, Decimal("0.50"))
        self.assertEqual(machine.inventory.water, 950)

    def test_restock_restores_full_inventory(self) -> None:
        machine = CoffeeMachine(inventory=Inventory(water=20, coffee=5, milk=10))

        message = machine.restock()

        self.assertIn("full capacity", message)
        self.assertEqual(machine.inventory.water, 1000)
        self.assertEqual(machine.inventory.coffee, 100)
        self.assertEqual(machine.inventory.milk, 500)

    def test_state_persists_to_disk(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            state_path = Path(temp_dir) / "coffee_state.json"
            machine = CoffeeMachine(state_path=state_path)
            machine.brew("espresso", Decimal("2.00"))

            reloaded = CoffeeMachine(state_path=state_path, auto_load=True)

            self.assertTrue(state_path.exists())
            self.assertEqual(reloaded.inventory.water, 950)
            self.assertEqual(reloaded.inventory.coffee, 82)


if __name__ == "__main__":
    unittest.main()

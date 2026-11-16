"""Coffee machine state and brewing logic."""

from dataclasses import dataclass
from decimal import Decimal
from typing import Mapping


@dataclass(frozen=True)
class Drink:
    name: str
    water: int
    coffee: int
    milk: int
    price: Decimal


@dataclass
class Inventory:
    water: int = 1000
    coffee: int = 100
    milk: int = 500

    def __post_init__(self) -> None:
        if min(self.water, self.coffee, self.milk) < 0:
            raise ValueError("Inventory amounts cannot be negative.")


@dataclass(frozen=True)
class BrewResult:
    success: bool
    message: str
    change: Decimal = Decimal("0.00")


DEFAULT_MENU: Mapping[str, Drink] = {
    "espresso": Drink("espresso", water=50, coffee=18, milk=0, price=Decimal("1.50")),
    "latte": Drink("latte", water=200, coffee=24, milk=150, price=Decimal("2.50")),
    "cappuccino": Drink("cappuccino", water=250, coffee=24, milk=100, price=Decimal("3.00")),
}


class CoffeeMachine:
    def __init__(
        self,
        inventory: Inventory | None = None,
        menu: Mapping[str, Drink] | None = None,
    ) -> None:
        self.inventory = inventory if inventory is not None else Inventory()
        self.menu = dict(menu if menu is not None else DEFAULT_MENU)

    def brew(self, drink_name: str, payment: Decimal) -> BrewResult:
        """Brew a drink if ingredients and payment are sufficient."""
        try:
            drink = self.menu[drink_name.lower()]
        except KeyError as exc:
            raise ValueError(f"Unknown drink: {drink_name}") from exc

        payment = Decimal(str(payment))
        if not payment.is_finite() or payment < 0:
            raise ValueError("Payment must be a finite, non-negative amount.")

        shortages = [
            ingredient
            for ingredient in ("water", "coffee", "milk")
            if getattr(self.inventory, ingredient) < getattr(drink, ingredient)
        ]
        if shortages:
            return BrewResult(
                False,
                "Not enough " + ", ".join(shortages) + ". Please choose another drink.",
            )

        if payment < drink.price:
            return BrewResult(
                False,
                f"Insufficient payment. {drink.name.title()} costs ${drink.price:.2f}.",
            )

        self.inventory.water -= drink.water
        self.inventory.coffee -= drink.coffee
        self.inventory.milk -= drink.milk
        change = (payment - drink.price).quantize(Decimal("0.01"))
        return BrewResult(
            True,
            f"Here is your {drink.name}. Enjoy!",
            change=change,
        )

    def report(self) -> str:
        return (
            "Resources:\n"
            f"Water: {self.inventory.water} ml\n"
            f"Coffee: {self.inventory.coffee} g\n"
            f"Milk: {self.inventory.milk} ml"
        )

"""Coffee machine state and brewing logic."""

import json
from dataclasses import dataclass
from decimal import Decimal
from pathlib import Path
from typing import Mapping


DEFAULT_INVENTORY = {"water": 1000, "coffee": 100, "milk": 500}


@dataclass(frozen=True)
class Drink:
    name: str
    water: int
    coffee: int
    milk: int
    price: Decimal


@dataclass
class Inventory:
    water: int = DEFAULT_INVENTORY["water"]
    coffee: int = DEFAULT_INVENTORY["coffee"]
    milk: int = DEFAULT_INVENTORY["milk"]

    def __post_init__(self) -> None:
        if min(self.water, self.coffee, self.milk) < 0:
            raise ValueError("Inventory amounts cannot be negative.")

    @classmethod
    def from_dict(cls, values: Mapping[str, int] | None = None) -> "Inventory":
        data = {"water": DEFAULT_INVENTORY["water"], "coffee": DEFAULT_INVENTORY["coffee"], "milk": DEFAULT_INVENTORY["milk"]}
        if values:
            data.update({key: int(value) for key, value in values.items() if key in data})
        return cls(**data)

    def to_dict(self) -> dict[str, int]:
        return {"water": self.water, "coffee": self.coffee, "milk": self.milk}

    def consume(self, drink: Drink) -> None:
        self.water -= drink.water
        self.coffee -= drink.coffee
        self.milk -= drink.milk

    def restock(self, ingredient: str | None = None, amount: int | None = None) -> None:
        if ingredient is None:
            self.water = DEFAULT_INVENTORY["water"]
            self.coffee = DEFAULT_INVENTORY["coffee"]
            self.milk = DEFAULT_INVENTORY["milk"]
            return

        if ingredient not in DEFAULT_INVENTORY:
            raise ValueError(f"Unknown ingredient: {ingredient}")

        refill = DEFAULT_INVENTORY[ingredient] if amount is None else amount
        if refill < 0:
            raise ValueError("Restock amount cannot be negative.")
        setattr(self, ingredient, getattr(self, ingredient) + refill)


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
        state_path: str | Path | None = None,
        auto_load: bool = False,
    ) -> None:
        self.inventory = inventory if inventory is not None else Inventory()
        self.menu = dict(menu if menu is not None else DEFAULT_MENU)
        self.state_path = Path(state_path) if state_path else Path.cwd() / "coffee_maker_state.json"
        if auto_load:
            self.load_state()

    def brew(self, drink_name: str, payment: Decimal) -> BrewResult:
        """Brew a drink if ingredients and payment are sufficient."""
        normalized_name = str(drink_name).strip().lower()
        try:
            drink = self.menu[normalized_name]
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

        self.inventory.consume(drink)
        change = (payment - drink.price).quantize(Decimal("0.01"))
        self.save_state()
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

    def list_menu(self) -> str:
        lines = ["Available drinks:"]
        for name, drink in self.menu.items():
            lines.append(f"- {name}: ${drink.price:.2f}")
        return "\n".join(lines)

    def restock(self, ingredient: str | None = None, amount: int | None = None) -> str:
        if ingredient is not None:
            ingredient_name = ingredient.strip().lower()
            self.inventory.restock(ingredient_name, amount)
            self.save_state()
            return f"{ingredient_name.title()} restocked. Current level: {getattr(self.inventory, ingredient_name)}"

        self.inventory.restock()
        self.save_state()
        return "Inventory restocked to full capacity."

    def save_state(self) -> Path:
        self.state_path.parent.mkdir(parents=True, exist_ok=True)
        with self.state_path.open("w", encoding="utf-8") as file:
            json.dump(self.inventory.to_dict(), file)
        return self.state_path

    def load_state(self) -> bool:
        if not self.state_path.exists():
            return False
        with self.state_path.open("r", encoding="utf-8") as file:
            payload = json.load(file)
        self.inventory = Inventory.from_dict(payload)
        return True

# Coffee Maker Machine

A small Python command-line coffee machine simulator that lets you prepare drinks, validate payment, manage stock, and persist inventory between runs.

## Overview

This project models a simple coffee maker with:

- Drink selection for `espresso`, `latte`, and `cappuccino`
- Ingredient tracking for water, coffee, and milk
- Payment validation and automatic change calculation
- Inventory checks before brewing
- Full inventory restocking
- Persistent state saved to `coffee_maker_state.json`

The logic is implemented in the `coffee_maker` package and can be run as a CLI or imported for programmatic use.

## Project structure

```text
.
├── LICENSE
├── README.md
└── coffee_maker/
    ├── README.md
    ├── pyproject.toml
    ├── coffee_maker/
    │   ├── __init__.py
    │   ├── __main__.py
    │   ├── cli.py
    │   └── machine.py
    └── tests/
        └── test_machine.py
```

## Quick start

From the `coffee_maker` directory:

```bash
cd coffee_maker
python3 -m pip install -e .
python3 -m coffee_maker
```

Or, after installation:

```bash
coffee-maker
```

## CLI commands

When the app is running, you can enter:

- `espresso` — brew an espresso
- `latte` — brew a latte
- `cappuccino` — brew a cappuccino
- `report` — view the current stock levels
- `menu` — list available drinks and prices
- `restock` — refill inventory to full capacity
- `off` — exit the program

When placing an order, you will be prompted for the amount paid in dollars, for example:

```text
What would you like? latte
Payment in dollars: 3.00
```

The machine validates whether the payment is enough and returns change if applicable.

## State persistence

The machine stores its current inventory in a file named `coffee_maker_state.json` in the working directory. This makes the stock persist between runs.

## Running tests

```bash
cd coffee_maker
python3 -m unittest discover -s tests -v
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

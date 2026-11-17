# Coffee Maker Machine

A Python coffee machine simulator with a command-line interface and a
Streamlit browser interface. It tracks water, coffee, and milk, checks stock
before brewing, validates payment, calculates change, and persists inventory.

## Features

- Espresso, latte, and cappuccino
- Payment validation and change calculation
- Ingredient inventory checks and restocking
- Inventory saved between runs in `coffee_maker_state.json`
- Terminal CLI and browser-based Streamlit UI

## Install

From the repository root:

```bash
cd coffee_maker
mkdir -p "$HOME/.venvs"
python3 -m venv "$HOME/.venvs/coffee-maker"
"$HOME/.venvs/coffee-maker/bin/python" -m pip install -e .
```

The virtual environment is stored outside the project folder to avoid
interference from project-folder sync or file locking.

## Run the Streamlit UI

From the repository root:

```bash
"$HOME/.venvs/coffee-maker/bin/python" -m streamlit run coffee_maker/coffee_maker/streamlit_app.py
```

The UI lets you select a drink, enter payment, see the menu and current
inventory, and restock the machine.

## Run the CLI

```bash
"$HOME/.venvs/coffee-maker/bin/python" -m coffee_maker
```

Enter `espresso`, `latte`, or `cappuccino` to order. The CLI also supports
`report`, `menu`, `restock`, and `off`.

## Run tests

```bash
cd coffee_maker
"$HOME/.venvs/coffee-maker/bin/python" -m unittest discover -s tests -v
```

## Project layout

```text
coffee_maker/
├── coffee_maker/
│   ├── cli.py
│   ├── machine.py
│   └── streamlit_app.py
├── tests/
└── pyproject.toml
```

See [LICENSE](LICENSE) for license details.

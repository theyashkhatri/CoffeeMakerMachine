# Coffee Maker Machine

A Python coffee machine simulator with a command-line interface and a
Streamlit browser app. It checks inventory and payment before brewing, returns
change, and saves inventory between runs.

## Features

- Brew espresso, latte, or cappuccino
- Validate payment and calculate change
- Check ingredient availability before brewing
- Restock the machine and view updated inventory
- Persist inventory in `coffee_maker_state.json`
- Use a terminal CLI or browser-based Streamlit UI

## Menu and starting inventory

| Drink | Price | Water | Coffee | Milk |
|---|---:|---:|---:|---:|
| Espresso | $1.50 | 50 ml | 18 g | 0 ml |
| Latte | $2.50 | 200 ml | 24 g | 150 ml |
| Cappuccino | $3.00 | 250 ml | 24 g | 100 ml |

The machine starts with 1000 ml water, 100 g coffee, and 500 ml milk.
Restocking restores those levels.

## Requirements

- Python 3.10 or later
- Git

## Installation

Clone the repository and move into the Python project directory:

```bash
git clone https://github.com/theyashkhatri/CoffeeMakerMachine.git
cd CoffeeMakerMachine/coffee_maker
```

Create and activate a virtual environment, then install the project:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
```

On Windows PowerShell, create and activate the environment with:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e .
```

## Run the Streamlit app

From the `coffee_maker` directory (the directory containing `pyproject.toml`):

```bash
python -m streamlit run coffee_maker/streamlit_app.py
```

The app opens in your browser. Select a drink, enter payment, then choose
**Brew drink**. The inventory display updates after brewing or restocking.

## Run the command-line app

```bash
python -m coffee_maker
```

Enter `espresso`, `latte`, or `cappuccino` to order. The CLI also supports:

- `report` — show current stock
- `menu` — show available drinks and prices
- `restock` — restore full inventory
- `off` — quit

## Inventory persistence

Inventory is loaded from and saved to `coffee_maker_state.json` in the
directory where the app is run. Restocking resets it to the full starting
amounts.

## Run tests

From the `coffee_maker` directory:

```bash
python -m unittest discover -s tests -v
```

## Project layout

```text
CoffeeMakerMachine/
├── LICENSE
├── README.md
└── coffee_maker/
    ├── coffee_maker/
    │   ├── cli.py
    │   ├── machine.py
    │   └── streamlit_app.py
    ├── tests/
    └── pyproject.toml
```

See [LICENSE](LICENSE) for license details.

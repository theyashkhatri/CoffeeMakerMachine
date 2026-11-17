# Coffee Maker Machine

A Python coffee machine simulator with a command-line interface and a
Streamlit browser app. It checks inventory and payment before brewing, returns
change, and saves inventory between runs.

## Features

- Brew espresso, latte, or cappuccino
- Validate payment and calculate change
- Check ingredient availability before brewing
- Restock the machine and display updated inventory
- Persist inventory in `coffee_maker_state.json`
- Use either the terminal CLI or browser-based Streamlit UI

## Menu and starting inventory

| Drink | Price | Water | Coffee | Milk |
|---|---:|---:|---:|---:|
| Espresso | $1.50 | 50 ml | 18 g | 0 ml |
| Latte | $2.50 | 200 ml | 24 g | 150 ml |
| Cappuccino | $3.00 | 250 ml | 24 g | 100 ml |

The machine starts with 1000 ml water, 100 g coffee, and 500 ml milk.
Restocking restores those full levels.

## Setup

The Python package requires Python 3.10 or later. These commands create an
environment outside the project folder and install the app with its Streamlit
dependency. Use the same environment for installation and running:

```bash
mkdir -p "$HOME/.venvs"
python3 -m venv "$HOME/.venvs/coffee-maker-fresh"
"$HOME/.venvs/coffee-maker-fresh/bin/python" -m pip --version
"$HOME/.venvs/coffee-maker-fresh/bin/python" -m pip install -e /Volumes/Helumi/Projects/coffee_maker
```

If that environment already exists but its `pip` is broken, create a new one
with a different name rather than clearing or reusing the broken environment.

## Run the Streamlit app

```bash
cd /Volumes/Helumi/Projects/coffee_maker && \
"$HOME/.venvs/coffee-maker-fresh/bin/python" -m streamlit run "$PWD/coffee_maker/streamlit_app.py"
```

Choose a drink, enter payment, then select **Brew drink**. The inventory
metrics update after brewing or restocking. **Restock machine** resets stock
to 1000 ml water, 100 g coffee, and 500 ml milk.

## Run the command-line app

```bash
cd /Volumes/Helumi/Projects/coffee_maker && \
"$HOME/.venvs/coffee-maker-fresh/bin/python" -m coffee_maker
```

Enter `espresso`, `latte`, or `cappuccino` to order. Other commands:

- `report` — show current stock
- `menu` — show drinks and prices
- `restock` — restore full inventory
- `off` — quit

## Run tests

```bash
cd /Volumes/Helumi/Projects/coffee_maker && \
"$HOME/.venvs/coffee-maker-fresh/bin/python" -m unittest discover -s tests -v
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

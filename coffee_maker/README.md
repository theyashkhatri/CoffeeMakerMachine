# Coffee Maker

A Python 3.10+ coffee machine simulator with a terminal CLI and a Streamlit
browser app. It validates payment and inventory, returns change, and persists
stock in `coffee_maker_state.json` in the current working directory.

## Drinks

| Drink | Price | Water | Coffee | Milk |
|---|---:|---:|---:|---:|
| Espresso | $1.50 | 50 ml | 18 g | 0 ml |
| Latte | $2.50 | 200 ml | 24 g | 150 ml |
| Cappuccino | $3.00 | 250 ml | 24 g | 100 ml |

Full inventory is 1000 ml water, 100 g coffee, and 500 ml milk. Restocking
resets the inventory to those amounts.

## Install

From the repository checkout, create an environment outside the project folder
and install the package:

```bash
mkdir -p "$HOME/.venvs"
python3 -m venv "$HOME/.venvs/coffee-maker-fresh"
"$HOME/.venvs/coffee-maker-fresh/bin/python" -m pip install -e .
```

If the environment already exists but its `pip` is broken, make a new
environment under a different name rather than clearing or reusing it.

## Run the Streamlit app

Run from the directory containing `pyproject.toml`:

```bash
"$HOME/.venvs/coffee-maker-fresh/bin/python" -m streamlit run coffee_maker/streamlit_app.py
```

Use the sidebar to select a drink and enter payment. The inventory metrics
refresh after brewing and restocking.

## Run the CLI

```bash
"$HOME/.venvs/coffee-maker-fresh/bin/python" -m coffee_maker
```

Available commands: `espresso`, `latte`, `cappuccino`, `report`, `menu`,
`restock`, and `off`.

## Run tests

```bash
"$HOME/.venvs/coffee-maker-fresh/bin/python" -m unittest discover -s tests -v
```

# Coffee Maker

A Python 3.10+ coffee machine simulator with a terminal CLI and a Streamlit
browser app. It validates payment and inventory, returns change, and persists
stock to `coffee_maker_state.json`.

## Setup

From the repository root:

```bash
git clone https://github.com/theyashkhatri/CoffeeMakerMachine.git
cd CoffeeMakerMachine/coffee_maker
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
```

On Windows PowerShell, use `py -m venv .venv` and
`.\.venv\Scripts\Activate.ps1` to create and activate the environment.

## Streamlit app

Run from the directory containing `pyproject.toml`:

```bash
python -m streamlit run coffee_maker/streamlit_app.py
```

The browser UI supports selecting a drink, entering payment, viewing
inventory, and restocking.

## Command-line app

```bash
python -m coffee_maker
```

Commands: `espresso`, `latte`, `cappuccino`, `report`, `menu`, `restock`, and
`off`.

## Tests

```bash
python -m unittest discover -s tests -v
```

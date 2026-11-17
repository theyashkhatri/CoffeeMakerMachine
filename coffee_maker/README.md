# Coffee Maker

A Python coffee machine simulator with a terminal CLI and a Streamlit browser
interface. It checks inventory and payment before brewing and saves inventory
to `coffee_maker_state.json` in the current working directory.

## Install

Run these commands from the directory containing `pyproject.toml`:

```bash
mkdir -p "$HOME/.venvs"
python3 -m venv "$HOME/.venvs/coffee-maker"
"$HOME/.venvs/coffee-maker/bin/python" -m pip install -e .
```

The virtual environment is kept outside the project directory to avoid
project-folder sync or file-lock problems.

## Run the Streamlit UI

From this directory:

```bash
"$HOME/.venvs/coffee-maker/bin/python" -m streamlit run coffee_maker/streamlit_app.py
```

The browser UI supports selecting espresso, latte, or cappuccino, entering
payment, viewing the menu and live inventory, and restocking.

## Run the CLI

```bash
"$HOME/.venvs/coffee-maker/bin/python" -m coffee_maker
```

Use `report`, `menu`, or `restock` to manage the machine, and `off` to quit.

## Run tests

```bash
"$HOME/.venvs/coffee-maker/bin/python" -m unittest discover -s tests -v
```

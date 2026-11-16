# Coffee Maker

A small, dependency-free command-line coffee maker simulator. It tracks water,
milk, and coffee, checks stock before brewing, and handles payment and change
using decimal arithmetic.

## Install

```bash
python3 -m pip install -e .
```

## Run

From this directory:

```bash
python3 -m coffee_maker
```

Or after installation:

```bash
coffee-maker
```

Choose `espresso`, `latte`, or `cappuccino`, then enter the amount paid in
dollars (for example, `2.50`). Use `report` to view remaining ingredients,
`menu` to view the drink list, `restock` to refill the machine, or `off` to quit.

The machine now persists inventory to a `coffee_maker_state.json` file in the
current working directory so your stock is restored between runs.

## Run tests

```bash
python3 -m unittest discover -s tests -v
```

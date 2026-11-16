# Coffee Maker

A small, dependency-free command-line coffee maker simulator. It tracks water,
milk, and coffee, checks stock before brewing, and handles payment and change
using decimal arithmetic.

## Run

From this directory:

```bash
python -m coffee_maker
```

Choose `espresso`, `latte`, or `cappuccino`, then enter the amount paid in
dollars (for example, `2.50`). Type `report` to view remaining ingredients or
`off` to quit.

## Run tests

```bash
python -m unittest discover -s tests -v
```

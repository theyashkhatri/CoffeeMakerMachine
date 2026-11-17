"""Streamlit user interface for the coffee maker."""

from __future__ import annotations

from decimal import Decimal, InvalidOperation

import streamlit as st

if __package__:
    from .machine import CoffeeMachine
else:  # Streamlit executes this file directly, so import its sibling module.
    from machine import CoffeeMachine


def _get_machine() -> CoffeeMachine:
    if "machine" not in st.session_state:
        st.session_state.machine = CoffeeMachine(auto_load=True)
    return st.session_state.machine


def _render_inventory(machine: CoffeeMachine) -> None:
    st.subheader("Inventory")
    st.code(machine.report(), language="text")


def main() -> None:
    st.set_page_config(page_title="Coffee Maker Machine", page_icon="☕", layout="centered")
    machine = _get_machine()

    st.title("Coffee Maker Machine")
    st.caption("Choose a drink, add payment, and enjoy your fresh coffee.")

    with st.sidebar:
        st.header("Controls")
        drink_name = st.selectbox(
            "Select a drink",
            options=list(machine.menu.keys()),
            index=0,
        )
        payment = st.number_input(
            "Payment in dollars",
            min_value=0.0,
            max_value=20.0,
            step=0.25,
            value=2.50,
            format="%.2f",
        )

        brew_clicked = st.button("Brew drink", use_container_width=True, type="primary")
        restock_clicked = st.button("Restock machine", use_container_width=True)

    _render_inventory(machine)

    if brew_clicked:
        try:
            result = machine.brew(drink_name, Decimal(str(payment)))
        except (InvalidOperation, ValueError) as error:
            st.error(f"Unable to process order: {error}")
        else:
            if result.success:
                st.success(result.message)
                if result.change:
                    st.write(f"Change: ${result.change:.2f}")
            else:
                st.warning(result.message)

    if restock_clicked:
        message = machine.restock()
        st.info(message)
        _render_inventory(machine)

    st.subheader("Menu")
    menu_data = [
        {"Drink": name, "Price": f"${drink.price:.2f}", "Water": drink.water, "Coffee": drink.coffee, "Milk": drink.milk}
        for name, drink in machine.menu.items()
    ]
    st.dataframe(menu_data, use_container_width=True)


if __name__ == "__main__":
    main()

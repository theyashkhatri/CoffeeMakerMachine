"""Interactive command-line interface."""

from decimal import Decimal, InvalidOperation

from .machine import CoffeeMachine


def main() -> None:
    machine = CoffeeMachine(auto_load=True)
    print("Coffee Maker ready. Drinks: espresso, latte, cappuccino.")
    print("Commands: report, menu, restock, off.")

    while True:
        choice = input("What would you like? ").strip().lower()
        if choice == "off":
            print("Coffee maker shutting down.")
            return
        if choice == "report":
            print(machine.report())
            continue
        if choice == "menu":
            print(machine.list_menu())
            continue
        if choice == "restock":
            print(machine.restock())
            continue
        if choice not in machine.menu:
            print("Please choose espresso, latte, cappuccino, report, menu, restock, or off.")
            continue

        try:
            payment = Decimal(input("Payment in dollars: ").strip())
            result = machine.brew(choice, payment)
        except (InvalidOperation, ValueError) as error:
            print(f"Unable to process order: {error}")
            continue

        print(result.message)
        if result.success and result.change:
            print(f"Here is ${result.change:.2f} in change.")


if __name__ == "__main__":
    main()

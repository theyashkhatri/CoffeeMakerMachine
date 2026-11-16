"""Interactive command-line interface."""

from decimal import Decimal, InvalidOperation

from .machine import CoffeeMachine


def main() -> None:
    machine = CoffeeMachine()
    print("Coffee Maker ready. Drinks: espresso, latte, cappuccino.")

    while True:
        choice = input("What would you like? ").strip().lower()
        if choice == "off":
            print("Coffee maker shutting down.")
            return
        if choice == "report":
            print(machine.report())
            continue
        if choice not in machine.menu:
            print("Please choose espresso, latte, cappuccino, report, or off.")
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

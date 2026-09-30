# Executes all the functions (imported from the other modules)
from menu import MENU, display_menu
from customer_input import ask_to_order, ask_another_order, get_menu_item, get_quantity
from orders import add_order
from calculations import calculate_subtotal, calculate_discount, calculate_total
from receipt import print_receipt, print_goodbye


def main():
    # To store the customer's orders
    orders = {}

    display_menu(MENU)

    if not ask_to_order():
        print_goodbye()
        return

    # Repeatedly gets items and quantities until the customer is finished
    while True:
        item = get_menu_item(MENU)
        quantity = get_quantity()

        add_order(orders, item, quantity)

        if not ask_another_order():
            break

    subtotal = calculate_subtotal(MENU, orders)
    discount = calculate_discount(subtotal)
    total = calculate_total(subtotal, discount)

    print_receipt(MENU, orders, subtotal, discount, total)


if __name__ == "__main__":
    main()

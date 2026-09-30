from menu import Menu
from order import Order


# Asks a yes/no question until a valid answer is given
def ask_yes_no(prompt):
    while True:
        choice = input(prompt).strip().lower()

        if choice in ("yes", "y"):
            return True
        elif choice in ("no", "n"):
            return False
        else:
            print("Invalid choice. Please enter yes or no.")


# Gets and validates the menu item entered by the customer
def get_menu_item(menu):
    while True:
        name = input("\nEnter the menu item: ").strip()
        item = menu.find_item(name)

        if item:
            return item

        print("Item not found. Please choose an item from the menu.")


# Gets and validates the quantity entered by the customer
def get_quantity():
    while True:
        try:
            quantity = int(input("Enter quantity: "))

            if quantity > 0:
                return quantity

            print("Quantity must be greater than 0.")

        except ValueError:
            print("Invalid quantity. Please enter a whole number.")


def main():
    menu = Menu()          # object (instance of Menu)
    order = Order(menu)    # object (instance of Order)

    menu.display()

    if not ask_yes_no("\nWould you like to order? (yes/no): "):
        print("\nThank you for visiting Nadera's Fast Food!")
        print("Have a great day!")
        return

    # Repeatedly gets items and quantities until the customer is finished
    while True:
        item = get_menu_item(menu)
        quantity = get_quantity()

        order.add_item(item, quantity)

        if not ask_yes_no("\nWould you like to order another item? (yes/no): "):
            break

    order.print_receipt()


if __name__ == "__main__":
    main()

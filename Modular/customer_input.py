# Everything that asks the customer for input


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


# Asks the customer if they want to place an order
def ask_to_order():
    return ask_yes_no("\nWould you like to order? (yes/no): ")


# Asks the customer if they want to order another item
def ask_another_order():
    return ask_yes_no("\nWould you like to order another item? (yes/no): ")


# Gets and validates the menu item entered by the customer
def get_menu_item(menu):
    while True:
        item = input("\nEnter the menu item: ").strip()

        # Allows the customer to ignore capitalization
        for menu_item in menu:
            if item.lower() == menu_item.lower():
                return menu_item

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

# Menu data and menu display

# Menu stored in a dictionary
MENU = {
    "Burger": 75.00,
    "Cheeseburger": 95.00,
    "Chicken Sandwich": 110.00,
    "French Fries": 55.00,
    "Chicken Meal": 150.00,
    "Spaghetti": 85.00,
    "Soft Drink": 40.00,
    "Iced Tea": 45.00,
    "Sundae": 50.00,
}


# Displays the complete menu and prices
def display_menu(menu):
    print("\n" + "=" * 50)
    print("             NADERA'S FAST FOOD")
    print("=" * 50)
    print(f"{'ITEM':<30}{'PRICE':>15}")
    print("-" * 50)

    for item, price in menu.items():
        print(f"{item:<30}₱{price:>13.2f}")

    print("=" * 50)

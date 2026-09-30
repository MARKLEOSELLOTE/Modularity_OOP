# Receipt and goodbye messages


# Prints the customer's official receipt
def print_receipt(menu, orders, subtotal, discount, total):
    print("\n")
    print("=" * 65)
    print("                       NADERA'S FAST FOOD")
    print("                       OFFICIAL RECEIPT")
    print("=" * 65)
    print(f"{'ITEM':<25}{'QTY':>7}{'PRICE':>15}{'TOTAL':>15}")
    print("-" * 65)

    for item, quantity in orders.items():
        price = menu[item]
        item_total = price * quantity

        print(
            f"{item:<25}"
            f"{quantity:>7}"
            f"₱{price:>14.2f}"
            f"₱{item_total:>14.2f}"
        )

    print("-" * 65)
    print(f"{'SUBTOTAL':<50}₱{subtotal:>14.2f}")
    print(f"{'DISCOUNT':<50}₱{discount:>14.2f}")
    print(f"{'TOTAL':<50}₱{total:>14.2f}")
    print("=" * 65)
    print("              Thank you for ordering!")
    print("                 Please come again!")
    print("=" * 65)


# Prints the goodbye message when the customer does not order
def print_goodbye():
    print("\nThank you for visiting Nadera's Fast Food!")
    print("Have a great day!")

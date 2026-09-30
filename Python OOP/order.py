class Order:
    """Blueprint for a customer's order."""

    DISCOUNT_THRESHOLD = 500
    DISCOUNT_RATE = 0.10

    def __init__(self, menu):
        # Attributes: the menu (for prices) and the ordered items
        self.menu = menu
        self.items = {}

    # Adds the selected item and quantity to the order
    def add_item(self, item, quantity):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    # Calculates the subtotal of all ordered items
    def calculate_subtotal(self):
        subtotal = 0

        for item, quantity in self.items.items():
            subtotal += self.menu.items[item] * quantity

        return subtotal

    # 10% discount for orders worth ₱500 or more
    def calculate_discount(self):
        subtotal = self.calculate_subtotal()

        if subtotal >= self.DISCOUNT_THRESHOLD:
            return subtotal * self.DISCOUNT_RATE

        return 0

    # Calculates the final total after applying the discount
    def calculate_total(self):
        return self.calculate_subtotal() - self.calculate_discount()

    # Prints the customer's official receipt
    def print_receipt(self):
        subtotal = self.calculate_subtotal()
        discount = self.calculate_discount()
        total = self.calculate_total()

        print("\n")
        print("=" * 65)
        print("                       NADERA'S FAST FOOD")
        print("                       OFFICIAL RECEIPT")
        print("=" * 65)
        print(f"{'ITEM':<25}{'QTY':>7}{'PRICE':>15}{'TOTAL':>15}")
        print("-" * 65)

        for item, quantity in self.items.items():
            price = self.menu.items[item]
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

# All computations for the bill


# Calculates the subtotal of all ordered items
def calculate_subtotal(menu, orders):
    subtotal = 0

    for item, quantity in orders.items():
        subtotal += menu[item] * quantity

    return subtotal


# Calculates a discount based on the subtotal
def calculate_discount(subtotal):
    # 10% discount for orders worth ₱500 or more
    if subtotal >= 500:
        return subtotal * 0.10

    return 0


# Calculates the final total after applying the discount
def calculate_total(subtotal, discount):
    return subtotal - discount

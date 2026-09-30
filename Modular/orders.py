# Handles the customer's order


# Adds the selected item and quantity to the customer's order
def add_order(orders, item, quantity):
    if item in orders:
        orders[item] += quantity
    else:
        orders[item] = quantity

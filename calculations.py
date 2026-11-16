def calculate_total_revenue(sales):
    """Calculate total revenue from all sales."""
    total = 0

    for sale in sales:
        total += sale["quantity"] * sale["unit_price"]

    return total


def calculate_total_orders(sales):
    """Return the number of orders processed."""
    return len(sales)


def calculate_total_units(sales):
    """Calculate the total quantity of products sold."""
    total = 0

    for sale in sales:
        total += sale["quantity"]

    return total

def best_selling_product(sales):
    """Return the product with the highest number of units sold."""

    product_sales = {}

    for sale in sales:
        product = sale["product"]
        quantity = sale["quantity"]

        if product in product_sales:
            product_sales[product] += quantity
        else:
            product_sales[product] = quantity

    best_product = max(product_sales, key=product_sales.get)

    return best_product, product_sales[best_product]
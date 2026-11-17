

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
def highest_revenue_product(sales):
    """Return the product with the highest total revenue."""

    product_revenue = {}

    for sale in sales:
        product = sale["product"]
        revenue = sale["quantity"] * sale["unit_price"]

        if product in product_revenue:
            product_revenue[product] += revenue
        else:
            product_revenue[product] = revenue

    if not product_revenue:
        return None, 0

    top_product = max(product_revenue, key=product_revenue.get)

    return top_product, product_revenue[top_product]
    """Return the product with the highest total revenue."""

    product_revenue = {}

    for sale in sales:
        product = sale["product"]
        revenue = sale["quantity"] * sale["unit_price"]

        if product in product_revenue:
            product_revenue[product] += revenue
        else:
            product_revenue[product] = revenue

    top_product = max(product_revenue, key=product_revenue.get)

    return top_product, product_revenue[top_product]
    if not product_revenue:
     return None, 0

def test_highest_revenue_product(self):
    sales = [
        {"product": "Laptop", "quantity": 2, "price": 1200},
        {"product": "Mouse", "quantity": 10, "price": 25},
        {"product": "Keyboard", "quantity": 5, "price": 75},
        {"product": "Laptop", "quantity": 1, "price": 1150},
    ]

    product, revenue = highest_revenue_product(sales)

    self.assertEqual(product, "Laptop")
    self.assertEqual(revenue, 3550)

def test_highest_revenue_product_empty(self):
    product, revenue = highest_revenue_product([])

    self.assertIsNone(product)
    self.assertEqual(revenue, 0)    
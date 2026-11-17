import unittest

from calculations import (
    calculate_total_revenue,
    calculate_total_orders,
    calculate_total_units,
    best_selling_product,
    highest_revenue_product,
)


class TestCalculations(unittest.TestCase):

    def test_total_orders(self):
        sales = [
            {"product": "Laptop", "quantity": 2, "unit_price": 1200},
            {"product": "Mouse", "quantity": 10, "unit_price": 25},
        ]

        result = calculate_total_orders(sales)

        self.assertEqual(result, 2)


    def test_total_units(self):
        sales = [
            {"product": "Laptop", "quantity": 2, "unit_price": 1200},
            {"product": "Mouse", "quantity": 10, "unit_price": 25},
        ]

        result = calculate_total_units(sales)

        self.assertEqual(result, 12)


    def test_total_revenue(self):
        sales = [
            {"product": "Laptop", "quantity": 2, "unit_price": 1200},
            {"product": "Mouse", "quantity": 10, "unit_price": 25},
        ]

        result = calculate_total_revenue(sales)

        self.assertEqual(result, 2650)


    def test_best_selling_product(self):
        sales = [
            {"product": "Laptop", "quantity": 2, "unit_price": 1200},
            {"product": "Mouse", "quantity": 10, "unit_price": 25},
        ]

        product, units = best_selling_product(sales)

        self.assertEqual(product, "Mouse")
        self.assertEqual(units, 10)


    def test_highest_revenue_product(self):
        sales = [
            {"product": "Laptop", "quantity": 2, "unit_price": 1200},
            {"product": "Mouse", "quantity": 10, "unit_price": 25},
            {"product": "Laptop", "quantity": 1, "unit_price": 1150},
        ]

        product, revenue = highest_revenue_product(sales)

        self.assertEqual(product, "Laptop")
        self.assertEqual(revenue, 3550)


    def test_highest_revenue_product_empty(self):
        product, revenue = highest_revenue_product([])

        self.assertIsNone(product)
        self.assertEqual(revenue, 0)


if __name__ == "__main__":
    unittest.main()
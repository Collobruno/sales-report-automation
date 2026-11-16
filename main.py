
from data_loader import load_sales
from calculations import (
    calculate_total_revenue,
    calculate_total_orders,
    calculate_total_units,
    best_selling_product,
)


def main():
    sales = load_sales("data/sales.csv")

    print("SALES SUMMARY")
    print("-" * 40)

    print(f"Orders Processed : {calculate_total_orders(sales)}")
    print(f"Units Sold       : {calculate_total_units(sales)}")
    print(f"Total Revenue    : ${calculate_total_revenue(sales):,.2f}")

    product, units = best_selling_product(sales)

    print(f"Best Selling Product : {product} ({units} units)")


if __name__ == "__main__":
    main()
from excel_report_generator import generate_excel_report

from report_generator import generate_sales_report
from data_loader import load_sales

from calculations import (
    calculate_total_revenue,
    calculate_total_orders,
    calculate_total_units,
    best_selling_product,
    highest_revenue_product,
)


def main():
    sales = load_sales("data/sales.csv")

    total_orders = calculate_total_orders(sales)
    total_units = calculate_total_units(sales)
    total_revenue = calculate_total_revenue(sales)

    best_product = best_selling_product(sales)
    highest_revenue = highest_revenue_product(sales)

    print("SALES SUMMARY")
    print("-" * 40)

    print(f"Orders Processed : {total_orders}")
    print(f"Units Sold       : {total_units}")
    print(f"Total Revenue    : ${total_revenue:,.2f}")

    print(
        f"Best Selling Product : "
        f"{best_product[0]} ({best_product[1]} units)"
    )

    print(
        f"Highest Revenue Product : "
        f"{highest_revenue[0]} "
        f"(${highest_revenue[1]:,.2f})"
    )


    generate_sales_report(
        total_orders,
        total_units,
        total_revenue,
        best_product,
        highest_revenue,
    )
    generate_excel_report(
    sales,
    total_orders,
    total_units,
    total_revenue,
    best_product,
    highest_revenue,
)
    print("\nReport saved successfully!")


if __name__ == "__main__":
    main()
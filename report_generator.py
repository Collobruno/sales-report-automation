from datetime import datetime


def generate_sales_report(
    orders,
    units,
    revenue,
    best_product,
    highest_revenue_product,
    output_file="reports/sales_report.txt",
):
    """
    Generate a text sales report.
    """

    with open(output_file, "w") as file:

        file.write("SALES REPORT\n")
        file.write("=" * 40 + "\n\n")

        file.write(
            f"Date Generated: {datetime.now().strftime('%d %B %Y')}\n\n"
        )

        file.write("SUMMARY\n")
        file.write("-" * 40 + "\n")
        file.write(f"Orders Processed: {orders}\n")
        file.write(f"Units Sold: {units}\n")
        file.write(f"Total Revenue: ${revenue:,.2f}\n\n")

        file.write("PRODUCT PERFORMANCE\n")
        file.write("-" * 40 + "\n")

        file.write(
            f"Best Selling Product: "
            f"{best_product[0]} ({best_product[1]} units)\n"
        )

        file.write(
            f"Highest Revenue Product: "
            f"{highest_revenue_product[0]} "
            f"(${highest_revenue_product[1]:,.2f})\n"
        )

    return output_file
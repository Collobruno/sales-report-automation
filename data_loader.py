import csv


def load_sales(filename):
    """
    Read and validate sales records from a CSV file.
    Returns a list of valid sales records.
    """
    sales_data = []

    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        required_columns = {
            "date",
            "order_id",
            "product",
            "category",
            "quantity",
            "unit_price",
        }

        if reader.fieldnames is None or not required_columns.issubset(reader.fieldnames):
            raise ValueError("CSV file is missing required columns.")

        for row in reader:
            try:
                # Remove leading/trailing whitespace
                row["date"] = row["date"].strip()
                row["order_id"] = row["order_id"].strip()
                row["product"] = row["product"].strip()
                row["category"] = row["category"].strip()

                # Convert numeric fields
                row["quantity"] = int(row["quantity"])
                row["unit_price"] = float(row["unit_price"])

                # Validate values
                if (
                    not row["product"]
                    or not row["category"]
                    or row["quantity"] <= 0
                    or row["unit_price"] <= 0
                ):
                    continue

                sales_data.append(row)

            except (ValueError, KeyError):
                continue

    return sales_data
from datetime import datetime

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Border, Side, Alignment
from openpyxl.utils import get_column_letter
from openpyxl.chart import BarChart, Reference


def _autosize(ws):
    for col in ws.iter_cols():
        letter = get_column_letter(col[0].column)
        width = max((len(str(c.value)) if c.value is not None else 0) for c in col) + 3
        ws.column_dimensions[letter].width = width


def generate_excel_report(
    sales,
    orders,
    units,
    revenue,
    best_product,
    highest_revenue_product,
    output_file="reports/sales_report.xlsx",
):
    workbook = Workbook()

    summary = workbook.active
    summary.title = "Sales Summary"

    detail = workbook.create_sheet("Product Performance")

    title_font = Font(size=18, bold=True)
    header_font = Font(bold=True, color="FFFFFF")
    header_fill = PatternFill(fill_type="solid", start_color="1F4E78")
    border = Border(
        left=Side(style="thin"),
        right=Side(style="thin"),
        top=Side(style="thin"),
        bottom=Side(style="thin"),
    )
    center = Alignment(horizontal="center")

    summary.merge_cells("A1:B1")
    summary["A1"] = "SALES REPORT"
    summary["A1"].font = title_font
    summary["A1"].alignment = center

    summary["A3"] = "Date Generated"
    summary["B3"] = datetime.now().strftime("%d %B %Y")

    summary["A5"] = "Metric"
    summary["B5"] = "Value"

    for cell in ("A5", "B5"):
        summary[cell].font = header_font
        summary[cell].fill = header_fill
        summary[cell].alignment = center

    rows = [
        ("Orders Processed", orders),
        ("Units Sold", units),
        ("Total Revenue", revenue),
        ("Best Selling Product", best_product[0]),
        ("Best Selling Units", best_product[1]),
        ("Highest Revenue Product", highest_revenue_product[0]),
        ("Highest Product Revenue", highest_revenue_product[1]),
    ]

    r = 6
    for metric, value in rows:
        summary[f"A{r}"] = metric
        summary[f"B{r}"] = value
        summary[f"A{r}"].border = border
        summary[f"B{r}"].border = border
        r += 1

    summary["B8"].number_format = "$#,##0.00"
    summary["B12"].number_format = "$#,##0.00"

    headers = ["Product", "Quantity", "Unit Price", "Revenue"]
    for i, h in enumerate(headers, start=1):
        c = detail.cell(row=1, column=i, value=h)
        c.font = header_font
        c.fill = header_fill
        c.alignment = center

    r = 2
    for sale in sales:
        detail.cell(r, 1, sale["product"])
        detail.cell(r, 2, sale["quantity"])
        detail.cell(r, 3, sale["unit_price"])
        detail.cell(r, 4, sale["quantity"] * sale["unit_price"])
        for c in range(1, 5):
            detail.cell(r, c).border = border
        detail.cell(r, 3).number_format = "$#,##0.00"
        detail.cell(r, 4).number_format = "$#,##0.00"
        r += 1

    _autosize(summary)
    _autosize(detail)

    # -----------------------------
    # Revenue Chart
    # -----------------------------
    chart = BarChart()
    chart.title = "Revenue by Product"
    chart.y_axis.title = "Revenue ($)"
    chart.x_axis.title = "Product"

    data = Reference(detail, min_col=4, min_row=1, max_row=r - 1)
    categories = Reference(detail, min_col=1, min_row=2, max_row=r - 1)

    chart.add_data(data, titles_from_data=True)
    chart.set_categories(categories)
    chart.height = 8
    chart.width = 16

    detail.add_chart(chart, "F2")

    workbook.save(output_file)
    return output_file

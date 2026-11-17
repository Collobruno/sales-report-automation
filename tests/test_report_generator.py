import unittest
import os

from report_generator import generate_sales_report


class TestReportGenerator(unittest.TestCase):

    def setUp(self):
        self.test_file = "tests/test_report.txt"


    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)


    def test_report_creation(self):

        generate_sales_report(
            10,
            37,
            4028,
            ("Mouse", 11),
            ("Laptop", 2550),
            self.test_file,
        )

        self.assertTrue(os.path.exists(self.test_file))


    def test_report_content(self):

        generate_sales_report(
            10,
            37,
            4028,
            ("Mouse", 11),
            ("Laptop", 2550),
            self.test_file,
        )

        with open(self.test_file, "r") as file:
            content = file.read()

        self.assertIn("SALES REPORT", content)
        self.assertIn("Mouse", content)
        self.assertIn("Laptop", content)
        self.assertIn("$4,028.00", content)


if __name__ == "__main__":
    unittest.main()
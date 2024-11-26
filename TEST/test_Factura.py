import unittest
from MODELO.Factura import Bill

class TestBill(unittest.TestCase):
    def test_initialization(self):
        bill = Bill("2024-11-26", 150.0, [])
        self.assertEqual(bill.date, "2024-11-26")
        self.assertEqual(bill.total, 150.0)
        self.assertEqual(len(bill.products), 0)

    def test_add_product(self):
        bill = Bill("2024-11-26", 200.0, [])
        product = {"name": "Product A", "price": 50.0}
        bill.products = product
        self.assertEqual(len(bill.products), 1)
        self.assertIn(product, bill.products)

    def test_associatedTo(self):
        bill = Bill("2024-11-27", 300.0, [])
        product = {"name": "Product B", "price": 75.0}
        bill.associatedTo(product)
        self.assertEqual(len(bill.products), 1)
        self.assertIn(product, bill.products)

    def test_str_method(self):
        bill = Bill("2024-11-28", 450.0, [])
        expected_output = "Fecha: 2024-11-28 Total: 450.0"
        self.assertEqual(str(bill), expected_output)

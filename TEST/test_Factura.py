import unittest
from MODELO.Factura import Bill

class TestBill(unittest.TestCase):
    def setUp(self):
        self.products = [{'name': 'Producto A', 'price': 50}, {'name': 'Producto B', 'price': 150}]
        self.bill = Bill(date="2024-10-27", total=200, products=self.products)

    def test_getters(self):
        """Prueba los getters de los atributos de Bill."""
        self.assertEqual(self.bill.date, "2024-10-27")
        self.assertEqual(self.bill.total, 200)
        self.assertEqual(self.bill.products, self.products)

    def test_setters(self):
        """Prueba los setters de los atributos de Bill."""
        self.bill.date = "2024-10-28"
        self.bill.total = 300
        new_products = [{'name': 'Producto C', 'price': 300}]
        self.bill.products = new_products

        self.assertEqual(self.bill.date, "2024-10-28")
        self.assertEqual(self.bill.total, 300)
        self.assertEqual(self.bill.products, new_products)

if __name__ == '__main__':
    unittest.main()

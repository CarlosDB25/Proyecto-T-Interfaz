import unittest
from MODELO.Cliente import Client
from MODELO.Factura import Bill

class TestClient(unittest.TestCase):
    def setUp(self):
        self.bills = [
            Bill(date="2024-10-27", total=100, products=[{'name': 'Producto A', 'price': 50}]),
            Bill(date="2024-10-28", total=200, products=[{'name': 'Producto B', 'price': 150}])
        ]
        self.client = Client(name="Juan Pérez", id="12345", bills=self.bills)

    def test_getters(self):
        """Prueba los getters de los atributos de Client."""
        self.assertEqual(self.client.name, "Juan Pérez")
        self.assertEqual(self.client.id, "12345")
        self.assertEqual(self.client.bills, self.bills)

    def test_setters(self):
        """Prueba los setters de los atributos de Client."""
        self.client.name = "Ana García"
        self.client.id = "67890"
        new_bills = [Bill(date="2024-10-29", total=300, products=[{'name': 'Producto C', 'price': 300}])]
        self.client.bills = new_bills

        self.assertEqual(self.client.name, "Ana García")
        self.assertEqual(self.client.id, "67890")
        self.assertEqual(self.client.bills, new_bills)

if __name__ == '__main__':
    unittest.main()

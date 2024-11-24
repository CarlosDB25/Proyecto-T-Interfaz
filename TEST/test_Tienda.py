import unittest
from MODELO.Cliente import Client
from MODELO.Factura import Bill
from MODELO.Tienda import Store

class TestStore(unittest.TestCase):
    def setUp(self):
        self.client1 = Client(name="Juan Pérez", id="12345", bills=[
            Bill(date="2024-10-27", total=100, products=[{'name': 'Producto A', 'price': 50}])
        ])
        self.client2 = Client(name="Ana García", id="67890", bills=[
            Bill(date="2024-10-28", total=200, products=[{'name': 'Producto B', 'price': 150}])
        ])
        self.store = Store(clients=[self.client1, self.client2])

    def test_getters(self):
        """Prueba los getters de los atributos de Store."""
        self.assertEqual(self.store.clients, [self.client1, self.client2])

    def test_setters(self):
        """Prueba los setters de los atributos de Store."""
        new_client = Client(name="Luis Martínez", id="54321", bills=[])
        self.store.clients = [new_client]
        self.assertEqual(self.store.clients, [new_client])

if __name__ == '__main__':
    unittest.main()

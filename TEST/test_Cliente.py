import unittest
from MODELO.Cliente import Client
from MODELO.Factura import Bill

class TestClient(unittest.TestCase):
    def test_initialization(self):
        client = Client("Juan Perez", "12345678", [])
        self.assertEqual(client.name, "Juan Perez")
        self.assertEqual(client.id, "12345678")
        self.assertEqual(len(client.bills), 0)

    def test_add_bill(self):
        client = Client("Ana Lopez", "87654321", [])
        bill = {"date": "2024-11-26", "total": 100.0}
        client.bills = bill
        self.assertEqual(len(client.bills), 1)
        self.assertIn(bill, client.bills)

    def test_associatedTo(self):
        client = Client("Luis Garcia", "11223344", [])
        bill = {"date": "2024-11-26", "total": 50.0}
        client.associatedTo(bill)
        self.assertEqual(len(client.bills), 1)
        self.assertIn(bill, client.bills)

    def test_str_method(self):
        client = Client("Carlos Rivera", "99999999", [])
        expected_output = "Documento identidad: 99999999 Nombre: Carlos Rivera"
        self.assertEqual(str(client), expected_output)

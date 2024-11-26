import unittest
from MODELO.Tienda import Store

class TestStore(unittest.TestCase):
    def test_initialization(self):
        clients = []
        store = Store(clients)
        self.assertEqual(len(store.clients), 0)

    def test_add_client(self):
        store = Store([])
        client = {"name": "Juan Perez", "id": "12345678", "bills": []}
        store.clients = client
        self.assertEqual(len(store.clients), 1)
        self.assertIn(client, store.clients)

    def test_associatedTo(self):
        store = Store([])
        client = {"name": "Ana Lopez", "id": "87654321", "bills": []}
        store.associatedTo(client)
        self.assertEqual(len(store.clients), 1)
        self.assertIn(client, store.clients)

from .pCrud import PCrud
from MODELO.Cliente import Client
from MODELO.Tienda import Store as store

class ClientCrud(PCrud):
    def create(self, name, id, store):
        clientRegister = Client(name, id, None)
        store.associatedTo(clientRegister)

        return clientRegister


    def searchBy(self, id, clients):
        clientsRegisters = clients

        for client in clientsRegisters:
            toCompare = client.id
            if toCompare == id:
                return client
                break
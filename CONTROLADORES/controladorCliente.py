from MODELO import Cliente
from CRUD import crudCliente


class ControllerClient:
    @staticmethod
    def create(name, id, store):
        crudInstance = crudCliente.ClientCrud()
        customer = crudInstance.create(name, id, store)
        return customer
    
    @staticmethod
    def searchBy(id, store):
        crudInstance = crudCliente.ClientCrud()
        return crudInstance.searchBy(id, store)
    
from MODELO.Tienda import Store

class ControllerStore:
    _store = None

    @staticmethod
    def create():
        if ControllerStore._store is None:
            ControllerStore._store = Store([])
        return ControllerStore._store

    @staticmethod
    def getStore():
        return ControllerStore._store
    
    @staticmethod
    def updateStore(newStore):
        ControllerStore._store = newStore

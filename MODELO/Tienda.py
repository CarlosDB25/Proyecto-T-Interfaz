
class Store:
    def __init__(self, clients):
        self.__clients = clients

    @property
    def clients(self):
        return self.__clients

    @clients.setter
    def clients(self, client):
        self.__clients.append(client)
    
    def associatedTo(self, client):
        self.clients = client




class Client:
    def __init__(self, name, id, bills):
            self.__name = name
            self.__id = id
            self.__bills = []

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def bills(self):
        return self.__bills

    @bills.setter
    def bills(self, bill):
        self.__bills.append(bill)
    
    def associatedTo(self, bill):
        self.bills = bill

    def __str__(self):
        string = "Documento identidad: {} Nombre: {}".format(self.__id, self.__name)
        return string


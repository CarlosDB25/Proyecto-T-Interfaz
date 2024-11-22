
class Bill:
    def __init__(self, date, total, products):
            self.__date = date
            self.__total = total
            self.__products = []
    
    @property
    def date(self):
        return self.__date
    
    @date.setter
    def date(self, date):
        self.__date = date

    @property
    def total(self):
        return self.__total
    
    @total.setter
    def total(self, total):
        self.__total = total

    @property
    def products(self):
        return self.__products
    
    @products.setter
    def products(self, product):
        self.__products.append(product)
    
    def associatedTo(self, product):
        self.products = product

    def __str__(self):
        string = "Fecha: {} Total: {}".format(self.date, self.total)
        return string

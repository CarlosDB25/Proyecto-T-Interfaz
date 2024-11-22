class ControlProduct:
    def __init__(self, ica, name, price, applicationFrequency):
            self.__ica = ica
            self.__name = name
            self.__price = price
            self.__applicationFrequency = applicationFrequency

    @property
    def ica(self):
        return self.__ica
    
    @ica.setter
    def ica(self, ica):
        self.__ica = ica

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, price):
        self.__price = price

    @property
    def applicationFrequency(self):
        return self.__applicationFrequency
    
    @applicationFrequency.setter
    def applicationFrequency(self, applicationFrequency):
        self.__applicationFrequency = applicationFrequency
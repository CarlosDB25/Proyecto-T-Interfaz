
class Antibiotic:
    def __init__(self, name, price, dose, animalType):
            self.__name = name
            self.__price = price
            self.__dose = dose
            self.__animalType = animalType

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
    def dose(self):
        return self.__dose
    
    @dose.setter
    def dose(self, dose):
        self.__dose = dose

    @property
    def animalType(self):
        return self.__animalType
    
    @animalType.setter
    def animalType(self, animalType):
        self.__animalType = animalType

    def __str__(self):
        string = "- {} - ${}".format(self.name, self.price)
        return string


producto1 = Antibiotic(**{"name": "Penicillin", "price": 25.99, "dose": "500mg", "animalType": "Caprino"})
producto2 = Antibiotic(**{"name": "Amoxicillin", "price": 20.99, "dose": "250mg", "animalType": "caprino"})
producto3 = Antibiotic(**{"name": "Tetracycline", "price": 18.75, "dose": "200mg", "animalType": "Porcino"})
producto4 = Antibiotic(**{"name": "Ciprofloxacin", "price": 30.50, "dose": "400mg", "animalType": "Bovino"})

antibioticsList = [producto1, producto2, producto3, producto4]
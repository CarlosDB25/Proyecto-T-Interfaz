from .pCrud import PCrud
from MODELO import Antibiotico

class AntibioticCrud(PCrud):
    def create(self, name, price, dose, animalType):
        product = Antibiotico.Antibiotic(name, price, dose, animalType)
        Antibiotico.Antibiotic.append(product)

    def searchBy(self, **kwargs):
        pass
from .pCrud import PCrud
from MODELO import ProductoControl 
from MODELO import ControlPlagas 
from MODELO import ControlFertilizantes 

class controlProductCrud(PCrud):
    def create(self, **kwargs):
        if kwargs['type'] == 'Pest':
            product = ControlPlagas.PestControl(kwargs['ica'], kwargs['name'], kwargs['price'], kwargs['applicationFrequency'], kwargs['deficiencyPeriod'])
            ControlPlagas.pestList.append(product)

        elif kwargs['type'] == 'Fertilizer':
            product = ControlPlagas.PestControl(kwargs['ica'], kwargs['name'], kwargs['price'], kwargs['applicationFrequency'], kwargs['lastAdministration'])
            ControlFertilizantes.fertilizersList.append(product)


    def searchBy(self, **kwargs):
        pass
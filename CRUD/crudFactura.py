from datetime import datetime
from .pCrud import PCrud
from MODELO.Factura import Bill
from MODELO.Tienda import Store as store


def getDate():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def getPrices(products):
    prices = []
    for product in products:
        prices.append(product.price)
    return prices


class BillCrud(PCrud):
    def create(self, products):
        billRegister = Bill(getDate(), sum(getPrices(products)), None)
        return billRegister


    def searchBy(self, **kwargs):
        pass

from MODELO import Factura
from CRUD import crudFactura

class ControllerBill:
    @staticmethod
    def create(products, customer):
        crudInstance = crudFactura.BillCrud()
        bill = crudInstance.create(products)

        for product in products:
            bill.associatedTo(product)

        customer.associatedTo(bill)

        return bill
from MODELO.Tienda import Store
from MODELO.Cliente import Client
from MODELO import ControlPlagas
from MODELO import ControlFertilizantes
from MODELO import Antibiotico
from UI import ui
from CRUD import crudCliente, crudFactura
import os

def endBilling(customer, bill, farmStore):
    farmStore.associatedTo(customer)
    print("|     FACTURA     |")
    print(customer)
    print(bill)

    for product in bill.products:
        print(product)

    return farmStore

def billing(productList, crudBill):
    products = ui.getProducts(productList)
    bill = crudBill.create(products=products)

    for product in products:
        bill.associatedTo(product)

    return bill

def makePurchase(productList, crudCustomer, crudBill, farmStore):
    clientData = ui.getClientData()
    customer = crudCustomer.searchBy(id = clientData[1], clients = farmStore.clients)
    os.system('cls')

    if customer == None:
        customer = crudCustomer.create(clientData[0], clientData[1], farmStore)
        os.system('cls')
        print("Cliente creado con éxito.\n\n")

    bill = billing(productList, crudBill)
    customer.associatedTo(bill)
    os.system('cls')
    farmStore = endBilling(customer, bill, crudBill, farmStore)

    return farmStore

def main():
    productList = [ControlPlagas.pestList, ControlFertilizantes.fertilizersList, Antibiotico.antibioticsList]
    farmStore = Store([])
    crudCustomer = crudCliente.ClientCrud()
    crudBill = crudFactura.BillCrud()

    while(True):
        print("\n\n")
        option = ui.mainMenu()
        os.system('cls')

        if((option > 2) or (option < 1)):
            break

        if(option == 1):
            farmStore = makePurchase(productList, crudCustomer, crudBill, farmStore)
            continue

        if(option == 2):
            if(not farmStore.clients):
                print("No hay facturas para mostrar.\n\n")
                continue
            id = ui.getId()
            customer = crudCustomer.searchBy(id = id, clients = farmStore.clients)

            if customer == None:
                print("No se encontró el cliente.\n\n")
                continue
            else:
                print(customer)
                for bill in customer.bills:
                    print("\n|     FACTURA     |")
                    print(bill)
                    for product in bill.products:
                        print(product)
            continue

if __name__ == "__main__":
    main()
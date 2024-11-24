def getProduct(productList):
    counter = 1
    for products in productList:
        for product in products:
            print(f'{counter}.{product.name} - ${product.price}')
            counter += 1

    chosenProduct = int(input("INGRESE EL NUMERO SEGUN EL QUE SEA SU PRODUCTO DESEADO: "))

    if chosenProduct <= 5 and chosenProduct > 0:
        return productList[0][chosenProduct]
    
    elif chosenProduct <= 10 and chosenProduct > 5:
        return productList[1][chosenProduct-5]
    
    else:
        return productList[2][chosenProduct-10]

def getProducts(productlist):
    products = []

    while True:
        products.append(getProduct(productlist))
        option = input("desea terminar la compra s/n ")

        if option == 's':
            return products

def getClientData():
    name = input("Digite su nombre: ")
    id = int(input("Digite su cedula: "))
    return [name, id]

def getId():
    id = int(input("Digite su ID: "))
    return id

def mainMenu():
    option = int((input("MENU PRINCIPAL\n"
            "1. Realizar compra\n"
            "2. Mostrar facturas\n"
            "3  Salir\n\n"
            "Digite la accion: ")))
    return option

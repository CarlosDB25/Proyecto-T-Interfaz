from PyQt6 import QtCore, QtGui, QtWidgets

class ListaComprasWindow(QtWidgets.QWidget):
    def __init__(self, id, customer):
        super().__init__()
        self.setWindowTitle(f"Historial de Compras - {id}")
        self.setGeometry(100, 100, 500, 400)  # Tamaño de la ventana (x, y, ancho, alto)
        
        # Título en la parte superior
        self.titulo_label = QtWidgets.QLabel("Historial de Compras", self)
        self.titulo_label.setGeometry(150, 10, 200, 30)
        self.titulo_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.titulo_label.setFont(QtGui.QFont("Arial", 16, QtGui.QFont.Weight.Bold))

        # Mostrar los datos del customer
        self.customer_label = QtWidgets.QLabel(f"{customer.id}    |    {customer.name}", self)
        self.customer_label.setGeometry(20, 50, 400, 20)
        
        # Crear la lista para mostrar las compras
        self.products_list = QtWidgets.QListWidget(self)
        self.products_list.setGeometry(20, 80, 460, 250)

        bills = customer.bills
        
        # Mostrar datos de las facturas y los productos en la interfaz gráfica
        y_offset = 80  # Espacio inicial para las facturas
        for bill in bills:
            # Mostrar la fecha de la factura
            date_label = QtWidgets.QLabel(f"Fecha: {bill.date}", self)
            date_label.setGeometry(20, y_offset, 400, 20)
            y_offset += 25
            
            # Mostrar los productos de la factura
            for product in bill.products:
                self.products_list.addItem(product)  # Agregar cada compra a la lista en la interfaz
            
            # Mostrar el total de la factura
            total_label = QtWidgets.QLabel(f"Total: ${bill.total}", self)
            total_label.setGeometry(20, y_offset, 400, 20)
            y_offset += 25  # Espacio para la siguiente factura

        self.show()

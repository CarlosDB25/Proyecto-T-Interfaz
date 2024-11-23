from PyQt6 import QtCore, QtGui, QtWidgets

class HistoryListWindow(QtWidgets.QWidget):
    def __init__(self, id, customer):
        super().__init__()
        self.setWindowTitle(f"Historial de Compras - {id}")
        self.setGeometry(100, 100, 600, 500)  # Tamaño ajustado para una mejor disposición
        
        # Diseño principal vertical
        self.layout = QtWidgets.QVBoxLayout(self)
        
        # Título en la parte superior
        self.titulo_label = QtWidgets.QLabel("Historial de Compras", self)
        self.titulo_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.titulo_label.setFont(QtGui.QFont("Arial", 16, QtGui.QFont.Weight.Bold))
        self.layout.addWidget(self.titulo_label)

        # Mostrar los datos del cliente
        self.customer_label = QtWidgets.QLabel(f"ID: {customer.id}    |    Nombre: {customer.name}", self)
        self.customer_label.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Weight.Bold))
        self.layout.addWidget(self.customer_label)

        # Separador visual
        self.addSeparator()

        # Lista para las facturas
        self.bills_list = QtWidgets.QListWidget(self)
        self.bills_list.setFont(QtGui.QFont("Arial", 11))
        self.layout.addWidget(self.bills_list)

        # Llenar la lista con las facturas y sus productos
        self.showList(customer)

    def addSeparator(self):
        """Añade un separador visual al diseño."""
        separator = QtWidgets.QFrame(self)
        separator.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        separator.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.layout.addWidget(separator)

    def showList(self, customer):
        bills = customer.bills
        
        for bill in bills:
            # Agregar la fecha de la factura como encabezado
            date_item = QtWidgets.QListWidgetItem(f"📅 Fecha: {bill.date}")
            date_item.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Weight.Bold))
            date_item.setFlags(QtCore.Qt.ItemFlag.NoItemFlags)  # Deshabilitar edición
            self.bills_list.addItem(date_item)
            
            # Agregar los productos de la factura
            for product in bill.products:
                product_item = QtWidgets.QListWidgetItem(f"    • {product.name} - ${product.price:.2f}")
                product_item.setFont(QtGui.QFont("Arial", 11))
                product_item.setFlags(QtCore.Qt.ItemFlag.NoItemFlags)  # Deshabilitar edición
                self.bills_list.addItem(product_item)
            
            # Agregar el total de la factura
            total_item = QtWidgets.QListWidgetItem(f"💰 Total: ${bill.total:.2f}")
            total_item.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Weight.Bold))
            total_item.setFlags(QtCore.Qt.ItemFlag.NoItemFlags)  # Deshabilitar edición
            self.bills_list.addItem(total_item)
            
            # Separador visual entre facturas
            separator_item = QtWidgets.QListWidgetItem(" ")
            separator_item.setFlags(QtCore.Qt.ItemFlag.NoItemFlags)
            self.bills_list.addItem(separator_item)

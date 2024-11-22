from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QTableWidget, QTableWidgetItem
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class Ui_InvoiceWindow:
    def setupUi(self, MainWindow, clientName, clientId, purchasedItems, bill):
        MainWindow.setWindowTitle("Factura")
        MainWindow.resize(400, 500)
        
        self.centralwidget = QWidget(MainWindow)
        layout = QVBoxLayout(self.centralwidget)

        # Título
        self.titleLabel = QLabel("Factura", self.centralwidget)
        self.titleLabel.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.titleLabel)

        # Información del cliente
        self.clientInfo = QLabel(f"Nombre: {clientName}     |     ID: {clientId}", self.centralwidget)
        self.clientInfo.setFont(QFont("Arial", 12))
        layout.addWidget(self.clientInfo)

        # Fecha
        self.dateLabel = QLabel(f"Fecha: {bill.date}", self.centralwidget)
        self.dateLabel.setFont(QFont("Arial", 12))
        layout.addWidget(self.dateLabel)

        # Espacio para productos
        self.productsLabel = QLabel("Productos:", self.centralwidget)
        self.productsLabel.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        layout.addWidget(self.productsLabel)

        # Tabla de productos
        self.productsTable = QTableWidget(self.centralwidget)
        self.productsTable.setColumnCount(3)  # Tres columnas: Producto, Cantidad, Precio
        self.productsTable.setHorizontalHeaderLabels(["Producto", "Cantidad", "Precio"])
        self.productsTable.setRowCount(len(purchasedItems))  # Ajusta el número de filas según la cantidad de productos
        layout.addWidget(self.productsTable)

        # Llenar la tabla con los productos
        total = bill.total
        for i, (producto, cantidad) in enumerate(purchasedItems):
            precio = f"${producto.price}"  # Solo como ejemplo, puedes calcular el precio real
            self.productsTable.setItem(i, 0, QTableWidgetItem(str(producto)))  # Cambié el tipo de datos a str
            self.productsTable.setItem(i, 1, QTableWidgetItem(str(cantidad)))
            self.productsTable.setItem(i, 2, QTableWidgetItem(precio))

        # Total
        self.totalLabel = QLabel(f"Total: ${total:.2f}", self.centralwidget)
        self.totalLabel.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        self.totalLabel.setAlignment(Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.totalLabel)

        MainWindow.setCentralWidget(self.centralwidget)

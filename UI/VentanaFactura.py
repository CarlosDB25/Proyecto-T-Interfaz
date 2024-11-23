from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QTableWidget, QTableWidgetItem
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QColor

class Ui_InvoiceWindow:
    def setupUi(self, MainWindow, clientName, clientId, purchasedItems, bill):
        MainWindow.setWindowTitle("Factura")
        MainWindow.resize(500, 600)  # Aumentar el tamaño para una mejor distribución
        
        self.centralwidget = QWidget(MainWindow)
        layout = QVBoxLayout(self.centralwidget)
        self.centralwidget.setStyleSheet("background-color: #f4f4f9;")  # Fondo suave
        
        # Título
        self.titleLabel = QLabel("Factura", self.centralwidget)
        self.titleLabel.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.titleLabel.setStyleSheet("color: #4CAF50;")  # Color verde para el título
        layout.addWidget(self.titleLabel)

        # Información del cliente
        self.clientInfo = QLabel(f"Nombre: {clientName}     |     ID: {clientId}", self.centralwidget)
        self.clientInfo.setFont(QFont("Arial", 12))
        self.clientInfo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.clientInfo.setStyleSheet("color: #555555;")  # Color gris para la información
        layout.addWidget(self.clientInfo)

        # Fecha
        self.dateLabel = QLabel(f"Fecha: {bill.date}", self.centralwidget)
        self.dateLabel.setFont(QFont("Arial", 12))
        self.dateLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.dateLabel.setStyleSheet("color: #555555;")  # Color gris para la fecha
        layout.addWidget(self.dateLabel)

        # Espacio para productos
        self.productsLabel = QLabel("Productos:", self.centralwidget)
        self.productsLabel.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        self.productsLabel.setStyleSheet("color: #4CAF50; margin-top: 20px;")  # Título verde para productos
        layout.addWidget(self.productsLabel)

        # Tabla de productos
        self.productsTable = QTableWidget(self.centralwidget)
        self.productsTable.setColumnCount(3)  # Tres columnas: Producto, Cantidad, Precio
        self.productsTable.setHorizontalHeaderLabels(["Producto", "Cantidad", "Precio"])
        self.productsTable.setRowCount(len(purchasedItems))  # Ajusta el número de filas según la cantidad de productos
        
        # Mejorar el estilo de la tabla
        self.productsTable.setStyleSheet("""
            QTableWidget {
                border: none;
                background-color: #ffffff;
                border-radius: 8px;
            }
            QHeaderView::section {
                background-color: #4CAF50;
                color: white;
                padding: 5px;
            }
            QTableWidget::item {
                padding: 10px;
                border-bottom: 1px solid #ddd;
            }
            QTableWidget::item:selected {
                background-color: #f1f1f1;
            }
        """)
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
        self.totalLabel.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        self.totalLabel.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.totalLabel.setStyleSheet("color: #4CAF50; margin-top: 20px;")  # Color verde para el total
        layout.addWidget(self.totalLabel)

        MainWindow.setCentralWidget(self.centralwidget)

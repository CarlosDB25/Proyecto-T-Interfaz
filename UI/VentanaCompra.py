from PyQt6 import QtWidgets, QtCore
import sys
import os

# Agregar el directorio raíz al sys.path
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if root_dir not in sys.path:
    sys.path.append(root_dir)

from MODELO import ControlPlagas, ControlFertilizantes, Antibiotico
from CONTROLADORES import controladorCliente, controladorFactura, controladorTienda
from VentanaFactura import Ui_InvoiceWindow


class Ui_MainWindow(object):
    def __init__(self):
        self.farmStore = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 771, 121))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 50, 49, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(70, 50, 191, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(350, 50, 141, 20))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(500, 50, 191, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 150, 771, 381))
        self.groupBox_2.setObjectName("groupBox_2")

        # Diseño del grid para las columnas
        self.grid_layout = QtWidgets.QGridLayout(self.groupBox_2)

        # Columnas con productos
        self.spin_boxes = []  # Para guardar referencias de los QSpinBox
        self.addProductColumn(
            self.grid_layout,
            0,
            "Productos: Control de Plagas",
            ControlPlagas.pestList,
        )
        self.addProductColumn(
            self.grid_layout,
            1,
            "Productos: Fertilizantes",
            ControlFertilizantes.fertilizersList,
        )
        self.addProductColumn(
            self.grid_layout,
            2,
            "Productos: Antibióticos",
            Antibiotico.antibioticsList,
        )

        # Botón "Terminar Compra"
        self.pushButton = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.pushButton.setText("Terminar Compra")
        self.pushButton.setFixedSize(200, 40)  # Tamaño del botón ajustado
        self.grid_layout.addWidget(
            self.pushButton,
            len(ControlPlagas.pestList) + 3,  # Última fila del grid
            2,  # Columna derecha
            alignment=QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignBottom,
        )
        
        # Conectar el botón para obtener valores y procesarlos
        self.pushButton.clicked.connect(self.handleButtonClick)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def handleButtonClick(self):
        try:
            print(self.farmStore.clients)
            # Procesar datos
            self.farmStore, clientName, clientId, purchasedItems, bill = self.saveClient(self.farmStore)
            controladorTienda.ControllerStore.updateStore(self.farmStore)

            print(self.farmStore.clients)

            # Abrir nueva ventana y pasar farmStore
            self.newWindow = QtWidgets.QMainWindow()
            ui = Ui_InvoiceWindow()
            ui.setupUi(self.newWindow, clientName, clientId, purchasedItems, bill)
            self.newWindow.show()

            # Cerrar la ventana actual
            #QtWidgets.QApplication.instance().activeWindow().close()
        except Exception as e:
            print(f"Error al mostrar la ventana de factura: {e}")

    def addProductColumn(self, layout, column, title, products):
        # Título de la columna
        label_title = QtWidgets.QLabel(self.groupBox_2)
        label_title.setText(f"<b>{title}</b>")
        layout.addWidget(label_title, 0, column * 2, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)

        # Lista de productos con SpinBoxes
        for row, product in enumerate(products, start=1):
            product_label = QtWidgets.QLabel(self.groupBox_2)
            product_label.setText(str(product))
            layout.addWidget(product_label, row, column * 2)

            spin_box = QtWidgets.QSpinBox(self.groupBox_2)
            spin_box.setRange(0, 10)
            layout.addWidget(spin_box, row, column * 2 + 1)

            # Guardar referencia del SpinBox junto con el producto
            self.spin_boxes.append((product, spin_box))

    def getInputData(self):
        # Obtener nombre e identificación del cliente
        clientName = self.lineEdit.text()
        clientId = self.lineEdit_2.text()

        # Obtener productos seleccionados
        purchasedItems = [(product, spin_box.value()) for product, spin_box in self.spin_boxes if spin_box.value() > 0]

        # Retornos necesarios
        return clientName, clientId, purchasedItems

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "REALIZAR COMPRA"))
        self.groupBox.setTitle(_translate("MainWindow", "Datos del Cliente"))
        self.label.setText(_translate("MainWindow", "Nombre:"))
        self.label_2.setText(_translate("MainWindow", "Número de identificación:"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Detalles de la Compra"))

    def saveClient(self, farmStore):
        if farmStore is None:
            farmStore = controladorTienda.ControllerStore.create()

        clientName, clientId, purchasedItems = self.getInputData()

        products = []
        for product, quantity in purchasedItems:
            while quantity > 0:
                products.append(product)
                quantity -= 1

        # Buscar o crear cliente
        customer = controladorCliente.ControllerClient.searchBy(clientId, farmStore.clients)
        if customer is None:
            customer = controladorCliente.ControllerClient.create(clientName, clientId, farmStore)

        # Crear la factura
        bill = controladorFactura.ControllerBill.create(products, customer)

        return farmStore, clientName, clientId, purchasedItems, bill


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    # Inicializar farmStore una vez
    farmStore = controladorTienda.ControllerStore.create()

    # Configurar la ventana principal con el farmStore
    ui = Ui_MainWindow()
    ui.farmStore = farmStore  # Pasar la referencia de farmStore a la ventana principal
    ui.setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec())

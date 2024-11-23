from PyQt6 import QtCore, QtGui, QtWidgets
import sys
from VentanaCompra import Ui_MainWindow as ShopForm
from VentanaFactura import Ui_InvoiceWindow as BillInfo
from VentanaBuscar import HistoryWindow as SearchForm
from VentanaHistorial import HistoryListWindow

from CONTROLADORES import controladorTienda, controladorCliente, controladorFactura  # Asegúrate de importar FarmStore

class Ui_MainWindow(object):
    def __init__(self):
        # Obtén la instancia única de farmStore desde el controlador
        self.farmStore = controladorTienda.ControllerStore.create()
        if self.farmStore is None:
            print("Error: No se ha creado una instancia de Store.")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)  # Aumenté el tamaño para una mejor distribución visual
        MainWindow.setStyleSheet(
            """
            QMainWindow {
                background-color: #f0f0f0;
            }
            QLabel {
                font-family: Arial;
                font-size: 14px;
                color: #333333;
            }
            QPushButton {
                font-family: Arial;
                font-size: 12px;
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            """
        )

        # Central widget
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Etiqueta de bienvenida
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 20, 120, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_2.setFont(QtGui.QFont("Arial", 16, QtGui.QFont.Weight.Bold))

        # Etiqueta de instrucciones
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 60, 250, 20))
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label.setFont(QtGui.QFont("Arial", 12))

        # Botón: Hacer compra
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(125, 100, 150, 40))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.openShopWindow)

        # Botón: Ver historial de compras
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(125, 160, 150, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.openHistoryWindow)

        MainWindow.setCentralWidget(self.centralwidget)

        # Menú y barra de estado
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sistema de Administración de Ventas"))
        self.pushButton.setText(_translate("MainWindow", "Hacer Compra"))
        self.pushButton_2.setText(_translate("MainWindow", "Ver Historial de Compras"))
        self.label.setText(_translate("MainWindow", "Seleccione la opción que desee:"))
        self.label_2.setText(_translate("MainWindow", "¡Bienvenido!"))

    def handleButtonClick(self, window, windowContainer):
        try:
            # Procesar datos
            window.farmStore, clientName, clientId, purchasedItems, bill = self.saveClient(window.farmStore, window)
            controladorTienda.ControllerStore.updateStore(window.farmStore)
            # Cerrar la ventana actual
            windowContainer.close()

            #mostrar la ventana de menu de nuevo
            MainWindow.show()

            # Abrir nueva ventana y pasar farmStore
            window.newWindow = QtWidgets.QMainWindow()
            billP = BillInfo()
            billP.setupUi(window.newWindow, clientName, clientId, purchasedItems, bill)
            window.newWindow.show()
            
        except Exception as e:
            print(f"Error al mostrar la ventana de factura: {e}")

    def getInputData(self, window):
        # Obtener nombre e identificación del cliente
        clientName = window.lineEdit.text()
        clientId = window.lineEdit_2.text()

        # Obtener productos seleccionados
        purchasedItems = [(product, spin_box.value()) for product, spin_box in window.spin_boxes if spin_box.value() > 0]

        # Retornos necesarios
        return clientName, clientId, purchasedItems

    def saveClient(self, farmStore, window):
        if farmStore is None:
            farmStore = controladorTienda.ControllerStore.create()

        clientName, clientId, purchasedItems = self.getInputData(window)

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

    def openShopWindow(self):
        try:
            self.farmStore = controladorTienda.ControllerStore.getStore()
            self.newWindow = QtWidgets.QMainWindow()
            uiCompra = ShopForm()
            uiCompra.farmStore = self.farmStore # Pasar la referencia de farmStore a la ventana principal
            uiCompra.setupUi(self.newWindow)
            self.newWindow.show()
            MainWindow.hide()
            uiCompra.pushButtonT.clicked.connect(lambda: self.handleButtonClick(uiCompra, self.newWindow))
        except Exception as e:
            print(e)

    def handleSearchClick(self, windowS):
        id = windowS.id_input.text().strip()
        if not id:
            QtWidgets.QMessageBox.warning(windowS, "Error", "Por favor, ingrese una identificación.")
            return

        self.farmStore = controladorTienda.ControllerStore.getStore()

        # Buscar cliente
        customer = controladorCliente.ControllerClient.searchBy(id, self.farmStore.clients)
        if customer is None:
            QtWidgets.QMessageBox.warning(windowS, "Error", "Cliente no encontrado.")
        else:
            self.showList(windowS, id, customer)

    def showList(self, windowS, id, customer):
        windowS.listaWindow = HistoryListWindow(id, customer)
        MainWindow.show()  # Muestra la ventana principal
        windowS.listaWindow.show()
        self.searchWindow.hide()# Cierra la ventana actual de búsqueda


    def openHistoryWindow(self):
        try:
            self.farmStore = controladorTienda.ControllerStore.getStore()
            if self.farmStore is None:
                QtWidgets.QMessageBox.warning(None, "Error", "No se ha podido acceder a la tienda.")
                return
            elif self.farmStore.clients == []:
                QtWidgets.QMessageBox.warning(None, "Error", "No hay clientes registrados.")
                return

            # Crea la ventana de historial correctamente
            self.searchWindow = SearchForm()  # Ya no se usa QMainWindow aquí
            self.searchWindow.show()
            MainWindow.hide()

            # Conectar el evento de búsqueda
            self.searchWindow.buscar_button.clicked.connect(lambda: self.handleSearchClick(self.searchWindow))
        except Exception as e:
            print(f"Error al abrir el historial: {e}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  
    MainWindow = QtWidgets.QMainWindow()    
    ui = Ui_MainWindow()                    
    ui.setupUi(MainWindow)  
    MainWindow.show()                       
    sys.exit(app.exec())

from PyQt6 import QtCore, QtGui, QtWidgets
import sys
from VentanaCompra import Ui_MainWindow as ShopForm
from CONTROLADORES import controladorTienda  # Asegúrate de importar FarmStore

class Ui_MainWindow(object):
    def __init__(self):
        # Obtén la instancia única de farmStore desde el controlador
        self.farmStore = controladorTienda.ControllerStore.create()
        if self.farmStore is None:
            print("Error: No se ha creado una instancia de Store.")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(310, 233)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 60, 111, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.openShopWindow)
        
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 120, 151, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 30, 171, 21))
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 10, 71, 16))
        self.label_2.setObjectName("label_2")
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 310, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SISTEMA DE ADMINISTRACION DE VENTAS"))
        self.pushButton.setText(_translate("MainWindow", "Hacer Compra"))
        self.pushButton_2.setText(_translate("MainWindow", "Ver Historial de compras"))
        self.label.setText(_translate("MainWindow", "Seleccione la opcion que desee:"))
        self.label_2.setText(_translate("MainWindow", "BIENVENIDO"))

    def openShopWindow(self):
        try:
            self.farmStore = controladorTienda.ControllerStore.getStore()
            self.newWindow = QtWidgets.QMainWindow()
            ui = ShopForm()
            ui.farmStore = self.farmStore # Pasar la referencia de farmStore a la ventana principal
            ui.setupUi(self.newWindow)
            self.newWindow.show()
            MainWindow.hide()
            ui.pushButton.clicked.connect(self.handleButtonClick)
        except Exception as e:
            print(e)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  
    MainWindow = QtWidgets.QMainWindow()    
    ui = Ui_MainWindow()                    
    ui.setupUi(MainWindow)  
    MainWindow.show()                       
    sys.exit(app.exec())

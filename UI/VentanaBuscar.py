from PyQt6 import QtCore, QtGui, QtWidgets
import os
from VentanaHistorial import ListaComprasWindow  # Importar la clase ListaComprasWindow
from CONTROLADORES import controladorCliente, controladorTienda



class HistorialComprasWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("HISTORIAL DE COMPRAS")
        self.setGeometry(100, 100, 400, 200)  # Tamaño de la ventana (x, y, ancho, alto)
        
        # Crear el campo de texto para ingresar la identificación
        self.label = QtWidgets.QLabel("Ingrese su identificación:", self)
        self.label.setGeometry(20, 30, 200, 20)
        
        self.id_input = QtWidgets.QLineEdit(self)
        self.id_input.setGeometry(20, 60, 260, 30)
        
        # Crear el botón de buscar
        self.buscar_button = QtWidgets.QPushButton("Buscar", self)
        self.buscar_button.setGeometry(290, 60, 100, 30)
        self.buscar_button.clicked.connect(self.buscarHistorial)
        
        # Mostrar la ventana
        self.show()
    
    def buscarHistorial(self):
        id = self.id_input.text()
        farmStore = controladorTienda.ControllerStore.getStore()  # Asumiendo que 'getStore' es correcto
        if farmStore is None:
            QtWidgets.QMessageBox.warning(self, "Error", "No hay clientes registrados.")
            # Aquí puedes cerrar la ventana y volver al menú principal si es necesario
            self.close()  # Cerrar la ventana actual
        elif id:
            customer = controladorCliente.ControllerClient.searchBy(id=id, clients=farmStore.clients)
            if customer is None:
                QtWidgets.QMessageBox.warning(self, "Error", "Cliente no encontrado.")
            else:
                self.mostrarLista(id, customer)
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Por favor ingrese una identificación.")

    def mostrarLista(self, id, customer):
        self.listaWindow = ListaComprasWindow(id, customer)  # Abrir la ventana con la lista
        self.listaWindow.show()
        self.close()  # Cerrar la ventana actual al abrir la lista


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = HistorialComprasWindow()  # Abrir la ventana principal
    sys.exit(app.exec())

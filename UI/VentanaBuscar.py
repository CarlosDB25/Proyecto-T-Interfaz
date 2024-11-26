from PyQt6 import QtCore, QtGui, QtWidgets
import os
import sys
from VentanaHistorial import HistoryListWindow  # Importar la clase HistoryListWindow
from CONTROLADORES import controladorCliente, controladorTienda, controladorFactura
from MODELO.Antibiotico import antibioticsList


class HistoryWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Historial de Compras")
        self.setGeometry(100, 100, 450, 250)  # Tamaño ajustado para mayor espacio

        # Diseño vertical principal
        layout = QtWidgets.QVBoxLayout(self)

        # Título
        title_label = QtWidgets.QLabel("Consulta tu Historial de Compras")
        title_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        title_label.setFont(QtGui.QFont("Arial", 16, QtGui.QFont.Weight.Bold))
        layout.addWidget(title_label)

        # Espaciador
        layout.addSpacing(20)

        # Etiqueta de entrada
        input_label = QtWidgets.QLabel("Ingrese su identificación:")
        input_label.setFont(QtGui.QFont("Arial", 12))
        layout.addWidget(input_label)

        # Campo de entrada
        self.id_input = QtWidgets.QLineEdit()
        self.id_input.setPlaceholderText("Ejemplo: 12345")
        self.id_input.setFont(QtGui.QFont("Arial", 12))
        self.id_input.setFixedHeight(30)
        layout.addWidget(self.id_input)

        # Botón de búsqueda
        self.buscar_button = QtWidgets.QPushButton("Buscar")
        self.buscar_button.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Weight.Bold))
        self.buscar_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.buscar_button.setStyleSheet(
            "background-color: #4CAF50; color: white; padding: 10px; border-radius: 5px;"
        )
        layout.addWidget(self.buscar_button)

        # Alineación del botón al centro
        layout.setAlignment(self.buscar_button, QtCore.Qt.AlignmentFlag.AlignHCenter)

        # Estilo de ventana
        self.setStyleSheet(
            """
            QWidget {
                background-color: #f5f5f5;
            }
            QLabel {
                color: #333333;
            }
            QLineEdit {
                border: 1px solid #cccccc;
                border-radius: 5px;
                padding: 5px;
                background-color: #ffffff;
            }
            """
        )

        # Mostrar la ventana
        self.show()


from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QMainWindow, QTableWidget, QTableWidgetItem, 
    QPushButton, QVBoxLayout, QWidget, QLineEdit, QLabel, 
    QSpinBox, QGridLayout, QMessageBox)
 
class ClientesWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cadastro de Clientes")
        self.setGeometry(0,0, 600, 400)
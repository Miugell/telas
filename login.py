
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QGridLayout, QVBoxLayout,
    QLabel, QLineEdit, QPushButton
)
#! CLASSE FILHO DE QMAINWINDOW 
class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login") #! nome da janela

        self.setGeometry(0, 0, 800, 300) #! posição e tamanho da janela 
        #? Atributos da Janela
        self.loginWidget = QWidget() # base
        self.vLayout = QVBoxLayout()# Layout

        # Configurando o layout principal
        self.setCentralWidget(self.loginWidget)
        self.loginWidget.setLayout(self.vLayout)

app = QApplication()
meu_login = LoginWindow() #! Objeto da classe que criamos 

meu_login.show()
app.exec()
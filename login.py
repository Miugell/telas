
from time import process_time_ns
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QGridLayout, QVBoxLayout,
    QLabel, QLineEdit, QPushButton
)

from PySide6.QtGui import QPixmap #? Controla imagens no PySide
from PySide6.QtCore import Qt #? Qt possui muitos valores úteis

#! CLASSE FILHO DE QMAINWINDOW 
class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login") #! nome da janela
        self.setGeometry(0, 0, 600, 300) #! posição e tamanho da janela 
        #! FIXAR TAMANHO DA JANELA - não deixa diminuir nem aumentar
        self.setFixedSize(self.width(), self.height())
        self.center_on_screen()

        #? Atributos da Janela
        self.loginWidget = QWidget() # base
        self.vLayout = QVBoxLayout()# Layout
        self.vLayout.setAlignment(Qt.AlignTop)
        #self.vLayout.setSpacing()

        #^ Configurando o layout principal
        self.setCentralWidget(self.loginWidget)
        self.loginWidget.setLayout(self.vLayout)

        #^ ADICIONANDO IMAGEM 
        self.logo_label = QLabel(self.loginWidget)
        self.pixmap = QPixmap('img/login-icon.png')
        self.pixmap = self.pixmap.scaled(80, 80, Qt.KeepAspectRatio)
        self.logo_label.setPixmap(self.pixmap)
        self.logo_label.setAlignment(Qt.AlignCenter)


         #! adicionando imagem (logo_label) no layout   
        self.vLayout.addWidget(self.logo_label)

        #?Caixa de email e senha
        self.email_label = QLabel("Emai: ")
        self.email_lineEdit = QLineEdit()
        self.senha_label = QLabel("Senha: ")
        self.senha_lineEdit = QLineEdit()
        #! Ocultandoa  senha digitada
        self.senha_lineEdit.setEchoMode(QLineEdit.Password)
        #* Adicionando email e senha no Layout
        self.vLayout.addWidget(self.email_label)
        self.vLayout.addWidget(self.email_lineEdit)
        self.vLayout.addWidget(self.senha_label)
        self.vLayout.addWidget(self.senha_lineEdit)

        #? Botão
        self.login_button = QPushButton("ENTRAR")
        #* Adicionando o botão no layout
        self.vLayout.addWidget(self.login_button)
        #?Slot signal
        self.login_button.clicked.connect(self.ler_credenciais)

    def ler_credenciais(self):
        #* recebendo e gravando valores
        email = self.email_lineEdit.text() # pega o texto digitado
        senha = self.email_lineEdit.text()
        print(f"Email: {email}") 
        print(f"Senha: {senha}") 

    def center_on_screen(self):
        #Retorna a geometria da janela em relação ao sistema...
        #... de coordenadas da área de trabalho.
        # Isso inclui as posições x e y da janela, bem como a largura e altura
        qr = self.frameGeometry()
        #Obtém a geometria da tela primária...
        # (aquela onde a aplicação principal esta sendo executada) e,
        #em seguida, calcula o ponto central dessa geometria.
        cp = QApplication.primaryScreen().geometry().center()
        #Move a geometria da janela (qr) para que seu ponto central (moveCenter)...
        #...coincida com o ponto centrar da tela (cp).
        qr.moveCenter(cp)
        #move a janela para a posição superior esquerda da...
        #geometria ajustada, garantindo que...
        #a janela esteja centralizada na tela.
        self.move(qr.topLeft())


app = QApplication()
meu_login = LoginWindow() #! Objeto da classe que criamos 

meu_login.show()
app.exec()
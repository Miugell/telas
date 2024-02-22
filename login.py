from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QLabel, QLineEdit, QPushButton, QMessageBox
)
from PySide6.QtGui import QPixmap #? Controla imagens no PySide
from PySide6.QtCore import Qt, Signal #? Qt possui muitos valores úteis
 
import qdarkstyle
 
#! CLASSE FILHO DE QMAINWINDOW
class LoginWindow(QMainWindow):
    #Criando um Signal próprio
    sucesso_login = Signal()
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login") #! nome da janela
        self.setGeometry(0, 0, 600, 300) #! posição e tamanho da janela
        #& Fixar tamanho da janela - não deixa diminuir
        #& nem deixa aumentar  (maximizar)
        self.setFixedSize(self.width(), self.height())
        self.center_on_screen()
 
        #? Atributos da Janela -----------------------
 
        # Configurando o formulário de login
        self.loginWidget = QWidget() #base
        self.vLayout = QVBoxLayout() #layout
        self.vLayout.setAlignment(Qt.AlignTop)
        #self.vLayout.setSpacing(37)
 
        # Configurando o layout principal
        self.setCentralWidget(self.loginWidget)
        self.loginWidget.setLayout(self.vLayout)
 
        # Aplicar estilo escuro
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())
 
        #Adicionando imagem da logo
        self.logo_label = QLabel(self.loginWidget)
        self.pixmap = QPixmap('img/login-icon.png') 
        self.pixmap = self.pixmap.scaled(80, 80, Qt.KeepAspectRatio)
        self.logo_label.setPixmap(self.pixmap)
        self.logo_label.setAlignment(Qt.AlignCenter)
 
        #! Adicionando imagem (logo_label) no Layout
        self.vLayout.addWidget(self.logo_label)
 
        #? Caixa de email e senha
        self.email_label = QLabel("Email:")
        self.email_lineEdit = QLineEdit()
        self.senha_label = QLabel("Senha:")
        self.senha_lineEdit = QLineEdit()
        #! Ocultando a senha digitada
        self.senha_lineEdit.setEchoMode(QLineEdit.Password)
        #* Adicionando email e senha no LAYOUT 
        self.vLayout.addWidget(self.email_label)
        self.vLayout.addWidget(self.email_lineEdit)
        self.vLayout.addWidget(self.senha_label)
        self.vLayout.addWidget(self.senha_lineEdit)
 
        #? Botão
        self.login_button = QPushButton("Entrar")
        #* Adicionando o botão no layout
        self.vLayout.addWidget(self.login_button)
        #? SLOT E SIGNAL
        self.login_button.clicked.connect(self.tentar_login)
    
    def tentar_login(self):
        if self.ler_credenciais() == True:
            #& Emit - Manda sinal verde pro Signal criado
            self.sucesso_login.emit()
            self.close()
        else:
            self.aviso_erro_login("O usuário e/ou a senha estão incorretos")
 
    def ler_credenciais(self):
        #* Recebendo e gravando valores
        email = self.email_lineEdit.text() #pega o texto digitado
        senha = self.senha_lineEdit.text()
        if email == "miguel@email.com" and senha == "miguel123":
            #Retorna verdadeiro
            return True
        else:
            return False
 
    def aviso_erro_login(self, texto):
        msgBox = QMessageBox()
        msgBox.setText(texto)
        msgBox.setIcon(msgBox.Icon.Question)
        msgBox.exec()
 
    def center_on_screen(self):
        # Retorna a geometria da janela em relação ao sistema ...
        # ...de coordenadas da área de trabalho. 
        #Isso inclui as posições x e y da janela, bem como a largura e altura.
        qr = self.frameGeometry()
        #Obtém a geometria da tela primária ...
        # (aquela onde a aplicação principal está sendo executada) e, 
        #em seguida, calcula o ponto central dessa geometria.
        cp = QApplication.primaryScreen().geometry().center()
        #Move a geometria da janela (qr) para que seu ponto central (moveCenter)... 
        #...coincida com o ponto central da tela (cp).
        qr.moveCenter(cp)
        #move a janela para a posição superior esquerda da ...
        # geometria ajustada, garantindo que ...
        #...a janela esteja centralizada na tela.
        self.move(qr.topLeft())

#! IMPORTAÇÕES INICIAIS
import sys
from PySide6.QtCore import Slot #^ para nomear as funções slot
from PySide6.QtGui import QFont
from PySide6.QtWidgets import(
    QApplication, QMainWindow, QWidget, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSpinBox
)
#? FUNÇÃO QUE SERÁ CHAMADA PELA ACTION 'MUDAR MENSAGEM'
@Slot
def muda_status(status_bar):
    status_bar.showMessage("Mensagem foi trocada")

#? O signal toggled passa de forma oculta um argumento/parâmetro
#? O esta_marcado é um parâmetro reponsavel por receber essa informação
@Slot
def ao_mudar_marcacao(esta_marcado):
    print("A marcação mudou!\n Agora foi para: ", esta_marcado)

#* AO RETORNARMOS ELA, ESTAMOS JOGANDO ELA PRO CONNECT
#* ELA ESTA ATRASANDO A EXECUÇÃO DO AO_MUDAR_MARCAÇÃO IGUAL UM LAMBDA
#& Assim o Connerct recever o inner (returno) onde a ação do inner 
#& Quando o signal for chamado é chamar o 'ao_mudar_marcacao'
@Slot
def chamar_outro_slot(acao):
    def inner():
        ao_mudar_marcacao(acao.isChecked())
    return inner

#!--------------------------------------
app = QApplication(sys.argv)
janela = QMainWindow()
centarlWidget = QWidget()
layout = QGridLayout()
#!--------------------------------------
#*--------------------------------------
font_label = QFont()
font_label.setPixelSize(30) #? Configura i, tamanho de fontepara uma VARIÁVEL

#Labels
nome_label = QLabel("Nome: ")
email_label = QLabel("Email: ")
idade_label = QLabel("Idade: ")
#* Configurando fonte padrão dos Labels
nome_label.setFont(font_label)
email_label.setFont(font_label)
idade_label.setFont(font_label)

#Inputs
nome_line_edit = QLineEdit()
email_line_edit = QLineEdit()
idade_spin_box = QSpinBox()

#Button
save_button = QPushButton("Confirmar")
save_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: #ffffff;
                border: none;
                padding: 10px;
                margin: 5px;
                border-radius: 5px;

            }
""")
#& PARES - LABEL - INPUT
nome_label.setBuddy(nome_line_edit)
email_label.setBuddy(email_line_edit)
idade_label.setBuddy(idade_spin_box)

#? POSICIONANDO NO LAYOUT
layout.addWidget(nome_label, 0, 0)
layout.addWidget(nome_line_edit, 0, 1)
layout.addWidget(email_label, 1, 0)
layout.addWidget(email_line_edit, 1, 1)
layout.addWidget(idade_label , 2, 0)
layout.addWidget(idade_spin_box, 2, 1)
layout.addWidget(save_button, 3, 0, 1, 2)

#&--------------------------------------
#& STATUS BAR E MENU BAR
status_bar = janela.statusBar()
status_bar.showMessage("Mensagem na barra")

menu = janela.menuBar()
menu_arquivo = menu.addMenu("Arquivo")
acao_mensagem = menu_arquivo.addAction("Mudar Mensagem")
#^ triddered = signal
#^ a função munda_status = slot
#^ lambda - FUNÇÃO ANÔNIMA
acao_mensagem.triggered.connect(
    lambda : muda_status(status_bar))

acao_marcado = menu_arquivo.addAction("Marcar")
#!TRANSFORMANDO ELA EM CHEKABLE (Liga e desliga)
acao_marcado.setCheckable(True)
#! ADICIONANDO O SIGNAL - E CONECTANDO COM ALGUM SLOT
acao_marcado.toggled.connect(ao_mudar_marcacao)


#? NOVO SIGNAL HOVERED - AO PASSAR O MOUSE SOBRE...
acao_marcado.hovered.connect(chamar_outro_slot(acao_marcado))


#&--------------------------------------


#*--------------------------------------
#!--------------------------------------
#! COLOCANDO UM DENTRO DO OUTRO
janela.setCentralWidget(centarlWidget)
centarlWidget.setLayout(layout)
janela.show()
app.exec()
#!--------------------------------------

from cProfile import label
from pydoc import cli
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QMainWindow, QTableWidget, QTableWidgetItem, 
    QPushButton, QVBoxLayout, QWidget, QLineEdit, QLabel, 
    QSpinBox, QGridLayout, QMessageBox, QApplication)


import qdarkstyle

class Cliente:
    def __init__(self, nome, email, idade):
        self.nome = nome
        self.email = email
        self.idade = idade

class ClientesWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cadastro de Clientes")
        self.setGeometry(0,0, 600, 400)
        self.lista_clientes = []
        #Vertical Layout
        v_layout = QVBoxLayout()
        self.center_on_screen()

        #! Desenhando tabela
        self.table = QTableWidget(self)
        #?numero de colunas
        self.table.setColumnCount(3)
        #? nome das colunas
        self.table.setHorizontalHeaderLabels(["Nome", "Idade", "Email"])

        # defina tamanhos dixos para as colunas
        self.table.setColumnWidth(0, 200)
        self.table.setColumnWidth(1, 80)
        self.table.setColumnWidth(2, 250)
        #Esticar a última coluna
        self.table.horizontalHeader().setStretchLastSection(True)
        v_layout.addWidget(self.table)

        #! base (central widget)
        centralWidget = QWidget()
        centralWidget.setLayout(v_layout)
        self.setCentralWidget(centralWidget)

        #! inputs para cadastro de Clientes
        label_font = QFont()
        label_font.setPixelSize(18)

        #? Labels
        label_nome = QLabel("Nome")
        label_idade = QLabel("Idade")
        label_email = QLabel("Email")
        #? Setando font
        label_nome.setFont(label_font)
        label_idade.setFont(label_font)
        label_email.setFont(label_font)

        #? Inputs
        self.ln_nome = QLineEdit()
        self.ln_nome.setPlaceholderText("Digite um nome ")
        self.ln_email = QLineEdit()
        self.ln_email.setPlaceholderText("digite um email")
        self.ln_email.returnPressed.connect(self.adicionar_cliente)
        self.sb_idade = QSpinBox()
        

        #?Setando Font nos Inputs
        self.ln_nome.setFont(label_font)
        self.ln_nome.setFont(label_font)
        self.sb_idade.setFont(label_font)

        #! Configurando os pares
        label_nome.setBuddy(self.ln_nome)
        label_email.setBuddy(self.ln_email)
        label_idade.setBuddy(self.sb_idade)

        #* Botões
        self.btn_adicionar = QPushButton("Adicionar Cliente")
        self.btn_deletar = QPushButton("Deletar Cliente")

        #!Conectar signal aos slots
        self.btn_adicionar.clicked.connect(self.adicionar_cliente)
        self.btn_deletar.clicked.connect(self.deletar_cliente)
        
        
        
        self.grid_layout = QGridLayout()
        self.grid_layout.addWidget(label_nome, 0, 0)
        self.grid_layout.addWidget(self.ln_nome, 0, 1)

        self.grid_layout.addWidget(label_idade, 0, 2)
        self.grid_layout.addWidget(self.sb_idade, 0, 3)

        self.grid_layout.addWidget(label_email, 1, 0)
        self.grid_layout.addWidget(self.ln_email, 1, 1)

        #& Adicionando o Grid dentro do V_Layout
        v_layout.addLayout(self.grid_layout)

        #& adicionando botões no v_layout
        v_layout.addWidget(self.btn_adicionar)
        v_layout.addWidget(self.btn_deletar)

        # aplicar o estilo dark
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())

    def adicionar_cliente(self):
        if self.ln_nome.text() == "":
            self.mostrar_erro("O nome do cliente não foi informado")
            return

        if self.ln_email.text() =="":
            self.mostrar_erro("O email do cliente não foi informado")
            return

        if self.sb_idade.value() == 0:
            self.mostrar_erro("A idade do cliente não foi informada")
            return

        cliente = Cliente(
            self.ln_nome.text(),
            self.ln_email.text(),
            self.sb_idade.value()
        )
        self.lista_clientes.append(cliente)
        self.limpar_campos()
        self.atualizar_tabela()
        for c in self.lista_clientes:
            print(c.nome)

    def deletar_cliente(self):
        if self.table.currentRow() != -1:
            del self.lista_clientes[self.table.currentRow()]
            self.atualizar_tabela()

    def atualizar_tabela(self):
        self.table.setRowCount(len(self.lista_clientes))
        for linha, cliente in enumerate(self.lista_clientes):
            self.table.setItem(linha, 0, QTableWidgetItem(cliente.nome))
            self.table.setItem(linha, 1, QTableWidgetItem(str(cliente.idade)))
            self.table.setItem(linha, 2, QTableWidgetItem(cliente.email))
 


    #? Ao adicionar cliente irá limpar os campos
    def limpar_campos(self):
        self.ln_nome.clear()
        self.ln_email.clear()
        self.sb_idade.clear()
    #! Quando faltar uma informação, o programa ira avisar
    def mostrar_erro(self, texto):
        msgBox = QMessageBox()
        msgBox.setText(texto)
        msgBox.setIcon(msgBox.Icon.Question)
        msgBox.exec()

    def center_on_screen(self):
       
        qr = self.frameGeometry()
        
        cp = QApplication.primaryScreen().geometry().center()
        
        qr.moveCenter(cp)
        
        self.move(qr.topLeft())
    
    #& Métodos úteis
from PySide6.QtWidgets import QApplication
 
#? login - nome do módulo que criamos (Arquivo Python)
#? LoginWindow - É a classe que criamos e importamos de login.py
from login import LoginWindow
from clientesWindow import ClientesWindow
 
#* __name__ - é o nome do arquivo (variavel)
#* __main__ - é o arquivo principal (utilizado o comando python ...py)
#? A checagem pergunta: "o arquivo atual é o principal?"
#? Isso protege para que SE um outro arquivo importe o main
#? ele não execute as linhas internas
if __name__ == "__main__":
    app = QApplication()
    meu_login = LoginWindow() #! objeto da classe que criamos
    clientes_window = ClientesWindow()
    
    #! 'preparamos' o show do clientes_window quando o
    #! signal 'sucesso_login' for emitido
    meu_login.sucesso_login.connect(clientes_window.show)
    meu_login.show()
    app.exec() 
import mysql.connector
def conectaBD():
    conexao = mysql.connector.connect(host='localhost', user="root", password="", database="george")
    if conexao.is_connected():
        print("BD conectado com sucesso!!")
        return conexao
import sqlite3 
from pathlib import Path
# Criando uma  conexão com o banco de dados sqlite3

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "clientes.db")
cursor = conexao.cursor()
print (conexao)

# Criando uma tabela de Banco de Dados

def criar_tabela (cursor):
    cursor.execute("CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT , nome VALCHER(100), email VALCHER(150) )")


def inserir_registro(conexao, cursor,nome,email):
    dados = ("Kyuichi", "Kyuichi@email.com")
    cursor.execute("INSERT INTO clientes (nome , email) VALUES (?, ?) ", dados )
    # INportante comitar os dados !
    conexao.commit()

# Criamos uma função para inserir registros no banco de dados
def atualizar_registro(conexao, cursor ,nome,email,id):
    data = (nome,email,id)
    cursor.execute("UPDATE clientes SET nome=? , email=? WHERE  id=? ; ", data )
    conexao.commit()

# Criamos uma função para inserir registros no banco de dados
def remover_registro(conexao, cursor ,id):
    data = (id,)
    cursor.execute("DELETE FROM clientes WHERE id=? ; ", data )
    conexao.commit()
# Criamos um metodo de deletar os registros do banco de dados .

#Criando varios clientes .
def inserir_muitos_registros(conexao, cursor ,dados): # as letras  em maiusculo são as variaveis que vamos usar em bancos de dados.
    cursor.executeamany("INSERT INTO clientes ( nome,email) VALUES (?,?)",dados)
    conexao.commit()

def mostrar_cliente(cursor, id):
    cursor.execute("SELECT * FROM clientes WHERE id=?" , (id,))# id é uma tupla por isso tem que ter uma virgula.
    return cursor.fetchone()

def listar_clientes(cursor):
    return cursor.execute("SELECT * FROM clientes;")

cliente = mostrar_cliente(cursor , 2)
print(cliente)

clientes= listar_clientes(cursor)

for cliente in clientes:
    print(cliente)



#dados = [
#    ("karina", "karina@gmail.com"),
 #   ("eduardo", "eduardo@gmail.com"),
  #  ("thayna", "thayna@gmail.com"),
   # ("bianca", "biaca@gmail.com"),
#]




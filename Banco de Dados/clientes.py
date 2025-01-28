import sqlite3 
from pathlib import Path
# Criando uma  conexão com o banco de dados sqlite3

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "clientes.db")
print (conexao)

# Criando uma tabela de Banco de Dados

def criar_tabela (cursor,):
    cursor.execute("CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT , nome VALCHER(100), email VALCHER(150) )")


def inserir_registro(conexao, cursor,nome,email):
    dados = ("Kyuichi", "Kyuichi@email.com")
    cursor.execute("INSERT INTO clientes (nome , email) VALUES (?, ?) ", dados )
    # INportante comitar os dados !
    conexao.commit()

def atualizar_registro(conexao, cursor ,nome,email,id):
    data = (nome,email,id)
    cursor.execute("UPDATE clientes SET nome=? , email=? WHERE  id=? ; ", data )
    conexao.commit()

cursor = conexao.cursor()

atualizar_registro(conexao, cursor, "isaque Kyuichi", "KyuichiHisamoto@gmail.com", 2)

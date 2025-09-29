import sqlite3
#Criando uma conexao com o banco de dados chamado "Biblioteca"
conexao = sqlite3.connect("biblioteca.db")

#Criando um objeto para executar os comandos do SQL
cursor = conexao.cursor()

#Criando tabelas no banco de dados
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTERGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano INTERGER,
    disponivel TEXT S/N
    )               
""")
print('Tabela criada com sucesso!')
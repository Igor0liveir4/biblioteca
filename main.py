import sqlite3
#Criando uma conexao com o banco de dados chamado "Biblioteca"
conexao = sqlite3.connect("biblioteca.db")

#Criando um objeto para executar os comandos do SQL
cursor = conexao.cursor()

#Criando tabelas no banco de dados
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano INTERGER,
    disponivel TEXT
    )               
""")
print('Tabela criada com sucesso!')

#Inserindo livro no banco de dados
def cadastrar(titulo, autor, ano):
    try:
        conexao = sqlite3.connect('bibliotec.db')
        titulo = input('Digite o titulo do livro: ')
        autor = input('Fale o nome do autor do livro: ')
        ano = int(input('Qual foi o ano de lançamento do Livro?: '))
        cursor = conexao.cursor()

        cursor.execute("""
        INSERT INTO clientes (titulo, autor, ano, disponivel)
        VALUES (?, ?, ?, ?)
        """, (titulo, autor, ano, "Sim")
        )
        conexao.commit
        print("Livro cadastrado com sucesso!")
    except Exception as erro:
        print(f'Erro ao cadastrar esse livro {erro}')
    finally:
        if conexao:
            conexao.close()

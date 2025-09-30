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
    ano INTEGER,
    disponivel TEXT
    )               
""")
print('Tabela criada com sucesso!')

#Inserindo livro no banco de dados
def cadastrar_livro():
    try:
        conexao = sqlite3.connect('biblioteca.db')
        titulo = input('Digite o titulo do livro: ')
        autor = input('Fale o nome do autor do livro: ')
        ano = int(input('Qual foi o ano de lançamento do Livro?: '))
        cursor = conexao.cursor()

        cursor.execute("""
        INSERT INTO clientes (titulo, autor, ano, disponivel)
        VALUES (?, ?, ?, ?)
        """, (titulo, autor, ano, "Sim")
        )
        conexao.commit()
        print("Livro cadastrado com sucesso!")
    except Exception as erro:
        print(f'Erro ao cadastrar esse livro {erro}')
    finally:
        if conexao:
            conexao.close()

#Listagem dos livros
def listar_livros():
    try:
        conexao = sqlite3.connect('biblioteca.db')
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM clientes")
        livros = cursor.fetchall()
        print("\nLista dos livros:")
        for livro in livros:
            print(f'ID: {livro[0]} | Titulo: {livro[1]} | Autor: {livro[2]} | Ano: {livro[3]} | Disponibilidade: {livro[4]}')
    except Exception as erro:
        print(f'Erro ao listar os livros {erro}')
    finally:
        if conexao:
            conexao.close()
    
#Atualizar se estiver disponivel 
def atualizar_livro():
    novo_status = input("Deseja marcar o livro como 'sim' ou 'não'?: ").strip().lower()
    id_livro = input('Digite o ID do livro que deseja atualizar: ').strip()
    if novo_status not in ("sim", "não"):
        print("Valor inválido! Digite 'sim' ou 'não'.")
        return

    if not id_livro.isdigit():
        print("ID inválido! Deve ser um número.")
        return
    id_livro = int(id_livro)

    conexao = sqlite3.connect('biblioteca.db')
    cursor = conexao.cursor()
    cursor.execute("""
        UPDATE clientes
        SET disponivel = ?
        WHERE id = ?
    """, (novo_status, id_livro))

    conexao.commit()
    conexao.close()
    print('Dados atualizados!')

#Remover livro cadastrado
def remover_livro():
    id_livro = input('Digite o ID do livro que deseja remover:  ').strip()
    if not id_livro.isdigit():
        print('ID inválido! Deve ser um número.')
        return
    id_livro = int(id_livro)
    confirmar = input(f'Tem certeza que deseja remover o livro com ID{id_livro}?: ')
    if confirmar != 'sim':
        print('Operaçaõ cancelada.')
        return
    conexao = sqlite3.connect('biblioteca.db')
    cursor = conexao.cursor()
    cursor.execute("""
            SELECT * FROM clientes
            WHERE id = ? """,
            (id_livro,))
    if cursor.fetchall():
        cursor.execute("""
            DELETE FROM clientes
            WHERE id = ? """,
            (id_livro,))
        conexao.commit()
        print('Livro removido com sucesso!')
    else:
        print('Livro não encotrado.')
    conexao.close()

while True:
    print("""
======= MENU =======
1 - Cadastrar livro
2 - Listar livros
3 - Atualizar disponibilidade
4 - Remover livro
5 - sair
====================
    """)
    opcao = input('Escolha uma opção que deseja: ').lower()
    if opcao == '1':
        cadastrar_livro()
    elif opcao == '2':
        listar_livros()
    elif opcao == '3':
        atualizar_livro()
    elif opcao == '4':
        remover_livro()
    elif opcao == '5':
        print('Saindo do sistema...')
        break
    else:
        print('Operação inválida. Tente novamente.')
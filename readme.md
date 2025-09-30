# 📚 Sistema de Gerenciamento de Biblioteca (SQLite + Python)

Este é um sistema simples de gerenciamento de biblioteca feito em **Python**, utilizando o banco de dados **SQLite**. Ele permite **cadastrar, listar, atualizar** e **remover livros** de uma base de dados local (`biblioteca.db`).

## 🚀 Funcionalidades

- ✅ Criar automaticamente a tabela de livros no banco de dados.
- 📥 Cadastrar novos livros com informações como título, autor e ano.
- 📃 Listar todos os livros cadastrados.
- 🔄 Atualizar a disponibilidade de um livro.
- ❌ Remover um livro pelo ID.

## 🗂 Estrutura da Tabela

A tabela `clientes` possui os seguintes campos:

| Campo        | Tipo     | Descrição                            |
|--------------|----------|---------------------------------------|
| `id`         | INTEGER  | Chave primária (auto incremento)     |
| `titulo`     | TEXT     | Título do livro                      |
| `autor`      | TEXT     | Autor do livro                       |
| `ano`        | INTEGER  | Ano de lançamento do livro           |
| `disponivel` | TEXT     | Disponibilidade (Sim/Não)            |

> 💡 *Dica:* Você pode renomear a tabela para `livros`, se desejar um nome mais intuitivo.

---

## 🧪 Como usar

1. **Execute o script Python**:
   ```bash
   python biblioteca.py

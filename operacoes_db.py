import sqlite3

def criar_tabela():

  conexao = sqlite3.connect('test-db.db')
  cursor = conexao.cursor()
  cursor.execute("""CREATE TABLE produtos (
                nome text,
                preco real,
                quantidade integer,
                codigo text
                )""")
  conexao.commit()
  return 0

def inserir_produto(nome, preco, quantidade, codigo):
  conexao = sqlite3.connect('test-db.db')
  cursor = conexao.cursor()
  cursor.execute("INSERT INTO produtos VALUES" +
               f"('{nome}', '{preco}', '{quantidade}', '{codigo}')")
  conexao.commit()
  return 0

def dropar_tabela():
  conexao = sqlite3.connect('test-db.db')
  cursor = conexao.cursor()
  cursor.execute('DROP TABLE produtos')
  conexao.commit()
  return 0


def procurar_produtos(termo):
  conexao = sqlite3.connect('test-db.db')
  cursor = conexao.cursor()
  cursor.execute(f"""SELECT * FROM produtos
                WHERE (
                preco = ? OR
                codigo = ? OR
                quantidade = ? OR
                nome LIKE ?
                )""", (termo, termo, termo, '%' + termo + '%'))
  items = cursor.fetchall()
  conexao.commit()
  return items

def mostrar_produtos():
  conexao = sqlite3.connect('test-db.db')
  cursor = conexao.cursor()
  cursor.execute('SELECT * FROM produtos')
  produtos = cursor.fetchall()
  conexao.commit()
  return produtos



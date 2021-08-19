import sqlite3

def criar_tabela():
  conexao = sqlite3.connect('clientes.db')
  cursor = conexao.cursor()
  cursor.execute("""CREATE TABLE clientes(
                nome text,
                divida real,
                notas text
                )""")
  conexao.commit()
  return 0

def inserir_cliente(nome, divida, notas):
  conexao = sqlite3.connect('clientes.db')
  cursor = conexao.cursor()
  cursor.execute("INSERT INTO clientes VALUES" +
               f"('{nome}', '{divida}', '{notas}')")
  conexao.commit()
  return 0

def dropar_tabela():
  conexao = sqlite3.connect('clientes.db')
  cursor = conexao.cursor()
  cursor.execute('DROP TABLE clientes')
  conexao.commit()
  return 0

def procurar_clientes(termo):
  conexao = sqlite3.connect('clientes.db')
  cursor = conexao.cursor()
  cursor.execute(f"""SELECT *, rowid FROM clientes
                WHERE (
                nome LIKE ?
                )""", ('%' + termo + '%', ))
  items = cursor.fetchall()
  conexao.commit()
  return items

def mostrar_clientes():
  conexao = sqlite3.connect('clientes.db')
  cursor = conexao.cursor()
  cursor.execute('SELECT *, rowid FROM clientes')
  clientes = cursor.fetchall()
  conexao.commit()
  return clientes

def pegar_nomes_clientes():
  conexao = sqlite3.connect('clientes.db')
  cursor = conexao.cursor()
  cursor.execute('SELECT nome FROM clientes')
  clientes_nomes = [i[0] for i in cursor.fetchall()]
  conexao.commit()
  return clientes_nomes

def modificar_cliente(dados):

  conexao = sqlite3.connect('clientes.db')
  cursor = conexao.cursor()


  cursor.execute('UPDATE clientes SET nome = ?, divida = ?, notas = ? WHERE nome = ?',(dados['nome'], dados['divida'], dados['notas'], dados['nome_antigo']))
  conexao.commit()
  return 0



if __name__ == '__main__':
  modificar_cliente(
    {'nome': 'clodoaldo',
    'divida': 5300,
    'notas': 'bandido FINO',
    'nome_antigo': 'clodoaldo'}
  )
  print(procurar_clientes('clodoaldo'))


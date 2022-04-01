import sqlite3
import re
from datetime import date, timedelta

def dividaPeloNome(nome):
	
  conexao = sqlite3.connect("clientes.db")
  cursor = conexao.cursor()
  cursor.execute("SELECT divida FROM clientes WHERE nome=?", (nome, ))
  divida = cursor.fetchone()
  conexao.commit()
  return divida[0]


conexao = sqlite3.connect("clientes.db")
cursor = conexao.cursor()
cursor.execute("SELECT nome, notas FROM clientes")
nome_notas = cursor.fetchall()
conexao.commit()

ultimo_pagamento = []
for nome, nota in nome_notas:
  nota = nota
  datas_re = re.findall('([0-9]{2})[/\-\.]([0-9]{2})[/\-\.]([0-9]{2,4})', nota)
  datas = []
  for i in datas_re:
    try:
      data = date(day=int(i[0]), month=int(i[1]), year=int('20' + i[2][-2::]))
    except:
      print(nome + '\n' + nota)
    datas.append(data)
  try:
    ultimo_pagamento.append([nome, max(datas)])
  except ValueError:
    pass

tempo_corrido = []
for i in ultimo_pagamento:
  data = i[1]
  delta = (date.today() - i[1]).days // 30
  tempo_corrido.append([i[0], delta])
tempo_corrido.sort(key=lambda x: x[1], reverse=True)

intervalo = []

for i in tempo_corrido:
  if i[1] >= 3 and i[1] <= 24:
    intervalo.append(i)	

with open('relatorio.txt', 'a') as relatorio:
  for cliente in intervalo:
    nome = cliente[0]
    divida = dividaPeloNome(cliente[0])
    meses_divida = cliente[1]
    if divida > 10:
      divida = str(divida).replace('.', ',')
      if meses_divida < 12:
        relatorio.write(f"{nome} deve R${divida} há {meses_divida} mes(es)\n")
      else:
        anos_divida = meses_divida // 12
        meses_divida %= 12
        relatorio.write(f"{nome} deve R${divida} há {anos_divida} ano(s) e {meses_divida} mes(es)\n")

  divida_total = sum([dividaPeloNome(cliente[0]) for cliente in intervalo])
  divida_total = str(divida_total).replace('.', ',')
  relatorio.write(f"\nNo total temos uma dívida de R${divida_total} sem nenhum pagamento efetuado entre 3 meses e 2 anos passados\n")

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QTableView, QHeaderView, QVBoxLayout
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from operacoes_db import procurar_produtos, mostrar_produtos

produtos = ['',]
colunas_headers = ('Nome', 'Preço', 'Qtd', 'Código')
model = QStandardItemModel(len(produtos), len(colunas_headers))

def mostrar_pesquisa(res):
  model.clear()
  model.setHorizontalHeaderLabels(colunas_headers)
  for i in range(len(res)):
    model.setItem(i, 0, QStandardItem(str(res[i][0])))
    model.setItem(i, 1, QStandardItem(str(res[i][1])))
    model.setItem(i, 2, QStandardItem(str(res[i][2])))
    model.setItem(i, 3, QStandardItem(str(res[i][3])))

def pesquisa(termo):
  res = procurar_produtos(termo)
  mostrar_pesquisa(res)

class Produto():
  def __init__(self, nome, preco, codigo):
    self.nome = nome
    self.preco = preco
    self.codigo = codigo

class AppDemo(QWidget):
  def __init__(self):
    super().__init__()
    self.setGeometry(300, 100, 700, 600)
    mainLayout = QVBoxLayout()


    #^^ implementa modelo tabela ...(linhas, colunas)
    model.setHorizontalHeaderLabels(colunas_headers)
    produtos = mostrar_produtos()
    mostrar_pesquisa(produtos)


    nome_entrada = QLineEdit()
    nome_entrada.setStyleSheet('font-size: 25px; height: 30px;')
    nome_entrada.textChanged.connect(pesquisa)

    mainLayout.addWidget(nome_entrada)

    table = QTableView()
    table.setStyleSheet('font-size: 15px;')
    #table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
    table.verticalHeader().setVisible(False)
    table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    table.setModel(model)
    mainLayout.addWidget(table)

    self.setLayout(mainLayout)

app = QApplication(sys.argv)
demo = AppDemo()
demo.show()
sys.exit(app.exec_())

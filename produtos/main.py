import sys
from PyQt5.QtWidgets import QGridLayout, QApplication, QWidget, QLineEdit, QTableView, QHeaderView, QVBoxLayout, QHBoxLayout, QPushButton, QStackedLayout, QMainWindow, QLabel, QFormLayout, QSpinBox, QDoubleSpinBox
from PyQt5.QtCore import Qt, QSortFilterProxyModel, QRect, QSize
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from operacoes_db import procurar_produtos, mostrar_produtos, inserir_produto

produtos = ['',]
colunas_headers = ('Nome', 'Preço', 'Qtd', 'ID')
model = QStandardItemModel(len(produtos), len(colunas_headers))

def mostrarItem(item):
  model.index(item.row(), item.column())
  print(str(colunas_headers[item.column()]) + ': ' + str(item.data()))

def mostrar_pesquisa(res):
  model.clear()
  model.setHorizontalHeaderLabels(colunas_headers)
  for i in range(len(res)):
    for k in range(len(colunas_headers)):
      model.setItem(i, k, QStandardItem(str(res[i][k])))

def pesquisa(termo):
  res = procurar_produtos(termo)
  mostrar_pesquisa(res)

class Produto():
  def __init__(self, nome, preco):
    self.nome = nome
    self.preco = preco

class BuscarProdutosWindow(QWidget):
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
    table.doubleClicked.connect(mostrarItem)
    table.setStyleSheet('font-size: 15px;')
    #table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
    table.verticalHeader().setVisible(False)
    table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    table.setModel(model)
    mainLayout.addWidget(table)

    self.setLayout(mainLayout)

class GerenciarProdutosWindow(QWidget):
  def __init__(self):
    super().__init__()
    self.setGeometry(300, 100, 700, 600)
    layout = QFormLayout()

    labels = {
                'nome': QLabel('Nome'),
                'preco': QLabel('Preço'),
                'quantidade': QLabel('Quantidade'),
              }
    entradas = {
                'nome': QLineEdit(),
                'preco': QDoubleSpinBox(),
                'quantidade': QSpinBox(),
              }

    button = QPushButton("Adicionar")

    for entrada in entradas.values():
      entrada.setMaximumWidth(450)

    button.setMaximumSize(QSize(80, 40))
    layout.setSpacing(5)

    for nome in labels.keys():
      layout.addWidget(labels[nome])
      layout.addWidget(entradas[nome])

    entradas['preco'].setSuffix('R$')
    entradas['preco'].setRange(0, 1000000)

    layout.addWidget(button)

    button.clicked.connect(lambda:inserir_produto(
      entradas['nome'].text(),
      entradas['preco'].value(),
      entradas['quantidade'].value(),
    ))
    for entrada in entradas.values():
      try:
        entrada.returnPressed.connect(lambda:inserir_produto(
          entradas['nome'].text(),
          entradas['preco'].value(),
          entradas['quantidade'].value(),
        ))
      except AttributeError:
        continue

    self.setLayout(layout)

class InicialWindow(QWidget):
  def __init__(self):
    super().__init__()
    self.setGeometry(300, 100, 700, 600)
    layout = QHBoxLayout()
    button = QPushButton("Buscar Produtos", self)
    button.setMaximumSize(150, 35)
    button2 = QPushButton("Gerenciar Produtos", self)
    button2.setMaximumSize(150, 35)
    button.clicked.connect(self.abrir_produtos_window)
    button2.clicked.connect(self.gerenciar_produtos_window)

    layout.addWidget(button)
    layout.addWidget(button2)

    self.setLayout(layout)

  def abrir_produtos_window(self, checked):
    self.w = BuscarProdutosWindow()
    self.w.show()
    #manter referencia?
  def gerenciar_produtos_window(self, checked):
    self.w2 = GerenciarProdutosWindow()
    self.w2.show()
    #manter referencia?

app = QApplication(sys.argv)
demo = InicialWindow()
demo.show()
sys.exit(app.exec_())


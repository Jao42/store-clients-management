import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QTableView, QHeaderView, QVBoxLayout
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem

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

    produtos = [['maçã', '20', '3', '33ddfa1']]
    colunas_headers = ('Nome', 'Preço', 'Qtd', 'Código')

    model = QStandardItemModel(len(produtos), len(colunas_headers))
    #^^ implementa modelo tabela ...(linhas, colunas)
    model.setHorizontalHeaderLabels(colunas_headers)

    for produto_index in range(len(produtos)):
      for campo_index in range(len(produtos[produto_index])):
        item = QStandardItem(produtos[produto_index][campo_index])
        model.setItem(produto_index, campo_index, item)

    filter_proxy_model = QSortFilterProxyModel()
    filter_proxy_model.setSourceModel(model)
    filter_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
    filter_proxy_model.setFilterKeyColumn(0)

    nome_entrada = QLineEdit()
    nome_entrada.setStyleSheet('font-size: 25px; height: 30px;')
    nome_entrada.textChanged.connect(filter_proxy_model.setFilterRegExp)

    mainLayout.addWidget(nome_entrada)

    table = QTableView()
    table.setStyleSheet('font-size: 15px;')
    #table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
    table.verticalHeader().setVisible(False)
    table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    table.setModel(filter_proxy_model)
    mainLayout.addWidget(table)

    self.setLayout(mainLayout)

app = QApplication(sys.argv)
demo = AppDemo()
demo.show()
sys.exit(app.exec_())



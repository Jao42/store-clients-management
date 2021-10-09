import sys
from PyQt5.QtWidgets import (QGridLayout,
                             QApplication,
                             QWidget,
                             QLineEdit,
                             QTableView,
                             QListView,
                             QHeaderView,
                             QVBoxLayout,
                             QHBoxLayout,
                             QPushButton,
                             QStackedLayout,
                             QMainWindow,
                             QLabel,
                             QFormLayout,
                             QSpinBox,
                             QDoubleSpinBox,
                             QComboBox
                             )
from PyQt5.QtCore import (Qt, QSortFilterProxyModel,
                          QRect, QSize,
                          QStringListModel, QEvent
                          )
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from operacoes_db import *
from cliente_tela import ClienteInfoTela
from add_cliente_tela import FormClienteTela


produtos = ['',]
model = QStringListModel()

model.setStringList(pegar_nomes_clientes())
layoutTela = [
  "display", "display", "select",
  "lista", "lista", "lista",
  "lista", "lista", "lista",
  "lista", "lista", "lista"
 ]

def pesquisa_nomes(termo):
  res = procurar_clientes(termo)
  nomes = [cliente[0] for cliente in res]
  model.setStringList(nomes)

def mostrar_item(item):
  print(item.data())

class ClientesListaTela(QWidget):
  def __init__(self):
    super().__init__()
    self.setGeometry(300, 100, 700, 600)
    mainLayout = QGridLayout()
    forma_busca = QComboBox()
    forma_busca.addItem('Nome')
    forma_busca.addItem('Dívida')
    self.lista = QListView()
    self.lista.setEditTriggers(self.lista.NoEditTriggers)
    self.lista.doubleClicked.connect(self.mostrarClienteInfo)
    procurar_pessoa = QLineEdit()
    procurar_pessoa.textChanged.connect(pesquisa_nomes)
    self.lista.setStyleSheet(
      'font-size: 20px;'+
      'margin: 5px 10px 15px 5px;'
    )
    self.lista.setModel(model)

    botao_adicionar = QPushButton('Adicionar Cliente')
    botao_adicionar.setStyleSheet('padding: 5px;')
    botao_adicionar.clicked.connect(self.adicionarClienteBotao)

    mainLayout.addWidget(procurar_pessoa, 0, 0, 1, 1)
    mainLayout.addWidget(forma_busca, 0, 2, 1, 2)
    mainLayout.addWidget(self.lista, 1, 0, 3, 4)
    mainLayout.addWidget(botao_adicionar, 4, 3, 1, 1)

    self.setLayout(mainLayout)

  def mostrarClienteInfo(self, row):
    cliente_nome = row.data()
    nome, divida, notas, id = procurar_clientes(cliente_nome, True)[0]

    self.cliente_info = ClienteInfoTela(nome, divida, notas)
    self.cliente_info.show()

  def adicionarClienteBotao(self):
    self.add_cliente = FormClienteTela()
    self.add_cliente.show()

  def keyPressEvent(self, e):
    if e.key() == Qt.Key_F5:
      model.setStringList(pegar_nomes_clientes())
      self.lista.setModel(model)


app = QApplication(sys.argv)
demo = ClientesListaTela()
demo.show()
sys.exit(app.exec_())

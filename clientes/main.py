import sys
from PyQt5.QtWidgets import QGridLayout, QApplication, QWidget, QLineEdit, QTableView, QListView, QHeaderView, QVBoxLayout, QHBoxLayout, QPushButton, QStackedLayout, QMainWindow, QLabel, QFormLayout, QSpinBox, QDoubleSpinBox, QComboBox
from PyQt5.QtCore import Qt, QSortFilterProxyModel, QRect, QSize, QStringListModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from operacoes_db import *

produtos = ['',]
model = QStringListModel()




model.setStringList(pegar_nomes_clientes())
layoutTela = [
  "display", "display", "select"
  "lista", "lista", "lista",
  "lista", "lista", "lista",
  "lista", "lista", "lista"
 ]

class ClientesTela(QWidget):
  def __init__(self):
    super().__init__()
    self.setGeometry(300, 100, 700, 600)
    mainLayout = QGridLayout()
    forma_busca = QComboBox()
    forma_busca.addItem('Nome')
    forma_busca.addItem('Dívida')
    lista = QListView()
    lista.setEditTriggers(lista.NoEditTriggers)
    procurar_pessoa = QLineEdit()
    lista.setStyleSheet('font-size: 20px; border: 3px solid red; margin: 5px 10px 15px 5px;')
    lista.setModel(model)
    mainLayout.addWidget(procurar_pessoa, 0, 0, 1, 1)
    mainLayout.addWidget(forma_busca, 0, 2, 1, 2)
    mainLayout.addWidget(lista, 1, 0, 3, 4)

    self.setLayout(mainLayout)

app = QApplication(sys.argv)
demo = ClientesTela()
demo.show()
sys.exit(app.exec_())


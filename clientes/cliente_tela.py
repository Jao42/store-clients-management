import sys
from PyQt5.QtWidgets import QGridLayout, QApplication, QWidget, QLineEdit, QTableView, QListView, QHeaderView, QVBoxLayout, QHBoxLayout, QPushButton, QStackedLayout, QMainWindow, QLabel, QFormLayout, QSpinBox, QDoubleSpinBox, QComboBox
from PyQt5.QtCore import Qt, QSortFilterProxyModel, QRect, QSize, QStringListModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem

produtos = ['',]
layoutTela = [
  "a", "a", "k", "k", "k", "a", "a"
  "a", "a", "a", "a", "a", "a", "a"
  "a", "w", "w", "a", "x", "x", "a"
  "a", "y", "y", "a", "a", "a", "a"
  "a", "z", "z", "z", "z", "z", "z"
  "a", "z", "z", "z", "z", "z", "z"
  "a", "z", "z", "z", "z", "z", "z"
 ]

class ClientesTela(QWidget):
  def __init__(self):
    super().__init__()
    self.setGeometry(300, 100, 700, 600)
    mainLayout = QGridLayout()

    nome = QLabel('Evaristo Conceicao de azevedo')
    labelDivida = QLabel('Dívida: ')
    divida = QLabel('320,32 R$')
    labelNotas = QLabel('Anotações: ')
    notas = QLabel('Me pagou somente 20 esse veaco')
    nome.setAlignment(Qt.AlignCenter)
    notas.setAlignment(Qt.AlignTop | Qt.AlignLeft)
    notas.setStyleSheet('border: 2px solid grey')

    mainLayout.addWidget(nome, 0, 0, 1, 7)
    mainLayout.addWidget(labelDivida, 2, 0, 1, 2)
    mainLayout.addWidget(divida, 2, 2, 1, 2)
    mainLayout.addWidget(labelNotas, 3, 0, 1, 2)
    mainLayout.addWidget(notas, 4, 0, 3, 7)

    self.setLayout(mainLayout)

app = QApplication(sys.argv)
demo = ClientesTela()
demo.show()
sys.exit(app.exec_())


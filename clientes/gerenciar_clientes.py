import sys
from PyQt5.QtWidgets import QGridLayout, QApplication, QWidget, QLineEdit, QTextEdit, QTableView, QHeaderView, QVBoxLayout, QHBoxLayout, QPushButton, QStackedLayout, QMainWindow, QLabel, QFormLayout, QSpinBox, QDoubleSpinBox
from PyQt5.QtCore import Qt, QSortFilterProxyModel, QRect, QSize
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from operacoes_db import inserir_cliente

class GerenciarProdutosWindow(QWidget):
  def __init__(self):
    super().__init__()
    self.setGeometry(300, 100, 700, 600)
    layout = QFormLayout()

    labels = {
                'nome': QLabel('Nome:'),
                'divida': QLabel('Dívida:'),
                'notas': QLabel('Anotações:'),
              }
    entradas = {
                'nome': QLineEdit(),
                'divida': QDoubleSpinBox(),
                'notas': QTextEdit(),
              }

    button = QPushButton("Adicionar")

    for entrada in entradas.values():
      entrada.setMaximumWidth(450)

    button.setMaximumSize(QSize(80, 40))
    layout.setSpacing(5)
    entradas['notas'].setFixedHeight(400)
    entradas['notas'].setAlignment(Qt.AlignTop)

    for nome in labels.keys():
      layout.addWidget(labels[nome])
      layout.addWidget(entradas[nome])

    entradas['divida'].setSuffix('R$')
    entradas['divida'].setRange(0, 1000000)

    button.clicked.connect(
      lambda: inserir_cliente(
        entradas['nome'].text(),
        entradas['divida'].value(),
        entradas['notas'].toPlainText()
      )
    )
    layout.addWidget(button)
    self.setLayout(layout)

app = QApplication(sys.argv)
demo = GerenciarProdutosWindow()
demo.show()
sys.exit(app.exec_())


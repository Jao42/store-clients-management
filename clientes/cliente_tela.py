import sys
from PyQt5.QtWidgets import QGridLayout, QApplication, QWidget, QLineEdit, QTableView, QListView, QHeaderView, QVBoxLayout, QHBoxLayout, QPushButton, QStackedLayout, QMainWindow, QLabel, QFormLayout, QSpinBox, QDoubleSpinBox, QComboBox, QScrollArea
from PyQt5.QtCore import Qt, QSortFilterProxyModel, QRect, QSize, QStringListModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont
from add_cliente_tela import FormClienteTela
from operacoes_db import modificar_cliente

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

class ClienteInfoTela(QWidget):
  def __init__(self, nome_var, divida_var, notas_var):
    super().__init__()

    self.nome_var = nome_var
    self.divida_var = divida_var
    self.notas_var = notas_var

    divida_str = f'{divida_var:.2f}'.replace('.', ',')
    self.setGeometry(300, 100, 700, 600)
    self.setFont(QFont("Arial", 15))
    mainLayout = QGridLayout()

    nome = QLabel(nome_var)
    labelDivida = QLabel('Dívida: ')
    divida = QLabel(divida_str + ' R$')
    labelNotas = QLabel('Anotações: ')
    notas = QLabel(notas_var)
    nome.setAlignment(Qt.AlignCenter)
    labelNotas.setAlignment(Qt.AlignBottom | Qt.AlignLeft)
    notas.setAlignment(Qt.AlignTop | Qt.AlignLeft)
    notas.setStyleSheet(
      'font-family: Arial;' +
      'font-size: 15px;'
    )
    editarButton = QPushButton('Editar')
    editarButton.clicked.connect(self.edit_cliente_botao)
    scrollNotas = QScrollArea()
    scrollNotas.setWidget(notas)
    scrollNotas.setWidgetResizable(True)

    mainLayout.addWidget(nome, 0, 0, 1, 7)
    mainLayout.addWidget(labelDivida, 2, 0, 1, 2)
    mainLayout.addWidget(divida, 2, 1, 1, 2)
    mainLayout.addWidget(labelNotas, 3, 0, 1, 2)
    mainLayout.addWidget(scrollNotas, 4, 0, 3, 7)
    mainLayout.addWidget(editarButton, 7, 6)

    for i in range(0, 8):
        mainLayout.setRowStretch(i , 1)


    self.setLayout(mainLayout)

  def edit_cliente_botao(self):
    self.tela_edit = FormClienteTela(self.nome_var,
                                     self.divida_var,
                                     self.notas_var,
                                     'modificar'
                                     )
    self.tela_edit.show()

if __name__ == '__main__':
  app = QApplication(sys.argv)
  nome_var = 'Evaristo Conceição de Azevedo'
  divida_var = 320.32
  notas_var = 'Me pagou somente 20 esse veaco'

  demo = ClienteInfoTela(nome_var, divida_var, notas_var)
  demo.show()
  sys.exit(app.exec_())

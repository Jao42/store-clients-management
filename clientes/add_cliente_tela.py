import sys
from PyQt5.QtWidgets import QGridLayout, QApplication, QWidget, QLineEdit, QTableView, QListView, QHeaderView, QVBoxLayout, QHBoxLayout, QPushButton, QStackedLayout, QMainWindow, QLabel, QFormLayout, QSpinBox, QDoubleSpinBox, QComboBox, QTextEdit
from PyQt5.QtCore import Qt, QSortFilterProxyModel, QRect, QSize, QStringListModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont
from operacoes_db import inserir_cliente, modificar_cliente


produtos = ['',]


class FormClienteTela(QWidget):

  def __init__(self, nome_var='', divida_var=0.0, notas_var='', contexto='adicionar'):
    super().__init__()
    self.nome_var = nome_var
    self.divida_var = divida_var
    self.notas_var = notas_var
    self.contexto = contexto
    self.initUI()

  def initUI(self):
    nome = QLabel('Nome: ')
    divida = QLabel('Dívida: ')
    notas = QLabel('Notas: ')

    nomeEdit = QLineEdit(self.nome_var)
    dividaEdit = QDoubleSpinBox()

    #formatacao com \n tava dando ruim
    notasEdit = QTextEdit()
    notasEdit.insertPlainText(self.notas_var)

    enviar = QPushButton(self.contexto.title())

    dividaEdit.setRange(0, 1000000)
    dividaEdit.setValue(self.divida_var)
    dividaEdit.setSuffix('R$')

    grid = QGridLayout()
    grid.setSpacing(10)

    grid.addWidget(nome, 1, 0)
    grid.addWidget(nomeEdit, 1, 1)

    grid.addWidget(divida, 2, 0)
    grid.addWidget(dividaEdit, 2, 1)

    grid.addWidget(notas, 3, 0)
    grid.addWidget(notasEdit, 3, 1, 5, 1)

    grid.addWidget(enviar, 8, 1, 1, 1,
                   Qt.Alignment(Qt.AlignRight | Qt.AlignTop))
    campos = [nomeEdit, dividaEdit, notasEdit]
    if self.contexto == 'adicionar':
      enviar.clicked.connect(
        lambda:self.addClienteGUI(
          nomeEdit.text(),
          dividaEdit.value(),
          notasEdit.toPlainText())
      )
    elif self.contexto == 'modificar':

      enviar.clicked.connect(
        lambda:modificar_cliente(
          {
          'nome': nomeEdit.text(),
          'divida': dividaEdit.value(),
          'notas': notasEdit.toPlainText(),
          'nome_antigo': self.nome_var
          }
        )
      )



    self.setGeometry(300, 100, 700, 600)
    self.setWindowTitle('Adicionar Cliente')
    self.setLayout(grid)
    
  def addClienteGUI(self, nome, divida, notas):
    inserir_cliente(nome, divida, notas)
    self.close()


def main():
    app = QApplication(sys.argv)
    clientes_tela = FormClienteTela()
    clientes_tela.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
  main()


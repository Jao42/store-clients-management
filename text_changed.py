import sys
from  PyQt5.QtWidgets import *

class WindowExample(QWidget):
  def __init__(self):
   super().__init__()
   self.setGeometry(500, 200, 800, 500)
   self.setWindowTitle('Produtos')

   email_input = QLineEdit()
   email_input.setFixedWidth(200)
   email_input.textChanged.connect(self.email_edit)

   form = QFormLayout()
   form.addRow('email: ', email_input)
   self.setLayout(form)

   self.show()
  def email_edit(self, text):
    print(text)

app = QApplication(sys.argv)
window = WindowExample()

sys.exit(app.exec_())


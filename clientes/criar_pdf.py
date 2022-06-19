from fpdf import FPDF

class PDF(FPDF):
  pdf_w=210
  pdf_h=297
  def lines(self):
    self.set_line_width(0.0)
    self.line(0, self.pdf_h/2, self.pdf_w, self.pdf_h/2)

  def titles(self):
    self.set_xy(0.0, 0.0)
    self.set_font('Arial', 'B', 16)
    self.set_text_color(0, 0, 0)
    self.cell(w=210.0, h=40.0, align='C', txt="RELATÓRIO", border=0)

  def texts(self, name):
    with open('relatorio.txt', 'rb') as relatorio:
      txt = relatorio.read().decode('UTF-8')
    self.set_xy(10.0, 40.0)
    self.set_text_color(0, 0, 0)
    self.set_font('Arial', '', 10)
    self.multi_cell(0, 5, txt)


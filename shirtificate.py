from fpdf import FPDF

class PDF():
    def __init__(self, name):
        self.pdf = FPDF (orientation ="P", unit ="mm", format = "A4")
        self.pdf.add_page()
        self.pdf.set_font ("helvetica", "B", 50)
        self.pdf.cell(w = 0, h = 60, text = "CS50 Shirtificate", new_x = "LMARGIN", new_y = "NEXT", align = "C")
        self.pdf.image("shirtificate.png", w = self.pdf.epw)
        self.pdf.set_font_size (30)
        self.pdf.set_text_color (255, 255, 255)
        self.pdf.text (x= 65, y = 140, text = f"{name} took CS50")

    def save(self, name):
        self.pdf.output (name)

name = input("Name :")
pdf = PDF(name)
pdf.save("shirtificate.pdf")

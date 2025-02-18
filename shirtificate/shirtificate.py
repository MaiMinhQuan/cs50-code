from fpdf import FPDF

class PDF():
    def __init__(self, t):
        self.a = FPDF()
        self.a.add_page()
        self.a.set_font("helvetica", "B", 45)
        self.a.cell(0, 59, "CS50 Shirtificate", new_x = "LMARGIN", new_y = "NEXT", align = "C")
        self.a.image("shirtificate.png", w = self.a.epw)
        self.a.set_font_size(30)
        self.a.set_text_color(210, 100, 150)
        self.a.text(x = 45, y = 140, txt = f"{t} took CS50")

    def save(self, name):
        self.a.output(name)

t = input("Name: ")
pdf = PDF(t)
pdf.save("shirtificate.pdf")
from fpdf import FPDF

class PDF():
    def __init__(self, name):
        self.pdf = FPDF()
        self.pdf.add_page()
        self.pdf.set_font("helvetica", "B", 50)
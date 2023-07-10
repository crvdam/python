from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Rendering logo:
        self.image("shirtificate.png", x=30, y=30, w=150, h=180)
        self.set_font("helvetica", "B", 30)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 10, "CS50 Shirtificate", align="C")
        # Performing a line break:
        self.ln(20)

    def footer(self):
        # Position cursor at 1.5 cm from bottom:
        self.set_y(-30)
        # Setting font: helvetica italic 8
        self.set_font("helvetica", "B", 20)
        # Printing page number:



# Instantiation of inherited class
def main():
    name = input("Name: ")
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Times", size=16)
    pdf.set_text_color(r=255,g=255,b=255)
    pdf.cell(0, 110
    , f"{name} took CS50", align="C")
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
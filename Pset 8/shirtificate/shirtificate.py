from fpdf import FPDF

# input name
name = input("Name: ")

# Create a PDF
pdf = FPDF()
pdf.add_page()

# adding image
pdf.image(
    "shirtificate.png",
    x= 20, y= 80, w=170
    )

# adding header
pdf.set_font('helvetica', 'IB', 35)
pdf.set_text_color(0,0,0)
pdf.cell(200, 50, 'CS50 Shirtificate', new_x="LMARGIN", new_y="NEXT", align='C')

# print on T-shirt
pdf.set_font('helvetica', 'B', 30)
pdf.set_text_color(176, 208, 232)
pdf.cell(200, 150, f'{name} took CS50', new_x="LMARGIN", new_y="NEXT", align='C')

pdf.output('shirtificate.pdf')

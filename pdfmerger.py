from PyPDF2 import PdfWriter

merger = PdfWriter()

pdf = []
n = int(input("How many pdf you want to merge?\n "))

for i in range(0 , n):
    name = input(f"Enter the name of {i+1} pdf: ")
    pdf.append(name)

for pdf in pdf:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()
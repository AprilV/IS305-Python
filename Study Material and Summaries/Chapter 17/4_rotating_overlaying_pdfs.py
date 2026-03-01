"""
Rotating and Overlaying PDF Pages (Watermarks)
This demonstrates page rotation and adding watermarks
"""

import PyPDF2

# ROTATING PAGES
pdfFile = open('example.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
pdfWriter = PyPDF2.PdfFileWriter()

page = pdfReader.getPage(0)
# Rotate clockwise by 90 degrees
page.rotateClockwise(90)
# Can also use: rotateCounterClockwise(90)
pdfWriter.addPage(page)

outputFile = open('rotated.pdf', 'wb')
pdfWriter.write(outputFile)
outputFile.close()
pdfFile.close()

# OVERLAYING PAGES (WATERMARKS)
pdfFile = open('document.pdf', 'rb')
watermarkFile = open('watermark.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFile)
watermarkReader = PyPDF2.PdfFileReader(watermarkFile)
pdfWriter = PyPDF2.PdfFileWriter()

watermarkPage = watermarkReader.getPage(0)

# Add watermark to each page
for pageNum in range(pdfReader.numPages):
    page = pdfReader.getPage(pageNum)
    page.mergePage(watermarkPage)
    pdfWriter.addPage(page)

resultFile = open('watermarked.pdf', 'wb')
pdfWriter.write(resultFile)
resultFile.close()
pdfFile.close()
watermarkFile.close()

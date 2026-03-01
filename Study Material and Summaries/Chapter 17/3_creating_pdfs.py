"""
Creating and Copying PDF Pages
This demonstrates creating new PDFs and copying pages
"""

import PyPDF2

# Reading source PDF
pdf1File = open('source.pdf', 'rb')
pdf2File = open('source2.pdf', 'rb')

pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
pdf2Reader = PyPDF2.PdfFileReader(pdf2File)

# Creating PDF writer object
pdfWriter = PyPDF2.PdfFileWriter()

# Copying pages from first PDF
for pageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

# Adding specific page from second PDF
pageObj = pdf2Reader.getPage(0)
pdfWriter.addPage(pageObj)

# Writing to new PDF file
pdfOutputFile = open('combined.pdf', 'wb')
pdfWriter.write(pdfOutputFile)

# Close all files
pdfOutputFile.close()
pdf1File.close()
pdf2File.close()

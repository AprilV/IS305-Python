"""
PyPDF2 Basics - Reading PDF Files
This demonstrates opening PDFs and getting basic information
"""

import PyPDF2

# Opening a PDF in read-binary mode
pdfFileObj = open('example.pdf', 'rb')

# Creating a PDF reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# Getting number of pages
print(f'Number of pages: {pdfReader.numPages}')

# Getting a specific page (0-indexed)
pageObj = pdfReader.getPage(0)

# Extracting text from page
text = pageObj.extractText()
print(text)

# Close the file
pdfFileObj.close()

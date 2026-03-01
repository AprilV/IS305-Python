"""
Encrypting PDF Files
This demonstrates adding password protection to PDFs
"""

import PyPDF2

# Open source PDF
pdfFile = open('document.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
pdfWriter = PyPDF2.PdfFileWriter()

# Copy all pages to writer
for pageNum in range(pdfReader.numPages):
    pdfWriter.addPage(pdfReader.getPage(pageNum))

# Encrypt with password
# encrypt(user_pwd, owner_pwd=None, use_128bit=True)
pdfWriter.encrypt('secretpassword')

# Save encrypted PDF
resultPdfFile = open('encrypted_document.pdf', 'wb')
pdfWriter.write(resultPdfFile)

resultPdfFile.close()
pdfFile.close()

print('PDF encrypted successfully')

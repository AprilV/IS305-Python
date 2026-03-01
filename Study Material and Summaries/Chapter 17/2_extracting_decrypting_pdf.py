"""
Extracting and Decrypting PDF Text
This demonstrates extracting text and handling encrypted PDFs
"""

import PyPDF2

# Reading encrypted PDF
pdfFile = open('encrypted.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)

# Check if PDF is encrypted
if pdfReader.isEncrypted:
    # Decrypt with password
    if pdfReader.decrypt('password') == 1:
        print('PDF decrypted successfully')
        
        # Now can extract text
        pageObj = pdfReader.getPage(0)
        print(pageObj.extractText())
    else:
        print('Incorrect password')
else:
    # Extract text from unencrypted PDF
    for pageNum in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        print(f'Page {pageNum}:')
        print(pageObj.extractText())

pdfFile.close()

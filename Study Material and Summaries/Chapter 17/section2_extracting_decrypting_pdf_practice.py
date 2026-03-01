# SECTION 2: EXTRACTING AND DECRYPTING PDF - Practice

# Q1: Import PyPDF2 module
# WHAT IT DOES: Makes PyPDF2 functions available for working with PDF files
# ┌─ EXAMPLE ─────────────
# │ import sys
# └───────────────────────




# Q2: Use open() with 'rb' mode to open 'secure.pdf' and store in variable pdfFile
# WHAT IT DOES: Opens an encrypted PDF file in read-binary mode
# ┌─ EXAMPLE ─────────────
# │ myFile = open('document.pdf', 'rb')
# └───────────────────────




# Q3: Use PyPDF2.PdfFileReader() with pdfFile to create reader and store in pdfReader
# WHAT IT DOES: Creates a reader object for the encrypted PDF
# ┌─ EXAMPLE ─────────────
# │ myReader = PyPDF2.PdfFileReader(myFile)
# └───────────────────────




# Q4: Use if statement to check if pdfReader.isEncrypted is True
# WHAT IT DOES: Checks whether the PDF file is password-protected
# ┌─ EXAMPLE ─────────────
# │ if myReader.isEncrypted:
# │     print('File is encrypted')
# └───────────────────────




# Q5: Use pdfReader.decrypt() with password 'mypassword123' and check if it returns 1
# WHAT IT DOES: Attempts to decrypt the PDF with a password, returns 1 if successful
# ┌─ EXAMPLE ─────────────
# │ if myReader.decrypt('secret') == 1:
# │     print('Decrypted!')
# └───────────────────────




# Q6: Use for loop with range(pdfReader.numPages) to extract text from all pages
# WHAT IT DOES: Loops through every page in the PDF to extract text
# ┌─ EXAMPLE ─────────────
# │ for pageNum in range(myReader.numPages):
# │     page = myReader.getPage(pageNum)
# │     print(page.extractText())
# └───────────────────────




# Q7: Use pdfFile.close() to close the file
# WHAT IT DOES: Closes the PDF file to free up system resources
# ┌─ EXAMPLE ─────────────
# │ myFile.close()
# └───────────────────────



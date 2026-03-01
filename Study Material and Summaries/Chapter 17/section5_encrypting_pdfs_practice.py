# SECTION 5: ENCRYPTING PDF FILES - Practice

# Q1: Import PyPDF2 module
# WHAT IT DOES: Makes PyPDF2 functions available for working with PDF files
# ┌─ EXAMPLE ─────────────
# │ import sys
# └───────────────────────




# Q2: Use open() with 'rb' to open 'invoice.pdf' and store in pdfFile
# WHAT IT DOES: Opens a PDF file that we want to encrypt
# ┌─ EXAMPLE ─────────────
# │ myFile = open('report.pdf', 'rb')
# └───────────────────────




# Q3: Use PyPDF2.PdfFileReader() with pdfFile to create pdfReader
# WHAT IT DOES: Creates a reader object for the PDF file
# ┌─ EXAMPLE ─────────────
# │ reader = PyPDF2.PdfFileReader(myFile)
# └───────────────────────




# Q4: Use PyPDF2.PdfFileWriter() to create pdfWriter
# WHAT IT DOES: Creates a writer object that will hold the encrypted PDF
# ┌─ EXAMPLE ─────────────
# │ writer = PyPDF2.PdfFileWriter()
# └───────────────────────




# Q5: Use for loop with range(pdfReader.numPages) to copy all pages using getPage() and pdfWriter.addPage()
# WHAT IT DOES: Copies all pages from the original PDF to the writer
# ┌─ EXAMPLE ─────────────
# │ for pageNum in range(reader.numPages):
# │     writer.addPage(reader.getPage(pageNum))
# └───────────────────────




# Q6: Use pdfWriter.encrypt() with password 'protect2024' to encrypt the PDF
# WHAT IT DOES: Adds password protection to the PDF file
# ┌─ EXAMPLE ─────────────
# │ writer.encrypt('secret123')
# └───────────────────────




# Q7: Use open() with 'wb' to create 'invoice_encrypted.pdf' as resultFile, use pdfWriter.write(), then close both files
# WHAT IT DOES: Saves the encrypted PDF and closes file handles
# ┌─ EXAMPLE ─────────────
# │ output = open('protected.pdf', 'wb')
# │ writer.write(output)
# │ output.close()
# │ myFile.close()
# └───────────────────────



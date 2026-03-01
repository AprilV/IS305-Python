# SECTION 3: CREATING AND COPYING PDF PAGES - Practice

# Q1: Import PyPDF2 module
# WHAT IT DOES: Makes PyPDF2 functions available for working with PDF files
# ┌─ EXAMPLE ─────────────
# │ import sys
# └───────────────────────




# Q2: Use open() with 'rb' to open 'first.pdf' as pdf1File and 'second.pdf' as pdf2File
# WHAT IT DOES: Opens two PDF files so we can combine them
# ┌─ EXAMPLE ─────────────
# │ file1 = open('doc1.pdf', 'rb')
# │ file2 = open('doc2.pdf', 'rb')
# └───────────────────────




# Q3: Use PyPDF2.PdfFileReader() to create pdf1Reader and pdf2Reader from the file objects
# WHAT IT DOES: Creates reader objects for both PDF files
# ┌─ EXAMPLE ─────────────
# │ reader1 = PyPDF2.PdfFileReader(file1)
# │ reader2 = PyPDF2.PdfFileReader(file2)
# └───────────────────────




# Q4: Use PyPDF2.PdfFileWriter() to create pdfWriter
# WHAT IT DOES: Creates a writer object that will hold pages for the new PDF
# ┌─ EXAMPLE ─────────────
# │ writer = PyPDF2.PdfFileWriter()
# └───────────────────────




# Q5: Use for loop with range(pdf1Reader.numPages) to copy all pages from pdf1Reader using getPage() and pdfWriter.addPage()
# WHAT IT DOES: Loops through all pages of first PDF and adds them to writer
# ┌─ EXAMPLE ─────────────
# │ for pageNum in range(reader1.numPages):
# │     page = reader1.getPage(pageNum)
# │     writer.addPage(page)
# └───────────────────────




# Q6: Use pdf2Reader.getPage(1) to get page 1 from second PDF and use pdfWriter.addPage() to add it
# WHAT IT DOES: Adds a specific page from the second PDF to the writer
# ┌─ EXAMPLE ─────────────
# │ page = reader2.getPage(0)
# │ writer.addPage(page)
# └───────────────────────




# Q7: Use open() with 'wb' to open 'merged.pdf' as pdfOutputFile
# WHAT IT DOES: Creates a new file in write-binary mode for the combined PDF
# ┌─ EXAMPLE ─────────────
# │ outputFile = open('combined.pdf', 'wb')
# └───────────────────────




# Q8: Use pdfWriter.write() with pdfOutputFile to write the combined PDF
# WHAT IT DOES: Writes all the pages to the new PDF file
# ┌─ EXAMPLE ─────────────
# │ writer.write(outputFile)
# └───────────────────────




# Q9: Use .close() to close pdfOutputFile, pdf1File, and pdf2File
# WHAT IT DOES: Closes all files to save changes and free resources
# ┌─ EXAMPLE ─────────────
# │ outputFile.close()
# │ file1.close()
# │ file2.close()
# └───────────────────────



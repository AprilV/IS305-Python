# SECTION 1: PYPDF2 BASICS - Practice

# Q1: Import PyPDF2 module
# WHAT IT DOES: Makes PyPDF2 functions available for working with PDF files
# ┌─ EXAMPLE ─────────────
# │ import sys
# └───────────────────────




# Q2: Use open() with 'rb' mode to open 'report.pdf' and store in variable pdfFileObj
# WHAT IT DOES: Opens a PDF file in read-binary mode so PyPDF2 can read it
# ┌─ EXAMPLE ─────────────
# │ fileObj = open('document.pdf', 'rb')
# └───────────────────────




# Q3: Use PyPDF2.PdfFileReader() with pdfFileObj to create reader object and store in pdfReader
# WHAT IT DOES: Creates a reader object that can extract information from the PDF
# ┌─ EXAMPLE ─────────────
# │ reader = PyPDF2.PdfFileReader(fileObj)
# └───────────────────────




# Q4: Use pdfReader.numPages to get total pages and print it
# WHAT IT DOES: Returns the total number of pages in the PDF document
# ┌─ EXAMPLE ─────────────
# │ page_count = reader.numPages
# │ print(page_count)
# └───────────────────────




# Q5: Use pdfReader.getPage(2) to get page 2 (third page) and store in pageObj
# WHAT IT DOES: Gets a specific page object from the PDF (pages are 0-indexed)
# ┌─ EXAMPLE ─────────────
# │ page = reader.getPage(0)
# └───────────────────────




# Q6: Use pageObj.extractText() to extract text and print it
# WHAT IT DOES: Extracts all text content from a PDF page as a string
# ┌─ EXAMPLE ─────────────
# │ text = page.extractText()
# │ print(text)
# └───────────────────────




# Q7: Use pdfFileObj.close() to close the file
# WHAT IT DOES: Closes the PDF file to free up system resources
# ┌─ EXAMPLE ─────────────
# │ fileObj.close()
# └───────────────────────



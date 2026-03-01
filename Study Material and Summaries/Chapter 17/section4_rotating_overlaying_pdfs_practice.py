# SECTION 4: ROTATING AND OVERLAYING PDF PAGES - Practice

# Q1: Import PyPDF2 module
# WHAT IT DOES: Makes PyPDF2 functions available for working with PDF files
# ┌─ EXAMPLE ─────────────
# │ import sys
# └───────────────────────




# Q2: Use open() with 'rb' to open 'document.pdf' and store in pdfFile
# WHAT IT DOES: Opens a PDF file for reading and rotating pages
# ┌─ EXAMPLE ─────────────
# │ myFile = open('sample.pdf', 'rb')
# └───────────────────────




# Q3: Use PyPDF2.PdfFileReader() with pdfFile to create pdfReader
# WHAT IT DOES: Creates a reader object for the PDF file
# ┌─ EXAMPLE ─────────────
# │ reader = PyPDF2.PdfFileReader(myFile)
# └───────────────────────




# Q4: Use pdfReader.getPage(0) to get page 0 and store in variable page
# WHAT IT DOES: Gets the first page object from the PDF
# ┌─ EXAMPLE ─────────────
# │ firstPage = reader.getPage(0)
# └───────────────────────




# Q5: Use page.rotateClockwise(180) to rotate the page 180 degrees
# WHAT IT DOES: Rotates a page clockwise by specified degrees (90, 180, 270)
# ┌─ EXAMPLE ─────────────
# │ firstPage.rotateClockwise(90)
# └───────────────────────




# Q6: Use PyPDF2.PdfFileWriter() to create pdfWriter
# WHAT IT DOES: Creates a writer object to save the rotated page
# ┌─ EXAMPLE ─────────────
# │ writer = PyPDF2.PdfFileWriter()
# └───────────────────────




# Q7: Use pdfWriter.addPage() with page to add the rotated page
# WHAT IT DOES: Adds the rotated page to the writer
# ┌─ EXAMPLE ─────────────
# │ writer.addPage(firstPage)
# └───────────────────────




# Q8: Use open() with 'rb' to open 'stamp.pdf' and store in stampFile
# WHAT IT DOES: Opens a PDF file that will be used as a watermark
# ┌─ EXAMPLE ─────────────
# │ watermark = open('logo.pdf', 'rb')
# └───────────────────────




# Q9: Use PyPDF2.PdfFileReader() with stampFile to create stampReader
# WHAT IT DOES: Creates a reader for the watermark PDF
# ┌─ EXAMPLE ─────────────
# │ watermarkReader = PyPDF2.PdfFileReader(watermark)
# └───────────────────────




# Q10: Use stampReader.getPage(0) to get page 0 and store in stampPage
# WHAT IT DOES: Gets the watermark page to overlay on other pages
# ┌─ EXAMPLE ─────────────
# │ watermarkPage = watermarkReader.getPage(0)
# └───────────────────────




# Q11: Use page.mergePage() with stampPage to overlay the watermark
# WHAT IT DOES: Merges/overlays one page on top of another page
# ┌─ EXAMPLE ─────────────
# │ firstPage.mergePage(watermarkPage)
# └───────────────────────




# Q12: Use open() with 'wb' to create 'rotated_stamped.pdf' as outputFile, use pdfWriter.write(), then close all files
# WHAT IT DOES: Saves the modified PDF and closes all file handles
# ┌─ EXAMPLE ─────────────
# │ output = open('final.pdf', 'wb')
# │ writer.write(output)
# │ output.close()
# │ myFile.close()
# │ watermark.close()
# └───────────────────────



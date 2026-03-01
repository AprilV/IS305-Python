# SECTION 7: CREATING AND STYLING WORD DOCUMENTS - Practice

# Q1: Import docx module
# WHAT IT DOES: Makes python-docx functions available for creating Word documents
# ┌─ EXAMPLE ─────────────
# │ import sys
# └───────────────────────




# Q2: Use docx.Document() with no arguments to create new document and store in doc
# WHAT IT DOES: Creates a blank Word document object
# ┌─ EXAMPLE ─────────────
# │ newDoc = docx.Document()
# └───────────────────────




# Q3: Use doc.add_heading() with 'Project Report' and level 0 to add main heading
# WHAT IT DOES: Adds a heading with specified text at level 0 (Title style)
# ┌─ EXAMPLE ─────────────
# │ newDoc.add_heading('Annual Report', 0)
# └───────────────────────




# Q4: Use doc.add_heading() with 'Introduction' and level 1 to add section heading
# WHAT IT DOES: Adds a heading at level 1 (Heading 1 style)
# ┌─ EXAMPLE ─────────────
# │ newDoc.add_heading('Overview', 1)
# └───────────────────────




# Q5: Use doc.add_paragraph() to add 'This report summarizes our findings.'
# WHAT IT DOES: Adds a regular paragraph with specified text
# ┌─ EXAMPLE ─────────────
# │ newDoc.add_paragraph('This is the introduction.')
# └───────────────────────




# Q6: Use doc.add_paragraph() with style 'Intense Quote' to add 'Important note'
# WHAT IT DOES: Adds a paragraph with a specific Word style applied
# ┌─ EXAMPLE ─────────────
# │ newDoc.add_paragraph('Key finding', 'Intense Quote')
# └───────────────────────




# Q7: Use doc.add_paragraph() to create para with 'Regular text, ', then use para.add_run() to add bold and italic text
# WHAT IT DOES: Creates paragraph with mixed formatting using runs
# ┌─ EXAMPLE ─────────────
# │ p = newDoc.add_paragraph('Normal, ')
# │ r = p.add_run('important, ')
# │ r.bold = True
# │ r2 = p.add_run('emphasized.')
# │ r2.italic = True
# └───────────────────────




# Q8: Use doc.add_page_break() to add a page break
# WHAT IT DOES: Inserts a page break to start new page
# ┌─ EXAMPLE ─────────────
# │ newDoc.add_page_break()
# └───────────────────────




# Q9: Use doc.add_picture() to add 'logo.png' with width of 3 inches using docx.shared.Inches()
# WHAT IT DOES: Inserts an image with specified width
# ┌─ EXAMPLE ─────────────
# │ newDoc.add_picture('image.jpg', width=docx.shared.Inches(2))
# └───────────────────────




# Q10: Use doc.save() to save document as 'project_report.docx'
# WHAT IT DOES: Saves the document to a file
# ┌─ EXAMPLE ─────────────
# │ newDoc.save('output.docx')
# └───────────────────────



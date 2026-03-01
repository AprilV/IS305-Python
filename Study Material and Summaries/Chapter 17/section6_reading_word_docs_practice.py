# SECTION 6: READING WORD DOCUMENTS - Practice

# Q1: Import docx module
# WHAT IT DOES: Makes python-docx functions available for working with Word documents
# ┌─ EXAMPLE ─────────────
# │ import sys
# └───────────────────────




# Q2: Use docx.Document() to open 'resume.docx' and store in variable doc
# WHAT IT DOES: Opens a Word document and creates a Document object
# ┌─ EXAMPLE ─────────────
# │ myDoc = docx.Document('letter.docx')
# └───────────────────────




# Q3: Use len(doc.paragraphs) to get number of paragraphs and print it
# WHAT IT DOES: Returns total count of paragraphs in the document
# ┌─ EXAMPLE ─────────────
# │ count = len(myDoc.paragraphs)
# │ print(count)
# └───────────────────────




# Q4: Use doc.paragraphs[3] to access paragraph at index 3 and print its text using .text
# WHAT IT DOES: Gets a specific paragraph and reads its text content
# ┌─ EXAMPLE ─────────────
# │ para = myDoc.paragraphs[0]
# │ print(para.text)
# └───────────────────────




# Q5: Use for loop to iterate through doc.paragraphs and print each paragraph's text
# WHAT IT DOES: Loops through all paragraphs in the document
# ┌─ EXAMPLE ─────────────
# │ for para in myDoc.paragraphs:
# │     print(para.text)
# └───────────────────────




# Q6: Get first paragraph using doc.paragraphs[0], then use len(para.runs) to get number of runs and print it
# WHAT IT DOES: Shows how many runs (text fragments with same style) are in a paragraph
# ┌─ EXAMPLE ─────────────
# │ firstPara = myDoc.paragraphs[0]
# │ runCount = len(firstPara.runs)
# │ print(runCount)
# └───────────────────────




# Q7: Use for loop to iterate through para.runs and print text, bold, and italic properties
# WHAT IT DOES: Loops through runs to check text styling (bold, italic, etc.)
# ┌─ EXAMPLE ─────────────
# │ for run in firstPara.runs:
# │     print(run.text, run.bold, run.italic)
# └───────────────────────



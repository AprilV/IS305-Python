# CHAPTER 14 - SECTION 4: FORMULAS

# What: Set Excel formulas in cells programmatically
# Why: Let Excel calculate values instead of Python
# How: Assign formula strings (starting with =) to cells

import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active

# Add numbers
sheet['A1'] = 200
sheet['A2'] = 300

# Add a formula (starts with =)
sheet['A3'] = '=SUM(A1:A2)'

wb.save('writeFormula.xlsx')

# When opened in Excel, A3 will show 500

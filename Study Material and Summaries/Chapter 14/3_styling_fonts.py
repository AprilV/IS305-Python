# CHAPTER 14 - SECTION 3: STYLING AND FONTS

# What: Apply font styles to cells in Excel
# Why: Make spreadsheets readable and highlight important data
# How: Create Font objects and assign to cell.font attribute

import openpyxl
from openpyxl.styles import Font

wb = openpyxl.Workbook()
sheet = wb['Sheet']

# Create a Font object and apply it
italic24Font = Font(size=24, italic=True)
sheet['A1'].font = italic24Font
sheet['A1'] = 'Hello, world!'

# Multiple font styles
fontObj1 = Font(name='Times New Roman', bold=True)
sheet['A1'].font = fontObj1
sheet['A1'] = 'Bold Times New Roman'

fontObj2 = Font(size=24, italic=True)
sheet['B3'].font = fontObj2
sheet['B3'] = '24 pt Italic'

wb.save('styles.xlsx')

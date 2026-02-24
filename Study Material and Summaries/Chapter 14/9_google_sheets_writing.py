# CHAPTER 14 - SECTION 9: WRITING GOOGLE SHEETS

# What: Write data to Google Sheets online
# Why: Create and update spreadsheets from Python
# How: Use sheet['A1'] = value or sheet.updateRow()

# NOTE: Code commented - requires EZSheets setup

# import ezsheets

# Create spreadsheet and get sheet
# ss = ezsheets.createSpreadsheet('My Data')
# sheet = ss[0]

# Write to cells
# sheet['A1'] = 'Name'
# sheet['B1'] = 'Age'

# Write entire row (faster!)
# sheet.updateRow(2, ['Alice', 30])
# sheet.updateRow(3, ['Bob', 25])

# Write entire column
# sheet.updateColumn('C', ['City', 'Seattle', 'Portland'])

# Create new sheet (tab)
# new_sheet = ss.createSheet('Summary')

# Resize sheet
# sheet.rowCount = 100
# sheet.columnCount = 10

# Download spreadsheet
# ss.downloadAsExcel()  # .xlsx file
# ss.downloadAsCSV()    # .csv file
# ss.downloadAsPDF()    # .pdf file

# Delete sheet
# sheet.delete()  # Move to trash

# REMEMBER:
# - sheet['A1'] = value writes to cell
# - sheet.updateRow() writes entire row (much faster)
# - sheet.updateColumn() writes entire column
# - Bulk updates are faster than cell-by-cell
# - Changes sync online immediately

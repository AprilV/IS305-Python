# CHAPTER 14 - SECTION 8: READING GOOGLE SHEETS

# What: Read data from Google Sheets online
# Why: Access spreadsheet data without downloading files
# How: Create/open Spreadsheet object, access sheets and cells

# NOTE: Code commented - requires EZSheets setup

# import ezsheets

# Create new spreadsheet
# ss = ezsheets.createSpreadsheet('My Data')
# print(ss.title, ss.url, ss.spreadsheetId)

# Open existing spreadsheet
# ss = ezsheets.Spreadsheet('spreadsheet-id-here')

# Get a sheet (tab)
# sheet = ss[0]  # First sheet
# sheet = ss['Sheet1']  # By name

# Read cells
# value = sheet['A1']
# value = sheet.getRow(1)  # Returns list
# value = sheet.getColumn('A')  # Returns list

# List all spreadsheets
# all_sheets = ezsheets.listSpreadsheets()

# Upload Excel file
# ss = ezsheets.upload('data.xlsx')

# Refresh if edited online
# ss.refresh()

# REMEMBER:
# - Spreadsheet = entire file, Sheet = one tab
# - sheet['A1'] reads single cell
# - sheet.getRow(1) reads entire row as list
# - sheet.getColumn('A') reads entire column as list
# - Row/column numbers start at 1

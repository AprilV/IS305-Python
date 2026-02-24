# SECTION 7: GOOGLE SHEETS SETUP - Practice

# Q1: Install ezsheets using pip install --user ezsheets in terminal (comment this line after installing)
# WHAT IT DOES: Installs the EZSheets module that wraps Google Sheets API for easy Python access
# ┌─ EXAMPLE ─────────────
# │ # Command in terminal:
# │ # pip install --user openpyxl
# └───────────────────────




# Q2: Import ezsheets module (first import will open browser for authentication)
# WHAT IT DOES: Makes EZSheets functions available and triggers Google account login on first use
# ┌─ EXAMPLE ─────────────
# │ import openpyxl
# └───────────────────────




# Q3: Use ezsheets.listSpreadsheets() to get dictionary of all spreadsheets and store in variable sheets_dict
# WHAT IT DOES: Returns dictionary with spreadsheet IDs as keys and titles as values
# ┌─ EXAMPLE ─────────────
# │ my_sheets = ezsheets.listSpreadsheets()
# │ print(my_sheets)
# └───────────────────────




# Q4: Use print() to display all spreadsheet titles using sheets_dict.values()
# WHAT IT DOES: Shows names of all Google Sheets files in your account
# ┌─ EXAMPLE ─────────────
# │ for title in my_sheets.values():
# │     print(title)
# └───────────────────────




# Q5: Use for loop with sheets_dict.items() to print each spreadsheet ID and title
# WHAT IT DOES: Displays both the unique spreadsheet ID and its title for all sheets
# ┌─ EXAMPLE ─────────────
# │ for sheet_id, title in my_sheets.items():
# │     print(f'{title}: {sheet_id}')
# └───────────────────────




# NOTE: Before running this file, you need:
# 1. Enable Google Sheets API at https://console.developers.google.com/
# 2. Enable Google Drive API
# 3. Download credentials.json and rename to credentials-sheets.json
# 4. Place credentials-sheets.json in same folder as this script
# 5. First import will create token-sheets.pickle and token-drive.pickle files

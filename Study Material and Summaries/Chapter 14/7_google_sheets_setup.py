# CHAPTER 14 - SECTION 7: GOOGLE SHEETS SETUP

# What: Install and configure EZSheets for Google Sheets access
# Why: Work with online spreadsheets from Python
# How: pip install ezsheets, get credentials from Google

# Installation: pip install --user ezsheets

# Setup steps:
# 1. Enable Google Sheets API at console.developers.google.com
# 2. Enable Google Drive API
# 3. Download credentials.json, rename to credentials-sheets.json
# 4. First import opens browser for authentication
# 5. Creates token-sheets.pickle and token-drive.pickle

# SECURITY: Never share credential or token files!

# After setup, test import:
# import ezsheets
# sheets = ezsheets.listSpreadsheets()
# print(sheets)  # Shows all your Google Sheets

# REMEMBER:
# - Need 3 files: credentials-sheets.json, token-sheets.pickle, token-drive.pickle
# - First import requires browser login
# - Keep credentials private (add to .gitignore)
# - Revoke credentials if accidentally shared

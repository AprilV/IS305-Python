# SECTION 8: READING GOOGLE SHEETS - Practice

# Q1: Import ezsheets module
# WHAT IT DOES: Makes EZSheets functions available for working with Google Sheets
# ┌─ EXAMPLE ─────────────
# │ import openpyxl
# └───────────────────────




# Q2: Use ezsheets.createSpreadsheet() with title 'My Test Sheet' to create new spreadsheet and store in variable ss
# WHAT IT DOES: Creates a new blank Google Sheets spreadsheet online and returns Spreadsheet object
# ┌─ EXAMPLE ─────────────
# │ my_ss = ezsheets.createSpreadsheet('Budget 2024')
# └───────────────────────




# Q3: Use print() to print ss.title
# WHAT IT DOES: Displays the name of the spreadsheet
# ┌─ EXAMPLE ─────────────
# │ print(my_ss.title)
# └───────────────────────




# Q4: Use print() to print ss.spreadsheetId
# WHAT IT DOES: Shows the unique ID that identifies this spreadsheet in Google Sheets
# ┌─ EXAMPLE ─────────────
# │ print(my_ss.spreadsheetId)
# └───────────────────────




# Q5: Use print() to print ss.url
# WHAT IT DOES: Displays the full URL to open this spreadsheet in a web browser
# ┌─ EXAMPLE ─────────────
# │ print(my_ss.url)
# └───────────────────────




# Q6: Use print() to print ss.sheetTitles
# WHAT IT DOES: Shows list of all sheet tab names in the spreadsheet
# ┌─ EXAMPLE ─────────────
# │ print(my_ss.sheetTitles)
# └───────────────────────




# Q7: Use ss[0] to get first sheet and store in variable sheet
# WHAT IT DOES: Accesses a specific sheet by index number
# ┌─ EXAMPLE ─────────────
# │ first_sheet = my_ss[0]
# └───────────────────────




# Q8: Set ss.title equal to 'Renamed Spreadsheet'
# WHAT IT DOES: Changes the name of the entire spreadsheet file
# ┌─ EXAMPLE ─────────────
# │ my_ss.title = 'Sales Report'
# └───────────────────────




# Q9: Use sheet['A1'] to get value of cell A1 and print it
# WHAT IT DOES: Reads contents of a cell using coordinate notation
# ┌─ EXAMPLE ─────────────
# │ cell_value = first_sheet['B2']
# │ print(cell_value)
# └───────────────────────




# Q10: Use sheet.getRow(1) to get first row as list and store in variable row1
# WHAT IT DOES: Returns all cell values from specified row number as a list
# ┌─ EXAMPLE ─────────────
# │ second_row = first_sheet.getRow(2)
# └───────────────────────




# Q11: Use sheet.getColumn('A') to get column A as list and store in variable colA
# WHAT IT DOES: Returns all cell values from specified column letter as a list
# ┌─ EXAMPLE ─────────────
# │ column_b = first_sheet.getColumn('B')
# └───────────────────────




# Q12: Use sheet.getColumn(1) to get first column by number and print it
# WHAT IT DOES: Gets column data using column number instead of letter (1=A, 2=B, etc)
# ┌─ EXAMPLE ─────────────
# │ col_data = first_sheet.getColumn(3)
# │ print(col_data)
# └───────────────────────




# Q13: Use ezsheets.Spreadsheet() with spreadsheet ID to open existing spreadsheet
# WHAT IT DOES: Opens a spreadsheet that already exists using its unique ID
# ┌─ EXAMPLE ─────────────
# │ existing = ezsheets.Spreadsheet('1abc123XYZ')
# └───────────────────────




# Q14: Use ezsheets.upload() to upload 'myfile.xlsx' Excel file to Google Sheets and store in variable uploaded_ss
# WHAT IT DOES: Converts and uploads local Excel file to Google Sheets online
# ┌─ EXAMPLE ─────────────
# │ new_ss = ezsheets.upload('data.xlsx')
# └───────────────────────




# Q15: Use ss.refresh() to update spreadsheet data from server
# WHAT IT DOES: Reloads latest changes if spreadsheet was edited by someone else
# ┌─ EXAMPLE ─────────────
# │ my_ss.refresh()
# └───────────────────────

print("=== EXERCISE 1: Create and Read Spreadsheet ===")
# Create a new spreadsheet with some data, then read it back

# UNCOMMENT after setup:
# import ezsheets
# 
# # Create spreadsheet
# ss = ezsheets.createSpreadsheet('Reading Practice')
# sheet = ss[0]
# 
# # Write some data
# sheet['A1'] = 'Name'
# sheet['B1'] = 'Score'
# sheet['A2'] = 'Alice'
# sheet['B2'] = '95'
# sheet['A3'] = 'Bob'  
# sheet['B3'] = '87'
# 
# # Read it back
# print(f"A1: {sheet['A1']}")
# print(f"B2: {sheet['B2']}")
# 
# # Read first row
# row1 = sheet.getRow(1)
# print(f"Row 1: {row1}")

print("\n=== EXERCISE 2: Column Letter Conversion ===")
# Practice converting between column letters and numbers

# import ezsheets
# 
# # Convert these numbers to letters
# numbers_to_convert = [1, 5, 26, 27, 52, 100]
# 
# for num in numbers_to_convert:
#     letter = ezsheets.getColumnLetterOf(num)
#     print(f"Column {num} = {letter}")
# 
# # Convert these letters to numbers  
# letters_to_convert = ['A', 'Z', 'AA', 'AZ', 'ZZ']
# 
# for letter in letters_to_convert:
#     num = ezsheets.getColumnNumberOf(letter)
#     print(f"Column {letter} = {num}")

print("\n=== EXERCISE 3: Address Conversion ===")
# Practice converting between address formats

# import ezsheets
# 
# # Convert these addresses to (column, row) tuples
# addresses = ['A1', 'B5', 'Z10', 'AA1', 'AB100']
# 
# for addr in addresses:
#     col, row = ezsheets.convertAddress(addr)
#     print(f"{addr} = ({col}, {row})")
# 
# # Convert back to addresses
# coordinates = [(1, 1), (2, 5), (26, 10), (27, 1)]
# 
# for col, row in coordinates:
#     addr = ezsheets.convertAddress(col, row)
#     print(f"({col}, {row}) = {addr}")

print("\n=== EXERCISE 4: Reading Student Data ===")
# Create a grade sheet and calculate averages

# import ezsheets
# 
# ss = ezsheets.createSpreadsheet('Student Grades')
# sheet = ss[0]
# 
# # Write headers and data
# sheet.updateRow(1, ['Name', 'Math', 'Science', 'English'])
# sheet.updateRow(2, ['Alice', '95', '88', '92'])
# sheet.updateRow(3, ['Bob', '87', '85', '90'])
# sheet.updateRow(4, ['Charlie', '92', '91', '89'])
# sheet.updateRow(5, ['Diana', '88', '94', '87'])
# 
# # Read and calculate averages
# print("Student Averages:")
# for row_num in range(2, 6):
#     row = sheet.getRow(row_num)
#     name = row[0]
#     scores = [int(score) for score in row[1:4]]
#     average = sum(scores) / len(scores)
#     print(f"{name}: {average:.1f}")

print("\n=== EXERCISE 5: Reading Inventory ===")
# Create an inventory sheet and find specific items

# import ezsheets
# 
# ss = ezsheets.createSpreadsheet('Store Inventory')
# sheet = ss[0]
# 
# # Write inventory data
# sheet.updateRow(1, ['Product', 'Quantity', 'Price'])
# sheet.updateRow(2, ['Apples', '150', '0.50'])
# sheet.updateRow(3, ['Bananas', '200', '0.30'])
# sheet.updateRow(4, ['Oranges', '100', '0.75'])
# sheet.updateRow(5, ['Grapes', '75', '1.20'])
# 
# # Find all products with quantity > 100
# print("Products with quantity > 100:")
# for row_num in range(2, 6):
#     row = sheet.getRow(row_num)
#     product = row[0]
#     quantity = int(row[1])
#     if quantity > 100:
#         print(f"  {product}: {quantity}")

print("\n=== EXERCISE 6: Reading Entire Columns ===")
# Read entire columns and perform calculations

# import ezsheets
# 
# ss = ezsheets.Spreadsheet('your-spreadsheet-id-here')
# sheet = ss[0]
# 
# # Read column A (names)
# names = sheet.getColumn('A')
# print(f"Names column: {names}")
# 
# # Read column B (numbers)
# numbers = sheet.getColumn('B')
# numbers = [float(n) for n in numbers if n]  # Convert to floats, skip empty
# print(f"Sum of column B: {sum(numbers)}")
# print(f"Average of column B: {sum(numbers) / len(numbers)}")

print("\n=== EXERCISE 7: List All Your Sheets ===")
# List all spreadsheets and their sheets

# import ezsheets
# 
# spreadsheets = ezsheets.listSpreadsheets()
# 
# print(f"Found {len(spreadsheets)} spreadsheet(s):\n")
# 
# for sheet_id, title in spreadsheets.items():
#     ss = ezsheets.Spreadsheet(sheet_id)
#     print(f"{title}:")
#     print(f"  URL: {ss.url}")
#     print(f"  Sheets: {ss.sheetTitles}")
#     print()

print("\n=== EXERCISE 8: Upload and Read Excel File ===")
# Upload an existing Excel file and read its data

# import ezsheets
# 
# # Upload Excel file
# ss = ezsheets.upload('my_data.xlsx')
# print(f"Uploaded: {ss.title}")
# 
# # Read first sheet
# sheet = ss[0]
# 
# # Get first 5 rows
# print("First 5 rows:")
# for row_num in range(1, 6):
#     row = sheet.getRow(row_num)
#     print(f"Row {row_num}: {row}")

print("\n=== CHALLENGE: Phone Book Search ===")
# Create a phone book and search for contacts

# import ezsheets
# 
# ss = ezsheets.createSpreadsheet('Phone Book')
# sheet = ss[0]
# 
# # Create phone book
# sheet.updateRow(1, ['Name', 'Phone', 'Email'])
# contacts = [
#     ['Alice Smith', '555-0101', 'alice@example.com'],
#     ['Bob Jones', '555-0102', 'bob@example.com'],
#     ['Charlie Brown', '555-0103', 'charlie@example.com'],
#     ['Alice Johnson', '555-0104', 'alice.j@example.com']
# ]
# 
# for i, contact in enumerate(contacts, start=2):
#     sheet.updateRow(i, contact)
# 
# # Search function
# def searchContacts(sheet, search_term):
#     """Search for contacts containing search term."""
#     results = []
#     # Skip header row
#     for row_num in range(2, sheet.rowCount + 1):
#         row = sheet.getRow(row_num)
#         if not row[0]:  # Empty row
#             break
#         # Check if search term in name
#         if search_term.lower() in row[0].lower():
#             results.append(row)
#     return results
# 
# # Search for "Alice"
# found = searchContacts(sheet, 'Alice')
# print(f"Found {len(found)} contact(s) matching 'Alice':")
# for contact in found:
#     print(f"  {contact[0]}: {contact[1]}")

print("\n" + "="*50)
print("KEY CONCEPTS:")
print("- Spreadsheet object = entire file")
print("- Sheet object = one tab/worksheet")
print("- sheet['A1'] reads a cell")
print("- sheet.getRow(n) reads entire row")
print("- sheet.getColumn('A') reads entire column")
print("- Row/column numbers start at 1")
print("="*50)

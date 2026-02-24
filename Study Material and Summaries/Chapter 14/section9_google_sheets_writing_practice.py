# SECTION 9: WRITING GOOGLE SHEETS - Practice

# Q1: Import ezsheets module
# WHAT IT DOES: Makes EZSheets functions available for working with Google Sheets
# ┌─ EXAMPLE ─────────────
# │ import openpyxl
# └───────────────────────




# Q2: Use ezsheets.createSpreadsheet() with title 'Student Grades' to create spreadsheet, store in ss, get first sheet with ss[0] in variable sheet
# WHAT IT DOES: Creates new spreadsheet and gets a Sheet object to write data to
# ┌─ EXAMPLE ─────────────
# │ my_ss = ezsheets.createSpreadsheet('Inventory')
# │ my_sheet = my_ss[0]
# └───────────────────────




# Q3: Use sheet['A1'] to write 'Name' to cell A1
# WHAT IT DOES: Sets the value of a cell using coordinate notation
# ┌─ EXAMPLE ─────────────
# │ my_sheet['B1'] = 'Price'
# └───────────────────────




# Q4: Use sheet['B1'] to write 'Score' to cell B1 and use sheet['A2'] to write 'Alice' to cell A2
# WHAT IT DOES: Writes text values to multiple cells
# ┌─ EXAMPLE ─────────────
# │ my_sheet['C1'] = 'Quantity'
# │ my_sheet['A3'] = 'Laptop'
# └───────────────────────




# Q5: Use sheet.updateRow() with row number 2 and list ['Bob', 85] to write entire row at once
# WHAT IT DOES: Writes multiple values to a row in single operation (much faster than cell by cell)
# ┌─ EXAMPLE ─────────────
# │ my_sheet.updateRow(3, ['Mouse', 25])
# └───────────────────────




# Q6: Use sheet.updateColumn() with column 'A' and list ['Name', 'Charlie', 'Diana'] to write column data
# WHAT IT DOES: Writes multiple values down a column in single operation
# ┌─ EXAMPLE ─────────────
# │ my_sheet.updateColumn('B', ['Price', 10.50, 7.25])
# └───────────────────────




# Q7: Use ss.createSheet() with title 'Summary' to add new sheet tab and store in variable new_sheet
# WHAT IT DOES: Creates a new worksheet tab in the spreadsheet
# ┌─ EXAMPLE ─────────────
# │ second_sheet = my_ss.createSheet('Details')
# └───────────────────────




# Q8: Use ss.createSheet() with title='First' and index=0 to add sheet at beginning
# WHAT IT DOES: Creates new sheet tab at specific position (0=first, 1=second, etc)
# ┌─ EXAMPLE ─────────────
# │ my_ss.createSheet(title='Cover', index=0)
# └───────────────────────




# Q9: Use sheet.title to set sheet name to 'Updated Name'
# WHAT IT DOES: Renames an existing sheet tab
# ┌─ EXAMPLE ─────────────
# │ my_sheet.title = 'March Data'
# └───────────────────────




# Q10: Use sheet.rowCount to set number of rows to 100
# WHAT IT DOES: Resizes the sheet to have exactly 100 rows
# ┌─ EXAMPLE ─────────────
# │ my_sheet.rowCount = 50
# └───────────────────────




# Q11: Use sheet.columnCount to set number of columns to 10
# WHAT IT DOES: Resizes the sheet to have exactly 10 columns
# ┌─ EXAMPLE ─────────────
# │ my_sheet.columnCount = 26
# └───────────────────────




# Q12: Use ss.downloadAsExcel() to download spreadsheet as Excel file
# WHAT IT DOES: Saves Google Sheet to your computer as .xlsx Excel file
# ┌─ EXAMPLE ─────────────
# │ my_ss.downloadAsExcel()
# └───────────────────────




# Q13: Use ss.downloadAsCSV() to download first sheet as CSV file
# WHAT IT DOES: Saves only the first sheet to your computer as .csv file
# ┌─ EXAMPLE ─────────────
# │ my_ss.downloadAsCSV()
# └───────────────────────




# Q14: Use ss.downloadAsPDF() to download spreadsheet as PDF file
# WHAT IT DOES: Saves spreadsheet to your computer as .pdf file
# ┌─ EXAMPLE ─────────────
# │ my_ss.downloadAsPDF()
# └───────────────────────




# Q15: Use sheet.delete() to delete a sheet from spreadsheet
# WHAT IT DOES: Removes the sheet tab from the spreadsheet (moved to trash, can be recovered)
# ┌─ EXAMPLE ─────────────
# │ my_sheet.delete()
# └───────────────────────




# Q16: Use ss.delete() to delete entire spreadsheet
# WHAT IT DOES: Moves entire spreadsheet file to Google Drive trash
# ┌─ EXAMPLE ─────────────
# │ my_ss.delete()
# └───────────────────────

print("=== EXERCISE 1: Create Gradebook ===")
# Create a gradebook with student names and grades

# UNCOMMENT after setup:
# import ezsheets
# 
# ss = ezsheets.createSpreadsheet('Class Gradebook')
# sheet = ss[0]
# 
# # Write headers
# sheet['A1'] = 'Student Name'
# sheet['B1'] = 'Homework'
# sheet['C1'] = 'Midterm'
# sheet['D1'] = 'Final'
# sheet['E1'] = 'Average'
# 
# # Write student data
# students = [
#     ['Alice', 95, 88, 92],
#     ['Bob', 87, 85, 90],
#     ['Charlie', 92, 91, 89],
#     ['Diana', 88, 94, 87]
# ]
# 
# row_num = 2
# for student in students:
#     name, hw, mid, final = student
#     avg = (hw + mid + final) / 3
#     sheet.updateRow(row_num, [name, hw, mid, final, f'{avg:.2f}'])
#     row_num += 1
# 
# print(f"Created gradebook: {ss.url}")

print("\n=== EXERCISE 2: Expense Tracker ===")
# Create expense tracking spreadsheet

# import ezsheets
# 
# ss = ezsheets.createSpreadsheet('Monthly Expenses')
# sheet = ss[0]
# 
# # Headers
# sheet.updateRow(1, ['Date', 'Category', 'Description', 'Amount'])
# 
# # Sample expenses
# expenses = [
#     ['2024-01-01', 'Food', 'Groceries', 85.50],
#     ['2024-01-02', 'Transport', 'Gas', 45.00],
#     ['2024-01-03', 'Entertainment', 'Movie tickets', 30.00],
#     ['2024-01-04', 'Food', 'Restaurant', 60.00],
#     ['2024-01-05', 'Utilities', 'Electric bill', 120.00]
# ]
# 
# for i, expense in enumerate(expenses, start=2):
#     sheet.updateRow(i, expense)
# 
# # Add total row
# last_row = len(expenses) + 2
# sheet[f'A{last_row}'] = 'TOTAL'
# sheet[f'D{last_row}'] = f'=SUM(D2:D{last_row-1})'
# 
# print(f"Expense tracker: {ss.url}")

print("\n=== EXERCISE 3: Multiplication Table ===")
# Create a 10x10 multiplication table

# import ezsheets
# 
# ss = ezsheets.createSpreadsheet('Multiplication Table')
# sheet = ss[0]
# sheet.title = '10x10 Times Table'
# 
# # Write column and row headers
# for i in range(1, 11):
#     sheet[1, i+1] = i  # First row
#     sheet[i+1, 1] = i  # First column
# 
# # Fill in multiplication values
# for row in range(1, 11):
#     values = []
#     for col in range(1, 11):
#         values.append(row * col)
#     sheet.updateRow(row + 1, [row] + values)
# 
# print(f"Multiplication table: {ss.url}")

print("\n=== EXERCISE 4: Todo List ===")
# Create a todo list with status tracking

# import ezsheets
# 
# ss = ezsheets.createSpreadsheet('Todo List')
# sheet = ss[0]
# 
# # Headers
# sheet.updateRow(1, ['Task', 'Priority', 'Status', 'Due Date'])
# 
# # Tasks
# tasks = [
#     ['Finish Python homework', 'High', 'In Progress', '2024-02-01'],
#     ['Study for exam', 'High', 'Not Started', '2024-02-05'],
#     ['Clean room', 'Medium', 'Not Started', '2024-02-03'],
#     ['Call dentist', 'Medium', 'Not Started', '2024-02-02'],
#     ['Buy groceries', 'Low', 'Completed', '2024-01-28']
# ]
# 
# for i, task in enumerate(tasks, start=2):
#     sheet.updateRow(i, task)
# 
# print(f"Todo list: {ss.url}")

print("\n=== EXERCISE 5: Update Existing Data ===")
# Practice updating cells and rows

# import ezsheets
# 
# ss = ezsheets.Spreadsheet('your-spreadsheet-id')
# sheet = ss[0]
# 
# # Update single cell
# sheet['B2'] = '100'
# 
# # Update entire row
# sheet.updateRow(3, ['New', 'Data', 'Here'])
# 
# # Update entire column
# sheet.updateColumn('C', ['Col C', '10', '20', '30'])
# 
# # Bulk update multiple rows
# rows = sheet.getRows()
# rows[1][0] = 'UPDATED'  # Change first cell of second row
# sheet.updateRows(rows)

print("\n=== EXERCISE 6: Create Multiple Sheets ===")
# Create spreadsheet with multiple tabs

# import ezsheets
# 
# ss = ezsheets.createSpreadsheet('Sales Data 2024')
# 
# # Create sheet for each quarter
# q1 = ss.createSheet('Q1 Sales', index=0)
# q2 = ss.createSheet('Q2 Sales', index=1)
# q3 = ss.createSheet('Q3 Sales', index=2)
# q4 = ss.createSheet('Q4 Sales', index=3)
# 
# # Delete default 'Sheet1'
# ss['Sheet1'].delete()
# 
# # Add headers to each sheet
# for sheet in ss.sheets:
#     sheet.updateRow(1, ['Month', 'Sales', 'Costs', 'Profit'])
# 
# print(f"Created spreadsheet with sheets: {ss.sheetTitles}")

print("\n=== EXERCISE 7: Download Spreadsheet ===")
# Download spreadsheet in different formats

# import ezsheets
# 
# ss = ezsheets.Spreadsheet('your-spreadsheet-id')
# 
# # Download as Excel
# filename = ss.downloadAsExcel()
# print(f"Downloaded Excel: {filename}")
# 
# # Download as CSV (first sheet only)
# filename = ss.downloadAsCSV()
# print(f"Downloaded CSV: {filename}")
# 
# # Download as PDF
# filename = ss.downloadAsPDF()
# print(f"Downloaded PDF: {filename}")

print("\n=== EXERCISE 8: Inventory System ===")
# Create complete inventory management system

# import ezsheets
# 
# ss = ezsheets.createSpreadsheet('Store Inventory System')
# sheet = ss[0]
# sheet.title = 'Current Inventory'
# 
# # Headers
# sheet.updateRow(1, ['SKU', 'Product', 'Quantity', 'Price', 'Total Value', 'Reorder Level'])
# 
# # Products
# inventory = [
#     ['SKU001', 'Widget A', 150, 10.50, '', 50],
#     ['SKU002', 'Widget B', 200, 7.25, '', 75],
#     ['SKU003', 'Gadget X', 80, 25.00, '', 40],
#     ['SKU004', 'Gadget Y', 120, 15.75, '', 60],
#     ['SKU005', 'Tool Z', 45, 50.00, '', 30]
# ]
# 
# # Write data with calculated total value
# for i, item in enumerate(inventory, start=2):
#     sku, product, qty, price, _, reorder = item
#     total_value = qty * price
#     sheet.updateRow(i, [sku, product, qty, price, f'${total_value:.2f}', reorder])
# 
# # Add conditional formatting check (manual in sheets)
# print("Low stock items (below reorder level):")
# for i in range(2, len(inventory) + 2):
#     row = sheet.getRow(i)
#     qty = int(row[2])
#     reorder = int(row[5])
#     if qty < reorder:
#         product = row[1]
#         print(f"  ⚠️  {product}: {qty} units (reorder at {reorder})")
# 
# print(f"\nInventory system: {ss.url}")

print("\n=== CHALLENGE: Budget Planner with Formulas ===")
# Create monthly budget with calculations

# import ezsheets
# 
# ss = ezsheets.createSpreadsheet('Monthly Budget Planner')
# sheet = ss[0]
# 
# # Income section
# sheet.updateRow(1, ['INCOME'])
# sheet.updateRow(2, ['Salary', 3500])
# sheet.updateRow(3, ['Freelance', 500])
# sheet.updateRow(4, ['Total Income', '=SUM(B2:B3)'])
# 
# # Expenses section
# sheet.updateRow(6, ['EXPENSES'])
# sheet.updateRow(7, ['Rent', 1200])
# sheet.updateRow(8, ['Utilities', 150])
# sheet.updateRow(9, ['Food', 400])
# sheet.updateRow(10, ['Transport', 200])
# sheet.updateRow(11, ['Entertainment', 100])
# sheet.updateRow(12, ['Total Expenses', '=SUM(B7:B11)'])
# 
# # Net savings
# sheet.updateRow(14, ['NET SAVINGS', '=B4-B12'])
# 
# # Read back the calculated values
# print("Budget Summary:")
# print(f"Total Income: {sheet['B4']}")
# print(f"Total Expenses: {sheet['B12']}")
# print(f"Net Savings: {sheet['B14']}")
# 
# print(f"\nBudget planner: {ss.url}")

print("\n" + "="*50)
print("KEY CONCEPTS:")
print("- sheet['A1'] = value writes to cell")
print("- sheet.updateRow() writes entire row")
print("- sheet.updateColumn() writes entire column")
print("- Bulk updates are much faster")
print("- Can use formulas like '=SUM(A1:A10)'")
print("- createSheet() adds new tabs")
print("- delete() removes sheets")
print("- Download in Excel, CSV, PDF formats")
print("="*50)

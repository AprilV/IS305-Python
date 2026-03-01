################################################################################
# My Practice - Lesson 6: Creating HTML Reports
################################################################################

# Q1: Import the CSV file into variable $myData
# WHAT IT DOES: Import-Csv reads CSV files and creates PowerShell objects from each row
# ┌─ EXAMPLE ─────────────
# │ $data = Import-Csv "C:\path\to\file.csv"
# └───────────────────────




# Q2: Pipe $myData to Select-Object -First 5, then pipe to ConvertTo-Html, store in variable $html
# WHAT IT DOES: ConvertTo-Html creates HTML table markup from PowerShell objects
# ┌─ EXAMPLE ─────────────
# │ $html = $employees | Select-Object -First 3 | ConvertTo-Html
# └───────────────────────




# Q3: Pipe $myData to Select-Object -First 10 Status, Project, Location, then pipe to ConvertTo-Html, store in variable $html
# WHAT IT DOES: You can select specific properties before converting to HTML
# ┌─ EXAMPLE ─────────────
# │ $html = $students | Select-Object -First 5 Name, Grade | ConvertTo-Html
# └───────────────────────




# Q4: Pipe $myData to Select-Object -First 5, then pipe to ConvertTo-Html with -Title "Construction Report", store in variable $html
# WHAT IT DOES: -Title adds a heading at the top of the HTML page
# ┌─ EXAMPLE ─────────────
# │ $html = $products | Select-Object -First 5 | ConvertTo-Html -Title "Product Catalog"
# └───────────────────────




# Q5: Create CSS style string with background-color: blue for th elements, store in variable $style using @" "@ here-string format
# WHAT IT DOES: CSS styles control colors, fonts, and formatting in HTML
# ┌─ EXAMPLE ─────────────
# │ $style = @"
# │ <style>
# │     th { background-color: green; color: white; }
# │ </style>
# │ "@
# └───────────────────────




# Q6: Pipe $myData to Select-Object -First 10, then pipe to ConvertTo-Html with -Head $style and -Title "Project Report", store in variable $html
# WHAT IT DOES: -Head inserts CSS styles into the HTML <head> section
# ┌─ EXAMPLE ─────────────
# │ $html = $orders | Select-Object -First 10 | ConvertTo-Html -Head $style -Title "Sales Report"
# └───────────────────────




# Q7: Display $html by typing $html on a line by itself
# WHAT IT DOES: Shows the HTML markup in the console so you can verify it
# ┌─ EXAMPLE ─────────────
# │ $html
# └───────────────────────
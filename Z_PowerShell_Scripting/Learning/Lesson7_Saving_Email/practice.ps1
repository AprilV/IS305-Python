################################################################################
# My Practice - Lesson 7: Saving Files and Sending Email
################################################################################

# Q1: Import the CSV file into variable $myData
# WHAT IT DOES: Import-Csv reads CSV files and creates PowerShell objects from each row
# ┌─ EXAMPLE ─────────────
# │ $data = Import-Csv "C:\path\to\file.csv"
# └───────────────────────




# Q2: Create variable $text with value "This is a test", pipe $text to Out-File with path "C:\temp\test.txt"
# WHAT IT DOES: Out-File writes text content to a file on disk
# ┌─ EXAMPLE ─────────────
# │ $text = "Hello World"
# │ $text | Out-File "C:\temp\hello.txt"
# └───────────────────────




# Q3: Pipe $html to Out-File with path "C:\temp\report.html" and -Encoding UTF8 parameter
# WHAT IT DOES: -Encoding UTF8 ensures special characters display correctly in HTML
# ┌─ EXAMPLE ─────────────
# │ $html | Out-File "C:\temp\report.html" -Encoding UTF8
# └───────────────────────




# Q4: Use Get-Date, store in variable $now, use Write-Host to display $now
# WHAT IT DOES: Get-Date returns the current system date and time
# ┌─ EXAMPLE ─────────────
# │ $now = Get-Date
# │ Write-Host $now
# └───────────────────────




# Q5: Use Get-Date with -Format "yyyyMMdd", store in variable $dateStamp, use Write-Host to display $dateStamp
# WHAT IT DOES: -Format parameter controls how dates are displayed
# ┌─ EXAMPLE ─────────────
# │ $dateStamp = Get-Date -Format "yyyyMMdd"
# │ Write-Host $dateStamp
# └───────────────────────




# Q6: Use Get-Date -Format "yyyyMMdd", store in variable $date. Create variable $filename with value "Report_$date.html"
# WHAT IT DOES: String interpolation combines text with date to create unique filenames
# ┌─ EXAMPLE ─────────────
# │ $date = Get-Date -Format "yyyyMMdd"
# │ $filename = "MyReport_$date.txt"
# └───────────────────────




# Q7: Use Test-Path to check if "C:\temp" exists, use if statement to Write-Host "Folder exists" if true
# WHAT IT DOES: Test-Path returns $true if a file or folder exists, $false if not
# ┌─ EXAMPLE ─────────────
# │ if (Test-Path "C:\somefolder") {
# │     Write-Host "Folder exists"
# │ }
# └───────────────────────




# Q8: Use if statement with -not (Test-Path "C:\Reports") to check if folder doesn't exist, then use New-Item with -Path "C:\Reports" and -ItemType Directory to create it
# WHAT IT DOES: New-Item creates new files or folders; -ItemType Directory makes it a folder
# ┌─ EXAMPLE ─────────────
# │ if (-not (Test-Path "C:\newfolder")) {
# │     New-Item -Path "C:\newfolder" -ItemType Directory
# │ }
# └───────────────────────
################################################################################
# Lesson 2: Import CSV and Display Data
# LEARN: Import-Csv, Select-Object, Format-Table, .Count
################################################################################

# ============================================================================
# WHAT WE'RE BUILDING: Construction Project Report
# ============================================================================
# Our project analyzes a CSV file with 10,254 construction project records
# This lesson teaches you how to IMPORT and DISPLAY that data
# ============================================================================


# ============================================================================
# PART 1: Import-Csv - Reading CSV Files
# ============================================================================
# Import-Csv reads a CSV (Comma-Separated Values) file
# It automatically converts each row into a PowerShell object
# Each column becomes a property you can access
#
# SYNTAX: $variable = Import-Csv "path\to\file.csv"
#
# IMPORTANT: Use the FULL path to the file
# ============================================================================

# Import the construction data
$data = Import-Csv "C:\ReactGitEC2\IS305 Scripting\Z_PowerShell_Scripting\Data\Construction_Data_PM_Forms_All_Projects.csv"

# At this point, $data contains ALL 10,254 records
# But we haven't displayed anything yet


# ============================================================================
# PART 2: .Count Property - How Many Records?
# ============================================================================
# Every collection (array) in PowerShell has a .Count property
# It tells you how many items are in the collection
#
# SYNTAX: $variable.Count
# ============================================================================

$totalRecords = $data.Count
Write-Host "Total construction records: $totalRecords"


# ============================================================================
# PART 3: Accessing Individual Records
# ============================================================================
# PowerShell uses [index] to access specific items
# Indexes start at 0 (first item = [0])
#
# SYNTAX: $variable[index]
# ============================================================================

# Get the first record (index 0)
$firstRecord = $data[0]

# Get the last record
$lastRecord = $data[-1]  # -1 means last item

# Display the first record (shows all properties)
Write-Host "`nFirst record:"
$firstRecord


# ============================================================================
# PART 4: Accessing Properties (Columns)
# ============================================================================
# Each record has properties matching the CSV column names
# Common properties in our data:
#   - Status (Open, Closed, etc.)
#   - Project (project name)
#   - Location
#   - Type
#   - OpenActions (number of open items)
#   - TotalActions (total items)
#   - OverDue (number overdue)
#
# SYNTAX: $record.PropertyName
# ============================================================================

Write-Host "`nFirst record details:"
Write-Host "Status: $($firstRecord.Status)"
Write-Host "Project: $($firstRecord.Project)"
Write-Host "Location: $($firstRecord.Location)"
Write-Host "Total Actions: $($firstRecord.TotalActions)"


# ============================================================================
# PART 5: Select-Object - Choosing Specific Rows or Columns
# ============================================================================
# Select-Object lets you:
#   - Get first/last N rows: -First, -Last
#   - Choose specific columns (properties)
#
# SYNTAX (get first N): $data | Select-Object -First N
# SYNTAX (choose columns): $data | Select-Object Property1, Property2
#
# The | symbol is called a "pipe" - it passes output to the next command
# ============================================================================

# Get first 5 records
Write-Host "`nFirst 5 records:"
$data | Select-Object -First 5

# Get first 5 records, but only show specific columns
Write-Host "`nFirst 5 records (selected columns):"
$data | Select-Object -First 5 Status, Project, Location


# ============================================================================
# PART 6: Format-Table - Making Data Readable
# ============================================================================
# Format-Table displays data in a table format
# Much easier to read than the default output
#
# SYNTAX: $data | Format-Table
# SYNTAX (auto-size columns): $data | Format-Table -AutoSize
# ============================================================================

Write-Host "`nFirst 10 records as a table:"
$data | Select-Object -First 10 | Format-Table -AutoSize

# Choose specific columns for the table
Write-Host "`nFirst 10 records (custom columns):"
$data | Select-Object -First 10 Status, Project, TotalActions, OverDue | Format-Table -AutoSize


# ============================================================================
# PART 7: Get-Member - Discovering Available Properties
# ============================================================================
# Get-Member shows you ALL properties and methods of an object
# Use this to see what columns are available in your CSV
#
# SYNTAX: $variable | Get-Member
# SYNTAX (just properties): $variable | Get-Member -MemberType NoteProperty
# ============================================================================

Write-Host "`nAvailable columns in the CSV:"
$data[0] | Get-Member -MemberType NoteProperty | Select-Object Name


# ============================================================================
# PART 8: Combining Commands with Pipes
# ============================================================================
# The pipe | lets you chain commands together
# Output from one command becomes input to the next
#
# Example: Get data → Select first 5 → Format as table
# ============================================================================

# This reads: "Take $data, get first 5 records, show as table"
$data | Select-Object -First 5 | Format-Table -AutoSize

# This reads: "Take $data, pick these columns, get first 10, show as table"
$data | Select-Object Status, Project, Location, OverDue | Select-Object -First 10 | Format-Table -AutoSize


################################################################################
# PRACTICE EXERCISES - Copy to practice.ps1 and complete
################################################################################
#
# Exercise 1: Import and Count
# - Import the CSV file into a variable called $records
# - Display the total number of records
# - Display the message: "Loaded [count] construction records"
#
# Exercise 2: Explore First and Last
# - Get the first record and display its Status and Project
# - Get the last record and display its Status and Project
# - Use Write-Host with descriptive labels
#
# Exercise 3: Select Specific Columns
# - Display the first 15 records
# - Show only: Status, Project, Location, TotalActions
# - Format as a table
#
# Exercise 4: Find Available Properties
# - Use Get-Member to see all property names in the CSV
# - Write them down - you'll need to know them for filtering later
#
# Exercise 5: Custom Display
# - Get the first 20 records
# - Show only Status, Project, and OverDue columns
# - Format as a table with -AutoSize
# - Add a Write-Host message before the table explaining what it shows
#
################################################################################

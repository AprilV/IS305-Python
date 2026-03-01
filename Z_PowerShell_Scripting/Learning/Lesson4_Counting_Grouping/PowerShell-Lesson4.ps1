################################################################################
# Lesson 4: Counting and Grouping Data
# LEARN: Measure-Object, Group-Object, Statistics
################################################################################

# ============================================================================
# WHAT WE'RE BUILDING: Construction Project Report
# ============================================================================
# Now we need to calculate metrics:
# - How many total records?
# - How many of each status (Open, Closed, etc.)?
# - Sum of all open actions
# - Average completion rates
# ============================================================================


# ============================================================================
# PART 1: Measure-Object - Calculating Statistics
# ============================================================================
# Measure-Object calculates statistics on collections
#
# CAPABILITIES:
# - Count: How many items
# - Sum: Add up numbers
# - Average: Calculate mean
# - Maximum: Find highest value
# - Minimum: Find lowest value
#
# SYNTAX (count): $collection | Measure-Object
# SYNTAX (sum): $collection | Measure-Object -Property PropertyName -Sum
# SYNTAX (multiple): $collection | Measure-Object -Property PropertyName -Sum -Average -Maximum -Minimum
# ============================================================================

# Import our data
$data = Import-Csv "C:\ReactGitEC2\IS305 Scripting\Z_PowerShell_Scripting\Data\Construction_Data_PM_Forms_All_Projects.csv"

# Count total records
$count = ($data | Measure-Object).Count
Write-Host "Total records: $count"


# ============================================================================
# PART 2: Measuring Numeric Properties
# ============================================================================
# Use -Property to specify which column to measure
# Use -Sum to add up values
# ============================================================================

# Sum of ALL TotalActions across all records
$totalActionsSum = ($data | Measure-Object -Property TotalActions -Sum).Sum
Write-Host "`nTotal actions across all projects: $totalActionsSum"

# Sum of ALL OverDue items
$totalOverdue = ($data | Measure-Object -Property OverDue -Sum).Sum
Write-Host "Total overdue items across all projects: $totalOverdue"

# Sum of ALL OpenActions
$totalOpen = ($data | Measure-Object -Property OpenActions -Sum).Sum
Write-Host "Total open actions across all projects: $totalOpen"


# ============================================================================
# PART 3: Average, Maximum, Minimum
# ============================================================================
# Get statistical summary of a column
# ============================================================================

# Get statistics for TotalActions
$stats = $data | Measure-Object -Property TotalActions -Average -Maximum -Minimum -Sum

Write-Host "`n=== TotalActions Statistics ==="
Write-Host "Count: $($stats.Count)"
Write-Host "Sum: $($stats.Sum)"
Write-Host "Average: $([Math]::Round($stats.Average, 2))"
Write-Host "Maximum: $($stats.Maximum)"
Write-Host "Minimum: $($stats.Minimum)"


# ============================================================================
# PART 4: Combining Filter and Measure
# ============================================================================
# Filter first, then measure
# Pattern: Filter → Measure
# ============================================================================

# How many OPEN projects?
$openCount = ($data | Where-Object {$_.Status -eq "Open"} | Measure-Object).Count
Write-Host "`nOpen projects: $openCount"

# Sum of TotalActions for ONLY open projects
$openActionsSum = ($data | Where-Object {$_.Status -eq "Open"} | Measure-Object -Property TotalActions -Sum).Sum
Write-Host "Total actions in open projects: $openActionsSum"

# Average TotalActions for open projects
$openAverage = ($data | Where-Object {$_.Status -eq "Open"} | Measure-Object -Property TotalActions -Average).Average
Write-Host "Average actions per open project: $([Math]::Round($openAverage, 2))"


# ============================================================================
# PART 5: Group-Object - Categorizing Data
# ============================================================================
# Group-Object groups records by a property value
# Like making categories: "Show me all Open, all Closed, etc."
#
# SYNTAX: $collection | Group-Object -Property PropertyName
#
# RESULT: Returns groups with:
# - Name: The category value
# - Count: How many in this category
# - Group: The actual records
# ============================================================================

# Group by Status
Write-Host "`n=== Projects Grouped by Status ==="
$statusGroups = $data | Group-Object -Property Status

foreach ($group in $statusGroups) {
    Write-Host "$($group.Name): $($group.Count) projects"
}


# ============================================================================
# PART 6: Displaying Group Details
# ============================================================================
# Access the actual records in each group using .Group
# ============================================================================

# Group by Status and show details
$statusGroups = $data | Group-Object -Property Status

foreach ($group in $statusGroups) {
    Write-Host "`n=== $($group.Name) Projects ($($group.Count) total) ==="
    $group.Group | Select-Object -First 3 | Format-Table Project, Location, TotalActions -AutoSize
}


# ============================================================================
# PART 7: Sorting Groups
# ============================================================================
# Sort groups by count (most common to least common)
# ============================================================================

Write-Host "`n=== Status Summary (Sorted by Count) ==="
$data | 
    Group-Object -Property Status | 
    Sort-Object Count -Descending | 
    Select-Object Name, Count | 
    Format-Table -AutoSize


# ============================================================================
# PART 8: Group by Multiple Properties
# ============================================================================
# You can group by more than one column
# ============================================================================

# Group by both Status AND Type
Write-Host "`n=== Projects by Status and Type ==="
$data | 
    Group-Object -Property Status, Type | 
    Sort-Object Count -Descending | 
    Select-Object -First 10 Name, Count | 
    Format-Table -AutoSize


# ============================================================================
# PART 9: Practical Example - Project Summary
# ============================================================================
# Combine everything for a real summary
# ============================================================================

Write-Host "`n============================================"
Write-Host "CONSTRUCTION PROJECT SUMMARY"
Write-Host "============================================"

# Total records
$totalCount = ($data | Measure-Object).Count
Write-Host "`nTotal Projects: $totalCount"

# Count by status
$openCount = ($data | Where-Object {$_.Status -eq "Open"} | Measure-Object).Count
$closedCount = ($data | Where-Object {$_.Status -eq "Closed"} | Measure-Object).Count

Write-Host "`nStatus Breakdown:"
Write-Host "  Open: $openCount"
Write-Host "  Closed: $closedCount"

# Total actions
$totalActions = ($data | Measure-Object -Property TotalActions -Sum).Sum
$totalOverdue = ($data | Measure-Object -Property OverDue -Sum).Sum

Write-Host "`nAction Summary:"
Write-Host "  Total Actions: $totalActions"
Write-Host "  Total Overdue: $totalOverdue"

# Projects with overdue items
$projectsWithOverdue = ($data | Where-Object {$_.OverDue -gt 0} | Measure-Object).Count
Write-Host "`nProjects with Overdue Items: $projectsWithOverdue"

Write-Host "`n============================================"


################################################################################
# PRACTICE EXERCISES - Copy to practice.ps1 and complete
################################################################################
#
# Exercise 1: Basic Counting
# - Import the CSV
# - Count total records
# - Count how many have Status = "Open"
# - Count how many have Status = "Closed"
# - Display all three counts with labels
#
# Exercise 2: Summing Values
# - Calculate the sum of ALL TotalActions
# - Calculate the sum of ALL OverDue items
# - Calculate the sum of ALL OpenActions
# - Display with labels
#
# Exercise 3: Statistics for Open Projects
# - Filter to ONLY open projects
# - Calculate sum, average, max, min of TotalActions for open projects
# - Display all four statistics
#
# Exercise 4: Grouping Practice
# - Group the data by Status
# - Display each status name and its count
# - Sort by count (highest to lowest)
#
# Exercise 5: Build a Summary Report
# - Create a report that shows:
#   - Total project count
#   - Count of each status (using Group-Object)
#   - Sum of all TotalActions
#   - Sum of all OverDue
#   - How many projects have at least 1 overdue item
# - Format it nicely with Write-Host and colors
#
################################################################################

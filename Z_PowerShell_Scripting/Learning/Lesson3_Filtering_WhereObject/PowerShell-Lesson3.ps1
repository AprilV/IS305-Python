################################################################################
# Lesson 3: Filtering Data with Where-Object
# LEARN: Where-Object, Comparison Operators, If Statements
################################################################################

# ============================================================================
# WHAT WE'RE BUILDING: Construction Project Report
# ============================================================================
# Now that we can import data, we need to FILTER it
# Example: Show me only "Open" projects, or only items with overdue tasks
# ============================================================================


# ============================================================================
# PART 1: Comparison Operators
# ============================================================================
# PowerShell uses special operators for comparisons (NOT the same as math!)
#
# OPERATOR    MEANING                 EXAMPLE
# -eq         equals                  $status -eq "Open"
# -ne         not equals              $status -ne "Closed"
# -gt         greater than            $count -gt 10
# -lt         less than               $count -lt 5
# -ge         greater than or equal   $count -ge 10
# -le         less than or equal      $count -le 5
#
# IMPORTANT: Use -eq NOT ==  (PowerShell is different from Python/C)
# ============================================================================

# Simple comparison examples
$age = 25

if ($age -gt 21) {
    Write-Host "Over 21"
}

if ($age -eq 25) {
    Write-Host "Exactly 25"
}


# ============================================================================
# PART 2: If Statements
# ============================================================================
# If statements let you make decisions in code
#
# SYNTAX:
# if (condition) {
#     # code runs if condition is true
# }
#
# SYNTAX with else:
# if (condition) {
#     # code if true
# } else {
#     # code if false
# }
#
# SYNTAX with elseif:
# if (condition1) {
#     # code if condition1 true
# } elseif (condition2) {
#     # code if condition2 true
# } else {
#     # code if all false
# }
# ============================================================================

$score = 85

if ($score -ge 90) {
    Write-Host "Grade: A"
} elseif ($score -ge 80) {
    Write-Host "Grade: B"
} elseif ($score -ge 70) {
    Write-Host "Grade: C"
} else {
    Write-Host "Grade: F"
}


# ============================================================================
# PART 3: Logical Operators - Combining Conditions
# ============================================================================
# You can combine multiple conditions:
#
# OPERATOR    MEANING              EXAMPLE
# -and        both must be true    ($age -gt 18) -and ($age -lt 65)
# -or         either can be true   ($status -eq "Open") -or ($status -eq "Pending")
# -not        opposite/negation    -not ($completed)
#
# IMPORTANT: Use parentheses to group conditions clearly
# ============================================================================

$age = 25
$hasLicense = $true

if (($age -ge 16) -and ($hasLicense -eq $true)) {
    Write-Host "Can drive"
}

$status = "Open"
if (($status -eq "Open") -or ($status -eq "Pending")) {
    Write-Host "Still in progress"
}


# ============================================================================
# PART 4: Where-Object - Filtering Collections
# ============================================================================
# Where-Object filters a collection based on a condition
# It keeps only items that match the condition
#
# SYNTAX: $collection | Where-Object {condition}
#
# Inside the {}, use $_ to refer to the current item
# $_ means "this item right now"
#
# EXAMPLES:
# $data | Where-Object {$_.Status -eq "Open"}
# $data | Where-Object {$_.OverDue -gt 0}
# ============================================================================

# Import our data first
$data = Import-Csv "C:\ReactGitEC2\IS305 Scripting\Z_PowerShell_Scripting\Data\Construction_Data_PM_Forms_All_Projects.csv"

# Filter: Only "Open" status
Write-Host "`nOpen projects:"
$openProjects = $data | Where-Object {$_.Status -eq "Open"}
Write-Host "Found $($openProjects.Count) open projects"
$openProjects | Select-Object -First 5 | Format-Table Status, Project, Location -AutoSize


# Filter: Only items with overdue tasks
Write-Host "`nProjects with overdue tasks:"
$overdueProjects = $data | Where-Object {$_.OverDue -gt 0}
Write-Host "Found $($overdueProjects.Count) projects with overdue tasks"
$overdueProjects | Select-Object -First 5 | Format-Table Project, TotalActions, OverDue -AutoSize


# Filter: Closed projects
Write-Host "`nClosed projects:"
$closedProjects = $data | Where-Object {$_.Status -eq "Closed"}
Write-Host "Found $($closedProjects.Count) closed projects"


# ============================================================================
# PART 5: Multiple Conditions with Where-Object
# ============================================================================
# You can combine conditions in Where-Object using -and, -or
# ============================================================================

# Filter: Open projects with more than 10 total actions
Write-Host "`nOpen projects with many actions:"
$busyProjects = $data | Where-Object {($_.Status -eq "Open") -and ($_.TotalActions -gt 10)}
Write-Host "Found $($busyProjects.Count) busy open projects"
$busyProjects | Select-Object -First 5 | Format-Table Status, Project, TotalActions -AutoSize


# Filter: Either Closed OR has zero overdue
Write-Host "`nProjects that are closed or have no overdue items:"
$goodProjects = $data | Where-Object {($_.Status -eq "Closed") -or ($_.OverDue -eq 0)}
Write-Host "Found $($goodProjects.Count) projects"


# ============================================================================
# PART 6: Chaining Filters and Selections
# ============================================================================
# You can chain Where-Object with other commands using |
# ============================================================================

# Get open projects, pick specific columns, show first 10
$data | 
    Where-Object {$_.Status -eq "Open"} | 
    Select-Object Project, Location, TotalActions, OverDue | 
    Select-Object -First 10 | 
    Format-Table -AutoSize


# ============================================================================
# PART 7: Counting Filtered Results
# ============================================================================
# Common pattern: Filter then count
# ============================================================================

# How many open projects?
$openCount = ($data | Where-Object {$_.Status -eq "Open"}).Count
Write-Host "`nOpen projects: $openCount"

# How many closed projects?
$closedCount = ($data | Where-Object {$_.Status -eq "Closed"}).Count
Write-Host "Closed projects: $closedCount"

# How many with overdue items?
$overdueCount = ($data | Where-Object {$_.OverDue -gt 0}).Count
Write-Host "Projects with overdue tasks: $overdueCount"


################################################################################
# PRACTICE EXERCISES - Copy to practice.ps1 and complete
################################################################################
#
# Exercise 1: Basic Filtering
# - Import the CSV data
# - Filter to show only records where Status = "Open"
# - Display the count
# - Show the first 10 records as a table
#
# Exercise 2: Numeric Filtering
# - Filter records where TotalActions is greater than 50
# - Count how many there are
# - Display them with Status, Project, and TotalActions columns
#
# Exercise 3: Multiple Conditions (AND)
# - Find records where:
#   - Status is "Open" AND
#   - OverDue is greater than 0
# - Count them
# - Display first 15 as a table
#
# Exercise 4: Multiple Conditions (OR)
# - Find records where:
#   - Status is "Closed" OR
#   - Status is "Cancelled"
# - Count how many total
# - Show first 10
#
# Exercise 5: Complex Filter
# - Find records where:
#   - Status is "Open" AND
#   - TotalActions is greater than 10 AND
#   - OverDue is greater than 0
# - These are "busy projects with overdue items"
# - Count them
# - Display them sorted (you learned Select-Object in Lesson 2)
#
################################################################################

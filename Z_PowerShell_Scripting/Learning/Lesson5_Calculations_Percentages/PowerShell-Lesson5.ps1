################################################################################
# Lesson 5: Calculations and Percentages
# LEARN: Math Operations, Rounding, Percentage Calculations, Formatting
################################################################################

# ============================================================================
# WHAT WE'RE BUILDING: Construction Project Report
# ============================================================================
# Now we need to calculate completion rates and percentages:
# - What % of projects are closed?
# - What % of actions are complete?
# - Completion rate for each project
# ============================================================================


# ============================================================================
# PART 1: Basic Math Review
# ============================================================================
# Math operators:
#   +   addition
#   -   subtraction
#   *   multiplication
#   /   division
#   %   modulus (remainder)
# ============================================================================

$total = 100
$completed = 75

# Calculate percentage: (part / whole) * 100
$percentage = ($completed / $total) * 100
Write-Host "Completion: $percentage%"


# ============================================================================
# PART 2: Rounding Numbers
# ============================================================================
# [Math]::Round() rounds decimal numbers
#
# SYNTAX: [Math]::Round(number, decimalPlaces)
#
# Examples:
# [Math]::Round(3.14159, 2) → 3.14
# [Math]::Round(75.666, 1) → 75.7
# [Math]::Round(99.4) → 99  (defaults to 0 decimal places)
# ============================================================================

$value = 3.14159
$rounded = [Math]::Round($value, 2)
Write-Host "`nOriginal: $value"
Write-Host "Rounded to 2 decimals: $rounded"

# Percentage with rounding
$percentage = ($completed / $total) * 100
$roundedPercentage = [Math]::Round($percentage, 1)
Write-Host "`nCompletion rate: $roundedPercentage%"


# ============================================================================
# PART 3: Other Math Functions
# ============================================================================
# [Math]::Ceiling() - Round UP to nearest whole number
# [Math]::Floor() - Round DOWN to nearest whole number
# [Math]::Abs() - Absolute value (remove negative sign)
# ============================================================================

$value = 3.2

Write-Host "`nMath Functions Demo:"
Write-Host "Original: $value"
Write-Host "Ceiling (round up): $([Math]::Ceiling($value))"    # → 4
Write-Host "Floor (round down): $([Math]::Floor($value))"      # → 3
Write-Host "Round: $([Math]::Round($value))"                   # → 3

$negative = -42
Write-Host "`nAbsolute value of $negative = $([Math]::Abs($negative))"


# ============================================================================
# PART 4: Calculating Completion Percentages
# ============================================================================
# Formula: (CompletedItems / TotalItems) * 100
# ============================================================================

# Import our data
$data = Import-Csv "C:\ReactGitEC2\IS305 Scripting\Z_PowerShell_Scripting\Data\Construction_Data_PM_Forms_All_Projects.csv"

# Total projects
$totalProjects = ($data | Measure-Object).Count

# Closed projects
$closedProjects = ($data | Where-Object {$_.Status -eq "Closed"} | Measure-Object).Count

# Calculate percentage
$closedPercentage = ($closedProjects / $totalProjects) * 100
$closedPercentage = [Math]::Round($closedPercentage, 2)

Write-Host "`nProject Status:"
Write-Host "Total Projects: $totalProjects"
Write-Host "Closed Projects: $closedProjects"
Write-Host "Closed Rate: $closedPercentage%"


# ============================================================================
# PART 5: Calculating Open vs Closed Rates
# ============================================================================

$openProjects = ($data | Where-Object {$_.Status -eq "Open"} | Measure-Object).Count
$openPercentage = [Math]::Round(($openProjects / $totalProjects) * 100, 2)

Write-Host "`nStatus Breakdown:"
Write-Host "  Open: $openProjects ($openPercentage%)"
Write-Host "  Closed: $closedProjects ($closedPercentage%)"


# ============================================================================
# PART 6: Action Completion Rates
# ============================================================================
# For each record: CompletedActions = TotalActions - OpenActions
# Overall completion: Sum all completed / Sum all total
# ============================================================================

# Calculate total actions and open actions across ALL projects
$totalActions = ($data | Measure-Object -Property TotalActions -Sum).Sum
$openActions = ($data | Measure-Object -Property OpenActions -Sum).Sum

# Completed = Total - Open
$completedActions = $totalActions - $openActions

# Completion rate
$actionCompletionRate = ($completedActions / $totalActions) * 100
$actionCompletionRate = [Math]::Round($actionCompletionRate, 2)

Write-Host "`nAction Completion:"
Write-Host "Total Actions: $totalActions"
Write-Host "Open Actions: $openActions"
Write-Host "Completed Actions: $completedActions"
Write-Host "Completion Rate: $actionCompletionRate%"


# ============================================================================
# PART 7: Overdue Analysis
# ============================================================================

$totalOverdue = ($data | Measure-Object -Property OverDue -Sum).Sum
$projectsWithOverdue = ($data | Where-Object {$_.OverDue -gt 0} | Measure-Object).Count

# What % of projects have overdue items?
$overdueProjectPercentage = ($projectsWithOverdue / $totalProjects) * 100
$overdueProjectPercentage = [Math]::Round($overdueProjectPercentage, 2)

Write-Host "`nOverdue Analysis:"
Write-Host "Total Overdue Items: $totalOverdue"
Write-Host "Projects with Overdue: $projectsWithOverdue ($overdueProjectPercentage%)"


# ============================================================================
# PART 8: String Formatting with -f
# ============================================================================
# The -f operator formats strings with placeholders
# Useful for aligning numbers and controlling decimal places
#
# SYNTAX: "text {0} more text {1}" -f value1, value2
# ============================================================================

$name = "April"
$score = 95.5

# Basic formatting
$message = "Hello {0}, your score is {1}" -f $name, $score
Write-Host "`n$message"

# Number formatting with decimal control
$percentage = 75.66666
$formatted = "Completion: {0:N2}%" -f $percentage  # N2 = 2 decimal places
Write-Host $formatted


# ============================================================================
# PART 9: Complete Summary Report with Calculations
# ============================================================================

Write-Host "`n============================================"
Write-Host "CONSTRUCTION PROJECT ANALYSIS"
Write-Host "============================================"

# Project counts
$totalProjects = ($data | Measure-Object).Count
$openProjects = ($data | Where-Object {$_.Status -eq "Open"} | Measure-Object).Count
$closedProjects = ($data | Where-Object {$_.Status -eq "Closed"} | Measure-Object).Count

Write-Host "`nPROJECT STATUS:"
Write-Host "  Total Projects: $totalProjects"
Write-Host "  Open: $openProjects ({0:N2}%)" -f (($openProjects / $totalProjects) * 100)
Write-Host "  Closed: $closedProjects ({0:N2}%)" -f (($closedProjects / $totalProjects) * 100)

# Action metrics
$totalActions = ($data | Measure-Object -Property TotalActions -Sum).Sum
$openActions = ($data | Measure-Object -Property OpenActions -Sum).Sum
$completedActions = $totalActions - $openActions

Write-Host "`nACTION METRICS:"
Write-Host "  Total Actions: $totalActions"
Write-Host "  Completed: $completedActions ({0:N2}%)" -f (($completedActions / $totalActions) * 100)
Write-Host "  Open: $openActions ({0:N2}%)" -f (($openActions / $totalActions) * 100)

# Overdue analysis
$totalOverdue = ($data | Measure-Object -Property OverDue -Sum).Sum
$projectsWithOverdue = ($data | Where-Object {$_.OverDue -gt 0} | Measure-Object).Count

Write-Host "`nOVERDUE ANALYSIS:"
Write-Host "  Total Overdue Items: $totalOverdue"
Write-Host "  Projects Affected: $projectsWithOverdue ({0:N2}%)" -f (($projectsWithOverdue / $totalProjects) * 100)

Write-Host "`n============================================"


################################################################################
# PRACTICE EXERCISES - Copy to practice.ps1 and complete
################################################################################
#
# Exercise 1: Basic Percentage
# - Create variables: $total = 200, $completed = 150
# - Calculate percentage complete
# - Round to 2 decimal places
# - Display: "Completion rate: X.XX%"
#
# Exercise 2: Project Status Percentages
# - Import the CSV
# - Count total, open, and closed projects
# - Calculate percentage for each
# - Display all with labels, rounded to 1 decimal
#
# Exercise 3: Action Completion
# - Calculate total actions (sum of TotalActions)
# - Calculate open actions (sum of OpenActions)
# - Calculate completed actions (total - open)
# - Calculate completion percentage
# - Display all values
#
# Exercise 4: Overdue Rate
# - Count how many projects have OverDue > 0
# - Calculate what percentage of ALL projects this represents
# - Display: "X out of Y projects (Z.Z%) have overdue items"
#
# Exercise 5: Complete Summary
# - Build a formatted summary report showing:
#   - Total projects
#   - Open/Closed counts and percentages
#   - Total/Completed/Open action counts and percentages
#   - Overdue analysis
# - Use -f formatting for clean decimal display
# - Add colors with -ForegroundColor for headers
#
################################################################################

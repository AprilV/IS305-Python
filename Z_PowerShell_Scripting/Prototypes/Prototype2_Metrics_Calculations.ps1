# Import the construction data
$data = Import-Csv "C:\ReactGitEC2\IS305 Scripting\Z_PowerShell_Scripting\Data\Construction_Data_PM_Forms_All_Projects.csv"

# Count total records
$totalCount = $data.Count

# Filter by Status (from Prototype 1)
$openProjects = $data | Where-Object {$_.Status -eq "Open"}
$closedProjects = $data | Where-Object {$_.Status -eq "Closed"}

# Display basic counts from Prototype 1
Write-Host "`n============================================"
Write-Host "CONSTRUCTION PROJECT STATUS - BASIC REPORT"
Write-Host "============================================"
Write-Host "`nTotal Projects: $totalCount"
Write-Host "Open Projects: $($openProjects.Count)"
Write-Host "Closed Projects: $($closedProjects.Count)"

# NEW: Group by Status and display breakdown
Write-Host "`n============================================"
Write-Host "ADVANCED METRICS & ANALYSIS"
Write-Host "============================================"

Write-Host "`nSTATUS BREAKDOWN (All Status Types):"
Write-Host "----------------------------------------"
$statusGroups = $data | Group-Object -Property Status
$statusGroups | Format-Table Name, Count -AutoSize

# Calculate sums using Measure-Object
$totalActions = ($data | Measure-Object -Property "Total Actions" -Sum).Sum
$openActions = ($data | Measure-Object -Property "Open Actions" -Sum).Sum

# Count overdue items (OverDue is TRUE/FALSE text, not numeric)
$overdueCount = ($data | Where-Object {$_.OverDue -eq "TRUE"}).Count

# Calculate completion percentage
$completedActions = $totalActions - $openActions
$completionRate = ($completedActions / $totalActions) * 100
$roundedRate = [Math]::Round($completionRate, 2)

# Display metrics summary
Write-Host "`nADVANCED METRICS:"
Write-Host "----------------------------------------"
Write-Host "Total Projects: $totalCount"
Write-Host "Total Actions: $totalActions"
Write-Host "Open Actions: $openActions"
Write-Host "Completed Actions: $completedActions"
Write-Host "Overdue Items: $overdueCount"
Write-Host "`nCompletion Rate: $roundedRate%"

# Statistical analysis on Total Actions
$stats = $data | Measure-Object -Property "Total Actions" -Average -Maximum -Minimum
Write-Host "`nSTATISTICAL ANALYSIS (Total Actions):"
Write-Host "----------------------------------------"
Write-Host "Average: $([Math]::Round($stats.Average, 2))"
Write-Host "Maximum: $($stats.Maximum)"
Write-Host "Minimum: $($stats.Minimum)"



# Import the construction data
$data = Import-Csv "C:\ReactGitEC2\IS305 Scripting\Z_PowerShell_Scripting\Data\Construction_Data_PM_Forms_All_Projects.csv"

# Count total records
$totalCount = $data.Count

# Filter by Status
$openProjects = $data | Where-Object {$_.Status -eq "Open"}
$closedProjects = $data | Where-Object {$_.Status -eq "Closed"}

# Count each status
$openCount = $openProjects.Count
$closedCount = $closedProjects.Count

# Display Report
Write-Host "`n============================================"
Write-Host "CONSTRUCTION PROJECT STATUS - BASIC REPORT"
Write-Host "============================================"
Write-Host "`nTotal Projects: $totalCount"
Write-Host "Open Projects: $openCount"
Write-Host "Closed Projects: $closedCount"

################################################################################
# My Practice - Lesson 5: Calculations and Percentages
################################################################################

# Q1: Import the CSV file into variable $myData
# WHAT IT DOES: Import-Csv reads CSV files and creates PowerShell objects from each row
# ┌─ EXAMPLE ─────────────
# │ $data = Import-Csv "C:\path\to\file.csv"
# └───────────────────────

$myData = Import-Csv "C:\ReactGitEC2\IS305 Scripting\Z_PowerShell_Scripting\Data\Construction_Data_PM_Forms_All_Projects.csv"



# Q2: Calculate (75 / 100) * 100, store in variable $percentage, use Write-Host to display "$percentage%"
# WHAT IT DOES: Percentage formula converts a fraction to a percentage
# ┌─ EXAMPLE ─────────────
# │ $percentage = (50 / 200) * 100
# │ Write-Host "$percentage%"
# └───────────────────────

$percentage = (75 / 100) * 100
Write-Host "$percentage%"



# Q3: Use [Math]::Round() to round 3.14159 to 2 decimal places, store in variable $rounded, use Write-Host to display $rounded
# WHAT IT DOES: [Math]::Round() rounds numbers to specified decimal places
# ┌─ EXAMPLE ─────────────
# │ $rounded = [Math]::Round(5.6789, 2)
# │ Write-Host $rounded
# └───────────────────────

$rounded = [Math]::Round(3.14159, 2)
Write-Host $rounded



# Q4: Use [Math]::Ceiling() to round 7.2 UP, store in variable $roundedUp, use Write-Host to display $roundedUp
# WHAT IT DOES: [Math]::Ceiling() always rounds UP (7.1 becomes 8)
# ┌─ EXAMPLE ─────────────
# │ $roundedUp = [Math]::Ceiling(4.1)
# │ Write-Host $roundedUp
# └───────────────────────

$roundedUp = [Math]::Ceiling(7.2)
Write-Host $roundedUp



# Q5: Use [Math]::Floor() to round 7.9 DOWN, store in variable $roundedDown
# WHAT IT DOES: [Math]::Floor() always rounds DOWN (7.9 becomes 7)
# ┌─ EXAMPLE ─────────────
# │ $roundedDown = [Math]::Floor(8.7)
# └───────────────────────

$roundedDown = [Math]::Floor(7.9)
Write-Host $roundedDown



# Q6: Count total records in $myData, store in $total. Filter $myData where Status -eq "Closed", count them, store in $closedCount. Calculate ($closedCount / $total) * 100, store in $pct
# WHAT IT DOES: Combining filtering and percentage calculation with real data
# ┌─ EXAMPLE ─────────────
# │ $total = 100
# │ $completed = 60
# │ $pct = ($completed / $total) * 100
# └───────────────────────

$total = $myData.Count
$closedCount = ($myData | Where-Object {$_.Status -eq "Closed"}).Count
$pct = ($closedCount / $total) * 100
Write-Host "Closed percentage: $pct%"



# Q7: Use [Math]::Round() to round $pct to 1 decimal place, store in variable $roundedPct
# WHAT IT DOES: Making percentages more readable by limiting decimal places
# ┌─ EXAMPLE ─────────────
# │ $rounded = [Math]::Round($percentage, 1)
# └───────────────────────

$roundedPct = [Math]::Round($pct, 1)
Write-Host "Rounded closed percentage: $roundedPct%"



# Q8: Create variable $totalActions = 20, variable $openActions = 5. Calculate ($totalActions - $openActions) / $totalActions * 100, store in variable $rate
# WHAT IT DOES: Real-world completion percentage calculation for project tracking
# ┌─ EXAMPLE ─────────────
# │ $completed = 15
# │ $total = 20
# │ $rate = ($completed / $total) * 100
# └───────────────────────

$totalActions = 20
$openActions = 5
$rate = (($totalActions - $openActions) / $totalActions) * 100
Write-Host "Completion rate: $rate%"
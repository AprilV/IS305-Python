################################################################################
# My Practice - Lesson 4: Counting and Grouping Data
################################################################################

# Q1: Import the CSV file into variable $myData
# WHAT IT DOES: Import-Csv reads CSV files and creates PowerShell objects from each row
# ┌─ EXAMPLE ─────────────
# │ $data = Import-Csv "C:\path\to\file.csv"
# └───────────────────────

$myData = Import-Csv "C:\ReactGitEC2\IS305 Scripting\Z_PowerShell_Scripting\Data\Construction_Data_PM_Forms_All_Projects.csv"



# Q2: Pipe $myData to Measure-Object, get the .Count property, store in variable $count, use Write-Host to display "Total records: $count"
# WHAT IT DOES: Measure-Object calculates statistics like Count, Sum, Average, Maximum, Minimum
# ┌─ EXAMPLE ─────────────
# │ $count = ($employees | Measure-Object).Count
# │ Write-Host "Total: $count"
# └───────────────────────

$count = ($myData | Measure-Object).Count
Write-Host "Total records: $count"



# Q3: Pipe $myData to Measure-Object with -Property TotalActions and -Sum parameters, get the .Sum property, store in variable $sum, use Write-Host to display "Total Actions: $sum"
# WHAT IT DOES: The -Sum parameter adds up all values in a property
# ┌─ EXAMPLE ─────────────
# │ $sum = ($sales | Measure-Object -Property Revenue -Sum).Sum
# │ Write-Host "Total: $sum"
# └───────────────────────

$sum = ($myData | Measure-Object -Property TotalActions -Sum).Sum
Write-Host "Total Actions: $sum"



# Q4: Pipe $myData to Measure-Object with -Property OverDue and -Sum parameters, get the .Sum property, store in variable $overDueSum, use Write-Host to display "Total OverDue: $overDueSum"
# WHAT IT DOES: Same as Q3 but for a different property
# ┌─ EXAMPLE ─────────────
# │ $totalHours = ($tasks | Measure-Object -Property Hours -Sum).Sum
# └───────────────────────

$overDueSum = ($myData | Measure-Object -Property OverDue -Sum).Sum
Write-Host "Total OverDue: $overDueSum"




# Q5: Use Measure-Object with $myData, -Property TotalActions, and -Average -Maximum -Minimum parameters. Store result in $stats variable. Display the Average.
# WHAT IT DOES: You can use multiple statistics at once with Measure-Object
# ┌─ EXAMPLE ─────────────
# │ $stats = $students | Measure-Object -Property Grade -Average -Maximum -Minimum
# │ Write-Host "Average: $($stats.Average)"
# └───────────────────────

$stats = $myData | Measure-Object -Property TotalActions -Average -Maximum -Minimum
Write-Host "Average: $($stats.Average)"
Write-Host "Maximum: $($stats.Maximum)"
Write-Host "Minimum: $($stats.Minimum)"



# Q6: Pipe $myData to Where-Object to filter Status -eq "Open", then pipe to Measure-Object, get the .Count property, store in variable $openCount
# WHAT IT DOES: Combining Where-Object and Measure-Object to count filtered results
# ┌─ EXAMPLE ─────────────
# │ $count = ($orders | Where-Object {$_.ShipStatus -eq "Pending"} | Measure-Object).Count
# └───────────────────────

$openCount = ($myData | Where-Object {$_.Status -eq "Open"} | Measure-Object).Count
Write-Host "Open projects: $openCount"



# Q7: Pipe $myData to Group-Object with -Property Status, store result in variable $grouped
# WHAT IT DOES: Group-Object organizes data into categories based on a property value
# ┌─ EXAMPLE ─────────────
# │ $grouped = $products | Group-Object -Property Department
# └───────────────────────

$grouped = $myData | Group-Object -Property Status



# Q8: Pipe $grouped to Format-Table with Name and Count properties
# WHAT IT DOES: Each group has Name and Count properties you can display
# ┌─ EXAMPLE ─────────────
# │ $grouped | Format-Table Name, Count
# └───────────────────────

$grouped | Format-Table Name, Count
################################################################################
# My Practice - Lesson 3: Filtering Data with Where-Object
################################################################################
$myData = Import-Csv "C:\ReactGitEC2\IS305 Scripting\Z_PowerShell_Scripting\Data\Construction_Data_PM_Forms_All_Projects.csv"
# Q1: Create variable $age = 30, use if statement to check if over 21
#
# Example:
# $score = 85
# if ($score -gt 80) {
#     Write-Host "Good score"
# }
$age = 30
if ($age -gt 21) {
    Write-Host "Over 21"
}



# Q2: Use -eq operator to check if $age equals 30
#
# Example:
# if ($name -eq "John") {
#     Write-Host "Hello John"
# }
if ($age -eq 30) {
    Write-Host "Your age is 30"
}
  



# Q3: Create if-elseif-else for grade scoring (A, B, C, F)
# Use variable $score = 75
#
# Example:
# if ($temp -gt 90) {
#     Write-Host "Hot"
# } elseif ($temp -gt 70) {
#     Write-Host "Warm"
# } else {
#     Write-Host "Cold"
# }
$score = 75
if ($score -gt 93) {
    Write-Host "A"
} elseif ($score -gt 85) {
    Write-Host "B"
} elseif ($score -gt 75) {
    Write-Host "C"
} elseif ($score -gt 65) {
    Write-Host "D"
} else {
    Write-Host "F"
}



# Q4: Filter $data to show only records where Status equals "Open"
#
# Example:
# $filtered = $myData | Where-Object {$_.Category -eq "Active"}
$filtered = $myData | Where-Object {$_.Status -eq "Open"}
$filtered | Format-Table



# Q5: Filter records where TotalActions is greater than 10
#
# Example:
# $filtered = $myData | Where-Object {$_.Count -gt 5}

$filtered = $myData | Where-Object {$_.TotalActions -gt 10}
$filtered | Format-Table

# Q6: Use -and to filter where Status is "Open" AND TotalActions greater than 5
#
# Example:
# $filtered = $myData | Where-Object {($_.Status -eq "Active") -and ($_.Count -gt 3)}
$filtered = $myData | Where-Object {($_.Status -eq "Open") -and ($_.TotalActions -gt 5)}
$filtered | Format-Table


# Q7: Use -or to filter where Status is "Open" OR "Pending"
#
# Example:
# $filtered = $myData | Where-Object {($_.Type -eq "A") -or ($_.Type -eq "B")}
 $filtered = $myData | Where-Object {($_.Status -eq "Open") -or ($_.Status -eq "Pending")}
 $filtered | Format-Table
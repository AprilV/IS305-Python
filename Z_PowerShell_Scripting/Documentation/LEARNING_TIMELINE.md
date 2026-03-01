# PowerShell Project Learning Timeline
**Student:** April SYKES  
**Project:** Construction Project Status Report Generator  
**Approach:** 10-15 lines of code per day, 4-week build  
**Total Estimated Code:** ~125 lines  
**Start Date:** January 30, 2026

---

## Overview

**Learning Philosophy:**
- Small daily code chunks (10-15 lines)
- Understand each piece before moving on
- Run and test after every addition
- Build incrementally, not all at once

**Total Timeline:** 4 weeks (Weeks 4-7 of class)
- Week 4: Import & Filter CSV data
- Week 5: Calculate metrics
- Week 6: Generate HTML report
- Week 7: Send email

---

## Week 4: CSV Data Import & Filtering
**Focus:** Learn to work with CSV data in PowerShell  
**Estimated Code:** ~30 lines total

### Day 1 (Jan 30) - Import CSV (5-10 lines)
```powershell
# Import the CSV file
$data = Import-Csv -Path ".\Data\Construction_Data_PM_Forms_All_Projects.csv"

# See how many records
Write-Host "Total records: $($data.Count)"

# Show first 5 records
$data | Select-Object -First 5
```

**What you learn:**
- Import-Csv command
- Variables ($data)
- Counting with .Count
- Pipe symbol |
- Select-Object

---

### Day 2 (Jan 31) - Basic Filtering (10 lines)
```powershell
# Filter to just "Open" status
$openItems = $data | Where-Object { $_.Status -eq "Open" }
Write-Host "Open items: $($openItems.Count)"

# Filter to overdue items
$overdueItems = $data | Where-Object { $_.OverDue -eq "Yes" }
Write-Host "Overdue items: $($overdueItems.Count)"

# Show first 3 overdue
$overdueItems | Select-Object -First 3 | Format-Table
```

**What you learn:**
- Where-Object for filtering
- $_ (current item)
- -eq comparison
- Format-Table for display

---

### Day 3 (Feb 1) - Multiple Filters (10 lines)
```powershell
# Filter by multiple conditions (Open AND Overdue)
$openOverdue = $data | Where-Object { 
    $_.Status -eq "Open" -and $_.OverDue -eq "Yes" 
}

Write-Host "Open AND Overdue: $($openOverdue.Count)"

# Filter by project name
$projectData = $data | Where-Object { $_.Project -like "*School*" }
Write-Host "School projects: $($projectData.Count)"
```

**What you learn:**
- -and operator
- -like for partial matching
- Combining filters

---

### Day 4 (Feb 2) - Sorting (10 lines)
```powershell
# Sort by Status
$sortedByStatus = $data | Sort-Object -Property Status

# Sort by multiple fields
$sortedMulti = $data | Sort-Object -Property Status, Project

# Sort descending
$sortedDesc = $data | Sort-Object -Property "Open Actions" -Descending

# Show top 10 with most open actions
$sortedDesc | Select-Object -First 10 | Format-Table Project, "Open Actions"
```

**What you learn:**
- Sort-Object
- Multiple sort fields
- -Descending option

---

## Week 5: Calculate Metrics
**Focus:** Count, sum, and calculate statistics  
**Estimated Code:** ~35 lines total

### Day 5 (Feb 3) - Count and Group (12 lines)
```powershell
# Count items by status
$statusGroups = $data | Group-Object -Property Status

# Show the groups
foreach ($group in $statusGroups) {
    Write-Host "$($group.Name): $($group.Count) items"
}

# Count by project
$projectGroups = $data | Group-Object -Property Project | 
    Sort-Object -Property Count -Descending

$projectGroups | Select-Object -First 5
```

**What you learn:**
- Group-Object
- Foreach loops
- .Name and .Count properties

---

### Day 6 (Feb 4) - Sum and Measure (12 lines)
```powershell
# Sum all open actions
$totalOpenActions = ($data | Measure-Object -Property "Open Actions" -Sum).Sum
Write-Host "Total Open Actions: $totalOpenActions"

# Sum all total actions
$totalActions = ($data | Measure-Object -Property "Total Actions" -Sum).Sum
Write-Host "Total Actions: $totalActions"

# Calculate completion percentage
$completionRate = (($totalActions - $totalOpenActions) / $totalActions) * 100
Write-Host "Completion Rate: $([math]::Round($completionRate, 2))%"
```

**What you learn:**
- Measure-Object
- -Sum parameter
- Math calculations
- Rounding numbers

---

### Day 7 (Feb 5) - Create Function (12 lines)
```powershell
function Get-ProjectMetrics {
    param($ProjectData)
    
    $totalForms = $ProjectData.Count
    $overdue = ($ProjectData | Where-Object {$_.OverDue -eq "Yes"}).Count
    $openActions = ($ProjectData | Measure-Object -Property "Open Actions" -Sum).Sum
    
    return @{
        TotalForms = $totalForms
        OverdueCount = $overdue
        OpenActions = $openActions
    }
}

$metrics = Get-ProjectMetrics -ProjectData $data
$metrics
```

**What you learn:**
- Creating functions
- Parameters
- Hashtables (@{})
- Return values

---

## Week 6: HTML Report Generation
**Focus:** Create formatted HTML output  
**Estimated Code:** ~30 lines total

### Day 8 (Feb 6) - Basic HTML (10 lines)
```powershell
# Convert to simple HTML table
$htmlTable = $data | Select-Object -First 10 | 
    ConvertTo-Html -Property Status, Project, Location

# Save to file
$htmlTable | Out-File -FilePath ".\Reports\simple_report.html"

Write-Host "Report saved to Reports\simple_report.html"
```

**What you learn:**
- ConvertTo-Html
- Out-File
- Selecting properties

---

### Day 9 (Feb 7) - Add CSS Styling (15 lines)
```powershell
# Create CSS styling
$css = @"
<style>
    body { font-family: Arial; }
    table { border-collapse: collapse; width: 100%; }
    th { background-color: #4CAF50; color: white; padding: 10px; }
    td { border: 1px solid #ddd; padding: 8px; }
    tr:nth-child(even) { background-color: #f2f2f2; }
</style>
"@

# Build full HTML
$fullHtml = $css + ($data | Select-Object -First 20 | ConvertTo-Html)
$fullHtml | Out-File -FilePath ".\Reports\styled_report.html"
```

**What you learn:**
- Here-strings (@" "@)
- CSS basics
- Combining strings

---

### Day 10 (Feb 8) - Complete Report (15 lines)
```powershell
# Build complete report with sections
$header = "<h1>Project Status Report - $(Get-Date -Format 'MM/dd/yyyy')</h1>"
$summary = "<h2>Summary</h2><p>Total Forms: $($data.Count)</p>"

$statusTable = $data | Group-Object Status | 
    Select-Object Name, Count | 
    ConvertTo-Html -Fragment

$overdueTable = $data | Where-Object {$_.OverDue -eq "Yes"} | 
    Select-Object Project, Location, Status | 
    ConvertTo-Html -Fragment -PreContent "<h2>Overdue Items</h2>"

$fullReport = $css + $header + $summary + $statusTable + $overdueTable
$fullReport | Out-File -FilePath ".\Reports\full_report.html"
```

**What you learn:**
- Get-Date formatting
- -Fragment parameter
- Building multi-section reports

---

## Week 7: Email Integration
**Focus:** Send email with report  
**Estimated Code:** ~30 lines total

### Day 11 (Feb 9) - Email Setup (10 lines)
```powershell
# Create credentials (secure)
$username = "your-email@gmail.com"
$password = ConvertTo-SecureString "your-app-password" -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential($username, $password)

# Test email parameters
$emailParams = @{
    From = $username
    To = "recipient@example.com"
    Subject = "Test Email"
    SmtpServer = "smtp.gmail.com"
    Port = 587
    UseSsl = $true
    Credential = $cred
}
```

**What you learn:**
- SecureString
- PSCredential
- Email parameters
- Hashtable for parameters

---

### Day 12 (Feb 10) - Send Report (10 lines)
```powershell
# Send email with HTML report
Send-MailMessage @emailParams `
    -Body $fullReport `
    -BodyAsHtml

Write-Host "✅ Report sent successfully to $($emailParams.To)"
```

**What you learn:**
- Send-MailMessage
- Splatting (@emailParams)
- -BodyAsHtml parameter

---

### Day 13 (Feb 11) - Complete Script (10 lines)
```powershell
# Add parameters to script
param(
    [string]$CsvPath = ".\Data\Construction_Data_PM_Forms_All_Projects.csv",
    [string]$EmailTo = "manager@example.com",
    [switch]$SendEmail
)

# Main execution
$data = Import-Csv -Path $CsvPath
$metrics = Get-ProjectMetrics -ProjectData $data
$report = New-HtmlReport -Metrics $metrics

if ($SendEmail) {
    Send-ProjectReport -HtmlContent $report -To $EmailTo
}
```

**What you learn:**
- Script parameters
- Switch parameters
- Conditional execution

---

## Total Code Summary

**Week 4:** ~30 lines (Import, filter, sort)  
**Week 5:** ~35 lines (Count, calculate, functions)  
**Week 6:** ~30 lines (HTML generation)  
**Week 7:** ~30 lines (Email integration)  

**TOTAL:** ~125 lines of PowerShell code

---

## Daily Workflow

**Each Session (30-45 minutes):**
1. Read today's code example
2. Type it yourself (don't copy-paste)
3. Run it and see what happens
4. Change one thing and run again
5. Make sure you understand before moving on

**If Stuck:**
- Read the comments
- Check PowerShell help: `Get-Help CommandName -Examples`
- Google the error message
- Ask for help

**Progress Tracking:**
- Check off each day when complete
- Save all scripts with dates
- Take screenshots of working output
- Note questions/problems for later

---

## Notes

- This is ESTIMATED - some days might be faster/slower
- Feel free to spend extra time on hard concepts
- The goal is UNDERSTANDING, not just finishing
- Each piece builds on the previous one
- By Week 7, you'll have a complete automation tool

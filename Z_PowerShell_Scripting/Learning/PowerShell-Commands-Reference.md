# PowerShell Commands Reference
**Quick reference for building the Construction Project Status Report**

---

## Basic Commands

### Import-Csv
**What it does:** Reads a CSV file and converts each row into an object
```powershell
$data = Import-Csv "path\to\file.csv"
```

### Write-Host
**What it does:** Displays text/output to the screen
```powershell
Write-Host "Hello World"
Write-Host "Total: $count" -ForegroundColor Green
```

---

## Working with Data

### Where-Object
**What it does:** Filters data based on conditions
```powershell
# Get only Open projects
$data | Where-Object {$_.Status -eq "Open"}

# Get projects with overdue items
$data | Where-Object {$_.OverDue -gt 0}
```

**Comparison operators:**
- `-eq` equals
- `-ne` not equals
- `-gt` greater than
- `-lt` less than
- `-ge` greater than or equal
- `-le` less than or equal

### Select-Object
**What it does:** Chooses specific columns or number of rows
```powershell
# Get first 10 rows
$data | Select-Object -First 10

# Get specific columns
$data | Select-Object Status, Project, Location
```

### Sort-Object
**What it does:** Sorts data
```powershell
# Sort by Status
$data | Sort-Object Status

# Sort by multiple columns
$data | Sort-Object Status, Project

# Sort descending
$data | Sort-Object OverDue -Descending
```

---

## Calculations

### Measure-Object
**What it does:** Counts, sums, averages data
```powershell
# Count records
$data | Measure-Object

# Sum a column
$data | Measure-Object -Property TotalActions -Sum

# Average
$data | Measure-Object -Property TotalActions -Average

# Min/Max
$data | Measure-Object -Property OverDue -Maximum -Minimum
```

### Group-Object
**What it does:** Groups data by a category
```powershell
# Group by Status
$data | Group-Object Status

# Group and count
$statusGroups = $data | Group-Object Status
foreach ($group in $statusGroups) {
    Write-Host "$($group.Name): $($group.Count)"
}
```

---

## Variables

### Creating Variables
```powershell
$name = "April"
$count = 100
$percentage = 75.5
$isComplete = $true
```

### Using Variables in Strings
```powershell
Write-Host "Total: $count"
Write-Host "Rate: $($percentage)%"  # Use $() for expressions
```

---

## HTML Report Generation

### ConvertTo-Html
**What it does:** Converts data to HTML table
```powershell
# Basic HTML table
$data | ConvertTo-Html

# With specific properties
$data | Select-Object Status, Project | ConvertTo-Html

# Save to file
$data | ConvertTo-Html | Out-File "report.html"

# With custom styling
$html = $data | ConvertTo-Html -Head $style -Body "<h1>Report</h1>"
```

---

## Email

### Send-MailMessage
**What it does:** Sends email
```powershell
Send-MailMessage `
    -From "sender@email.com" `
    -To "recipient@email.com" `
    -Subject "Project Report" `
    -Body "See attached report" `
    -Attachments "report.html" `
    -SmtpServer "smtp.gmail.com" `
    -Port 587 `
    -UseSsl
```

---

## File Operations

### Out-File
**What it does:** Saves output to a file
```powershell
$html | Out-File "C:\Reports\report.html"
```

### Get-Date
**What it does:** Gets current date/time
```powershell
$today = Get-Date
$formatted = Get-Date -Format "yyyy-MM-dd"
Write-Host "Report generated: $formatted"
```

---

## Piping (|)

**What it does:** Passes output from one command to the next
```powershell
# Chain multiple commands
$data | Where-Object {$_.Status -eq "Open"} | 
        Sort-Object OverDue -Descending | 
        Select-Object -First 10
```

---

## Loops

### ForEach
```powershell
foreach ($item in $collection) {
    Write-Host $item
}
```

### ForEach-Object (in pipeline)
```powershell
$data | ForEach-Object {
    Write-Host $_.Project
}
```

---

## If Statements

```powershell
if ($count -gt 100) {
    Write-Host "Large dataset"
} elseif ($count -gt 50) {
    Write-Host "Medium dataset"
} else {
    Write-Host "Small dataset"
}
```

---

## Math Operations

```powershell
# Basic math
$total = 100
$completed = 75
$percentage = ($completed / $total) * 100

# Rounding
$rounded = [Math]::Round($percentage, 2)
```

---

## Common Patterns for This Project

### Count by Status
```powershell
$statusGroups = $data | Group-Object Status
foreach ($group in $statusGroups) {
    Write-Host "$($group.Name): $($group.Count) projects"
}
```

### Calculate Completion Rate
```powershell
$totalProjects = ($data | Measure-Object).Count
$closedProjects = ($data | Where-Object {$_.Status -eq "Closed"} | Measure-Object).Count
$completionRate = ($closedProjects / $totalProjects) * 100
Write-Host "Completion Rate: $([Math]::Round($completionRate, 2))%"
```

### Find Overdue Items
```powershell
$overdue = $data | Where-Object {$_.OverDue -gt 0}
$overdueCount = ($overdue | Measure-Object).Count
Write-Host "Projects with overdue items: $overdueCount"
```

---

## Tips

1. **Use Tab completion** - Type part of a command and press Tab
2. **Get help** - Type `Get-Help CommandName` for info
3. **Properties** - Access with `$object.PropertyName` or `$_.PropertyName` in pipeline
4. **Count** - Use `.Count` on any collection: `$data.Count`
5. **Backtick (`)** - Line continuation character for long commands
6. **Case insensitive** - PowerShell doesn't care about capitalization

---

## Week-by-Week Learning Plan

**Week 1:** Import-Csv, Write-Host, Select-Object, basic variables
**Week 2:** Where-Object, Sort-Object, comparisons, if statements
**Week 3:** Measure-Object, Group-Object, calculations, math
**Week 4:** ConvertTo-Html, Out-File, Send-MailMessage, styling

---

*Use this as a quick reference while learning and coding!*

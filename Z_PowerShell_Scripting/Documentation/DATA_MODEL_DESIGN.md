# Data Model Design - Project Status Report Generator

**Student:** April SYKES  
**Project:** PowerShell Project Status Report Generator  
**Data Source:** Construction Project Management Tasks (Real-World Data)  
**Date:** January 19, 2026

---

## 📊 Data Source Overview

**Dataset:** Construction/Project Management Report Examples  
**File:** `Construction_Data_PM_Tasks_All_Projects.csv`  
**URL:** https://www.kaggle.com/datasets/claytonmiller/construction-and-project-management-example-data  
**Size:** ~2.2 MB  
**Origin:** Real construction project data from Ireland  
**License:** CC BY-NC-SA 4.0 (Educational use approved)

---

## 🎯 Data Model Purpose

This CSV file will serve as the **primary data source** for your PowerShell script. The script will:
1. Import CSV data using `Import-Csv` cmdlet
2. Process and analyze task information
3. Calculate project metrics
4. Generate HTML reports
5. Send email notifications

---

## 📋 Expected CSV Structure

Based on construction project management tracking systems, the CSV likely contains:

### **Core Task Fields:**
```
TaskID            - Unique identifier for each task/action item
ProjectName       - Which construction project the task belongs to
TaskDescription   - What needs to be done
Status            - Current state (e.g., Open, In Progress, Completed, Closed)
Priority          - Importance level (High, Medium, Low, Critical)
Category          - Type (Quality, Safety, Site Management, Defect)
AssignedTo        - Person responsible for the task
CreatedDate       - When the task was created
DueDate           - When the task should be completed
CompletedDate     - When the task was actually completed (if applicable)
Location          - Site location or area
Notes             - Additional information
```

### **Additional Possible Fields:**
- Severity
- Estimated Hours
- Actual Hours
- Cost Impact
- Resolution Notes
- Last Updated
- Created By

---

## 🔧 PowerShell Data Model

### **Object Structure in PowerShell**

When imported via `Import-Csv`, each row becomes a PowerShell custom object:

```powershell
# Example of one task object after Import-Csv
$task = @{
    TaskID = "12345"
    ProjectName = "Building A Construction"
    TaskDescription = "Fix safety railing on 3rd floor"
    Status = "In Progress"
    Priority = "High"
    Category = "Safety"
    AssignedTo = "John Smith"
    CreatedDate = "01/05/2026"
    DueDate = "01/20/2026"
    CompletedDate = ""
    Location = "Floor 3, North Wing"
}
```

### **Data Types for Processing**

```powershell
# PowerShell will treat imported CSV data as:
TaskID          : String
ProjectName     : String
TaskDescription : String
Status          : String (will filter/group on this)
Priority        : String (will filter/group on this)
Category        : String
AssignedTo      : String
CreatedDate     : String → Convert to [DateTime] for calculations
DueDate         : String → Convert to [DateTime] for calculations
CompletedDate   : String → Convert to [DateTime] for calculations
Location        : String
```

---

## 📐 Metrics to Calculate

Based on the data model, your PowerShell script will calculate:

### **1. Status Metrics**
```powershell
# Count tasks by status
$totalTasks = ($tasks).Count
$openTasks = ($tasks | Where-Object {$_.Status -eq "Open"}).Count
$inProgressTasks = ($tasks | Where-Object {$_.Status -eq "In Progress"}).Count
$completedTasks = ($tasks | Where-Object {$_.Status -eq "Completed"}).Count
$completionRate = ($completedTasks / $totalTasks) * 100
```

### **2. Overdue Tasks**
```powershell
# Find tasks past due date
$today = Get-Date
$overdueTasks = $tasks | Where-Object {
    $_.Status -ne "Completed" -and 
    ([DateTime]$_.DueDate) -lt $today
}
$overdueCount = $overdueTasks.Count
```

### **3. Priority Breakdown**
```powershell
# Group by priority
$highPriority = ($tasks | Where-Object {$_.Priority -eq "High"}).Count
$mediumPriority = ($tasks | Where-Object {$_.Priority -eq "Medium"}).Count
$lowPriority = ($tasks | Where-Object {$_.Priority -eq "Low"}).Count
```

### **4. Category Analysis**
```powershell
# Group by category
$tasks | Group-Object -Property Category | Select-Object Name, Count
```

### **5. Time-Based Metrics**
```powershell
# Average days to completion
$completedWithDates = $tasks | Where-Object {
    $_.Status -eq "Completed" -and 
    $_.CompletedDate -ne "" -and 
    $_.CreatedDate -ne ""
}

$averageDays = ($completedWithDates | ForEach-Object {
    ([DateTime]$_.CompletedDate - [DateTime]$_.CreatedDate).TotalDays
} | Measure-Object -Average).Average
```

### **6. Project Breakdown**
```powershell
# Tasks per project
$tasks | Group-Object -Property ProjectName | 
    Select-Object Name, Count | 
    Sort-Object Count -Descending
```

---

## 📊 Report Sections

Your HTML report will include:

### **1. Executive Summary**
- Total tasks
- Completion percentage
- Overdue tasks count
- High priority open tasks

### **2. Status Distribution**
- Pie chart or table showing Open/In Progress/Completed/Closed

### **3. Priority Matrix**
- High/Medium/Low breakdown
- Highlight critical items

### **4. Overdue Tasks Table**
- Task ID
- Description
- Assigned To
- Due Date
- Days Overdue

### **5. Category Breakdown**
- Quality issues
- Safety issues
- Site management tasks

### **6. Project Summary**
- Per-project metrics
- Completion rates by project

---

## 🔄 Data Processing Workflow

```powershell
# Week 4: Import & Basic Filtering
$csvPath = ".\Data\Construction_Data_PM_Tasks_All_Projects.csv"
$tasks = Import-Csv -Path $csvPath

# Filter example
$openTasks = $tasks | Where-Object {$_.Status -eq "Open"}

# Week 5: Calculations & Metrics
function Get-OverdueTasks {
    param($TaskList)
    $today = Get-Date
    return $TaskList | Where-Object {
        $_.Status -ne "Completed" -and 
        ([DateTime]$_.DueDate) -lt $today
    }
}

# Week 6: HTML Generation
$htmlReport = $metrics | ConvertTo-Html -Property Name, Value

# Week 7: Email
Send-MailMessage -To "recipient@email.com" -Body $htmlReport
```

---

## 🎨 Data Visualization Plan

### **In HTML Report:**

**Status Chart:**
```html
<table>
  <tr><th>Status</th><th>Count</th><th>Percentage</th></tr>
  <tr><td>Open</td><td>45</td><td>30%</td></tr>
  <tr><td>In Progress</td><td>35</td><td>23%</td></tr>
  <tr><td>Completed</td><td>70</td><td>47%</td></tr>
</table>
```

**Priority Distribution:**
- Use CSS color coding: Red (High), Yellow (Medium), Green (Low)

**Overdue Tasks:**
- Highlight in red
- Sort by days overdue (most urgent first)

---

## ✅ Data Quality Considerations

### **Expected Issues & Solutions:**

**1. Missing Dates:**
```powershell
# Handle null/empty dates
if ($task.DueDate -eq "" -or $null -eq $task.DueDate) {
    Write-Warning "Task $($task.TaskID) has no due date"
    continue
}
```

**2. Date Format Variations:**
```powershell
# Flexible date parsing
try {
    $dueDate = [DateTime]::Parse($task.DueDate)
} catch {
    Write-Warning "Invalid date format for task $($task.TaskID)"
}
```

**3. Inconsistent Status Values:**
```powershell
# Standardize status names
$status = $task.Status.Trim().ToLower()
switch ($status) {
    "open" { $standardStatus = "Open" }
    "in progress" { $standardStatus = "In Progress" }
    "completed" { $standardStatus = "Completed" }
    default { $standardStatus = "Unknown" }
}
```

---

## 📝 Sample PowerShell Function Structure

```powershell
function Get-ProjectMetrics {
    param(
        [string]$CsvPath
    )
    
    # Import data
    $tasks = Import-Csv -Path $CsvPath
    
    # Calculate metrics
    $metrics = @{
        TotalTasks = $tasks.Count
        OpenTasks = ($tasks | Where-Object {$_.Status -eq "Open"}).Count
        CompletedTasks = ($tasks | Where-Object {$_.Status -eq "Completed"}).Count
        OverdueTasks = (Get-OverdueTasks -TaskList $tasks).Count
        CompletionRate = [math]::Round((
            ($tasks | Where-Object {$_.Status -eq "Completed"}).Count / 
            $tasks.Count * 100
        ), 2)
    }
    
    return $metrics
}
```

---

## 🚀 Next Steps (Week by Week)

### **Week 3 (Jan 20-26): PowerShell Fundamentals**
- Learn variable syntax
- Practice with simple CSV files
- Understand data types

### **Week 4 (Jan 27-Feb 2): CSV Import**
- Download the real dataset
- Import with `Import-Csv`
- Explore data structure
- Practice filtering with `Where-Object`

### **Week 5 (Feb 3-9): Metrics Calculation**
- Convert date strings to DateTime objects
- Calculate overdue tasks
- Count tasks by status/priority
- Create metric functions

### **Week 6 (Feb 10-16): HTML Reports**
- Use `ConvertTo-Html` cmdlet
- Add CSS styling
- Generate report sections
- Save to HTML file

### **Week 7 (Feb 17-23): Email Integration**
- Configure SMTP settings
- Use `Send-MailMessage`
- Attach HTML report
- Test email delivery

### **Week 8 (Feb 24-Mar 2): Integration & Testing**
- Combine all components
- Add error handling
- Test with full dataset
- Refine report formatting

---

## 📚 Reference: PowerShell Cmdlets You'll Use

```powershell
Import-Csv          # Read CSV file
Where-Object        # Filter data
Select-Object       # Choose specific properties
Group-Object        # Group by property
Sort-Object         # Sort data
Measure-Object      # Calculate statistics
ForEach-Object      # Loop through items
ConvertTo-Html      # Generate HTML
Send-MailMessage    # Send email
Get-Date            # Work with dates
```

---

## 🎓 Learning Resources

**PowerShell CSV Processing:**
- `Get-Help Import-Csv -Examples`
- `Get-Help Where-Object -Examples`
- `Get-Help ConvertTo-Html -Examples`

**Date Handling:**
- `Get-Help Get-Date -Examples`
- `[DateTime]` type conversion

**HTML Styling:**
- CSS basics for report formatting
- PowerShell HTML customization

---

**Status:** Ready for dataset download  
**Next Action:** Download CSV from Kaggle and save to Data folder  
**Last Updated:** January 19, 2026

# PowerShell Project Status Report Generator - Architecture & Flow

**Student:** April SYKES  
**Project:** Project Status Report Generator  
**Date:** January 19, 2026

---

## 📋 PROJECT OVERVIEW

**What It Does:**
Reads construction project data from a CSV file, analyzes it, calculates metrics, generates an HTML report, and emails it to stakeholders.

**Input:** Construction_Data_PM_Forms_All_Projects.csv (10,254 records)  
**Output:** HTML report + Email notification  
**Language:** PowerShell 5.1  
**Platform:** Windows

---

## 🔄 SYSTEM FLOW DIAGRAM

```
┌─────────────────────────────────────────────────────────────────┐
│                    START: User Runs Script                      │
│                    .\Generate-ProjectReport.ps1                 │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│  STEP 1: INPUT - Read CSV Data                                  │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │  Import-Csv -Path "Data\Construction_Data.csv"            │  │
│  │  → Loads 10,254 construction project records              │  │
│  │  → Each record becomes a PowerShell object                │  │
│  └───────────────────────────────────────────────────────────┘  │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│  STEP 2: FILTER - Select Relevant Data                          │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │  Where-Object to filter records:                          │  │
│  │  • Status = "Open" or "In Progress"                       │  │
│  │  • OverDue = "Yes" (for overdue tasks)                    │  │
│  │  • By Project name                                        │  │
│  └───────────────────────────────────────────────────────────┘  │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│  STEP 3: CALCULATE - Generate Metrics                           │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │  Function: Get-ProjectMetrics                             │  │
│  │  ┌─────────────────────────────────────────────────────┐  │  │
│  │  │ • Total Forms: Count all records                    │  │  │
│  │  │ • Open Actions: Sum of "Open Actions" field         │  │  │
│  │  │ • Total Actions: Sum of "Total Actions" field       │  │  │
│  │  │ • Completion Rate: (Total-Open)/Total * 100         │  │  │
│  │  │ • Overdue Count: Count where OverDue = "Yes"        │  │  │
│  │  │ • Status Breakdown: Group-Object by Status          │  │  │
│  │  │ • Project Breakdown: Group-Object by Project        │  │  │
│  │  │ • Type Distribution: Group-Object by Type           │  │  │
│  │  └─────────────────────────────────────────────────────┘  │  │
│  └───────────────────────────────────────────────────────────┘  │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│  STEP 4: FORMAT - Build HTML Report                             │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │  Function: New-HtmlReport                                 │  │
│  │  ┌─────────────────────────────────────────────────────┐  │  │
│  │  │ HTML Structure:                                     │  │  │
│  │  │                                                     │  │  │
│  │  │  <html>                                             │  │  │
│  │  │    <head>                                           │  │  │
│  │  │      <style> (CSS for formatting)                   │  │  │
│  │  │    </head>                                          │  │  │
│  │  │    <body>                                           │  │  │
│  │  │      <h1>Project Status Report</h1>                 │  │  │
│  │  │                                                     │  │  │
│  │  │      [SECTION 1: Executive Summary]                │  │  │
│  │  │      • Total Forms                                  │  │  │
│  │  │      • Completion Rate                              │  │  │
│  │  │      • Overdue Items                                │  │  │
│  │  │                                                     │  │  │
│  │  │      [SECTION 2: Status Breakdown Table]           │  │  │
│  │  │      ConvertTo-Html for status counts              │  │  │
│  │  │                                                     │  │  │
│  │  │      [SECTION 3: Overdue Items Table]              │  │  │
│  │  │      List of overdue forms with details            │  │  │
│  │  │                                                     │  │  │
│  │  │      [SECTION 4: Project Summary]                  │  │  │
│  │  │      Forms per project                             │  │  │
│  │  │                                                     │  │  │
│  │  │    </body>                                          │  │  │
│  │  │  </html>                                            │  │  │
│  │  └─────────────────────────────────────────────────────┘  │  │
│  └───────────────────────────────────────────────────────────┘  │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│  STEP 5: SAVE - Write Report to File                            │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │  Out-File -FilePath "Reports\ProjectReport_DATE.html"    │  │
│  │  → Saves HTML to Reports folder                          │  │
│  │  → Filename includes timestamp                           │  │
│  └───────────────────────────────────────────────────────────┘  │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│  STEP 6: EMAIL - Send Report                                    │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │  Send-MailMessage:                                        │  │
│  │  • From: your-email@gmail.com                            │  │
│  │  • To: recipient@email.com                               │  │
│  │  • Subject: "Project Status Report - [Date]"             │  │
│  │  • Body: HTML report content                             │  │
│  │  • SMTP: smtp.gmail.com (with app password)              │  │
│  └───────────────────────────────────────────────────────────┘  │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                    END: Report Sent Successfully                │
│                    Display confirmation message                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🏗️ PROJECT STRUCTURE

```
Z_PowerShell_Scripting/
│
├── Data/                                    ← Input folder
│   ├── Construction_Data_PM_Forms_All_Projects.csv   (10,254 records)
│   └── README.md
│
├── Scripts/                                 ← Code folder
│   ├── Generate-ProjectReport.ps1          (Main script - Week 8)
│   │
│   ├── modules/                             ← Helper functions
│   │   ├── Import-ProjectData.ps1          (Week 4)
│   │   ├── Get-ProjectMetrics.ps1          (Week 5)
│   │   ├── New-HtmlReport.ps1              (Week 6)
│   │   └── Send-ProjectEmail.ps1           (Week 7)
│   │
│   └── test/                                ← Practice scripts
│       └── Test-HelloWorld.ps1
│
├── Reports/                                 ← Output folder
│   ├── ProjectReport_2026-01-19.html       (Generated reports)
│   └── archive/                             (Old reports)
│
├── Documentation/                           ← Project docs
│   ├── PROJECT_ARCHITECTURE.md             (This file)
│   ├── DATA_MODEL_DESIGN.md
│   ├── DATA_SOURCES.md
│   └── Module2_Project_Proposal.md
│
└── PROJECT_PROGRESS.md                      ← Weekly tracking
```

---

## 🎯 DATA FLOW - DETAILED

### **INPUT DATA (CSV)**
```
CSV File Structure (10,254 rows):
┌──────┬────────┬──────────┬──────┬────────────┬──────┬────────┐
│ Ref  │ Status │ Location │ Name │  Created   │ Type │ OverDue│
├──────┼────────┼──────────┼──────┼────────────┼──────┼────────┤
│ 1234 │ Open   │ Floor 3  │ ...  │ 01/15/2026 │ QA   │  Yes   │
│ 1235 │ Closed │ Floor 1  │ ...  │ 01/10/2026 │ Safe │  No    │
│ 1236 │ Open   │ Floor 2  │ ...  │ 01/12/2026 │ Site │  No    │
└──────┴────────┴──────────┴──────┴────────────┴──────┴────────┘

Additional Columns:
- Open Actions (number)
- Total Actions (number)
- Project (name)
- Images, Comments, Documents (counts)
```

### **PROCESSING PIPELINE**

```
CSV Data → PowerShell Objects → Filtered Data → Calculated Metrics → HTML → Email

Example transformation:

RAW CSV ROW:
"1234,Open,Floor 3,Safety Check,01/15/2026,Safety,Yes,5,10,Building A,No,2,3,1"

↓ Import-Csv

POWERSHELL OBJECT:
$form = @{
    Ref = "1234"
    Status = "Open"
    Location = "Floor 3"
    Name = "Safety Check"
    Created = "01/15/2026"
    Type = "Safety"
    OverDue = "Yes"
    OpenActions = "5"
    TotalActions = "10"
    Project = "Building A"
}

↓ Filtering (Where-Object)

FILTERED OBJECT (if Status = "Open"):
Keep this record for analysis

↓ Metrics Calculation

METRICS OBJECT:
$metrics = @{
    TotalForms = 10254
    OpenForms = 3421
    ClosedForms = 6833
    OverdueForms = 892
    CompletionRate = 66.6%
    TotalOpenActions = 15432
}

↓ HTML Generation

HTML TABLE:
<table>
  <tr><th>Metric</th><th>Value</th></tr>
  <tr><td>Total Forms</td><td>10,254</td></tr>
  <tr><td>Completion Rate</td><td>66.6%</td></tr>
  <tr><td style="color:red">Overdue</td><td>892</td></tr>
</table>

↓ Email

EMAIL BODY:
From: yourscript@automation.com
To: manager@construction.com
Subject: Project Status Report - January 19, 2026
Body: [HTML content above]
```

---

## 🔧 FUNCTION BREAKDOWN

### **Function 1: Import-ProjectData.ps1** (Week 4)
```
PURPOSE: Load and validate CSV data
INPUT:   CSV file path
OUTPUT:  Array of PowerShell objects
LOGIC:   
  1. Check if file exists (Test-Path)
  2. Import CSV (Import-Csv)
  3. Validate data (check required columns)
  4. Return data array
```

### **Function 2: Get-ProjectMetrics.ps1** (Week 5)
```
PURPOSE: Calculate all project metrics
INPUT:   Array of form objects
OUTPUT:  Hashtable of metrics
LOGIC:   
  1. Count total forms
  2. Group by Status (Open, Closed, etc.)
  3. Filter overdue items (OverDue = "Yes")
  4. Sum Open Actions and Total Actions
  5. Calculate completion percentage
  6. Group by Project
  7. Group by Type
  8. Return metrics hashtable
```

### **Function 3: New-HtmlReport.ps1** (Week 6)
```
PURPOSE: Generate formatted HTML report
INPUT:   Metrics hashtable + original data
OUTPUT:  HTML string
LOGIC:   
  1. Create HTML header with CSS
  2. Build executive summary section
  3. Convert status breakdown to HTML table
  4. Create overdue items table
  5. Add project breakdown chart/table
  6. Close HTML tags
  7. Return complete HTML string
```

### **Function 4: Send-ProjectEmail.ps1** (Week 7)
```
PURPOSE: Email the report
INPUT:   HTML content, recipient email
OUTPUT:  Success/failure message
LOGIC:   
  1. Set up SMTP parameters
  2. Create email message
  3. Attach HTML as body
  4. Send via Send-MailMessage
  5. Handle errors
  6. Return confirmation
```

### **Main Script: Generate-ProjectReport.ps1** (Week 8)
```
PURPOSE: Orchestrate entire workflow
INPUT:   Command-line parameters (optional)
OUTPUT:  Report file + email
LOGIC:   
  1. Set parameters (CSV path, email recipient)
  2. Call Import-ProjectData
  3. Call Get-ProjectMetrics
  4. Call New-HtmlReport
  5. Save HTML to file (Out-File)
  6. Call Send-ProjectEmail
  7. Display success message
```

---

## ⚙️ SCRIPT PARAMETERS

```powershell
# User can customize when running the script

.\Generate-ProjectReport.ps1 `
    -CsvPath ".\Data\Construction_Data.csv" `
    -EmailTo "manager@company.com" `
    -EmailFrom "reports@automation.com" `
    -SmtpServer "smtp.gmail.com" `
    -SmtpPort 587 `
    -SaveReport $true `
    -ReportPath ".\Reports\"
```

---

## 📊 METRICS CALCULATED

### **1. Overall Statistics**
- Total Forms Count
- Open Forms Count  
- Closed Forms Count
- In Progress Count
- Completion Rate (percentage)

### **2. Action Items**
- Total Open Actions (sum across all forms)
- Total Actions Overall
- Actions Completion Rate

### **3. Overdue Analysis**
- Count of Overdue Forms
- List of Overdue Items with Details
- Overdue Rate (percentage)

### **4. Status Breakdown**
- Group by Status field
- Count per status
- Percentage per status

### **5. Project Analysis**
- Forms per Project
- Completion rate per Project
- Overdue items per Project

### **6. Type Distribution**
- Forms by Type (Quality, Safety, Site)
- Completion rate by Type

### **7. Location Analysis**
- Forms by Location
- Hotspot identification

---

## 🎨 HTML REPORT LAYOUT

```
┌─────────────────────────────────────────────────────────────┐
│  PROJECT STATUS REPORT                                      │
│  Generated: January 19, 2026                                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  📊 EXECUTIVE SUMMARY                                       │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Total Forms:        10,254                         │   │
│  │  Open Forms:         3,421    (33.4%)               │   │
│  │  Closed Forms:       6,833    (66.6%)               │   │
│  │  Overdue:            892      (🔴 8.7%)             │   │
│  │  Open Actions:       15,432                         │   │
│  │  Total Actions:      45,678                         │   │
│  │  Completion Rate:    66.2%                          │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  📈 STATUS BREAKDOWN                                        │
│  ┌──────────────┬──────────┬────────────┐                  │
│  │ Status       │  Count   │ Percentage │                  │
│  ├──────────────┼──────────┼────────────┤                  │
│  │ Open         │  3,421   │   33.4%    │                  │
│  │ In Progress  │    892   │    8.7%    │                  │
│  │ Closed       │  6,833   │   66.6%    │                  │
│  │ Cancelled    │    108   │    1.1%    │                  │
│  └──────────────┴──────────┴────────────┘                  │
│                                                             │
│  🚨 OVERDUE ITEMS (892 Total)                              │
│  ┌──────┬──────────┬──────────────┬────────┬─────────┐    │
│  │ Ref  │ Project  │ Location     │ Type   │ Days    │    │
│  ├──────┼──────────┼──────────────┼────────┼─────────┤    │
│  │ 1234 │Build A   │ Floor 3      │ Safety │  45     │    │
│  │ 1567 │Build A   │ Floor 1      │ QA     │  32     │    │
│  │ 2890 │Build B   │ Basement     │ Site   │  18     │    │
│  └──────┴──────────┴──────────────┴────────┴─────────┘    │
│                                                             │
│  🏗️ PROJECT SUMMARY                                         │
│  ┌──────────────┬────────┬──────────┬──────────┐           │
│  │ Project      │ Total  │ Complete │ % Done   │           │
│  ├──────────────┼────────┼──────────┼──────────┤           │
│  │ Building A   │ 4,521  │  3,012   │  66.6%   │           │
│  │ Building B   │ 3,892  │  2,591   │  66.6%   │           │
│  │ Building C   │ 1,841  │  1,230   │  66.8%   │           │
│  └──────────────┴────────┴──────────┴──────────┘           │
│                                                             │
│  Report Generated by PowerShell Automation                  │
└─────────────────────────────────────────────────────────────┘
```

---

## 🗓️ WEEKLY DEVELOPMENT PLAN

### **Week 3 (Jan 20-26): PowerShell Basics**
- Learn variables, operators, conditionals
- Practice with simple scripts
- Understand data types

### **Week 4 (Jan 27-Feb 2): CSV Import**
- Create `Import-ProjectData.ps1`
- Test with your CSV file
- Practice filtering with `Where-Object`

### **Week 5 (Feb 3-9): Metrics**
- Create `Get-ProjectMetrics.ps1`
- Calculate all statistics
- Test with real data

### **Week 6 (Feb 10-16): HTML Reports**
- Create `New-HtmlReport.ps1`
- Add CSS styling
- Generate sample reports

### **Week 7 (Feb 17-23): Email**
- Create `Send-ProjectEmail.ps1`
- Set up Gmail app password
- Test email delivery

### **Week 8 (Feb 24-Mar 2): Integration**
- Create main `Generate-ProjectReport.ps1`
- Combine all modules
- Full end-to-end testing
- Error handling & refinement

---

## 🔐 SECURITY & CONFIGURATION

### **Email Setup (Week 7)**
```
SMTP Settings:
- Server: smtp.gmail.com
- Port: 587
- Use SSL: Yes
- Authentication: App Password (NOT regular password)
- Stored in: Secure credential file (not hardcoded)
```

### **File Permissions**
- CSV file: Read-only
- Reports folder: Write access
- Scripts folder: Read/Execute

---

## ✅ SUCCESS CRITERIA

**The project is complete when:**
1. ✅ Script reads 10,254 CSV records successfully
2. ✅ Calculates all metrics accurately
3. ✅ Generates formatted HTML report
4. ✅ Saves report to Reports folder
5. ✅ Sends email with report attached
6. ✅ Includes error handling
7. ✅ Can be run with parameters
8. ✅ Code is documented with comments

---

## 🎓 LEARNING OUTCOMES

**PowerShell Skills:**
- Import-Csv, Where-Object, Group-Object, Measure-Object
- Functions and parameters
- HTML generation with ConvertTo-Html
- Email automation with Send-MailMessage
- Error handling (try/catch)
- File I/O operations

**Project Management Skills:**
- Data modeling
- Work breakdown structure
- Weekly milestone tracking
- Documentation

**Presentation Skills:**
- Demo the working script
- Compare PowerShell vs Python
- Explain architecture and data flow

---

**Last Updated:** January 19, 2026  
**Status:** Architecture complete, ready for Week 3 development  
**Data Status:** CSV file ready (10,254 records)

# PowerShell Project - Code Component Design
**Project:** Construction Project Status Report Generator  
**Student:** April SYKES  
**Date:** January 30, 2026

---

## Purpose of This Document

This document outlines WHAT code components we will create, in WHAT ORDER, and HOW they relate to each other. This is the planning/design work done BEFORE writing code.

---

## Component Overview

**Total System:** 5 main components that work together

```
┌─────────────────────────────────────────────────────────────┐
│                    MAIN SCRIPT                              │
│              Generate-ProjectReport.ps1                     │
│                                                             │
│  Orchestrates all components and controls execution flow   │
└─────────────────────────────────────────────────────────────┘
                            │
                            │ calls ↓
        ┌───────────────────┴───────────────────┐
        │                                       │
        ▼                                       ▼
┌───────────────────┐                  ┌────────────────────┐
│   COMPONENT 1     │                  │   COMPONENT 2      │
│   Data Import     │                  │   Data Filter      │
│                   │─────────────────→│                    │
│ Read CSV file     │    passes data   │ Filter & Sort      │
└───────────────────┘                  └────────────────────┘
                                                │
                                                │ passes filtered data
                                                ▼
                                       ┌────────────────────┐
                                       │   COMPONENT 3      │
                                       │   Metrics Engine   │
                                       │                    │
                                       │ Calculate stats    │
                                       └────────────────────┘
                                                │
                                                │ passes metrics
                                                ▼
                                       ┌────────────────────┐
                                       │   COMPONENT 4      │
                                       │   HTML Generator   │
                                       │                    │
                                       │ Create report      │
                                       └────────────────────┘
                                                │
                                                │ passes HTML
                                                ▼
                                       ┌────────────────────┐
                                       │   COMPONENT 5      │
                                       │   Email Sender     │
                                       │                    │
                                       │ Send report        │
                                       └────────────────────┘
```

---

## Component Details (In Order of Creation)

### COMPONENT 1: Data Import Module
**File:** `Import-ConstructionData.ps1` (or as function in main script)  
**Purpose:** Read CSV file and load into memory  
**Created:** Week 4, Days 1-2

**What it does:**
1. Accepts CSV file path as input
2. Uses Import-Csv to read file
3. Validates file exists and has data
4. Returns PowerShell objects (array of records)

**Code Structure:**
```
Function: Import-ConstructionData
├─ Parameter: $CsvPath
├─ Validate file exists
├─ Import CSV
├─ Count records
└─ Return data
```

**Lines of code:** ~10 lines

**Input:** File path (string)  
**Output:** Array of PowerShell objects (10,254 records)

---

### COMPONENT 2: Data Filter Module
**File:** `Filter-ProjectData.ps1` (or as function)  
**Purpose:** Filter and sort data based on criteria  
**Created:** Week 4, Days 3-4

**What it does:**
1. Accepts data and filter criteria
2. Filters by Status (Open, Closed, In Progress)
3. Filters by OverDue (Yes/No)
4. Filters by Project name (optional)
5. Sorts results
6. Returns filtered dataset

**Code Structure:**
```
Function: Filter-ProjectData
├─ Parameters:
│  ├─ $Data (required)
│  ├─ $Status (optional)
│  ├─ $OverdueOnly (optional switch)
│  └─ $ProjectName (optional)
├─ Apply Where-Object filters
├─ Apply Sort-Object
└─ Return filtered data
```

**Lines of code:** ~15-20 lines

**Input:** Array of objects + filter parameters  
**Output:** Filtered/sorted array

---

### COMPONENT 3: Metrics Calculation Engine
**File:** `Get-ProjectMetrics.ps1` (or as function)  
**Purpose:** Calculate statistics and metrics from data  
**Created:** Week 5, Days 5-7

**What it does:**
1. Accepts filtered data
2. Counts total forms
3. Counts overdue items
4. Sums open actions
5. Sums total actions
6. Calculates completion rate
7. Groups by status
8. Groups by project
9. Returns hashtable of metrics

**Code Structure:**
```
Function: Get-ProjectMetrics
├─ Parameter: $ProjectData
├─ Calculate counts
│  ├─ Total forms (.Count)
│  ├─ Overdue count (Where-Object + Count)
│  └─ Status breakdown (Group-Object)
├─ Calculate sums
│  ├─ Total open actions (Measure-Object -Sum)
│  └─ Total actions (Measure-Object -Sum)
├─ Calculate percentages
│  └─ Completion rate (formula)
├─ Build result hashtable
└─ Return metrics
```

**Lines of code:** ~25-30 lines

**Input:** Array of filtered objects  
**Output:** Hashtable with metrics
```powershell
@{
    TotalForms = 1234
    OverdueCount = 56
    OpenActions = 789
    TotalActions = 2000
    CompletionRate = 60.5
    StatusBreakdown = @{Open=400; Closed=600; InProgress=234}
    ProjectBreakdown = @{...}
}
```

---

### COMPONENT 4: HTML Report Generator
**File:** `New-HtmlReport.ps1` (or as function)  
**Purpose:** Create formatted HTML report from metrics  
**Created:** Week 6, Days 8-10

**What it does:**
1. Accepts metrics hashtable
2. Creates HTML structure
3. Adds CSS styling
4. Builds report sections:
   - Header with date
   - Executive summary
   - Status breakdown table
   - Overdue items table
   - Project summary
5. Returns complete HTML string

**Code Structure:**
```
Function: New-HtmlReport
├─ Parameter: $Metrics
├─ Define CSS styles (here-string)
├─ Build header section
│  ├─ Title
│  └─ Date
├─ Build summary section
│  ├─ Total forms
│  ├─ Completion rate
│  └─ Overdue count
├─ Build status table
│  └─ ConvertTo-Html -Fragment
├─ Build overdue table
│  └─ ConvertTo-Html -Fragment
├─ Build project summary
│  └─ ConvertTo-Html -Fragment
├─ Combine all sections
└─ Return HTML string
```

**Lines of code:** ~40-45 lines

**Input:** Hashtable of metrics  
**Output:** HTML string (complete report)

---

### COMPONENT 5: Email Delivery Module
**File:** `Send-ProjectReport.ps1` (or as function)  
**Purpose:** Email the HTML report to recipients  
**Created:** Week 7, Days 11-12

**What it does:**
1. Accepts HTML content and recipient email
2. Creates secure credentials
3. Configures SMTP settings
4. Sends email with HTML body
5. Confirms delivery

**Code Structure:**
```
Function: Send-ProjectReport
├─ Parameters:
│  ├─ $HtmlContent
│  ├─ $To
│  ├─ $From
│  └─ $Credential (optional)
├─ Build email parameters hashtable
│  ├─ From/To addresses
│  ├─ Subject (with date)
│  ├─ SMTP server settings
│  └─ SSL/credentials
├─ Call Send-MailMessage
└─ Write confirmation
```

**Lines of code:** ~15-20 lines

**Input:** HTML string + email addresses  
**Output:** Sent email (success/failure message)

---

### MAIN ORCHESTRATION SCRIPT
**File:** `Generate-ProjectReport.ps1`  
**Purpose:** Tie all components together  
**Created:** Week 7, Day 13

**What it does:**
1. Defines script parameters
2. Calls Component 1 (import)
3. Calls Component 2 (filter)
4. Calls Component 3 (metrics)
5. Calls Component 4 (HTML)
6. Optionally calls Component 5 (email)
7. Saves HTML to file
8. Displays summary

**Code Structure:**
```
Main Script: Generate-ProjectReport.ps1
├─ Script parameters (param block)
│  ├─ $CsvPath
│  ├─ $Status
│  ├─ $EmailTo
│  └─ $SendEmail (switch)
├─ Step 1: Import data
│  └─ Call Import-ConstructionData
├─ Step 2: Filter data
│  └─ Call Filter-ProjectData
├─ Step 3: Calculate metrics
│  └─ Call Get-ProjectMetrics
├─ Step 4: Generate HTML
│  └─ Call New-HtmlReport
├─ Step 5: Save report to file
│  └─ Out-File
├─ Step 6: Optionally send email
│  └─ Call Send-ProjectReport (if -SendEmail)
└─ Display completion message
```

**Lines of code:** ~20-25 lines

**Input:** Command-line parameters  
**Output:** HTML file + optional email + console messages

---

## Data Flow Diagram

```
USER RUNS SCRIPT
      │
      ▼
[Parse Parameters]
      │
      ├─→ $CsvPath = "Data\Construction_Data.csv"
      ├─→ $Status = "Open"
      ├─→ $EmailTo = "manager@example.com"
      └─→ $SendEmail = $true
      │
      ▼
┌─────────────────────────────────────┐
│ COMPONENT 1: Import Data            │
│                                     │
│ Input: File path string             │
│ Process: Import-Csv                 │
│ Output: 10,254 PowerShell objects   │
└─────────────────────────────────────┘
      │
      │ [Raw Data Array]
      ▼
┌─────────────────────────────────────┐
│ COMPONENT 2: Filter Data            │
│                                     │
│ Input: 10,254 objects + filters     │
│ Process: Where-Object, Sort-Object  │
│ Output: ~500 filtered objects       │
└─────────────────────────────────────┘
      │
      │ [Filtered Data Array]
      ▼
┌─────────────────────────────────────┐
│ COMPONENT 3: Calculate Metrics      │
│                                     │
│ Input: 500 objects                  │
│ Process: Count, Sum, Calculate      │
│ Output: Hashtable with 8 metrics    │
└─────────────────────────────────────┘
      │
      │ [Metrics Hashtable]
      ▼
┌─────────────────────────────────────┐
│ COMPONENT 4: Generate HTML          │
│                                     │
│ Input: Metrics hashtable            │
│ Process: ConvertTo-Html, CSS        │
│ Output: HTML string (~500 lines)    │
└─────────────────────────────────────┘
      │
      ├─────────────────┬─────────────────┐
      │                 │                 │
      ▼                 ▼                 ▼
[Save to File]   [Display Preview]   [Send Email?]
      │                                   │
      │                                   ▼
      │                          ┌─────────────────────┐
      │                          │ COMPONENT 5: Email  │
      │                          │                     │
      │                          │ Input: HTML string  │
      │                          │ Process: SMTP send  │
      │                          │ Output: Email sent  │
      │                          └─────────────────────┘
      │                                   │
      ▼                                   ▼
┌──────────────────────────────────────────────┐
│         COMPLETION MESSAGE                   │
│ "✅ Report generated successfully!"          │
│ "📊 Saved to: Reports\report_01-30-2026.html"│
│ "📧 Emailed to: manager@example.com"         │
└──────────────────────────────────────────────┘
```

---

## Creation Order and Dependencies

### Week 4: Foundation
1. **Day 1-2:** Component 1 (Import) - NO dependencies
2. **Day 3-4:** Component 2 (Filter) - DEPENDS ON Component 1

### Week 5: Logic
3. **Day 5-7:** Component 3 (Metrics) - DEPENDS ON Component 2

### Week 6: Presentation
4. **Day 8-10:** Component 4 (HTML) - DEPENDS ON Component 3

### Week 7: Delivery
5. **Day 11-12:** Component 5 (Email) - DEPENDS ON Component 4
6. **Day 13:** Main Script - DEPENDS ON ALL components

**Why this order?**
- Each component builds on the previous one
- Can't calculate metrics without filtered data
- Can't generate HTML without metrics
- Can't send email without HTML
- Main script ties everything together at the end

---

## Testing Strategy

**Component 1 Testing:**
- Verify file loads
- Check record count (should be 10,254)
- Display first 5 records

**Component 2 Testing:**
- Filter by each status type
- Verify counts make sense
- Test sorting works

**Component 3 Testing:**
- Check all metrics calculate
- Verify math is correct
- Test with different data subsets

**Component 4 Testing:**
- Open HTML in browser
- Check formatting looks good
- Verify all sections appear

**Component 5 Testing:**
- Send test email to yourself
- Verify HTML displays correctly in email
- Check attachment if needed

**Integration Testing:**
- Run full script end-to-end
- Verify each step completes
- Check final output matches expectations

---

## File Structure (Final)

```
Z_PowerShell_Scripting/
├── Scripts/
│   ├── Generate-ProjectReport.ps1        (Main script - 25 lines)
│   └── modules/
│       ├── Import-ConstructionData.ps1   (Component 1 - 10 lines)
│       ├── Filter-ProjectData.ps1        (Component 2 - 20 lines)
│       ├── Get-ProjectMetrics.ps1        (Component 3 - 30 lines)
│       ├── New-HtmlReport.ps1            (Component 4 - 45 lines)
│       └── Send-ProjectReport.ps1        (Component 5 - 20 lines)
├── Data/
│   └── Construction_Data_PM_Forms_All_Projects.csv
├── Reports/
│   └── (generated HTML files saved here)
└── Documentation/
    └── (this file and others)
```

**Total Lines:** ~150 lines (with comments and spacing)  
**Functional Code:** ~125 lines

---

## Key Design Decisions

**1. Modular Functions vs. One Big Script**
- **Decision:** Use separate functions/modules
- **Why:** Easier to test, easier to understand, reusable components

**2. Hashtable for Metrics**
- **Decision:** Return hashtable from metrics function
- **Why:** Clean structure, named values, easy to pass to HTML generator

**3. Separate Email Component**
- **Decision:** Email is optional, controlled by switch parameter
- **Why:** Can generate reports without emailing (testing, manual review)

**4. HTML Fragment Approach**
- **Decision:** Use -Fragment with ConvertTo-Html
- **Why:** Allows custom CSS and multi-section reports

**5. File-Based Output First**
- **Decision:** Save HTML to file before (optionally) emailing
- **Why:** Allows review, debugging, and keeps local copy

---

## Next Steps

1. ✅ Create this design document
2. ✅ Create learning timeline
3. ⏳ Day 1: Write Component 1 code (Import CSV)
4. ⏳ Test Component 1
5. ⏳ Day 2: Add basic filtering
6. ⏳ Continue through timeline...

**Current Status:** Design phase complete, ready to code!

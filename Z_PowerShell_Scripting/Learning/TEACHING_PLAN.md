# PowerShell Learning Plan - IS305 Final Project
**AI Reference Document for Teaching Consistency**

---

## OFFICIAL SOURCES - VERIFICATION REQUIRED

**All lessons MUST be verified against official Microsoft PowerShell documentation.**

### Primary Documentation Source:
- **Microsoft Learn PowerShell Docs**: https://learn.microsoft.com/en-us/powershell/
- **PowerShell Module Reference**: https://learn.microsoft.com/en-us/powershell/module/

### Verification Process:
1. **Before teaching ANY lesson**, AI must verify cmdlet syntax against Microsoft docs
2. Reference SOURCES.md file in Z_PowerShell_Scripting/ folder
3. Each lesson file includes reference links in comments
4. Examples and syntax must match official documentation
5. Parameter names, types, and usage must be accurate

### Teaching Without a Textbook:
- **Python Course**: Has textbook (Automate the Boring Stuff with Python)
- **PowerShell Course**: No textbook - relies on official Microsoft documentation
- **Critical**: Lessons must teach PowerShell fundamentals BEYOND just the project needs
- **Goal**: Build solid foundation, not just project-specific skills

---

## PROJECT OVERVIEW

**Student:** April SYKES  
**Course:** IS305 Scripting  
**Instructor:** Dr. Lindsey Handley  
**Project:** Construction Project Status Report Generator  
**Weight:** 50% of final grade  
**Due:** Week 10 Presentation  
**GitHub:** https://github.com/AprilV/IS305-PowerShell-Project.git

**Data Source:**
- File: Construction_Data_PM_Forms_All_Projects.csv
- Records: 10,254 construction project records
- Columns: Status, Project, Location, Type, OpenActions, TotalActions, OverDue

**Project Requirements:**
1. Import and analyze 10,254 CSV records
2. Calculate metrics (completion rates, overdue counts, status breakdown)
3. Generate professional HTML report with styling
4. Save report to file
5. (Optional) Send email notification
6. (Optional) Create GUI for presentation

---

## TEACHING METHODOLOGY

**Core Principles:**
1. Follow the same format used for Python teaching (Q1, Q2, Q3 practice format)
2. One concept at a time - no rushing
3. Explain EVERY line of code
4. Explain WHY things are done certain ways (capitalization, syntax, operators)
5. Practice before moving on
6. Build incrementally toward the final project
7. **TEACH FUNDAMENTALS BEYOND PROJECT NEEDS** - solid foundation, not just "enough to get by"

**Fundamental Coverage - NOT Just Project-Specific:**
The lessons build on each other progressively, teaching core PowerShell concepts that apply broadly:
- **Lesson 1**: Core language syntax (variables, output, math) - universal skills
- **Lesson 2**: Data import/display - applies to ANY data file, not just our CSV
- **Lesson 3**: Filtering/conditionals - fundamental programming concepts
- **Lesson 4**: Aggregation/grouping - data analysis foundation
- **Lesson 5**: Math/calculations - general computation skills
- **Lesson 6**: Report generation - applies to ANY HTML output
- **Lesson 7**: File operations/automation - universal scripting skills

**Each lesson teaches transferable skills that work beyond this specific project.**

**File Structure:**
```
Learning/
├── Lesson1_WriteHost_Variables_Math/
│   ├── PowerShell-Lesson1.ps1  (reference - complete examples)
│   └── practice.ps1 (student workspace with Q1, Q2, Q3...)
├── Lesson2_Import_CSV_Display/
│   ├── PowerShell-Lesson2.ps1
│   └── practice.ps1
...
├── PowerShell-Commands-Reference.md (quick command lookup)
```

**Daily Process:**
1. AI reads LEARNING_PROCESS.md at start of each session
2. AI verifies lesson content against official Microsoft documentation
3. AI posts lesson content in chat (student has one screen)
4. Student practices in practice.ps1 file (Q1, Q2, Q3 format)
5. Verify output is correct
6. Move to next lesson only when current is mastered

**Lesson File Format (MANDATORY):**
- Clear section headers with separator lines
- Explanation blocks BEFORE code
- State rules (REQUIRED vs OPTIONAL)
- Examples with expected output
- Comments explaining EVERY line
- Microsoft documentation references
- Practice file has Q1, Q2, Q3 format with examples
- Follow Python teaching format exactly

---

## LESSON BREAKDOWN

### Lesson 1: The Absolute Basics
**Status:** COMPLETE  
**Location:** Learning/Lesson1/

**Topics:**
- Write-Host (displaying output)
- Variables ($name syntax)
- Basic math (+, -, *, /)
- Capitalization rules (not case-sensitive but use PascalCase)
- Data types (strings, integers, decimals)

**Key Explanations:**
- PowerShell NOT case-sensitive (unlike Python)
- Variables ALWAYS start with $
- Quotes required for strings
- Commands are Verb-Noun (Write-Host, Import-Csv)

**Practice Exercises:** 4 exercises (display info, age calculator, math, price calculator)

---

### Lesson 2: Import CSV and Display Data
**Status:** COMPLETE  
**Location:** Learning/Lesson2/

**Topics:**
- Import-Csv (reading CSV files)
- .Count property
- Accessing records by index [0], [-1]
- Accessing properties (.Status, .Project, etc.)
- Select-Object (-First, -Last, selecting columns)
- Format-Table (-AutoSize)
- Pipe operator |
- Get-Member (discovering properties)

**Key Explanations:**
- CSV rows become PowerShell objects
- Each column becomes a property
- Pipe passes output to next command
- Use full file paths

**Practice Exercises:** 5 exercises (import/count, explore records, select columns, find properties, custom display)

---

### Lesson 3: Filtering Data
**Status:** COMPLETE  
**Location:** Learning/Lesson3/

**Topics:**
- Comparison operators (-eq, -ne, -gt, -lt, -ge, -le)
- If statements (if, elseif, else)
- Logical operators (-and, -or, -not)
- Where-Object (filtering collections)
- $_ (current item in pipeline)
- Multiple conditions
- Chaining filters
- Counting filtered results

**Key Explanations:**
- Use -eq NOT == (PowerShell is different)
- $_ means "this item right now"
- Parentheses to group conditions
- Filter then count pattern

**Practice Exercises:** 5 exercises (basic filter, numeric filter, AND conditions, OR conditions, complex filter)

---

### Lesson 4: Counting and Grouping Data
**Status:** COMPLETE  
**Location:** Learning/Lesson4/

**Topics:**
- Measure-Object (Count, Sum, Average, Max, Min)
- -Property parameter
- Combining Filter and Measure
- Group-Object (categorizing data)
- .Name, .Count, .Group properties
- Sorting groups
- Grouping by multiple properties

**Key Explanations:**
- Measure gives you statistics
- Group creates categories
- Access group data with .Group
- Sort-Object to order results

**Practice Exercises:** 5 exercises (basic counting, summing values, statistics, grouping, summary report)

---

### Lesson 5: Calculations and Percentages
**Status:** COMPLETE  
**Location:** Learning/Lesson5/

**Topics:**
- Math operations review
- [Math]::Round() for rounding decimals
- [Math]::Ceiling(), Floor(), Abs()
- Percentage calculations: (part/whole) * 100
- Completion rate formulas
- String formatting with -f operator
- {0:N2} decimal control

**Key Explanations:**
- Always round percentages for readability
- Use [Math]:: for math functions
- -f operator for clean formatting
- Calculate metrics for the report

**Practice Exercises:** 5 exercises (basic percentage, status percentages, action completion, overdue rate, complete summary)

---

### Lesson 6: Creating HTML Reports
**Status:** COMPLETE  
**Location:** Learning/Lesson6/

**Topics:**
- ConvertTo-Html basics
- Selecting columns for HTML
- -Title and -Head parameters
- CSS styling (colors, fonts, borders)
- -PreContent and -PostContent
- Multi-section reports
- -Fragment for partial HTML
- Combining sections

**Key Explanations:**
- HTML displays data as webpage
- CSS controls appearance
- Fragment creates just table (no full page)
- Combine fragments into complete report

**Practice Exercises:** 5 exercises (basic table, styled report, multi-section, custom styling, complete report)

---

### Lesson 7: Saving Files and Sending Email
**Status:** COMPLETE  
**Location:** Learning/Lesson7/

**Topics:**
- Out-File (saving to files)
- File paths and directories
- Test-Path, New-Item (check/create folders)
- Get-Date (current date/time)
- Date formatting for filenames
- Send-MailMessage (email basics)
- -BodyAsHtml parameter
- Complete integration script

**Key Explanations:**
- Folder must exist before saving
- Use timestamps in filenames
- Email requires SMTP configuration
- Integration: Import → Analyze → Generate → Save

**Practice Exercises:** 5 exercises (save HTML, dynamic filenames, directory check, complete generation, final project script)

---

## COMMAND REFERENCE

**Essential Commands by Category:**

**Data Import/Export:**
- Import-Csv
- Out-File
- ConvertTo-Html

**Display/Output:**
- Write-Host
- Format-Table
- Select-Object

**Filtering/Analysis:**
- Where-Object
- Measure-Object
- Group-Object
- Sort-Object

**Utilities:**
- Get-Date
- Get-Member
- Test-Path
- New-Item

**Math:**
- [Math]::Round()
- [Math]::Ceiling()
- [Math]::Floor()

**Email (Optional):**
- Send-MailMessage

---

## PROGRESSION TIMELINE

**Week 4 (Current - Day 1):**
- Lesson 1: Basics (Write-Host, variables)
- Lesson 2: Import CSV, display data
- Start writing first 10-15 lines in ProjectTicketAnalyzer.ps1

**Week 5:**
- Lesson 3: Filtering (Where-Object)
- Lesson 4: Counting/Grouping (Measure-Object, Group-Object)
- Add filtering and metric calculation to project file

**Week 6:**
- Lesson 5: Calculations (percentages, rounding)
- Start Lesson 6: HTML generation
- Calculate completion rates in project file

**Week 7:**
- Complete Lesson 6: HTML styling
- Lesson 7: Saving files
- Complete HTML report generation

**Week 8-9:**
- Integration and testing
- Optional: GUI development
- Refinement and documentation

**Week 10:**
- Final presentation
- Demonstrate working project

---

## PROJECT FILE STRUCTURE

**Main Project File:** ProjectTicketAnalyzer.ps1 (root level - visible in GitHub)
**Purpose:** The actual graded project code
**Status:** Header complete, code to be added incrementally

**Expected Sections (in order):**
1. Data import (Import-Csv)
2. Metric calculations (counts, sums, percentages)
3. CSS styling definition
4. HTML report generation (summary + tables)
5. File output (save to Output folder)
6. (Optional) Email sending

**Expected Length:** ~125 lines total
- Week 4: ~30 lines (Import, basic display)
- Week 5: ~35 lines (Filtering, metrics)
- Week 6: ~30 lines (HTML generation)
- Week 7: ~30 lines (Styling, file output)

---

## AI BEHAVIOR RULES

**When Teaching:**
1. Read LEARNING_PROCESS.md at start of EVERY session
2. Follow Python Chapter format for all lessons
3. Explain WHY, not just WHAT
4. One concept at a time
5. Include practice exercises
6. Verify understanding before moving on

**When Helping with Code:**
1. Reference which lesson teaches the concept
2. Show example from lesson file
3. Guide student to practice file
4. Don't write project code for student - teach the concept

**When Student is Stuck:**
1. Ask which lesson they're on
2. Review that lesson's concepts
3. Show similar example
4. Let student try again in practice file

**Forbidden Actions:**
1. Writing complete project code without teaching
2. Skipping explanation of syntax/rules
3. Assuming student knows concepts
4. Creating random new files without purpose
5. Deviating from documented lesson plan

---

## SUCCESS CRITERIA

**Student Can:**
- Import CSV data independently
- Filter data by multiple conditions
- Calculate metrics (counts, percentages)
- Generate styled HTML reports
- Save reports to files
- Explain what each command does

**Project Deliverables:**
- Working PowerShell script (ProjectTicketAnalyzer.ps1)
- Professional HTML output (saved in Output folder)
- GitHub repository with clean structure
- (Optional) GUI demonstration
- Presentation-ready demo

**Teaching Success:**
- Student completes lessons independently
- Student writes code without constant AI help
- Student understands PowerShell fundamentals
- Project completed on time for Week 10 presentation

---

## OPTIONAL: GUI DEVELOPMENT

**If Time Permits (Week 8-9):**
- Windows Forms or WPF interface
- Buttons to generate report, view report, send email
- Date range selection
- Status filter checkboxes
- Professional appearance for presentation

**Not required but enhances presentation value**

---

## REFERENCES

**Documentation to Follow:**
- LEARNING_PROCESS.md (teaching methodology)
- WHAT_WE_NEED_TO_BUILD.md (task breakdown)
- AI_EXECUTION_CONTRACT.md (AI behavior rules)
- BEST_PRACTICES.md (coding standards)

**Student's Python Learning Reference:**
- Study Material and Summaries/Chapter 1/ (format to emulate)
- Chapter_1_Summary.md (explanation style)
- Chapter_1_Practice_Exercises.md (exercise format)

---

**LAST UPDATED:** January 31, 2026  
**STATUS:** All 7 lessons created and ready for use  
**NEXT ACTION:** Student begins Lesson 1 practice

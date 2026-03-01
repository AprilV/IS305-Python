# Canva AI Presentation Prompt & Content Guide

**For:** PowerShell Final Project Presentation  
**Duration:** 10-15 minutes  
**Due:** Week 10  
**Created:** February 18, 2026  
**Last Updated:** February 18, 2026

---

## 🎨 STEP 1: Canva AI Generation Prompt

**Go to Canva.com → Create Presentation → Use AI/Magic Design**

**COPY AND PASTE THIS EXACT PROMPT INTO CANVA:**

---

### 📋 COMPLETE CANVA AI PROMPT (Copy Everything Below):

```
Create a professional technical presentation for a college Information Systems scripting course final project worth 200 points. This is a 10-15 minute in-class presentation that will be graded on problem statement, technology overview, language comparison, code walkthrough, live demonstration, learning resources, and APA-formatted references.

PROJECT DETAILS:
- Student: April SYKES
- Course: IS305 Scripting
- Instructor: Dr. Lindsey Handley
- Project Title: "Construction Project Status Report Generator"
- Technology: PowerShell automation for analyzing 10,254 construction project records from CSV files
- Output: Automated HTML status reports with professional styling
- Business Value: Reducing hours of manual Excel work to seconds of automation

PRESENTATION STRUCTURE (14 slides total):

SLIDE 1 - Title Slide:
- Project title: "Construction Project Status Report Generator"
- Subtitle: "Automated Data Analysis with PowerShell"
- Student name, course number, instructor name, presentation date
- Professional, corporate style
- Add space for PowerShell logo

SLIDE 2 - The Problem - Business Context:
- Title: "The Challenge"
- Describe the business problem being solved
- Must include bullet points for:
  * Scenario: Managing construction project data across multiple sites
  * Data volume: 10,254 construction project records
  * Current manual process problems (time-consuming, error-prone)
  * Pain points: Hours to generate reports, risk of errors, inconsistent formatting, can't quickly identify overdue items
- Include icon or image representing data/spreadsheets/construction
- Professional blue/gray color scheme

SLIDE 3 - The Solution:
- Title: "Automated PowerShell Solution"
- Explain what was built and the benefits
- Bullet points for:
  * What was built (automated report generation system)
  * Processing speed (10,254 records in seconds)
  * Output format (professional HTML reports)
  * Key benefits (saves 2-3 hours per report, eliminates errors, consistent formatting, instant issue identification)
- Include before/after comparison visual or workflow diagram

SLIDE 4 - Technology Stack:
- Title: "Tools & Technologies"
- List all technologies used in the project
- Must include sections for:
  * Primary language (PowerShell 5.1)
  * Development environment (PowerShell ISE, VS Code)
  * Data source (CSV file)
  * Output format (HTML)
  * Optional features (email automation, GUI)
- Include technology logos: PowerShell, VS Code, CSV, HTML
- Clean, professional layout

SLIDE 5 - Why PowerShell?:
- Title: "Why We Chose PowerShell"
- Explain the rationale for choosing PowerShell over other options
- Two sections:
  * Advantages (checkmarks): Native Windows integration, built-in cmdlets, object-based pipeline, perfect for Windows admin, no extra libraries needed
  * Ideal use cases: Windows automation, system administration, report generation, file operations
- Include PowerShell logo or Windows ecosystem diagram

SLIDE 6 - PowerShell vs Python: Similarities:
- Title: "Common Ground: PowerShell & Python"
- List what both languages have in common
- Bullet points with checkmarks:
  * Both are scripting/interpreted languages
  * Variables, loops, conditionals, functions
  * Object-oriented programming
  * Excellent for automation
  * Active communities and resources
  * Can work with CSV, JSON, APIs
  * Cross-platform capabilities
- Two-column layout with icons for both languages
- Balanced, neutral comparison style

SLIDE 7 - PowerShell vs Python: Key Differences:
- Title: "Key Differences"
- Create a professional comparison TABLE with these columns: Feature, PowerShell, Python
- Table rows must include:
  * Primary Use: Windows admin vs General-purpose
  * Syntax Style: Verb-Noun cmdlets vs Library imports
  * Variables: $variable vs variable
  * Pipeline: Object-based vs Text-based
  * Platform: Windows-native vs Cross-platform
  * Best For: Windows systems vs Data science/web dev
  * Learning Curve: Moderate vs Gentle
- Add text below table: "When to Use Each" with bullet points
  * PowerShell for: Windows automation, system administration, enterprise IT
  * Python for: Cross-platform apps, data analysis, machine learning, web development
- Professional table styling with alternating row colors

SLIDE 8 - Code Walkthrough Part 1: Data Import:
- Title: "Step 1: Importing the Data"
- Include large area for CODE SCREENSHOT (monospace font, syntax highlighting)
- Code example showing PowerShell CSV import with comments
- Below code, add "Explanation" section with bullet points:
  * Import-Csv reads CSV and converts to PowerShell objects
  * Each CSV row becomes an object with properties
  * Data count shows total records
  * Data ready for filtering and analysis
- Dark code background with light text for readability
- Leave white space around code for professional look

SLIDE 9 - Code Walkthrough Part 2: Analysis & Filtering:
- Title: "Step 2: Analyzing the Data"
- Large code screenshot area showing filtering and metric calculations
- PowerShell code with Where-Object filtering, counts, percentages
- "Key Concepts" explanation section below:
  * Pipeline operator passes data between commands
  * Where-Object filters based on conditions
  * Math functions for calculations
- Same code styling as previous slide for consistency

SLIDE 10 - Code Walkthrough Part 3: HTML Generation:
- Title: "Step 3: Generating the Report"
- Code screenshot showing HTML report generation
- PowerShell code with CSS styling, ConvertTo-Html, file output
- "What This Does" explanation:
  * Defines professional CSS styling
  * Converts data to HTML table
  * Adds timestamp to filename
  * Saves complete report
- Professional code presentation matching previous slides

SLIDE 11 - Live Demonstration:
- Title: "Demo: Watch It Work!"
- Section titled "Demo Plan" with numbered checklist:
  1. Show the CSV data file (10,254 records)
  2. Run the PowerShell script in console
  3. Watch metrics calculate in real-time
  4. View generated HTML report in browser
  5. Highlight key statistics (total forms, completion rate, overdue items, project breakdown)
- Section titled "Backup" noting screenshots/video ready if issues
- Large area for SCREENSHOT of HTML report output
- Engaging, demonstration-focused layout

SLIDE 12 - Learning Resources:
- Title: "Want to Learn PowerShell?"
- Organized in clear sections:
  * Official Documentation (with book emoji): Microsoft Learn links, PowerShell Module Reference, PowerShell Gallery
  * Video Tutorials (with video emoji): YouTube channels, Microsoft Virtual Academy, Pluralsight
  * Recommended Books (with book emoji): "Learn PowerShell in a Month of Lunches", "PowerShell for Sysadmins"
  * Practice Tools (with computer emoji): PowerShell ISE, VS Code, Windows Terminal
- Include relevant icons for each section
- Easy-to-scan layout with clear visual hierarchy
- Blue highlights for hyperlinks

SLIDE 13 - References Page:
- Title: "References"
- APA 7th Edition format REQUIRED
- List academic references in proper APA format:
  * Book citations
  * Microsoft documentation citations
  * Web resources with URLs
  * All sources used in project development
- Clean, academic formatting
- Proper hanging indents for APA style
- Professional academic appearance

SLIDE 14 - Closing Slide:
- Title: "Thank You!"
- Center text: "Questions?"
- Display GitHub repository link prominently
- Student contact information
- Key takeaway message: "PowerShell transforms hours of manual work into seconds of automation"
- Professional closing image or project logo
- Clean, minimal design for Q&A focus

DESIGN SPECIFICATIONS:
- Overall Style: Professional, technical, corporate
- Color Scheme: Blue (#4472C4) and gray professional palette, white backgrounds
- Typography: Sans-serif fonts (Arial, Helvetica, or similar), minimum 24pt for body text, 36pt for titles
- Code Blocks: Monospace font (Courier New or Consolas), dark background with syntax highlighting colors
- Spacing: Clean, minimal design with plenty of white space
- Tables: Professional styling with headers in blue, alternating row colors for readability
- Icons: Simple, professional tech icons where appropriate
- Consistency: Same template style across all slides
- Accessibility: High contrast, readable fonts, clear visual hierarchy

PURPOSE: This is a formal academic presentation for IS305 college course final project worth 200 points. The student will present live for 10-15 minutes and must demonstrate professionalism, technical competence, clear communication, and thorough understanding of PowerShell automation. The presentation will be followed by Q&A session.

IMPORTANT: Leave space on code slides for screenshots to be inserted. Include section dividers between major topics. Use consistent formatting throughout all slides. Create professional, academic-quality presentation suitable for college-level evaluation.
```

---

### ✅ After You Paste This Into Canva:

1. **Review Generated Slides** - Canva will create the structure and design
2. **Adjust Colors** - Make sure blue/gray theme is professional
3. **Check Font Sizes** - Ensure all text is readable (min 24pt)
4. **Verify All 14 Slides** - Make sure nothing was missed
5. **Prepare to Add Your Content** - Screenshots, actual code, real data

The AI should give you a complete presentation framework ready for your specific content!

---

## 📋 STEP 2: Content to Add to Each Slide

### Slide 1: Title
**Title:** Construction Project Status Report Generator  
**Subtitle:** Automated Data Analysis with PowerShell  
**Your Name:** April SYKES  
**Course:** IS305 Scripting  
**Instructor:** Dr. Lindsey Handley  
**Date:** [Your presentation date]

---

### Slide 2: The Problem - Context
**Title:** The Challenge

**Content:**
- **Scenario:** Managing construction project data across multiple sites
- **Data Volume:** 10,254 construction project records
- **Current Process:** Manual analysis in Excel - time-consuming and error-prone
- **Pain Points:**
  - Hours to generate status reports
  - High risk of human error
  - Inconsistent report formatting
  - Unable to quickly identify overdue items

**Visual:** Icon or image representing data/spreadsheets/construction

---

### Slide 3: The Solution
**Title:** Automated PowerShell Solution

**Content:**
- **What We Built:** Automated report generation system
- **Processing Time:** 10,254 records analyzed in seconds
- **Output:** Professional HTML status reports
- **Benefits:**
  - Saves 2-3 hours per report
  - Eliminates manual errors
  - Consistent formatting every time
  - Instant identification of issues

**Visual:** Before/After comparison or workflow diagram

---

### Slide 4: Technology Stack
**Title:** Tools & Technologies

**Content:**
- **Primary Language:** PowerShell 5.1
- **Development Environment:** 
  - Windows PowerShell ISE
  - Visual Studio Code with PowerShell extension
- **Data Source:** CSV file (Construction_Data.csv)
- **Output Format:** Styled HTML reports
- **Optional Features:** Email automation, GUI interface

**Visual:** Logos of PowerShell, VS Code, CSV, HTML

---

### Slide 5: Why PowerShell?
**Title:** Why We Chose PowerShell

**Content:**
**Advantages:**
- ✅ Native Windows integration
- ✅ Built-in cmdlets for CSV, HTML, email
- ✅ Powerful object-based pipeline
- ✅ Perfect for Windows administration tasks
- ✅ No additional libraries needed for core functionality

**Ideal For:**
- Windows automation
- System administration
- Report generation
- File/folder operations

**Visual:** PowerShell logo or Windows ecosystem diagram

---

### Slide 6: PowerShell vs Python - Similarities
**Title:** Common Ground: PowerShell & Python

**Both Languages Share:**
- ✓ Scripting/interpreted languages
- ✓ Variables, loops, conditionals, functions
- ✓ Object-oriented programming
- ✓ Excellent for automation
- ✓ Active communities and resources
- ✓ Can work with CSV, JSON, APIs
- ✓ Cross-platform capabilities (with PowerShell Core)

**Visual:** Two-column layout with icons

---

### Slide 7: PowerShell vs Python - Key Differences
**Title:** Key Differences

| Feature | PowerShell | Python |
|---------|-----------|--------|
| **Primary Use** | Windows admin & automation | General-purpose programming |
| **Syntax Style** | Verb-Noun cmdlets | Library imports |
| **Variables** | $variable | variable |
| **Pipeline** | Object-based | Text-based (traditionally) |
| **Platform** | Windows-native (Core is cross-platform) | Fully cross-platform |
| **Best For** | Windows systems, Active Directory, Exchange | Data science, web dev, AI/ML |
| **Learning Curve** | Moderate (Windows admins) | Gentle (beginners) |

**When to Use Each:**
- **PowerShell:** Windows automation, system administration, enterprise IT
- **Python:** Cross-platform apps, data analysis, machine learning, web development

---

### Slide 8: Code Walkthrough - Data Import
**Title:** Step 1: Importing the Data

**Code:**
```powershell
# Import 10,254 construction records from CSV
$data = Import-Csv -Path ".\Data\Construction_Data.csv"

# Display total record count
Write-Host "Total records imported: $($data.Count)"
Write-Host "Processing construction project data..."
```

**Explanation:**
- `Import-Csv` reads CSV file and converts to PowerShell objects
- Each CSV row becomes an object with properties
- `$data.Count` gives us the total number of records
- Data is now ready for filtering and analysis

**Visual:** Add screenshot of CSV file or code in VS Code

---

### Slide 9: Code Walkthrough - Data Filtering & Metrics
**Title:** Step 2: Analyzing the Data

**Code:**
```powershell
# Filter by status
$openItems = $data | Where-Object { $_.Status -eq "Open" }
$closedItems = $data | Where-Object { $_.Status -eq "Closed" }
$overdueItems = $data | Where-Object { $_.OverDue -eq "Yes" }

# Calculate metrics
$totalForms = $data.Count
$openCount = $openItems.Count
$overdueCount = $overdueItems.Count

# Calculate completion rate
$completed = $totalForms - $openCount
$completionRate = [math]::Round(($completed / $totalForms) * 100, 2)

Write-Host "Completion Rate: $completionRate%"
Write-Host "Overdue Items: $overdueCount"
```

**Key Concepts:**
- Pipeline operator `|` passes data to next command
- `Where-Object` filters based on conditions
- `[math]::Round()` for precise calculations

---

### Slide 10: Code Walkthrough - HTML Report Generation
**Title:** Step 3: Generating the Report

**Code:**
```powershell
# Create CSS styling
$css = @"
<style>
  body { font-family: Arial; }
  table { border-collapse: collapse; width: 100%; }
  th { background-color: #4472C4; color: white; padding: 10px; }
  td { border: 1px solid #ddd; padding: 8px; }
  .summary { background-color: #f0f0f0; padding: 15px; }
</style>
"@

# Generate HTML table
$htmlTable = $data | ConvertTo-Html -Property Status, Project, Location

# Combine CSS and HTML
$fullReport = $css + $htmlTable

# Save to file with timestamp
$timestamp = Get-Date -Format "yyyy-MM-dd_HHmm"
$outputPath = ".\Output\StatusReport_$timestamp.html"
$fullReport | Out-File -FilePath $outputPath

Write-Host "Report saved to: $outputPath"
```

**What This Does:**
- Defines professional CSS styling
- Converts data to HTML table
- Adds timestamp to filename
- Saves complete report to Output folder

---

### Slide 11: Live Demonstration
**Title:** Demo: Watch It Work!

**Demo Plan:**
1. ✅ Show the CSV data file (10,254 records)
2. ✅ Run the PowerShell script in console
3. ✅ Watch metrics calculate in real-time
4. ✅ View generated HTML report in browser
5. ✅ Highlight key statistics:
   - Total forms processed
   - Completion rate percentage
   - Number of overdue items
   - Project breakdown by status

**Backup:** Screenshots/video ready if live demo has issues

**Visual:** Screenshot of your HTML report or script running

---

### Slide 12: Learning Resources
**Title:** Want to Learn PowerShell?

**Official Documentation:**
- 📚 Microsoft Learn: https://learn.microsoft.com/en-us/powershell/
- 📖 PowerShell Module Reference: https://learn.microsoft.com/en-us/powershell/module/
- 🔧 PowerShell Gallery (community scripts): https://www.powershellgallery.com/

**Video Tutorials:**
- 🎥 YouTube: "PowerShell Master Class" by John Savill
- 🎥 Microsoft Virtual Academy PowerShell courses
- 🎥 Pluralsight PowerShell learning paths

**Recommended Books:**
- 📗 "Learn PowerShell in a Month of Lunches" by Don Jones & Jeffrey Hicks
- 📗 "PowerShell for Sysadmins" by Adam Bertram

**Practice Tools:**
- 💻 PowerShell ISE (built into Windows)
- 💻 VS Code with PowerShell extension
- 💻 Windows Terminal with PowerShell 7

---

### Slide 13: References (APA Format)
**Title:** References

**Format examples - adjust with your actual sources:**

Bertram, A. (2020). *PowerShell for sysadmins: Workflow automation made easy*. No Starch Press.

Jones, D., & Hicks, J. (2023). *Learn PowerShell in a month of lunches* (4th ed.). Manning Publications.

Microsoft. (2026). *PowerShell documentation*. Microsoft Learn. https://learn.microsoft.com/en-us/powershell/

Microsoft. (2026). *Import-Csv (Microsoft.PowerShell.Utility)*. Microsoft Learn. https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/import-csv

Microsoft. (2026). *ConvertTo-Html (Microsoft.PowerShell.Utility)*. Microsoft Learn. https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/convertto-html

[Add any other resources you actually used: tutorials, Stack Overflow posts, blog articles, etc.]

**Note:** Follow APA 7th edition format strictly

---

### Slide 14: Thank You / Questions
**Title:** Thank You!

**Content:**
**Questions?**

**GitHub Repository:**
https://github.com/AprilV/IS305-PowerShell-Project.git

**Contact:**
April SYKES

**Key Takeaway:**
PowerShell transforms hours of manual work into seconds of automation.

**Visual:** Professional closing image or your project logo

---

## 🎯 STEP 3: After Canva Generates Slides

### What to Do Next:

1. **Review the Layout**
   - Canva will create slide designs
   - Adjust colors/fonts if needed
   - Keep it professional and readable

2. **Add Your Code Screenshots**
   - Take clean screenshots of your PowerShell code
   - Make sure code is readable
   - Use syntax highlighting

3. **Insert Your Actual Data**
   - Replace placeholder numbers with your real metrics
   - Add screenshots of your HTML report
   - Include your actual CSV data sample

4. **Add Visual Elements**
   - Screenshot of your script running
   - HTML report screenshot
   - Before/after comparison
   - Flow diagrams if helpful

5. **Polish Transitions**
   - Keep transitions simple (fade or none)
   - Don't distract from content

6. **Test Timing**
   - Practice presentation
   - Should be 10-15 minutes
   - Adjust slide content if too long/short

7. **Download**
   - Export as PowerPoint (.pptx) OR PDF
   - Test that file opens correctly
   - Keep a backup copy

---

## 💡 Tips for Using Canva

**DO:**
- ✅ Use professional themes (avoid too colorful/playful)
- ✅ Keep text readable (minimum 24pt font)
- ✅ Use bullet points, not paragraphs
- ✅ Add code with monospace font
- ✅ Include visuals where helpful

**DON'T:**
- ❌ Overcrowd slides with too much text
- ❌ Use too many different fonts
- ❌ Add distracting animations
- ❌ Make code screenshots too small to read
- ❌ Forget to proofread!

---

## 📸 Screenshots You'll Need

Take these screenshots before creating your presentation:

1. **CSV file open in Excel** (showing 10,254 rows)
2. **PowerShell code in VS Code** (clean, syntax highlighted)
3. **Script running in terminal** (showing output)
4. **Generated HTML report in browser** (professional look)
5. **Close-up of key metrics** (completion rate, overdue count)
6. **(Optional) GUI if you build one**

---

## ⏱️ Presentation Timing Guide

**Total: 10-15 minutes**

- Intro (1 min): Title, your name, overview
- Problem (2 min): What you're solving
- Tech & Comparison (3 min): PowerShell overview, vs Python
- Code (4 min): Walk through key sections
- Demo (3 min): Show it working
- Resources (1 min): Where to learn
- Q&A (built into class time)

---

## 🚀 Ready to Go!

1. Copy the Canva AI prompt from Step 1
2. Let Canva generate the slide structure
3. Fill in the content from Step 2
4. Add your screenshots and code
5. Practice your presentation
6. Export as PowerPoint or PDF
7. Upload to Canvas on presentation day

**You've got this! 🎯**

---

**Last Updated:** February 18, 2026  
**Status:** Ready for Canva AI generation  
**Next Step:** Go to Canva.com and paste the prompt!

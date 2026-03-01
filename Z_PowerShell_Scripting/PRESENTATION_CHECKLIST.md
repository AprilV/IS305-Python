# PowerShell Final Presentation - Preparation Checklist

**Presentation Date:** Week 10 (TBD)  
**Duration:** 10-15 minutes  
**Points:** 200 points (50% of final grade)  
**Created:** February 18, 2026  
**Last Updated:** February 18, 2026

---

## ✅ Pre-Presentation Checklist

### Code & Project
- [ ] ProjectTicketAnalyzer.ps1 is complete and working
- [ ] Script successfully imports 10,254 CSV records
- [ ] All metrics calculate correctly
- [ ] HTML report generates successfully
- [ ] Report has professional styling
- [ ] (Optional) Email functionality works
- [ ] (Optional) GUI is functional
- [ ] Code is commented and clean
- [ ] GitHub repository is up-to-date and organized

### Presentation Materials
- [ ] PowerPoint/Google Slides created
- [ ] Problem statement slide prepared
- [ ] PowerShell overview slides ready
- [ ] PowerShell vs Python comparison prepared
- [ ] Code screenshots/snippets in slides
- [ ] Demo plan outlined
- [ ] Learning resources slide created
- [ ] APA references page completed
- [ ] GitHub link ready to share

### Practice & Testing
- [ ] Practiced presentation (timed 10-15 min)
- [ ] Tested live demo multiple times
- [ ] Backup plan if demo fails (screenshots/video)
- [ ] Can explain code without reading slides
- [ ] Prepared for common questions

---

## 📋 Presentation Outline Template

### Slide 1: Title
- **Project Title:** Construction Project Status Report Generator
- **Your Name:** April SYKES
- **Course:** IS305 Scripting
- **Instructor:** Dr. Lindsey Handley

### Slide 2-3: The Problem
- **Context:** Managing 10,254 construction project records
- **Challenge:** Manual analysis is time-consuming and error-prone
- **Solution:** Automated PowerShell report generation
- **Business Value:** Save hours of manual work, reduce errors, consistent reporting

### Slide 4-5: Technology Overview
- **Primary Language:** PowerShell 5.1
- **Tools Used:**
  - Windows PowerShell / PowerShell ISE / VS Code
  - CSV data import (Import-Csv)
  - HTML generation (ConvertTo-Html)
  - Email automation (Send-MailMessage)
  - (Optional) Windows Forms GUI
- **Why PowerShell?**
  - Native Windows integration
  - Built-in cmdlets for CSV, HTML, email
  - Powerful for system administration
  - Ideal for Windows-based automation

### Slide 6-7: PowerShell vs Python Comparison

**Similarities:**
- Both scripting languages
- Variables, loops, conditionals, functions
- Object-oriented
- Excellent for automation
- Active communities

**Differences:**

| Feature | PowerShell | Python |
|---------|-----------|--------|
| Platform | Windows-native | Cross-platform |
| Syntax | Verb-Noun cmdlets | Library functions |
| Variables | $variable | variable |
| Strengths | Windows admin, systems | General-purpose, data science |
| Pipeline | Object-based | Text-based (traditionally) |

**When to Use Each:**
- **PowerShell:** Windows automation, Active Directory, Exchange, IIS, system configs
- **Python:** Cross-platform, data science, web dev, AI/ML, broader application domains

### Slide 8-10: Code Walkthrough

**Show Key Sections:**

1. **Data Import:**
```powershell
$data = Import-Csv -Path ".\Data\Construction_Data.csv"
Write-Host "Total records: $($data.Count)"
```

2. **Data Filtering:**
```powershell
$openItems = $data | Where-Object { $_.Status -eq "Open" }
$overdueItems = $data | Where-Object { $_.OverDue -eq "Yes" }
```

3. **Metric Calculations:**
```powershell
$totalForms = $data.Count
$openCount = $openItems.Count
$completionRate = [math]::Round((($totalForms - $openCount) / $totalForms) * 100, 2)
```

4. **HTML Generation:**
```powershell
$html = $data | ConvertTo-Html -Property Status, Project, Location
$styledHtml = $css + $html
$styledHtml | Out-File -FilePath ".\Output\StatusReport.html"
```

### Slide 11: Live Demo
- **Demo Plan:**
  1. Show the CSV data file (10,254 records)
  2. Run the PowerShell script
  3. Watch as it processes data
  4. Display metrics in console
  5. Open generated HTML report
  6. Show report styling and data
  7. (Optional) Demonstrate GUI or email sending

- **Backup Plan:** Have screenshots/video ready if live demo fails

### Slide 12: Learning Resources

**Official Documentation:**
- Microsoft Learn PowerShell: https://learn.microsoft.com/en-us/powershell/
- PowerShell Module Reference: https://learn.microsoft.com/en-us/powershell/module/
- PowerShell Gallery: https://www.powershellgallery.com/

**Video Tutorials:**
- YouTube: "PowerShell Master Class" by John Savill
- Pluralsight: PowerShell courses
- Microsoft Virtual Academy

**Practice:**
- PowerShell ISE (built-in Windows)
- VS Code with PowerShell extension
- Practice with real CSV files and data

**Books:**
- "Learn PowerShell in a Month of Lunches" by Don Jones
- "PowerShell for Sysadmins" by Adam Bertram

### Slide 13: References (APA Format)

**Example References:**

Microsoft. (2026). *PowerShell Documentation*. Microsoft Learn. https://learn.microsoft.com/en-us/powershell/

Microsoft. (2026). *Import-Csv cmdlet reference*. Microsoft Learn. https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/import-csv

Jones, D., & Hicks, J. (2023). *Learn PowerShell in a Month of Lunches* (4th ed.). Manning Publications.

[Add your actual sources used during development]

### Slide 14: Thank You / Questions
- Thank audience
- Open for questions
- Display GitHub link: https://github.com/AprilV/IS305-PowerShell-Project.git

---

## 🎤 Presentation Delivery Tips

### Opening (Strong Start):
"Hi, I'm April Sykes, and today I'm going to show you how I automated construction project status reporting using PowerShell. This project analyzes over 10,000 construction records and generates professional HTML reports in seconds—a task that would take hours manually."

### During Code Walkthrough:
- **Don't read code line-by-line** - explain what sections DO
- Use simple language: "This section filters the data to show only open items"
- Point out interesting features: "Notice how PowerShell's pipeline makes this very readable"

### During Demo:
- **Talk while you demo:** "Now I'm running the script... It's importing 10,254 records... Calculating metrics... Generating the report..."
- **Show confidence:** Even if something goes wrong, stay calm
- **Highlight results:** "Here you can see the completion rate is 87%, and we have 23 overdue items"

### Handling Questions:
- Listen fully before answering
- It's okay to say "That's a great question—let me show you that section"
- Refer back to your code/slides if needed
- Be honest if you don't know something

---

## 🎯 Common Questions to Prepare For

1. **"Why did you choose PowerShell over Python?"**
   - Answer: Windows-native, built-in cmdlets for CSV and HTML, better for Windows administration tasks

2. **"What was the hardest part of this project?"**
   - Be honest: Maybe HTML styling, or understanding the pipeline, or working with date calculations

3. **"Could this work on Mac/Linux?"**
   - Answer: PowerShell Core works cross-platform, but some cmdlets (like Send-MailMessage) work best on Windows

4. **"How long does it take to run?"**
   - Know your answer: "It processes all 10,254 records in about X seconds"

5. **"Could you adapt this for other types of data?"**
   - Answer: Yes! The Import-Csv, filtering, and HTML generation would work for any CSV data

6. **"What would you improve if you had more time?"**
   - Be prepared: Maybe add error handling, GUI improvements, database integration, scheduled automation

---

## 📊 Success Metrics

**Your presentation is successful if you:**
- ✅ Stay within 10-15 minutes
- ✅ Clearly explain the problem and solution
- ✅ Demonstrate working code
- ✅ Compare PowerShell and Python effectively
- ✅ Answer questions confidently
- ✅ Show enthusiasm for your project
- ✅ Provide helpful resources for others

---

## 🚀 Final Week Before Presentation

### 1 Week Before:
- [ ] Complete all code
- [ ] Test thoroughly
- [ ] Create all slides
- [ ] Practice once

### 3 Days Before:
- [ ] Practice presentation 2-3 times
- [ ] Time yourself
- [ ] Get feedback from someone
- [ ] Refine slides

### 1 Day Before:
- [ ] Final practice run
- [ ] Test demo on actual presentation computer
- [ ] Prepare backup screenshots
- [ ] Get good sleep

### Day Of:
- [ ] Arrive early
- [ ] Test equipment
- [ ] Upload slides to Canvas
- [ ] Upload GitHub link/zip file
- [ ] Take deep breath
- [ ] Nail it! 🎯

---

**Last Updated:** February 18, 2026  
**Status:** Preparation checklist ready  
**Next Steps:** Complete project code, begin slide creation

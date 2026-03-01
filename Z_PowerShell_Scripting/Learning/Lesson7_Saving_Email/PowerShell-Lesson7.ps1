################################################################################
# Lesson 7: Saving Files and Sending Email
# LEARN: Out-File, Send-MailMessage, Get-Date, Final Integration
################################################################################

# ============================================================================
# WHAT WE'RE BUILDING: Construction Project Report
# ============================================================================
# Final lesson! We'll learn to:
# - Save HTML reports to files
# - Send emails with PowerShell
# - Put everything together into the complete project
# ============================================================================


# ============================================================================
# PART 1: Out-File - Saving to Files
# ============================================================================
# Out-File saves output to a text file
#
# SYNTAX: $content | Out-File "C:\path\to\file.txt"
# SYNTAX (overwrite): $content | Out-File "path" -Force
# SYNTAX (encoding): $content | Out-File "path" -Encoding UTF8
# ============================================================================

# Simple example
$message = "Hello, this is a test file"
$message | Out-File "C:\temp\test.txt"
Write-Host "File saved to C:\temp\test.txt"


# Save HTML report to file
$data = Import-Csv "C:\ReactGitEC2\IS305 Scripting\Z_PowerShell_Scripting\Data\Construction_Data_PM_Forms_All_Projects.csv"

$html = $data | 
    Select-Object -First 10 Status, Project, Location | 
    ConvertTo-Html -Title "Test Report"

# Save to file
$html | Out-File "C:\temp\report.html" -Encoding UTF8
Write-Host "HTML report saved to C:\temp\report.html"


# ============================================================================
# PART 2: File Paths and Directories
# ============================================================================
# IMPORTANT: The folder must exist before saving!
# Create folder if it doesn't exist
# ============================================================================

# Check if directory exists, create if not
$outputFolder = "C:\ReactGitEC2\IS305 Scripting\Z_PowerShell_Scripting\Output"

if (-not (Test-Path $outputFolder)) {
    New-Item -Path $outputFolder -ItemType Directory
    Write-Host "Created folder: $outputFolder"
}

# Now save to that folder
$html | Out-File "$outputFolder\report.html" -Encoding UTF8
Write-Host "Report saved to Output folder"


# ============================================================================
# PART 3: Dynamic File Names with Dates
# ============================================================================
# Get-Date gets the current date/time
# Use -Format to format it as a string
# ============================================================================

# Get current date/time
$now = Get-Date
Write-Host "`nCurrent date/time: $now"

# Format date for filenames (no spaces or special chars)
$dateStamp = Get-Date -Format "yyyyMMdd_HHmmss"
Write-Host "Date stamp: $dateStamp"

# Create filename with date
$filename = "ProjectReport_$dateStamp.html"
Write-Host "Filename: $filename"

# Save with dynamic name
$html | Out-File "$outputFolder\$filename" -Encoding UTF8
Write-Host "Saved as: $filename"


# ============================================================================
# PART 4: Get-Date Formatting Options
# ============================================================================
# Common date formats:
#   yyyy-MM-dd          → 2026-01-31
#   yyyyMMdd            → 20260131
#   yyyy-MM-dd HH:mm    → 2026-01-31 14:30
#   yyyyMMdd_HHmmss     → 20260131_143045
#   MMMM dd, yyyy       → January 31, 2026
# ============================================================================

Write-Host "`nDate Format Examples:"
Write-Host "Standard: $(Get-Date -Format 'yyyy-MM-dd')"
Write-Host "Compact: $(Get-Date -Format 'yyyyMMdd')"
Write-Host "With time: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
Write-Host "Readable: $(Get-Date -Format 'MMMM dd, yyyy')"
Write-Host "Filename safe: $(Get-Date -Format 'yyyyMMdd_HHmmss')"


# ============================================================================
# PART 5: Send-MailMessage - Sending Emails
# ============================================================================
# Send-MailMessage sends emails via SMTP
#
# BASIC SYNTAX:
# Send-MailMessage `
#     -From "sender@email.com" `
#     -To "recipient@email.com" `
#     -Subject "Email subject" `
#     -Body "Email body text" `
#     -SmtpServer "smtp.gmail.com" `
#     -Port 587 `
#     -UseSsl `
#     -Credential (Get-Credential)
#
# NOTE: Requires SMTP server access and credentials
# ============================================================================

# Example structure (won't actually send without real credentials)
<#
$emailParams = @{
    From = "your-email@gmail.com"
    To = "recipient@email.com"
    Subject = "Construction Project Report - $(Get-Date -Format 'yyyy-MM-dd')"
    Body = "Please see the attached construction project report."
    SmtpServer = "smtp.gmail.com"
    Port = 587
    UseSsl = $true
}

# Send-MailMessage @emailParams -Credential (Get-Credential)
#>

Write-Host "`nEmail sending requires SMTP configuration"
Write-Host "For this project, we'll focus on generating and saving the report"


# ============================================================================
# PART 6: Sending HTML Email Body
# ============================================================================
# You can send HTML directly as the email body
# Use -BodyAsHtml parameter
# ============================================================================

<#
# HTML email example
$emailBody = @"
<h1>Project Report</h1>
<p>This is an automated report.</p>
<p>Please review the attached data.</p>
"@

$emailParams = @{
    From = "sender@email.com"
    To = "recipient@email.com"
    Subject = "Project Report"
    Body = $emailBody
    BodyAsHtml = $true
    SmtpServer = "smtp.gmail.com"
    Port = 587
    UseSsl = $true
}

# Send-MailMessage @emailParams -Credential (Get-Credential)
#>


# ============================================================================
# PART 7: Complete Report Generation Script
# ============================================================================
# Putting it all together: Import → Analyze → Generate HTML → Save to File
# ============================================================================

Write-Host "`n=========================================="
Write-Host "GENERATING COMPLETE PROJECT REPORT"
Write-Host "=========================================="

# 1. Import data
Write-Host "`n[1/5] Importing data..."
$data = Import-Csv "C:\ReactGitEC2\IS305 Scripting\Z_PowerShell_Scripting\Data\Construction_Data_PM_Forms_All_Projects.csv"
Write-Host "Loaded $($data.Count) records"

# 2. Calculate metrics
Write-Host "`n[2/5] Calculating metrics..."
$totalProjects = ($data | Measure-Object).Count
$openProjects = ($data | Where-Object {$_.Status -eq "Open"} | Measure-Object).Count
$closedProjects = ($data | Where-Object {$_.Status -eq "Closed"} | Measure-Object).Count
$overdueProjects = ($data | Where-Object {$_.OverDue -gt 0} | Measure-Object).Count

# 3. Create CSS style
Write-Host "`n[3/5] Creating HTML style..."
$css = @"
<style>
    body { font-family: Arial; margin: 20px; background: #f5f5f5; }
    h1 { color: #2c3e50; border-bottom: 3px solid #3498db; }
    h2 { color: #34495e; margin-top: 25px; }
    table { border-collapse: collapse; width: 100%; background: white; margin: 15px 0; }
    th { background: #3498db; color: white; padding: 12px; text-align: left; }
    td { padding: 10px; border-bottom: 1px solid #ddd; }
    tr:hover { background: #ecf0f1; }
    .summary { background: white; padding: 20px; margin: 15px 0; border-left: 5px solid #3498db; }
</style>
"@

# 4. Build HTML report
Write-Host "`n[4/5] Building HTML report..."
$reportDate = Get-Date -Format "MMMM dd, yyyy - HH:mm"

$summary = @"
<h1>Construction Project Status Report</h1>
<p><strong>Generated:</strong> $reportDate</p>

<div class="summary">
    <h2>Overall Statistics</h2>
    <ul>
        <li><strong>Total Projects:</strong> $totalProjects</li>
        <li><strong>Open:</strong> $openProjects ($([Math]::Round(($openProjects/$totalProjects)*100, 1))%)</li>
        <li><strong>Closed:</strong> $closedProjects ($([Math]::Round(($closedProjects/$totalProjects)*100, 1))%)</li>
        <li><strong>Projects with Overdue Items:</strong> $overdueProjects</li>
    </ul>
</div>
"@

$openTable = $data | 
    Where-Object {$_.Status -eq "Open"} | 
    Select-Object -First 20 Project, Location, TotalActions, OpenActions, OverDue | 
    ConvertTo-Html -Fragment -PreContent "<h2>Open Projects (Top 20)</h2>"

$overdueTable = $data | 
    Where-Object {$_.OverDue -gt 0} | 
    Sort-Object OverDue -Descending |
    Select-Object -First 15 Project, Status, TotalActions, OverDue | 
    ConvertTo-Html -Fragment -PreContent "<h2>Projects with Overdue Items</h2>"

$reportHtml = ConvertTo-Html -Head $css -Body "$summary $openTable $overdueTable" -Title "Construction Project Report"

# 5. Save to file
Write-Host "`n[5/5] Saving report..."
$outputFolder = "C:\ReactGitEC2\IS305 Scripting\Z_PowerShell_Scripting\Output"
if (-not (Test-Path $outputFolder)) {
    New-Item -Path $outputFolder -ItemType Directory | Out-Null
}

$dateStamp = Get-Date -Format "yyyyMMdd_HHmmss"
$filename = "ConstructionReport_$dateStamp.html"
$fullPath = "$outputFolder\$filename"

$reportHtml | Out-File $fullPath -Encoding UTF8

Write-Host "`n=========================================="
Write-Host "REPORT GENERATION COMPLETE!" -ForegroundColor Green
Write-Host "=========================================="
Write-Host "File saved: $fullPath"
Write-Host "Open this file in a web browser to view the report"


################################################################################
# PRACTICE EXERCISES - Copy to practice.ps1 and complete
################################################################################
#
# Exercise 1: Save Simple HTML
# - Create a simple HTML report (first 10 records)
# - Save it to the Output folder
# - Use a descriptive filename
# - Verify the file was created
#
# Exercise 2: Dynamic Filenames
# - Create a report
# - Save with filename: "ProjectReport_YYYYMMDD_HHMMSS.html"
# - Use Get-Date to generate the timestamp
#
# Exercise 3: Check and Create Directory
# - Write code that checks if Output folder exists
# - Create it if it doesn't exist
# - Save a report there
#
# Exercise 4: Complete Report Generation
# - Import data
# - Calculate metrics (total, open, closed, overdue)
# - Create styled HTML with summary and tables
# - Save to Output folder with timestamped name
# - Display success message with file location
#
# Exercise 5: Final Project Script
# - Create the COMPLETE project script with:
#   - Data import
#   - All metric calculations
#   - Professional HTML styling
#   - Multiple sections (summary, open projects, overdue, closed)
#   - Save to Output folder
#   - Display generation summary
# - This should be YOUR version of ProjectTicketAnalyzer.ps1!
#
################################################################################

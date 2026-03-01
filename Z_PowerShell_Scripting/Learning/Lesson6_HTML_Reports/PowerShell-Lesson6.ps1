################################################################################
# Lesson 6: Creating HTML Reports
# LEARN: ConvertTo-Html, HTML Styling, Multi-Section Reports
################################################################################

# ============================================================================
# WHAT WE'RE BUILDING: Construction Project Report
# ============================================================================
# Now we create the HTML report that shows our data in a webpage format
# - Convert data to HTML tables
# - Add CSS styling (colors, borders, fonts)
# - Combine multiple sections into one report
# ============================================================================


# ============================================================================
# PART 1: ConvertTo-Html Basics
# ============================================================================
# ConvertTo-Html converts PowerShell objects to HTML table format
#
# SYNTAX: $data | ConvertTo-Html
# SYNTAX (with properties): $data | Select-Object Prop1, Prop2 | ConvertTo-Html
# ============================================================================

# Import data
$data = Import-Csv "C:\ReactGitEC2\IS305 Scripting\Z_PowerShell_Scripting\Data\Construction_Data_PM_Forms_All_Projects.csv"

# Convert first 5 records to HTML
$html = $data | Select-Object -First 5 | ConvertTo-Html

# Display (just to see what it looks like)
Write-Host "HTML output:"
$html


# ============================================================================
# PART 2: Selecting Specific Columns for HTML
# ============================================================================
# Control which columns appear in the HTML table
# ============================================================================

# Create HTML with only specific columns
$html = $data | 
    Select-Object -First 10 Status, Project, Location, TotalActions, OverDue | 
    ConvertTo-Html

# At this point, $html contains the HTML code as an array of strings


# ============================================================================
# PART 3: Adding a Title and Header
# ============================================================================
# Use -Title and -Head parameters to customize the HTML
#
# SYNTAX: ConvertTo-Html -Title "Page Title" -Head "<style>CSS here</style>"
# ============================================================================

$html = $data | 
    Select-Object -First 10 Status, Project, Location | 
    ConvertTo-Html -Title "Construction Project Report"


# ============================================================================
# PART 4: CSS Styling
# ============================================================================
# CSS controls how the HTML looks (colors, fonts, spacing)
# Add CSS in the -Head parameter
# ============================================================================

# Define CSS style
$style = @"
<style>
    body {
        font-family: Arial, sans-serif;
        margin: 20px;
        background-color: #f5f5f5;
    }
    h1 {
        color: #333;
        border-bottom: 3px solid #007acc;
        padding-bottom: 10px;
    }
    table {
        border-collapse: collapse;
        width: 100%;
        background-color: white;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    th {
        background-color: #007acc;
        color: white;
        padding: 12px;
        text-align: left;
        font-weight: bold;
    }
    td {
        padding: 10px;
        border-bottom: 1px solid #ddd;
    }
    tr:hover {
        background-color: #f0f0f0;
    }
</style>
"@

# Use the style in HTML
$html = $data | 
    Select-Object -First 10 Status, Project, Location, TotalActions | 
    ConvertTo-Html -Title "Construction Projects" -Head $style


# ============================================================================
# PART 5: Adding Pre/Post Content
# ============================================================================
# -PreContent: Add HTML before the table
# -PostContent: Add HTML after the table
# ============================================================================

$header = "<h1>Construction Project Report</h1><p>Generated: $(Get-Date -Format 'yyyy-MM-dd HH:mm')</p>"
$footer = "<p>Total Records: $(($data | Measure-Object).Count)</p>"

$html = $data | 
    Select-Object -First 10 Status, Project, TotalActions, OverDue | 
    ConvertTo-Html -Head $style -PreContent $header -PostContent $footer


# ============================================================================
# PART 6: Building Multi-Section Reports
# ============================================================================
# Create a report with multiple tables and sections
# Build HTML manually by combining fragments
# ============================================================================

# Section 1: Summary Statistics
$totalProjects = ($data | Measure-Object).Count
$openProjects = ($data | Where-Object {$_.Status -eq "Open"} | Measure-Object).Count
$closedProjects = ($data | Where-Object {$_.Status -eq "Closed"} | Measure-Object).Count

$summaryHtml = @"
<h2>Project Summary</h2>
<ul>
    <li><strong>Total Projects:</strong> $totalProjects</li>
    <li><strong>Open Projects:</strong> $openProjects</li>
    <li><strong>Closed Projects:</strong> $closedProjects</li>
</ul>
"@

# Section 2: Open Projects Table
$openProjectsHtml = $data | 
    Where-Object {$_.Status -eq "Open"} | 
    Select-Object -First 15 Project, Location, TotalActions, OverDue | 
    ConvertTo-Html -Fragment -PreContent "<h2>Open Projects (Top 15)</h2>"

# Section 3: Projects with Overdue Items
$overdueProjectsHtml = $data | 
    Where-Object {$_.OverDue -gt 0} | 
    Select-Object -First 15 Project, Status, TotalActions, OverDue | 
    ConvertTo-Html -Fragment -PreContent "<h2>Projects with Overdue Items</h2>"

# Combine all sections
$fullHtml = ConvertTo-Html -Head $style -Body "$summaryHtml $openProjectsHtml $overdueProjectsHtml" -Title "Construction Report"


# ============================================================================
# PART 7: Using -Fragment for Partial HTML
# ============================================================================
# -Fragment creates just the table (no <html>, <head>, <body> tags)
# Useful when combining multiple tables
# ============================================================================

# Create fragment (table only)
$table1 = $data | Select-Object -First 5 | ConvertTo-Html -Fragment

# Create complete page with fragment inside
$completePage = ConvertTo-Html -Head $style -Body $table1 -Title "Report"


# ============================================================================
# PART 8: Complete Report Example
# ============================================================================

Write-Host "`nGenerating complete HTML report..."

# CSS
$css = @"
<style>
    body { font-family: Arial; margin: 20px; background: #f9f9f9; }
    h1 { color: #2c3e50; border-bottom: 3px solid #3498db; }
    h2 { color: #34495e; margin-top: 30px; }
    table { border-collapse: collapse; width: 100%; background: white; margin: 15px 0; }
    th { background: #3498db; color: white; padding: 12px; text-align: left; }
    td { padding: 10px; border-bottom: 1px solid #ddd; }
    tr:hover { background: #ecf0f1; }
    .summary { background: white; padding: 15px; margin: 15px 0; border-left: 4px solid #3498db; }
</style>
"@

# Calculate metrics
$total = ($data | Measure-Object).Count
$open = ($data | Where-Object {$_.Status -eq "Open"} | Measure-Object).Count
$closed = ($data | Where-Object {$_.Status -eq "Closed"} | Measure-Object).Count
$openPct = [Math]::Round(($open / $total) * 100, 1)
$closedPct = [Math]::Round(($closed / $total) * 100, 1)

# Summary section
$summary = @"
<h1>Construction Project Status Report</h1>
<p><strong>Generated:</strong> $(Get-Date -Format 'MMMM dd, yyyy - HH:mm')</p>

<div class="summary">
    <h2>Overall Statistics</h2>
    <ul>
        <li>Total Projects: $total</li>
        <li>Open: $open ($openPct%)</li>
        <li>Closed: $closed ($closedPct%)</li>
    </ul>
</div>
"@

# Table 1: Open Projects
$table1 = $data | 
    Where-Object {$_.Status -eq "Open"} | 
    Select-Object -First 20 Project, Location, TotalActions, OpenActions, OverDue | 
    ConvertTo-Html -Fragment -PreContent "<h2>Open Projects (Top 20)</h2>"

# Table 2: Recently Closed
$table2 = $data | 
    Where-Object {$_.Status -eq "Closed"} | 
    Select-Object -First 10 Project, Location, TotalActions | 
    ConvertTo-Html -Fragment -PreContent "<h2>Recently Closed Projects</h2>"

# Combine
$reportHtml = ConvertTo-Html -Head $css -Body "$summary $table1 $table2" -Title "Project Report"

Write-Host "HTML report generated (stored in `$reportHtml variable)"
Write-Host "Next lesson: We'll save this to a file!"


################################################################################
# PRACTICE EXERCISES - Copy to practice.ps1 and complete
################################################################################
#
# Exercise 1: Basic HTML Table
# - Import the CSV
# - Convert first 10 records to HTML
# - Include columns: Status, Project, Location, TotalActions
# - Store in a variable and display
#
# Exercise 2: Styled HTML Report
# - Create a simple CSS style (at minimum: table border, header color)
# - Convert first 15 records to HTML with your style
# - Add a title
#
# Exercise 3: Multi-Section Report
# - Create Section 1: Summary stats (total projects, open count, closed count)
# - Create Section 2: Table of open projects (first 10)
# - Create Section 3: Table of projects with overdue items
# - Combine all sections into one HTML page
#
# Exercise 4: Custom Styling
# - Create your own CSS style
# - Include: body background, table colors, hover effects, header styling
# - Apply to a report with at least one table
#
# Exercise 5: Complete Report
# - Generate a full report with:
#   - Title and generation date
#   - Summary statistics (use calculated metrics from Lesson 5)
#   - Table 1: Open projects
#   - Table 2: Projects with overdue > 5
#   - Table 3: Status breakdown (using Group-Object)
# - Style it professionally
# - Display the HTML code
#
################################################################################

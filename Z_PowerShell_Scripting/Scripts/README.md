# PowerShell Scripts

This folder contains the PowerShell scripts for the Project Status Report Generator automation.

## Project Structure

- **Generate-ProjectReport.ps1** - Main script (to be developed)
- **test/** - Test scripts for learning PowerShell fundamentals
- **modules/** - Helper functions and modules (if needed)

## Development Progress

### Week 2: Environment Setup ✅
- PowerShell 5.1 verified
- VS Code with PowerShell extension installed
- Project folder structure created

### Week 3: PowerShell Fundamentals
- [ ] Basic syntax practice scripts
- [ ] Variables and data types
- [ ] Loops and conditionals

### Week 4: CSV Processing
- [ ] Import-Csv practice
- [ ] Data filtering and sorting

### Week 5: Metrics Calculation
- [ ] Date handling
- [ ] Status analysis functions

### Week 6: HTML Report Generation
- [ ] ConvertTo-Html implementation
- [ ] CSS styling

### Week 7: Email Automation
- [ ] Send-MailMessage configuration
- [ ] SMTP setup

### Week 8: Integration & Testing
- [ ] Complete script integration
- [ ] End-to-end testing

## Running Scripts

To run a PowerShell script:
```powershell
.\ScriptName.ps1
```

To run with parameters:
```powershell
.\Generate-ProjectReport.ps1 -CsvPath "path\to\data.csv" -EmailTo "recipient@email.com"
```

## Notes

- PowerShell execution policy may need to be set: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
- All scripts should include proper error handling
- Follow PowerShell naming conventions (Verb-Noun)

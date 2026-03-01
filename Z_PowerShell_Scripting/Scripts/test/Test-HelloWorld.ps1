# Test-HelloWorld.ps1
# Purpose: Basic PowerShell script to verify environment setup
# Week 2: Environment Setup

# Display a welcome message
Write-Host "Hello from PowerShell!" -ForegroundColor Green

# Display PowerShell version
Write-Host "`nPowerShell Version:" -ForegroundColor Cyan
$PSVersionTable.PSVersion

# Display current directory
Write-Host "`nCurrent Directory:" -ForegroundColor Cyan
Get-Location

# Display current date/time
Write-Host "`nCurrent Date/Time:" -ForegroundColor Cyan
Get-Date

Write-Host "`nEnvironment setup verified successfully!" -ForegroundColor Green

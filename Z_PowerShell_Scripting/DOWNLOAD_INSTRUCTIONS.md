# 📥 Dataset Download Instructions

**Quick Guide to Getting Your Real-World Project Data**

---

## 🎯 What You're Downloading

**Dataset:** Construction/Project Management Report Examples  
**Contains:** Real construction project task tracking data from Ireland  
**Size:** 5.75 MB (ZIP), extracts to ~2.2 MB CSV  
**Format:** CSV (Perfect for PowerShell Import-Csv)  
**License:** Educational use approved (CC BY-NC-SA 4.0)

---

## ⚡ Quick Steps (5 Minutes)

### **Step 1: Go to Kaggle**
🔗 **Click here:** https://www.kaggle.com/datasets/claytonmiller/construction-and-project-management-example-data

### **Step 2: Create Free Account** (if you don't have one)
- Click "Sign In" or "Register" (top right)
- Use your school email or personal email
- Verify your email address
- **No payment required - 100% free**

### **Step 3: Download the Dataset**
- Look for the blue "Download" button (top right of dataset page)
- Click "Download" 
- File will download as `archive.zip` or similar (5.75 MB)
- Save to your Downloads folder

### **Step 4: Extract the ZIP**
- Go to your Downloads folder
- Right-click the ZIP file
- Select "Extract All..." 
- Choose a location or just extract in place

### **Step 5: Move CSV to Your Project**
You'll see 2 CSV files. **Copy this one:**
- Construction_Data_PM_Tasks_All_Projects.csv

**Paste it here:**
- C:\ReactGitEC2\IS305 Scripting\Z_PowerShell_Scripting\Data\

### **Step 6: Verify It Worked**
Open PowerShell and run these commands:

cd "C:\ReactGitEC2\IS305 Scripting\Z_PowerShell_Scripting\Data"
Test-Path ".\Construction_Data_PM_Tasks_All_Projects.csv"

Should return: True ✅

---

## 📸 Visual Guide

### What the Kaggle Page Looks Like:
Look for "Construction/Project Management Report Examples" at the top
Click the blue "Download" button on the right side

### After Extracting:
You'll see a folder with 2 CSV files:
- Construction_Data_PM_Forms_All_Projects.csv
- Construction_Data_PM_Tasks_All_Projects.csv  ← COPY THIS ONE

### Where to Put It:
Copy the CSV file to:
C:\ReactGitEC2\IS305 Scripting\Z_PowerShell_Scripting\Data\

---

## ✅ Verification Test

After moving the file, test it in PowerShell:

```powershell
# Test 1: Check file exists
$filePath = "C:\ReactGitEC2\IS305 Scripting\Z_PowerShell_Scripting\Data\Construction_Data_PM_Tasks_All_Projects.csv"
Test-Path $filePath

# Test 2: Import the data
$tasks = Import-Csv -Path $filePath

# Test 3: Count how many tasks
Write-Host "Total tasks: $($tasks.Count)"

# Test 4: Show first task
$tasks[0]

# Test 5: List all column names
$tasks[0].PSObject.Properties.Name
```

**Expected Output:**
Test 1 - Check file exists:
$filePath = "C:\ReactGitEC2\IS305 Scripting\Z_PowerShell_Scripting\Data\Construction_Data_PM_Tasks_All_Projects.csv"
Test-Path $filePath

Test 2 - Import the data:
$tasks = Import-Csv -Path $filePath

Test 3 - Count how many tasks:
Write-Host "Total tasks: $($tasks.Count)"

Test 4 - Show first task:
$tasks[0]

Test 5 - List all column names:
$tasks[0].PSObject.Properties.Name

**Expected Output:**
- Test 1: TrueImport-Csv gives error"**
**Solution:** Check:
1. File path is correct (no typos)
2. File is actually a CSV (not still zipped)
3. You're in the right directory

### **Problem: "File is corrupted"**
**Solution:** Re-download from Kaggle. Delete the partial download first.

---

## 🎓 What You'll See in the CSV

Once you open it in Excel or import in PowerShell, expect columns like:

- **Task/Issue ID** - Unique identifier
- **Project Name** - Which construction site
- **Description** - What the task is about
- **Status** - Open, In Progress, Completed, Closed
- **Priority** - High, Medium, Low
- **Category** - Quality, Safety, Site Management
- **Assigned To** - Person responsible
- **Created Date** - When task was created
- **Due Date** - Deadline
- **Completed Date** - When it was finished (if applicable)
- **Location** - Area of the site

*(Exact column names may vary - you'll explore this in Week 4)*

---

## 📋 Checklist

Mark each step as you complete it:

- [ ] Visited Kaggle dataset page
- [ ] Created Kaggle account (or logged in)
- [ ] Downloaded ZIP file (5.75 MB)
- [ ] Extracted ZIP file
- [ ] Found `Construction_Data_PM_Tasks_All_Projects.csv`
- [ ] Copied CSV to `Data` folder in project
- [ ] Verified file with PowerShell Test-Path
- [ ] Successfully imported with Import-Csv
- [ ] Checked row count (tasks.Count)
- [ ] Viewed column names

---

## 🎯 After Download

Once you have the CSV:

1. **Document it:** Note which dataset you're using in your project progress
2. **Explore it:** Open in Excel to see the structure
3. **Don't modify it:** Keep the original data intact
4. **Tell your instructor:** Show her you have real-world data
5. **Wait for Week 4:** That's when you'll start processing it in PowerShell

---

## 📞 Need Help?

**Stuck on Kaggle account:** Email Kaggle support or ask in class  
**Can't download:** Try on different network (home vs. school)  
**File won't extract:** Download 7-Zip (free) or use Windows built-in extractor  
**Import-Csv errors:** We'll troubleshoot in Week 4 when you learn PowerShell  

---

## 🌟 You're All Set!

Once you have the CSV file in your Data folder, you're ready to:
- Show your instructor you have real data ✅
- Start designing your data model ✅
- Begin Week 3 PowerShell learning ✅
- Build an actual useful tool with real data ✅

**This is exciting!** You're working with real construction project data that actual project managers use. Your PowerShell script will be able to generate reports from genuine project tracking information!

---

**Last Updated:** January 19, 2026  
**Time Required:** 5-10 minutes  
**Difficulty:** Easy - just download and copy a file  
**Status:** Ready to begin

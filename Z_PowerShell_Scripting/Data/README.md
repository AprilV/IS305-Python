# Project Data Folder

This folder contains the CSV data files for the PowerShell Project Status Report Generator.

---

## 📥 Required Data Files

### **Primary Dataset: Construction Project Tasks**
- **Filename:** `Construction_Data_PM_Tasks_All_Projects.csv`
- **Source:** https://www.kaggle.com/datasets/claytonmiller/construction-and-project-management-example-data
- **Size:** ~2.2 MB
- **Status:** ⏳ TO BE DOWNLOADED

---

## 🚀 How to Download

1. **Visit Kaggle:**
   - Go to: https://www.kaggle.com/datasets/claytonmiller/construction-and-project-management-example-data

2. **Create Account (if needed):**
   - Free Kaggle account required
   - Use your school email or personal email

3. **Download Dataset:**
   - Click the blue "Download" button (top right)
   - File will download as a ZIP (5.75 MB)

4. **Extract Files:**
   - Unzip the downloaded file
   - You'll get 2 CSV files:
     - `Construction_Data_PM_Tasks_All_Projects.csv` ← **THIS ONE**
     - `Construction_Data_PM_Forms_All_Projects.csv`

5. **Save to This Folder:**
   - Copy `Construction_Data_PM_Tasks_All_Projects.csv` here
   - Path should be: `Z_PowerShell_Scripting\Data\Construction_Data_PM_Tasks_All_Projects.csv`

---

## 📁 Expected File Structure

```
Z_PowerShell_Scripting/
│
├── Data/
│   ├── README.md (this file)
│   └── Construction_Data_PM_Tasks_All_Projects.csv  ← Place file here
│
├── Documentation/
│   ├── DATA_SOURCES.md
│   └── DATA_MODEL_DESIGN.md
│
└── Scripts/
    └── Generate-ProjectReport.ps1 (to be created)
```

---

## ✅ Verification Checklist

After downloading, verify:
- [ ] CSV file is in this folder
- [ ] File size is approximately 2-3 MB
- [ ] File opens in Excel/Notepad
- [ ] Contains columns like: TaskID, Status, DueDate, Priority, etc.
- [ ] Has multiple rows of data (likely hundreds or thousands)

---

## 🔒 Data Privacy & License

- **License:** CC BY-NC-SA 4.0
- **Usage:** Educational purposes approved
- **Privacy:** No personal identifiable information
- **Source:** Real construction project data from Ireland
- **Attribution:** Dataset donated by Jason Rymer (BIM Manager)

---

## 🧪 Test Your Import

Once downloaded, test that PowerShell can read it:

```powershell
# Navigate to Data folder
cd "C:\ReactGitEC2\IS305 Scripting\Z_PowerShell_Scripting\Data"

# Import the CSV
$tasks = Import-Csv -Path ".\Construction_Data_PM_Tasks_All_Projects.csv"

# Check how many tasks
$tasks.Count

# View first few tasks
$tasks | Select-Object -First 5

# See what columns are available
$tasks[0] | Get-Member -MemberType NoteProperty
```

---

## 📊 Data Usage Plan

**Week 4:** Import and explore the CSV  
**Week 5:** Filter and calculate metrics  
**Week 6:** Generate HTML reports from data  
**Week 7:** Email reports  
**Week 8:** Full integration testing  

---

## 🆘 Troubleshooting

**Problem:** Can't download from Kaggle  
**Solution:** Create free Kaggle account, verify email

**Problem:** ZIP won't extract  
**Solution:** Right-click → Extract All, or use 7-Zip

**Problem:** CSV won't import in PowerShell  
**Solution:** Check file path, ensure CSV is not corrupted

**Problem:** File is too large  
**Solution:** This dataset is only 2.2 MB - should be fine

---

## 📝 Notes

- **Do NOT** commit large CSV files to Git (add to .gitignore if needed)
- Keep original filename for clarity
- Make a backup copy before testing
- Document any data cleaning steps you perform

---

**Last Updated:** January 19, 2026  
**Status:** Awaiting dataset download  
**Next Step:** Download CSV from Kaggle

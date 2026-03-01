# Real-World Data Sources for PowerShell Project

**Project:** Project Status Report Generator  
**Data Format:** CSV  
**Updated:** January 19, 2026

---

## 🎯 Recommended Data Sources

### **OPTION 1: Construction/Project Management (RECOMMENDED) ✅**
- **URL:** https://www.kaggle.com/datasets/claytonmiller/construction-and-project-management-example-data
- **Size:** 5.75 MB (2 files)
- **Real-World:** Yes - Real construction project data from Ireland
- **Files:**
  - `Construction_Data_PM_Tasks_All_Projects.csv` - Action items/tasks with quality/safety issues
  - `Construction_Data_PM_Forms_All_Projects.csv` - Checklists for quality/safety/site management
- **License:** CC BY-NC-SA 4.0
- **Downloads:** 8,198+ 
- **Why it's great:** Real project management data with tasks, status tracking, dates, priorities
- **Best for:** Learning task tracking, status analysis, deadline management

### **OPTION 2: Apache JIRA Issues (Advanced)**
- **URL:** https://www.kaggle.com/datasets/tedlozzo/apaches-jira-issues
- **Size:** 8.78 GB (4 files)
- **Real-World:** Yes - Real Apache Software Foundation issue tracking
- **Files:**
  - `issues.csv` - Issue metadata, status, priority, timestamps
  - `changelog.csv` - Historical changes (2.73 GB)
  - `comments.csv` - Discussion logs
  - `issuelinks.csv` - Issue dependencies
- **License:** Apache 2.0
- **Why it's powerful:** Industry-standard JIRA data with complete history
- **Caution:** VERY large dataset - may be overwhelming for learning project

---

## 📋 User-Provided Options

### **OPTION 3: Project Management Dataset**
- **URL:** https://www.kaggle.com/datasets/hosammhmdali/project-management-dataset
- **Type:** General project management
- **Status:** Need to verify contents and size
- **License:** To be checked

### **OPTION 4: Multilingual Customer Support Tickets**
- **URL:** https://www.kaggle.com/datasets/tobiasbueck/multilingual-customer-support-tickets
- **Size:** ~50,000 ticket entries
- **Features:** Priorities, queues, types, tags
- **Real-World:** Yes
- **Pros:** Similar workflow to project tasks (status tracking, priorities)
- **Cons:** More help-desk focused than project management

### **OPTION 5: Customer Support Ticket Dataset**
- **URL:** https://www.kaggle.com/datasets/suraj520/customer-support-ticket-dataset
- **Type:** CSV format
- **Status:** Need to verify contents

### **OPTION 6: Help Desk Tickets (Mendeley)**
- **URL:** https://data.mendeley.com/datasets/btm76zndnt/2
- **Type:** Research dataset
- **Format:** Downloadable CSV
- **Status:** Need to verify

### **OPTION 7: Montgomery County Government IT Help Desk**
- **URL:** https://catalog.data.gov/dataset/public-customer-service-operations-records-6f74b
- **Type:** Government open data
- **Real-World:** Yes - Real government IT tickets
- **Pros:** True government data, publicly accessible
- **Format:** CSV available

---

## 🎓 Recommendation for Your Project

### **Best Choice: Option 1 - Construction Project Management Data**

**Why this is perfect for you:**

1. **Real-World & Resume-Worthy:** Actual construction project data from Ireland
2. **Perfect Size:** 5.75 MB - Large enough to be meaningful, small enough to manage
3. **Proven Quality:** 8,000+ downloads, well-documented, 9.41 usability rating
4. **Ideal Structure:** Has TASKS file which aligns perfectly with your project goals
5. **Learning-Friendly:** Clean data structure, good for PowerShell beginners
6. **Project Management Focus:** Directly aligns with "Project Status Report Generator"

**Expected Data Structure (Construction_Data_PM_Tasks_All_Projects.csv):**
- Task ID
- Project Name/ID
- Task Description
- Status (Open, In Progress, Completed, etc.)
- Priority (High, Medium, Low)
- Assigned To
- Due Date
- Created Date
- Category (Quality, Safety, Site Management)

This gives you everything you need to calculate:
- ✅ Tasks by status
- ✅ Overdue tasks
- ✅ Completion percentages
- ✅ Hours/time tracking
- ✅ Priority distribution

---

## 🚀 Next Steps

1. **Download the recommended dataset:**
   - Go to: https://www.kaggle.com/datasets/claytonmiller/construction-and-project-management-example-data
   - Create free Kaggle account (if needed)
   - Click "Download" button
   - Extract CSV files

2. **Save to your project:**
   - Place CSV in: `Z_PowerShell_Scripting/Data/`
   - Keep original filename or rename to `project_tasks.csv`

3. **Explore the data:**
   - Open in Excel/Google Sheets
   - Understand column structure
   - Identify key fields for your metrics

4. **Design your data model:**
   - Map CSV columns to your needs
   - Plan which metrics to calculate
   - Determine report sections

---

## 📊 Alternative: Help Desk Data

If you prefer customer service/IT ticket data instead of construction:

**Best Option:** Montgomery County Government IT Help Desk (Option 7)
- Real government data
- Public domain
- Relevant to IT projects
- Similar structure to project tasks

**Or:** Multilingual Customer Support Tickets (Option 4)
- Large dataset (50K entries)
- Well-structured
- Good for status/priority analysis

---

## 📝 Notes

- **Kaggle Account Required:** Most datasets require free Kaggle login
- **File Storage:** Save CSV files in `/Data` folder (not tracked in git if needed)
- **Data Ethics:** All listed datasets are publicly available and properly licensed
- **Instructor Approval:** Show instructor which dataset you selected

---

## ✅ Decision Checklist

Before downloading:
- [ ] Dataset has clear task/ticket structure
- [ ] Includes status/priority fields
- [ ] Has date fields (created, due, completed)
- [ ] CSV format (PowerShell-friendly)
- [ ] Reasonable size (< 100 MB for learning)
- [ ] Properly licensed for educational use
- [ ] Real-world data (not synthetic)

---

**Last Updated:** January 19, 2026  
**Status:** Ready to download and begin data modeling

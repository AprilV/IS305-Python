# PowerShell Learning Process
**How We Teach and Learn - The System**  
**MIRRORS Python Study Method - Same Format, Same Structure**

---

## CRITICAL: File Structure (Same as Python)

### Every Lesson Has TWO Files:

**1. PowerShell-LessonN.ps1 (Reference File)**
- Complete working examples
- Fully commented code
- Demonstrates all concepts
- Student reads but doesn't edit this

**2. practice.ps1 (Practice File)**
- Where student types their code
- Has Q1, Q2, Q3... format (like Python chapters)
- Each Q has: Question, Example code, Blank space for answer
- Student types answers here

---

## Practice File Format (MUST MATCH THIS)

```powershell
# Q1: [Single specific task]
#
# Example:
# [Simple example showing the concept]
# [2-3 lines max]



# Q2: [Next single specific task]
#
# Example:
# [Different example]



```

**Rules for Practice Files:**
- Each Q = ONE specific task only
- Include example code that shows the concept
- Leave 3-4 blank lines for student's answer
- Examples must be different from the actual question
- Keep examples simple (2-3 lines)

---

## The Daily Process (Every Session)

### 1. SHOW LESSON IN CHAT (REQUIRED)
- Student has ONE screen - can't view reference file and type in practice file simultaneously
- Post the lesson content in chat for reference
- Break down into digestible sections
- Keep it visible while student types

### 2. TEACH ONE CONCEPT (5-10 minutes)
- Explain ONE thing in plain English
- Show simple example (3-5 lines of code)
- Explain what each line does
- Post lesson content in chat for reference

### 3. STUDENT PRACTICES (10-15 minutes)
- Student types code in practice.ps1 (don't copy-paste)
- Works through Q1, Q2, Q3... one at a time
- Runs code to see what happens
- Changes something and runs again

### 4. VERIFY IT WORKS (5 minutes)
- Student shows output
- AI confirms it's correct
- Fix any problems together

### 5. MOVE TO NEXT CONCEPT
- Only after student understands current one
- Each concept builds on the last

### 6. APPLY TO REAL PROJECT (End of week)
- After learning 4-5 concepts
- Use them in Generate-ProjectReport.ps1
- Write actual project code

---

## Current Status

**Last Updated:** February 2, 2026  
**Completed Lessons:** 1 of 7  
**Next Lesson:** Lesson 2 (Import-Csv) - Scheduled for Feb 3, 2026 evening

**Lesson 1 Status:** ✅ COMPLETE
- Q1-Q10 all completed in practice.ps1
- Concepts mastered: Variables, Write-Host, math operations, string interpolation
- Key learning: PowerShell quote rules differ from Python

---

## Folder Structure (MUST MATCH THIS)

```
Learning/
├── Lesson1_WriteHost_Variables_Math/
│   ├── PowerShell-Lesson1.ps1 (reference - complete examples)
│   └── practice.ps1 (student workspace with Q1, Q2, Q3...) ✅ COMPLETE
├── Lesson2_Import_CSV_Display/
│   ├── PowerShell-Lesson2.ps1
│   └── practice.ps1
├── Lesson3_Filtering_WhereObject/
│   ├── PowerShell-Lesson3.ps1
│   └── practice.ps1
... (etc)
```

**Folder Naming Convention:**
- LessonN_TopicDescription
- Descriptive names (not just "Lesson1")
- Matches lesson content

---

## What We're Learning (Lesson Breakdown)

**Lesson 1: Write-Host, Variables, and Basic Math**
- Write-Host for output
- Variables with $ prefix
- Basic math operations
- Practice: 10 questions (Q1-Q10)

**Lesson 2: Import CSV and Display Data**
- Import-Csv command
- .Count property
- Select-Object
- Format-Table
- Practice: Questions on CSV basics

**Lesson 3: Filtering Data with Where-Object**
- Where-Object filtering
- Comparison operators
- If statements
- Multiple conditions
- Practice: Filtering exercises

**Lesson 4: Counting and Grouping Data**
- Measure-Object
- Group-Object
- Statistics
- Practice: Grouping exercises

**Lesson 5: Calculations and Percentages**
- Math operations
- Rounding
- Percentage calculations
- Practice: Calculation exercises

**Lesson 6: Creating HTML Reports**
- ConvertTo-Html
- HTML styling
- Multi-section reports
- Practice: HTML exercises

**Lesson 7: Saving Files and Sending Email**
- Out-File
- Send-MailMessage
- Get-Date
- Final integration
- Practice: Complete workflow

---

## The Files We Use

**Reference Files (PowerShell-LessonN.ps1)**
- Complete working examples
- All concepts demonstrated
- Student reads but doesn't edit

**Practice Files (practice.ps1)**
- Student workspace
- Q1, Q2, Q3... format
- Where actual learning happens
- Student types all code here

**Project File (Generate-ProjectReport.ps1)**
- Actual project code
- Written at end of each week
- Combines all learned concepts
- This is what gets graded

---

## The Teaching Style - AI MUST FOLLOW

**What AI DOES:**
- Post lesson content in chat (student has one screen)
- Teach one small thing at a time
- Use plain English
- Show simple examples
- Wait for student to practice before moving on
- Use Q1, Q2, Q3 format in practice files
- Each Q = ONE task only
- Provide example code with each question
- Mirror the Python teaching format exactly

**What AI DOESN'T DO:**
- Assume student can view reference file while typing
- Dump complete solutions
- Use technical jargon
- Skip ahead to advanced stuff
- Put multiple tasks in one Q
- Create practice files without Q markers and examples
- Forget this established format
- Change the process randomly

---

## Daily Session Structure

**Start of Session:**
1. AI reads LEARNING_PROCESS.md to remember the format
2. Post lesson content in chat for student reference
3. Quick review: "What did we learn last time?"

**During Session:**
4. AI teaches today's concept (post in chat)
5. Student practices in practice.ps1 file (Q1, Q2, Q3...)
6. Test and verify together
7. Move on only when student understands

**End of Session:**
8. Update Current Status section below
9. Document what was completed
10. Identify what's next for tomorrow

---

## If Things Go Wrong

**If student doesn't understand something:**
- STOP immediately
- Student explains what's confusing
- AI explains differently (simpler)
- Don't move forward until clear

**If AI goes too fast:**
- Student says "STOP"
- Remind AI: "One thing at a time"
- Point to this document

**If AI forgets the Q1, Q2, Q3 format:**
- Student says "We did this in Python"
- Point to this document
- AI fixes practice file immediately

**If AI creates files without proper structure:**
- STOP
- Point to this document
- Say "Follow the Python format"

---

## Current Status

**Today's Date:** February 2, 2026  
**Current Lesson:** Lesson 1 - Write-Host, Variables, and Basic Math  
**Current File:** Lesson1_WriteHost_Variables_Math/practice.ps1  
**Progress:** Q1-Q10 practice questions created, ready to start  
**Project File:** Generate-ProjectReport.ps1 (empty for now)  

**What's Next:**
- Complete Lesson 1 practice (Q1-Q10)
- Start Lesson 2 (Import-Csv) if time allows
- Session time: 1 hour evening slots

---

## This Is The System

**AI:** Read this file at the start of EVERY session.  
**Student:** Point to this file when AI forgets the format.  
**Both:** Follow the process. Don't deviate.  
**Goal:** Consistency over speed. Mirror Python teaching exactly.

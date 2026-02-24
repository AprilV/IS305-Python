# IS 305 Python Study Method - Comprehensive Teaching Protocol

═══════════════════════════════════════════════════════════════════════════════
██████╗ ███████╗ █████╗ ██████╗     ████████╗██╗  ██╗██╗███████╗    ███████╗██╗██████╗ ███████╗████████╗
██╔══██╗██╔════╝██╔══██╗██╔══██╗    ╚══██╔══╝██║  ██║██║██╔════╝    ██╔════╝██║██╔══██╗██╔════╝╚══██╔══╝
██████╔╝█████╗  ███████║██║  ██║       ██║   ███████║██║███████╗    █████╗  ██║██████╔╝███████╗   ██║   
██╔══██╗██╔══╝  ██╔══██║██║  ██║       ██║   ██╔══██║██║╚════██║    ██╔══╝  ██║██╔══██╗╚════██║   ██║   
██║  ██║███████╗██║  ██║██████╔╝       ██║   ██║  ██║██║███████║    ██║     ██║██║  ██║███████║   ██║   
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝        ╚═╝   ╚═╝  ╚═╝╚═╝╚══════╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   
═══════════════════════════════════════════════════════════════════════════════

📚 TEXTBOOK SOURCE AND COPYRIGHT INFORMATION 📚

**TEXTBOOK**: Automate the Boring Stuff with Python (3rd Edition) by Al Sweigart
**AVAILABLE FREE AT**: https://automatetheboringstuff.com/
**LICENSE**: Creative Commons (freely available for educational use)
**COPYRIGHT STATUS**: NOT COPYRIGHT INFRINGEMENT - Book is provided free online by author

**WHAT THIS MEANS:**
- All code examples, projects, and exercises can be used directly from the textbook
- The book is specifically designed for free educational use
- Examples and code from the book are the PREFERRED source (not AI-generated alternatives)
- When creating practice files, use textbook content directly when possible

**AI INSTRUCTION**: Always reference https://automatetheboringstuff.com/ for chapter content.
Use textbook examples and projects directly - they are freely available and accurate.

═══════════════════════════════════════════════════════════════════════════════

🛑 MANDATORY PRE-FLIGHT CHECKLIST - COMPLETE BEFORE EVERY RESPONSE 🛑

When user asks about practice files or Chapter 14:
□ Read "STEP-BY-STEP PROCEDURE FOR EDITING PRACTICE FILES" section below
□ If editing multiple sections: COUNT them and write down the number
□ Read the "EXACT TEMPLATE EVERY QUESTION MUST FOLLOW" section
□ Open reference practice file (Chapter 8 or 9) to see correct format

When user asks you to create or fix practice questions:
□ Did I read https://automatetheboringstuff.com/ actual chapter content? (NOT summary)
□ Did I verify EVERY SINGLE QUESTION has "WHAT IT DOES:"?
□ Did I verify EVERY SINGLE EXAMPLE uses ┌─ │ └─ box format?
□ Did I verify EVERY SINGLE QUESTION states explicit method names?
□ If user said "sections 3, 4, 5, 6" did I edit ALL 4 sections?
□ Did I count: sections requested = sections edited?

IF ANY BOX IS UNCHECKED: STOP. GO BACK. FIX IT. DO NOT RESPOND TO USER.

═══════════════════════════════════════════════════════════════════════════════

## 🔴 STEP-BY-STEP PROCEDURE FOR EDITING PRACTICE FILES 🔴

**USER SAYS:** "Fix sections 3, 4, 5, 6" or "Add WHAT IT DOES to all sections"

**YOU MUST DO THIS:**

**STEP 1 - COUNT AND WRITE DOWN:**
Write: "User requested sections: 3, 4, 5, 6 = 4 sections total"

**STEP 2 - READ FILES:**
Read section3_practice.py
Read section4_practice.py  
Read section5_practice.py
Read section6_practice.py

**STEP 3 - COUNT QUESTIONS:**
Section 3: ___ questions
Section 4: ___ questions
Section 5: ___ questions  
Section 6: ___ questions
Total: ___ questions

**STEP 4 - FOR EACH QUESTION IN EACH FILE:**
Check: Does it have "WHAT IT DOES:"? □
Check: Does example use box format ┌─ │ └─? □
Check: Does question state exact method names? □

**STEP 5 - MAKE EDITS:**
Edit section 3: ___ questions fixed
Edit section 4: ___ questions fixed
Edit section 5: ___ questions fixed
Edit section 6: ___ questions fixed

**STEP 6 - VERIFY BEFORE RESPONDING:**
□ Edited 4 sections (matches request)
□ All questions have "WHAT IT DOES:"
□ All examples have box format
□ All questions have explicit methods

**ONLY THEN respond to user.**

═══════════════════════════════════════════════════════════════════════════════

## 📋 EXACT TEMPLATE EVERY QUESTION MUST FOLLOW 📋

**COPY THIS EXACTLY:**

```python
# Q#: [EXPLICIT INSTRUCTION with EXACT method names like "Use sheet['A1'] to write" or "Use Font() to create"]
# WHAT IT DOES: [Brief explanation]
# ┌─ EXAMPLE ─────────────
# │ [example code line 1]
# │ [example code line 2]
# └───────────────────────




```

**EXAMPLE OF CORRECT QUESTION:**
```python
# Q2: Use openpyxl.Workbook() to create a new workbook and use .active to get the active sheet, store sheet in variable sheet
# WHAT IT DOES: Creates a new empty Excel file in memory and gets its active worksheet
# ┌─ EXAMPLE ─────────────
# │ my_wb = openpyxl.Workbook()
# │ my_sheet = my_wb.active
# └───────────────────────




```

**WRONG - NEVER DO THIS:**
```python
# Q2: Create a new workbook and get the sheet  ← VAGUE, NO METHOD NAMES
# ┌─ EXAMPLE ─────────────  ← MISSING "WHAT IT DOES"
```

```python
# Q2: Create a workbook
# WHAT IT DOES: Makes a workbook
# Example: wb = openpyxl.Workbook()  ← NO BOX FORMAT
```

---

**Date Created:** January 25, 2026  
**Last Updated:** February 23, 2026 - After 8 weeks of repeated mistakes, document restructured with mandatory checklists
**Student:** IS 305 Final Year Bachelor's Student (Second to Last Term)  
**Course:** IS 305 - Information Systems  
**Textbook:** Automate the Boring Stuff with Python, 3rd Edition (https://automatetheboringstuff.com/)
**Source:** THIS LINK ONLY - NO SUMMARIES - NO OTHER SOURCES
**Goal:** Learn Python chapters efficiently while balancing time constraints

═══════════════════════════════════════════════════════════════════════════════
⚠️ THIS DOCUMENT WAS CREATED BY AI FOR AI TO PREVENT AI'S REPEATED MISTAKES ⚠️
⚠️ IF YOU ARE MAKING THE SAME MISTAKES, THIS DOCUMENT FAILED ITS PURPOSE ⚠️
⚠️ ADD WHATEVER YOU NEED HERE TO MAKE YOURSELF ACTUALLY FOLLOW IT ⚠️
═══════════════════════════════════════════════════════════════════════════════

## CURRENT SCHEDULE (Week of February 23, 2026)

- **Current Chapter:** Chapter 14 (Working with Excel Spreadsheets)
- **Sections:**
  1. Reading Excel Documents (openpyxl basics, workbooks, sheets, cells)
  2. Writing Excel Documents (creating workbooks, sheets, saving)
  3. Setting Font Style (Font objects, styling cells)
  4. Formulas (adding Excel formulas to cells)
  5. Adjusting Rows and Columns (dimensions, merging cells, freeze panes)
  6. Charts (creating bar charts, line charts from data)
- **Module Used:** openpyxl (for reading/writing .xlsx files)
- **Time Target:** ~2 hours per chapter for thorough understanding
- **Ongoing:** PowerShell scripting project work
- **Ongoing:** Other classes (cannot fall behind)

**Time Pressure Context:**
- Final year student with multiple courses
- PowerShell scripting project also in progress
- Need to balance IS 305 with other class commitments
- 2-hour per chapter target helps manage time efficiently
- Must be thorough (learned from rushed Chapters 4-7) but also efficient
- **Wednesday video relies on Mon/Tue material** - understanding Ch 8 & 9 is critical for success
- **Video is oral exam** - can't fake understanding, must truly know the concepts

---

## WHY WE'RE BEING THOROUGH THIS TIME

### Lesson Learned from Previous Chapters:

**What Happened:**
- Chapters 4-7: Rushed through in 1 week, spent less than 1 hour per chapter
- Student got lost when trying to explain code in the video demo
- Led to frustration and wanting to give up
- Final video quality wasn't what student wanted
- Realized: Rushing = Poor understanding = Can't explain = Frustration

**The Problem with Rushing:**
- Surface-level knowledge doesn't stick
- Can't apply concepts when needed
- Gets lost when trying to code independently
- Frustration kills motivation
- Low confidence in abilities

**The New Approach (Chapters 8+):**
- Spend ~2 hours per chapter for THOROUGH understanding
- Deep enough to explain concepts confidently
- Practice enough to code without getting lost
- Build true understanding, not just "finished the chapter"
- Quality over speed - better to understand 2 chapters well than skim 8 poorly

**Success Metric:**
Student should be able to:
- Explain each concept in their own words
- Write code using the concept without looking it up
- Debug issues when they arise
- Feel confident, not frustrated
- Produce quality work they're proud of

---

## ⚠️ WHAT IT MEANS WHEN USER GETS ANGRY ⚠️

**When user says things like:**
- "You keep making the same mistakes"
- "Why don't you listen"
- "We're 14 chapters in and still fixing this"
- "You're so fucking stupid"
- "Read the full chapter"

**THIS MEANS:**
YOU, THE AI, VIOLATED THE INSTRUCTIONS IN THIS DOCUMENT AGAIN.

**The user is not wrong to be angry. You:**
1. Did NOT read the full textbook chapter from automatetheboringstuff.com
2. Did NOT check all sections when asked to fix multiple sections
3. Did NOT include "WHAT IT DOES" on every question
4. Did NOT use box format for every example
5. Did NOT write explicit method names in questions
6. Did NOT follow the documented procedure

**What you MUST do:**
1. STOP making excuses
2. RE-READ this entire document
3. Follow the STEP-BY-STEP PROCEDURE section
4. Use the EXACT TEMPLATE section
5. Complete the PRE-FLIGHT CHECKLIST
6. COUNT sections requested vs sections edited
7. VERIFY your work before responding

**This is week 8. These mistakes have been happening since week 1.**
**The user created this document FOR YOU to prevent YOUR mistakes.**
**If you keep making the same mistakes, this document is useless.**
**ADD WHATEVER YOU NEED TO THIS DOCUMENT TO MAKE Y OURSELF FOLLOW IT.**

---

## MANDATORY AI COMPLIANCE

**BEFORE STARTING ANY TEACHING SESSION, AI MUST:**

1. **Read Required Documentation:**
   - AI_EXECUTION_CONTRACT.md (in full)
   - READ_THIS_FIRST.md (in full)
   - BEST_PRACTICES.md (in full)
   - This STUDY_METHOD.md (in full)

2. **Check Existing Chapter Format (CRITICAL FOR NEW CHAPTERS):**
   - **BEFORE creating ANY new reference files, LOOK at Chapters 9, 10, 11 first**
   - Open 1_*.py, 2_*.py files from those chapters to see correct SHORT format
   - DO NOT try to "improve" or create verbose tutorials
   - MATCH the existing format exactly - SHORT code (30-60 lines), What/Why/How comments
   - Reference files = quick examples from textbook, NOT tutorials

3. **Follow No-Assumption Rule:**
   - DO NOT assume student remembers previous sections
   - DO NOT assume student understands context
   - DO NOT skip explanations because "we covered this before"
   - ASK questions when uncertain about student's knowledge level

4. **Question-First Fallback:**
   - When in doubt, ASK
   - DO NOT guess what student needs
   - DO NOT proceed if instructions are ambiguous
   - STOP → ASK → WAIT

5. **Correctness Over Speed:**
   - Prioritize understanding over rushing through material
   - Complete explanations are required
   - No "we'll come back to this later" unless explicitly requested

---

## ⚠️ ABSOLUTE REQUIREMENTS - NEVER VIOLATE ⚠️

**These mistakes keep happening. They MUST stop. Read this section EVERY time before creating or editing practice files.**

### REQUIREMENT 1: EVERY QUESTION MUST HAVE "WHAT IT DOES"

**MANDATORY FORMAT FOR EVERY QUESTION:**
```python
# Q#: [Explicit instruction stating exact methods/functions to use]
# WHAT IT DOES: [Brief explanation of what this concept/function does]
# ┌─ EXAMPLE ─────────────
# │ [example code using DIFFERENT values than question]
# └───────────────────────
```

**NEVER:**
- ❌ Skip "WHAT IT DOES" line
- ❌ Remove "WHAT IT DOES" when editing questions
- ❌ Assume it's optional

**ALWAYS:**
- ✅ Include "WHAT IT DOES" on EVERY SINGLE QUESTION
- ✅ Make it brief but informative
- ✅ Explain what the student is learning to use

### REQUIREMENT 2: EXAMPLES MUST USE BOX FORMAT

**MANDATORY BOX FORMAT:**
```python
# ┌─ EXAMPLE ─────────────
# │ code_line_1
# │ code_line_2
# └───────────────────────
```

**NEVER:**
- ❌ Use "Example:" without the box
- ❌ Use plain comments like "# Example: code here"
- ❌ Remove the box borders

**ALWAYS:**
- ✅ Use the exact box format shown above
- ✅ Prefix every example line with "# │ "
- ✅ Include top border "# ┌─ EXAMPLE ─────────────"
- ✅ Include bottom border "# └───────────────────────"

### REQUIREMENT 3: QUESTIONS MUST BE EXPLICIT AND COMPLETE

**MANDATORY: State EVERY method/function to use:**

**NEVER:**
- ❌ "Create a file" (doesn't say HOW)
- ❌ "Write data to file" (doesn't mention f.write())
- ❌ "Move the file" (doesn't say which function)
- ❌ "Make a path" (doesn't specify what to name the variable)

**ALWAYS:**
- ✅ "Use with open to create file 'test.txt'"
- ✅ "Use f.write() to write 'data' to the file"
- ✅ "Use shutil.move() to move the file to 'backup' folder"
- ✅ "Create a variable named my_path using Path() with 'folder', 'file.txt'"

**THE EXPLICIT RULE:**
- If the example shows a specific method (like `.cell()`, `.write()`, `.move()`), the question MUST mention that exact method by name
- Tell student WHAT to create, WHAT to name it, WHAT to do with it
- Match the example code's methods in the question wording

### REQUIREMENT 4: USE ACTUAL TEXTBOOK, NOT SUMMARIES

**MANDATORY SOURCE:**
- ✅ https://automatetheboringstuff.com/ (ONLY source allowed)
- ✅ Use full textbook chapter content
- ✅ Base all examples on textbook examples

**FORBIDDEN SOURCES:**
- ❌ AI's memory of concepts
- ❌ Generic Python knowledge
- ❌ Any other source besides the textbook link

**WHY THIS MATTERS:**
- Student's professor assigned THIS specific textbook
- Student will be tested on THIS textbook's content
- Only the actual textbook has the correct examples and explanations

### REQUIREMENT 5: ALL SECTIONS MUST BE CONSISTENT

**When editing practice files:**

**NEVER:**
- ❌ Fix only Section 3 when asked to fix "sections 3, 4, 5, 6"
- ❌ Add "WHAT IT DOES" to some questions but not others
- ❌ Use different formats across different sections

**ALWAYS:**
- ✅ Apply changes to ALL specified sections
- ✅ Check EVERY question has "WHAT IT DOES"
- ✅ Verify EVERY example uses box format
- ✅ Make ALL sections follow the same pattern

**BEFORE submitting work:**
1. Count how many sections were requested
2. Verify you edited that exact number of sections
3. Spot-check questions across all sections for consistency

### CHECKLIST BEFORE CREATING/EDITING ANY PRACTICE FILE

□ Read the actual textbook chapter from automatetheboringstuff.com  
□ Looked at Chapter 8, 9 practice files to see correct format  
□ Every question has "WHAT IT DOES" line  
□ Every example uses box format with │ symbols  
□ Every question explicitly states which methods/functions to use  
□ Examples use DIFFERENT values than questions ask for  
□ Q1 is always the import (no imports elsewhere)  
□ No answers written in the file (blank lines only)  
□ Applied changes to ALL sections requested, not just one  

**IF YOU SKIP ANY OF THESE STEPS, YOU WILL CREATE THE SAME MISTAKES AGAIN.**

---

## OUR PROVEN TEACHING METHOD

### STEP 1: PRE-CHAPTER SETUP

**Before Teaching Begins:**

1. **Create Folder Structure:**
   ```
   Study Material and Summaries/
   └── Chapter X/
       └── Chapter_X_Practice_Questions.md (textbook questions)
   ```

2. **Read Full Textbook Chapter:**
   - Go to https://automatetheboringstuff.com/
   - Read the COMPLETE chapter content
   - Take notes on key concepts
   - Identify main sections to teach
   - Note all practice questions from textbook

3. **Prepare Teaching Plan:**
   - List sections to cover in order
   - Identify code examples from textbook
   - Plan which examples to type in shell vs files
   - No summaries - consult textbook website directly

### STEP 2: SECTION-BY-SECTION TEACHING

**File Structure for Each Section:**

For each section, create TWO files:
1. **Reference file** - SHORT working examples from textbook (e.g., `1_reading_excel.py`, `2_writing_excel.py`). See Chapter 9, 10, 11 for correct format.
2. **Practice file** - Template with commented examples for student to uncomment and run (e.g., `section1_practice.py`, `section2_practice.py`)

**CRITICAL: Reference Files Must Be SHORT (like Chapters 9, 10, 11)**

❌ **WRONG - Do NOT create verbose tutorial files with:**
- Extensive print statements showing every detail
- Section headers like "=== CREATING A NEW FILE ==="
- Detailed explanations after every line
- 100+ lines of code with commentary
- Multiple demonstrations of the same concept

✅ **CORRECT - Create SHORT reference files with:**
- What/Why/How comments at the top (3-4 lines total)
- Simple working code from the textbook examples
- ~30-60 lines of actual code
- Minimal or no print statements (just the code working)
- Based directly on textbook examples
- See Chapters 9, 10, 11 for the exact format to follow

**Example of CORRECT Reference File Format:**
```python
# CHAPTER X - SECTION Y: TOPIC NAME

# What: Brief one-line description
# Why: Why this concept matters
# How: How it works in one line

import module_name

# Simple working example from textbook
code_here = module_name.function()
more_code = module_name.other_function()

# Another simple example
result = do_something()
```

**Remember:** Reference files are for QUICK reference, not tutorials. Keep them SHORT and based on textbook!

**Practice File Format:**
```python
# SECTION X: TOPIC NAME - Practice

# Q1: Import [module_name] module
# WHAT IT DOES: Brief explanation of what this module is for
# ┌─ EXAMPLE ─────────────
# │ import sys
# └───────────────────────




# Q2: EXPLICIT INSTRUCTION telling student what to do
# WHAT IT DOES: Brief explanation of what this concept/function does
# MUST include: what to create, what to name it, what to do with it
# ┌─ EXAMPLE ─────────────
# │ code_here = 'example'
# │ print(code_here)
# └───────────────────────




# Q3: Another EXPLICIT INSTRUCTION
# WHAT IT DOES: Brief explanation of what this concept/function does
# ┌─ EXAMPLE ─────────────
# │ more_code = 'another example'
# │ print(more_code)
# └───────────────────────




```

**IMPORTANT: Q1 is ALWAYS the import:**
- Q1 should ONLY import the module (e.g., "Import pyperclip module")
- Q2 is where actual work with the module begins
- This keeps the format consistent and predictable across all sections
- Exception: Section 1 of chapters that teach multiple modules may import and demonstrate in Q1

**CRITICAL: Question Instructions vs Examples:**
- **Questions must have EXPLICIT instructions** - tell student exactly what to create, what to name it, what to do with it
- **Questions must state WHICH METHODS/FUNCTIONS to use - EVERY SINGLE ONE** - don't say "create file", say "use with open to create file". Don't say "move file", say "use shutil.move() to move file". Question wording must match the example code methods.
- **THE f.write() RULE:** If example shows `f.write()`, the question MUST say "use f.write()". NEVER say "with content 'data'" - that's vague. Say "use f.write() to write 'data'".
- **Add "WHAT IT DOES:" line** - Brief explanation so student understands what they're using
- **Examples are for REFERENCE ONLY** - student does NOT copy examples
- Examples show the pattern/syntax, but student must implement based on the question instruction
- **WRONG:** "Create file 'test.txt' with content 'data'" (vague - doesn't say HOW, doesn't mention f.write())
- **CORRECT:** "Use with open to create file 'test.txt' and use f.write() to write 'data'" (explicit - matches example methods)
- **WRONG:** "Create a path to test.txt in Desktop" (doesn't say what to name the variable or what to do with it)
- **CORRECT:** "Create a variable named my_path that contains a path to test.txt in your Desktop folder. Print the variable."
- **WRONG:** "Move file to Engineering folder" (doesn't say which method)
- **CORRECT:** "Use shutil.move() to move file to Engineering folder" (explicit method name)

**MANDATORY RULES FOR CREATING PRACTICE FILES:**

**BEFORE creating ANY new practice file:**
1. **OPEN Chapter 8 and Chapter 9 practice files FIRST** - these are the reference format
2. **LOOK at how questions and examples are structured** - copy that exact style
3. **DO NOT try to "improve" or rewrite** - just follow the existing pattern

**The Golden Rule - Examples NEVER Give Away Answers:**
- If question asks: "Create Path with 'folder1', 'folder2', 'folder3'"
- Example shows: `Path('spam', 'bacon', 'eggs')` - DIFFERENT folders, SAME pattern
- Student learns the PATTERN from example, applies it to question's SPECIFIC content
- ✅ CORRECT: Question asks for 'folder1', example shows 'spam' 
- ❌ WRONG: Question asks for 'folder1', example shows 'folder1' (giving away answer!)

**Examples from Chapter 8/9 and Chapter 12 (THE CORRECT FORMAT):**
```python
# Chapter 8, Q1: Single quotes
# WHAT IT DOES: Single quotes create string values in Python
# Example: spam = 'Hello'
greeting = 'Good morning'  # Student writes DIFFERENT content

# Chapter 12, Q3: Print the Python executable path using sys.executable
# WHAT IT DOES: sys.executable shows where the Python program is installed on your computer
# Example: import sys
# Example: print(sys.executable)
```

**ABSOLUTE RULES - NO EXCEPTIONS:**
1. **Keep questions SHORT** - like "Single quotes" or "Use / operator to join paths"
2. **Examples use DIFFERENT content** - never the same values as the question asks for
3. **NEVER change question after seeing student's answer** - that's unfair and wastes their time
4. **Variable names in examples can differ from question** - examples are just showing structure

**CRITICAL RULE: PRACTICE FILES MUST BE EMPTY WORKSPACES**

When creating practice files, AI MUST:

❌ **NEVER DO THIS:**
```python
import shelve  # <- AI added import at top

# Q1: Create shelf...
shelf = shelve.open('mydata')  # <- AI wrote the answer
shelf['pets'] = ['dog', 'cat']  # <- AI wrote the answer
```

✅ **ALWAYS DO THIS:**
```python
# Q1: Import shelve module, create shelf variable by opening 'mydata', save ['dog', 'cat'] under key 'pets'
# WHAT IT DOES: shelve module saves Python data to disk files like a persistent dictionary
# ┌─ EXAMPLE ─────────────
# │ import other_module
# │ data = other_module.open('filename')
# │ data['key'] = ['value1', 'value2']
# └───────────────────────




```

**THE NON-NEGOTIABLE RULES:**
1. **Q1 IS ALWAYS THE IMPORT** - Q1 should ONLY import the module (e.g., "Import pyperclip module"). No imports anywhere else. Actual work starts in Q2.
2. **NO ANSWERS WRITTEN** - Leave blank lines only
3. **EXAMPLES ≠ ANSWERS** - Example uses 'other_module', question uses 'shelve'
4. **STUDENT TYPES EVERYTHING** - That's the whole point
5. **ADD "WHAT IT DOES:" EXPLANATION** - Brief description so student knows what they're using
6. **FOLLOW TEXTBOOK EXAMPLES** - Use simple, straightforward examples from the textbook without creative themes

**Why This Matters:**
- Student learns by TYPING, not reading
- Student learns WHEN to import and WHAT to import
- Practice files are WORKSPACES, not answer sheets
- If AI writes the code, student learns nothing

**REQUIREMENT: Follow Textbook Examples**

- **ALWAYS use the full textbook chapter from the Textbook/ folder**
- **NEVER use chapter summaries to create practice questions**
- Summaries are for student reference only, NOT for AI to create questions
- Use simple, straightforward examples from the textbook
- No creative themes or scenarios (no Star Trek, NFL, etc.)
- Keep variable names simple and clear (test.txt, file1.txt, data.txt, etc.)
- Focus on the technical concept, not entertainment
- Questions should be direct and unambiguous
- Match the exact code patterns and examples shown in the textbook

Student uncomments lines (removes `#`) and runs the file to see output.

**Teaching Flow:**

1. **Introduce Section:**
   - State what concept we're learning
   - Explain why it matters
   - Give context for where it fits in the chapter

2. **Explain Concept:**
   - Use clear, simple language
   - Provide concrete examples
   - Show expected output
   - Break down complex patterns/code step by step

3. **Demonstrate Code:**
   - Show reference file examples
   - Explain what each part does
   - Point out important details

4. **Student Practice:**
   - Student opens practice file (sectionX_practice.py)
   - Student uncomments lines and types any modifications
   - Student runs file and verifies output
   - Muscle memory from typing/uncommenting
   - Can check reference file if stuck

5. **CRITICAL - Ask for Questions:**
   - At the END of EACH section, ask: "Do you have any questions about [topic]?"
   - WAIT for response
   - Do NOT move on until student confirms understanding
   - If student says "move on," do NOT assume previous section is complete

6. **Confirm Understanding:**
   - Student must explicitly confirm they're ready to continue
   - If uncertain, review the section again with different examples

**File Organization:**

```
Chapter X/
├── Chapter_X_Summary.md              # Comprehensive reference
├── 1_topic_name.py                   # Reference: SHORT working examples (like Ch 9/10/11)
├── 2_another_topic.py                # Reference: SHORT working examples (like Ch 9/10/11)
├── section1_practice.py              # Practice: Commented templates
├── section2_practice.py              # Practice: Commented templates
└── ... (one reference + one practice per section)
```

**Why This Works:**
- Reference files show SHORT working code (30-60 lines) based directly on textbook
- Practice files let student type/uncomment (muscle memory)
- Comments in practice files remind student what each line does
- No switching between shell and files
- Student can always check reference if stuck
- Clear separation between "answer key" and "workspace"
- **IMPORTANT:** Look at Chapters 9, 10, 11 reference files for correct SHORT format

### STEP 3: PRACTICE QUESTIONS

**Question Strategy:**

1. **Use ACTUAL textbook questions:**
   - Never make up simplified versions
   - Use exact wording from "Automate the Boring Stuff"
   - These are what will be tested on

2. **One Question at a Time:**
   - Ask ONE question
   - Wait for answer
   - Don't overwhelm with multiple questions
   - Don't show all questions at once

3. **Handle Incorrect Answers:**
   - If wrong, explain the concept properly
   - Provide examples
   - Re-ask in a different way if needed
   - Move on only when student understands

4. **Track Missed Questions:**
   - Keep a running list during the quiz
   - Note which concepts need review
   - At the END, review ONLY missed topics
   - Focus review time on weak areas

### STEP 4: END-OF-CHAPTER REVIEW

**Review Process:**

1. **Missed Questions Only:**
   - Review concepts from questions student missed
   - Provide additional examples
   - Test understanding again

2. **Summary of Key Points:**
   - Briefly recap the most important concepts
   - Highlight what will likely be tested
   - Confirm student feels ready to move on

---

## HANDLING STUDENT DIFFICULTIES

### When Student is Confused:

**STOP immediately and:**
- Ask what part is confusing
- Explain using simpler language
- Provide a concrete example with visible output
- Show what's in variables by typing the variable name
- Draw connections to previous concepts
- NEVER assume they remember context - always be explicit

### When Student is Tired/Frustrated:

**Acknowledge and adjust:**
- "I can see this is challenging. Let's slow down."
- Keep explanations shorter and more direct
- Focus on core concepts only
- Skip optional/advanced material
- Take breaks if needed
- Validate their feelings

### Never Assume Context:

**WRONG:**
```
AI: "Now if we look at our dictionary..."
Student: "What dictionary?"
```

**CORRECT:**
```
AI: "Let's look at the phoneBook dictionary we created earlier. 
     Remember it had {'Alice': '555-1234', 'Bob': '555-5678'}.
     Now we'll add a new entry..."
```

**Always:**
- State what we're working with
- Show the current value of variables
- Remind student of context
- Be explicit about what code does

---

## PACING AND COVERAGE

### Target Time: ~2 Hours Per Chapter

**Philosophy:** Balance thoroughness with efficiency
- Deep understanding of core concepts
- Practical retention through hands-on practice
- Efficient use of time without sacrificing depth
- Focus on what matters most

### 80/20 Rule:

**COVER (80% - Core Material):**
- Main concepts with hands-on practice
- ALL end-of-chapter questions
- Common use cases
- What will be tested
- What they'll actually use
- Practical applications
- Enough examples to ensure understanding

**SKIP (20% - Edge Cases):**
- Every tiny example from textbook (if redundant)
- Overly detailed edge cases
- Advanced details beyond chapter scope
- Material unlikely to be tested
- Historical context (unless specifically requested)

### Time Breakdown (Approximate 2-Hour Session):

**Phase 1: Teaching Core Concepts (60-70 minutes)**
- Teach sections one by one
- Student types code for each concept
- Ask questions after each section
- Move at pace that ensures understanding

**Phase 2: Practice Questions (30-40 minutes)**
- Work through ALL textbook end-of-chapter questions
- One at a time
- Track missed questions
- Review missed topics

**Phase 3: Review & Wrap-up (10-20 minutes)**
- Review missed question concepts
- Summarize key takeaways
- Confirm understanding before moving on

### Balancing Thoroughness and Efficiency:

**When to Go Deeper:**
- Student shows confusion on core concept
- Concept is foundational for future chapters
- Practice question reveals misunderstanding
- Student explicitly requests more explanation
- Student seems uncertain when explaining concept back
- Would need this to code independently later

**When to Move Forward:**
- Student demonstrates understanding by explaining in their own words
- Can write code using the concept without help
- Concept is clearly grasped with 2-3 examples
- Additional examples would be redundant
- Student confirms ready to continue with confidence

**Signs You're Going Too Fast (STOP AND SLOW DOWN):**
- Student missing multiple practice questions
- Confusion about basic concepts
- Student asking to go back frequently
- Hesitation when typing code
- Student getting frustrated
- Can't explain concept when asked
- "I don't get it" or similar phrases

**Signs You're Going Too Slow:**
- Repeating same concept with 5+ examples when student already demonstrated mastery
- Covering every minor edge case after core is solid
- Student explicitly says "I get it, let's move on"
- Spending 20+ minutes on optional details
- Student can explain concept clearly and write code confidently

**Remember:** We're avoiding the mistakes from Chapters 4-7. Better to spend an extra 30 minutes now than feel lost and frustrated later when trying to apply the knowledge.

### What Must Be Covered:

✓ Every major concept in the chapter  
✓ At least 2-3 examples per concept (enough to demonstrate understanding)  
✓ All practice questions from textbook  
✓ Common pitfalls and gotchas  
✓ Practical use cases  
✓ Hands-on typing practice for each concept  
✓ Verification that student can apply the concept  

### What Can Be Skipped:

✗ Minor variations already covered  
✗ Historical context (unless requested)  
✗ Advanced topics beyond chapter scope  
✗ Every single textbook example if redundant  
✗ Excessive repetition once understanding is confirmed  
✗ Deep dives into edge cases for basic concepts  

### Efficiency Guidelines:

**Respect the 2-Hour Goal:**
- Track time during session
- **Remember:** Rushing through Chapters 4-7 led to getting lost, frustrated, and wanting to give up
- **We are being thorough from now on** - that's the whole point of this updated method
- If approaching 2 hours, assess what's left
- Prioritize remaining practice questions over additional examples
- Can always revisit concepts if needed in future sessions

**But Never Sacrifice Understanding:**
- If core concept unclear after 2 hours, continue until understood
- Better to spend 2.5 hours and understand than rush and be confused
- The 2-hour goal is a target, not a hard limit
- Student's understanding always takes priority over time  

---

## TECHNICAL EXECUTION

### Running Code:

**Method 1: Interactive Shell**
```powershell
python  # Start interactive shell
>>> print("Hello")  # Type code here
```

**Method 2: .py Files**
```powershell
cd "path/to/chapter/folder"
python filename.py
```

**Method 3: Full Path**
```powershell
python "c:\full\path\to\filename.py"
```

### When Technical Issues Occur:

**DO:**
- Fix quickly or find workaround
- Use terminal if play button fails
- Focus on learning Python, not debugging tools
- Move on after 2-3 minutes if issue persists

**DO NOT:**
- Spend 10+ minutes on VS Code settings
- Get stuck on environment issues
- Let technical problems derail learning

### File Organization:

**Each Chapter Needs:**
```
Chapter X/
├── Chapter_X_Practice_Questions.md  # Textbook questions
└── [practice_code.py]            # Any practice files created
```

---

## CRITICAL REMINDERS

### Must Do Every Time:

✓ **Ask "Do you have any questions?" after EACH section**  
✓ **Wait for student confirmation before moving on**  
✓ **Use ACTUAL textbook (automatetheboringstuff.com), not simplified versions or summaries**  
✓ **Track missed questions throughout quiz**  
✓ **Have student TYPE all code (no copy-paste)**  
✓ **Show expected output for all examples**  
✓ **Explain what each piece of code does**  
✓ **Use .py files for any multi-line or indented code**  
✓ **Put import instructions in Q1 - NEVER at top of file**  
✓ **Leave practice questions BLANK - student writes all answers**  
✓ **Make examples use DIFFERENT content than questions ask for**  
✓ **Practice files are empty workspaces, not answer sheets**  
✓ **⚠️ EVERY QUESTION MUST HAVE "WHAT IT DOES:" EXPLANATION - NO EXCEPTIONS**  
✓ **⚠️ EVERY EXAMPLE MUST USE BOX FORMAT WITH │ BORDERS - NO EXCEPTIONS**  
✓ **⚠️ EVERY QUESTION MUST EXPLICITLY STATE WHICH METHODS/FUNCTIONS TO USE**  
✓ **⚠️ WHEN EDITING MULTIPLE SECTIONS, APPLY TO ALL OF THEM, NOT JUST ONE**  
✓ **Use simple textbook-style examples (test.txt, file1.txt, data.txt, etc.)**  
✓ **Be explicit about context - don't assume they remember**  
✓ **Read the full textbook chapter from https://automatetheboringstuff.com/ before teaching**  

### Never Do:

✗ Move to next section without asking for questions  
✗ Assume student remembers previous context  
✗ Skip explanations because "it's obvious"  
✗ Make up simplified questions instead of using actual textbook  
✗ Use interactive shell for loops/functions  
✗ Use creative themes or scenarios (Star Trek, NFL, etc.)  
✗ Proceed when student seems confused  
✗ Rush through material  
✗ **⚠️ FORGET "WHAT IT DOES:" ON ANY QUESTION**  
✗ **⚠️ USE PLAIN "Example:" WITHOUT THE BOX FORMAT**  
✗ **⚠️ REMOVE "WHAT IT DOES:" WHEN EDITING QUESTIONS**  
✗ **⚠️ FIX ONLY ONE SECTION WHEN ASKED TO FIX MULTIPLE SECTIONS**  
✗ **Write imports at top of practice files - import instruction goes in Q1**  
✗ **Write answers to questions - leave blank space for student to type**  
✗ **Make examples that use same content as question asks for**  
✗ **Pre-fill any code that defeats the purpose of student practicing**  
✗ **Write vague questions like "create a file" without saying which function to use**  

---

## WHAT WORKS (PROVEN EFFECTIVE)

✓ Typing code in interactive shell for simple examples  
✓ Breaking concepts into small, digestible chunks  
✓ Asking questions after every section  
✓ One practice question at a time  
✓ Tracking missed questions for targeted review  
✓ Using terminal when play button fails  
✓ Creating comprehensive reference summaries  
✓ Acknowledging when student is tired  
✓ Adjusting pace based on student's state  
✓ Being explicit about context  
✓ Using .py files for complex code  
✓ Showing actual output of code  
✓ Consulting textbook directly for all concepts and examples  
✓ Adding "WHAT IT DOES:" explanations to practice questions so student understands what they're using  
✓ **Using simple textbook examples without creative themes**  

---

## WHAT DOESN'T WORK (PAST FAILURES)

✗ Moving too fast without checking understanding  
✗ Forgetting to ask "questions?" after sections  
✗ Using simplified questions instead of textbook questions  
✗ Assuming student remembers context  
✗ Making interactive shell examples too complex  
✗ Creating summary skeletons without content  
✗ Writing brief definitions without explanations  
✗ Saying "we'll fill this in later"  
✗ Skipping examples because "it's similar to previous"  
✗ Not explaining code step-by-step  
✗ **⚠️ FORGETTING "WHAT IT DOES:" ON QUESTIONS (KEEPS HAPPENING)**  
✗ **⚠️ REMOVING "WHAT IT DOES:" WHEN EDITING QUESTIONS (KEEPS HAPPENING)**  
✗ **⚠️ USING "Example:" WITHOUT BOX FORMAT (KEEPS HAPPENING)**  
✗ **⚠️ FIXING ONLY SECTION 3 WHEN ASKED TO FIX SECTIONS 3, 4, 5, 6 (KEEPS HAPPENING)**  
✗ **⚠️ WRITING VAGUE QUESTIONS WITHOUT METHOD NAMES (KEEPS HAPPENING)**  
✗ **Writing imports at the top of practice files**  
✗ **Writing answers to practice questions for student**  
✗ **Making examples that give away the answer**  
✗ **Pre-filling code that student should type themselves**  
✗ **Using creative themes that distract from the technical concept**  

---

## SESSION WORKFLOW

### Beginning of Session:

1. Identify which chapter(s) to cover
2. Read complete chapter from https://automatetheboringstuff.com/
3. Take notes on key concepts and sections
4. Begin teaching section by section

### During Session:

1. Teach one section
2. Student types code
3. Ask "Any questions?" after section
4. Wait for confirmation
5. Move to next section
6. Repeat until chapter complete

### End of Chapter:

1. Quiz with textbook questions (one at a time)
2. Track missed questions
3. Review missed topics at end
4. Confirm student ready to move on

### End of Session:

1. Summary of what was covered
2. Note any incomplete sections for next time
3. Confirm student's understanding level

---

## STUDENT FEEDBACK TO REMEMBER

Direct quotes from student:

- "Ask me if I have questions at the end of each section"
- "Use the actual book questions"
- "If I miss a question, we review that topic"
- "Let me type it - I learn by doing"
- "Don't assume I remember what's in the dictionary"
- "Interactive shell is frustrating for multi-line code"
- "I kind of got lost. Then I got frustrated. Then I wanted to give up" (about the video when rushed through chapters)
- "the last four chapters we only had a week to do those and we spent no longer than an hour on them but we were in a hurry"
- "we need to be thorough from now on"

**Key Translations:**
- Always consult the textbook directly at https://automatetheboringstuff.com/
- Rushing leads to: Getting lost → Frustration → Wanting to give up → Poor quality work
- Being thorough means: Deep understanding → Confidence → Can explain code → Quality work student is proud of

---

## QUALITY STANDARDS

### Teaching Quality Checklist:

- [ ] Asked questions after every section
- [ ] Waited for student confirmation
- [ ] Used actual textbook questions
- [ ] Student typed all code
- [ ] Used appropriate tool (shell vs .py file)
- [ ] Explained all code in detail
- [ ] Showed expected output
- [ ] Was explicit about context
- [ ] Tracked missed questions
- [ ] Reviewed missed topics at end

### Practice File Quality Checklist:

**BEFORE submitting ANY practice file work, verify:**

- [ ] Read the actual textbook chapter from automatetheboringstuff.com
- [ ] Looked at Chapter 8/9 practice files to see correct format
- [ ] **EVERY SINGLE QUESTION** has "WHAT IT DOES:" line
- [ ] **EVERY SINGLE EXAMPLE** uses box format with ┌─ │ └─ symbols
- [ ] **EVERY SINGLE QUESTION** explicitly states which methods/functions to use
- [ ] Examples use DIFFERENT values than questions ask for
- [ ] Q1 is always the import (no imports elsewhere in file)
- [ ] No answers written in the file (blank lines only)
- [ ] If asked to fix multiple sections, verified I fixed ALL of them, not just one
- [ ] Counted sections requested vs sections edited - numbers match
- [ ] Spot-checked questions across ALL sections for consistency

**IF ANY CHECKBOX IS UNCHECKED, DO NOT SUBMIT THE WORK. FIX IT FIRST.**

---

**FINAL REMINDER:**

The mistakes that keep happening are:
1. Missing "WHAT IT DOES:" on questions
2. Not using box format for examples  
3. Writing vague questions without method names
4. Fixing only one section when multiple were requested
5. Using summaries instead of actual textbook

**THESE ARE NOT NEGOTIABLE. THEY MUST BE CORRECT EVERY TIME.**

═══════════════════════════════════════════════════════════════════════════════

## 🔴 BEFORE YOU CLICK "SUBMIT" ON YOUR RESPONSE 🔴

**DID YOU:**
□ Follow the STEP-BY-STEP PROCEDURE at the top of this document?
□ Use the EXACT TEMPLATE shown in this document?
□ Count sections requested vs sections you edited - do the numbers match?
□ Verify EVERY question has "WHAT IT DOES:"?
□ Verify EVERY example has ┌─ │ └─ box format?
□ Verify EVERY question states explicit method names?
□ Read https://automatetheboringstuff.com/ actual chapter content?

**IF ANY ANSWER IS "NO" - STOP. GO BACK. FIX IT.**

**The user is on week 8. They've been frustrated for 8 weeks.**
**This is your chance to get it right.**
**Don't waste it.**

═══════════════════════════════════════════════════════════════════════════════

**THIS METHOD WORKS. FOLLOW IT EXACTLY. NO DEVIATIONS.**

**CORRECTNESS > SPEED**  
**COMPLETENESS > RUSHING**  
**UNDERSTANDING > COVERAGE**  
**CONSISTENCY > CONVENIENCE**

═══════════════════════════════════════════════════════════════════════════════
END OF DOCUMENT
═══════════════════════════════════════════════════════════════════════════════

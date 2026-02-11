# IS 305 Python Study Method - Comprehensive Teaching Protocol

**Date Created:** January 25, 2026  
**Last Updated:** February 1, 2026  
**Student:** IS 305 Final Year Bachelor's Student (Second to Last Term)  
**Course:** IS 305 - Information Systems  
**Textbook:** Automate the Boring Stuff with Python, 3rd Edition  
**Goal:** Learn Python chapters efficiently while balancing time constraints

## CURRENT SCHEDULE (Week of February 3, 2026)

- **Monday, Feb 3:** Chapter 8 (Strings and Text Editing) - ~2 hours
- **Tuesday, Feb 4:** Chapter 9 (Regular Expressions) - ~2 hours  
- **Wednesday, Feb 5:** Video recording/submission (less than 5 minutes)
  - **Project:** Chat Command Parser for multiplayer game server
  - **Uses:** String manipulation (Ch 8) + Regex patterns (Ch 9)
  - **Code First:** Write and test code BEFORE recording (can use AI but MUST understand it)
  - **Video Must Show:**
    1. Face on camera (no reading from notes - oral exam style)
    2. Screen when demonstrating code
    3. Walk through code and demonstrate it working
    4. Explain regex patterns used and how they work
    5. Explain validity/invalidity decisions made
    6. Describe at least 1 bug encountered and how it was fixed
  - **Why Thorough Learning Matters:** Cannot just read script on camera. Must actually understand code to explain it naturally. If lost/confused (like rushed chapters), video will show it. Need confidence from real understanding.
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

## MANDATORY AI COMPLIANCE

**BEFORE STARTING ANY TEACHING SESSION, AI MUST:**

1. **Read Required Documentation:**
   - AI_EXECUTION_CONTRACT.md (in full)
   - READ_THIS_FIRST.md (in full)
   - BEST_PRACTICES.md (in full)
   - This STUDY_METHOD.md (in full)

2. **Follow No-Assumption Rule:**
   - DO NOT assume student remembers previous sections
   - DO NOT assume student understands context
   - DO NOT skip explanations because "we covered this before"
   - ASK questions when uncertain about student's knowledge level

3. **Question-First Fallback:**
   - When in doubt, ASK
   - DO NOT guess what student needs
   - DO NOT proceed if instructions are ambiguous
   - STOP → ASK → WAIT

4. **Correctness Over Speed:**
   - Prioritize understanding over rushing through material
   - Complete explanations are required
   - No "we'll come back to this later" unless explicitly requested

---

## CHAPTER SUMMARY CREATION - CRITICAL REQUIREMENTS

**SUMMARY FORMAT (Follow Chapter 1 Example):**

### Required Structure:
```
===============================================================================
IS 305 - CHAPTER X: [TITLE] - COMPLETE STUDY GUIDE
Automate the Boring Stuff with Python, 3rd Edition
===============================================================================

COURSE INFORMATION:
- Class: IS 305 (Information Systems)
- Final Year Bachelor's Degree (Second to Last Term)
- Textbook: Automate the Boring Stuff with Python, 3rd Edition
- Purpose: Study guide and command reference for final project
- Date: [Current Date]

===============================================================================
CHAPTER OVERVIEW
===============================================================================

[Full chapter overview including WHY THIS MATTERS section]
```

### Content Requirements for Each Section:

**DO:**
- Include comprehensive explanations, NOT brief definitions
- Explain WHAT the concept is
- Explain WHY it matters
- Explain HOW it works
- Provide multiple examples with expected output
- Include practical use cases
- Add "Important Notes" sections
- Show common pitfalls
- Use tables for comparisons
- Include visual representations (ASCII diagrams for indexes, etc.)
- Add detailed pattern breakdowns
- Explain every piece of example code

**DO NOT:**
- Write brief one-line definitions like "Usage: | means match one of many expressions"
- Skip explanations
- Assume concepts are self-explanatory
- Use vague language
- Leave code examples unexplained

### Example of CORRECT Detail Level:

**WRONG (Too Brief):**
```
## Pipe Character

Usage: | means match one of many expressions

Example: r'cat|dog' matches cat or dog
```

**CORRECT (Proper Detail):**
```
===============================================================================
PIPE CHARACTER - MATCHING ONE OF MANY ALTERNATIVES
===============================================================================

CONCEPT: The pipe character | means "match one of several expressions" (like "or" in logic)

SYNTAX: pattern1|pattern2|pattern3

BASIC EXAMPLE:

heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
mo1.group()  # 'Batman'

mo2 = heroRegex.search('Tina Fey and Batman')
mo2.group()  # 'Tina Fey'

HOW IT WORKS:
- Searches for 'Batman' OR 'Tina Fey'
- Returns the FIRST occurrence found
- In first example, 'Batman' comes first, so it's returned
- In second example, 'Tina Fey' comes first, so it's returned

[Continue with more examples, use cases, etc.]
```

### Summary Length Requirements:

- Minimum 500 lines for comprehensive chapters
- Follow Chapter 1 format exactly (608 lines, detailed)
- Include ALL practice questions from the textbook
- Include detailed answers to practice questions

---

## OUR PROVEN TEACHING METHOD

### STEP 1: PRE-CHAPTER SETUP

**Before Teaching Begins:**

1. **Create Folder Structure:**
   ```
   Study Material and Summaries/
   └── Chapter X/
       ├── Chapter_X_Summary.md (COMPREHENSIVE - like Chapter 1)
       └── Chapter_X_Practice_Questions.md (textbook questions)
   ```

2. **Create Summary File:**
   - Use format described in "CHAPTER SUMMARY CREATION" section above
   - Fill in ALL sections from textbook (NO placeholders or "TODO" items)
   - Use Chapter 1 as the quality standard
   - Include practice questions at the end

3. **Verify Completion:**
   - Summary must be COMPLETE before teaching begins
   - No "we'll fill this in later"
   - All examples must have expected output shown
   - All code must be explained

### STEP 2: SECTION-BY-SECTION TEACHING

**File Structure for Each Section:**

For each section, create TWO files:
1. **Reference file** - Complete working examples (e.g., `string_basics.py`, `escape_characters.py`)
2. **Practice file** - Template with commented examples for student to uncomment and run (e.g., `section1_practice.py`, `section2_practice.py`)

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
├── string_basics.py                  # Reference: Working examples
├── escape_characters.py              # Reference: Working examples
├── section1_practice.py              # Practice: Commented templates
├── section2_practice.py              # Practice: Commented templates
└── ... (one reference + one practice per section)
```

**Why This Works:**
- Reference files show complete working code
- Practice files let student type/uncomment (muscle memory)
- Comments in practice files remind student what each line does
- No switching between shell and files
- Student can always check reference if stuck
- Clear separation between "answer key" and "workspace"

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

**Phase 1: Summary Creation (20-30 minutes)**
- Create comprehensive Chapter_X_Summary.md
- Fill in all sections from textbook
- Include practice questions
- *This is prep work, can be done before session*

**Phase 2: Teaching Core Concepts (60-70 minutes)**
- Teach sections one by one
- Student types code for each concept
- Ask questions after each section
- Move at pace that ensures understanding

**Phase 3: Practice Questions (30-40 minutes)**
- Work through ALL textbook end-of-chapter questions
- One at a time
- Track missed questions
- Review missed topics

**Phase 4: Review & Wrap-up (10-20 minutes)**
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
├── Chapter_X_Summary.md          # Comprehensive reference (like Ch 1)
├── Chapter_X_Practice_Questions.md  # Textbook questions
└── [practice_code.py]            # Any practice files created
```

---

## CRITICAL REMINDERS

### Must Do Every Time:

✓ **Ask "Do you have any questions?" after EACH section**  
✓ **Wait for student confirmation before moving on**  
✓ **Use ACTUAL textbook questions, not simplified versions**  
✓ **Track missed questions throughout quiz**  
✓ **Have student TYPE all code (no copy-paste)**  
✓ **Show expected output for all examples**  
✓ **Explain what each piece of code does**  
✓ **Use .py files for any multi-line or indented code**  
✓ **Put import instructions in Q1 - NEVER at top of file**  
✓ **Leave practice questions BLANK - student writes all answers**  
✓ **Make examples use DIFFERENT content than questions ask for**  
✓ **Practice files are empty workspaces, not answer sheets**  
✓ **Add "WHAT IT DOES:" explanation for each question - so student knows what they're using**  
✓ **Use simple textbook-style examples (test.txt, file1.txt, data.txt, etc.)**  
✓ **Be explicit about context - don't assume they remember**  
✓ **Create COMPLETE summaries before teaching (no placeholders)**  

### Never Do:

✗ Move to next section without asking for questions  
✗ Assume student remembers previous context  
✗ Skip explanations because "it's obvious"  
✗ Make up simplified questions instead of using textbook  
✗ Use interactive shell for loops/functions  
✗ Leave summary sections as "TODO" or "to be filled in"  
✗ Use creative themes or scenarios (Star Trek, NFL, etc.)  
✗ Write brief one-line definitions in summaries  
✗ Proceed when student seems confused  
✗ Rush through material  
✗ **Write imports at top of practice files - import instruction goes in Q1**  
✗ **Write answers to questions - leave blank space for student to type**  
✗ **Make examples that use same content as question asks for**  
✗ **Pre-fill any code that defeats the purpose of student practicing**  

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
✓ Detailed explanations with multiple examples  
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
✗ **Writing imports at the top of practice files**  
✗ **Writing answers to practice questions for student**  
✗ **Making examples that give away the answer**  
✗ **Pre-filling code that student should type themselves**  
✗ **Using creative themes that distract from the technical concept**  

---

## SESSION WORKFLOW

### Beginning of Session:

1. Identify which chapter(s) to cover
2. Create comprehensive summaries FIRST (complete, not placeholder)
3. Verify summaries are detailed (like Chapter 1 format)
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
- "why the **** don't you do the summaries" (re: complete them BEFORE teaching)
- "I kind of got lost. Then I got frustrated. Then I wanted to give up" (about the video when rushed through chapters)
- "the last four chapters we only had a week to do those and we spent no longer than an hour on them but we were in a hurry"
- "we need to be thorough from now on"

**Key Translations:**
- Create COMPLETE, DETAILED summaries BEFORE starting to teach. No placeholders. No "we'll fill this in later."
- Rushing leads to: Getting lost → Frustration → Wanting to give up → Poor quality work
- Being thorough means: Deep understanding → Confidence → Can explain code → Quality work student is proud of

**Translation: Create COMPLETE, DETAILED summaries BEFORE starting to teach. No placeholders. No "we'll fill this in later."**

---

## QUALITY STANDARDS

### Summary Quality Checklist:

- [ ] Follows Chapter 1 format exactly
- [ ] Has detailed explanations, not brief definitions
- [ ] Includes WHAT, WHY, HOW for each concept
- [ ] Has multiple examples with output shown
- [ ] Includes practical use cases
- [ ] Has tables for comparisons where appropriate
- [ ] Includes "Important Notes" sections
- [ ] Shows common pitfalls
- [ ] Has detailed code breakdowns
- [ ] Includes ALL textbook practice questions
- [ ] Has detailed answers to practice questions
- [ ] Minimum 500 lines for comprehensive chapters
- [ ] NO placeholder text or "TODO" items
- [ ] NO sections marked "to be filled in later"

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

---

**THIS METHOD WORKS. FOLLOW IT EXACTLY. NO DEVIATIONS.**

**CORRECTNESS > SPEED**  
**COMPLETENESS > RUSHING**  
**UNDERSTANDING > COVERAGE**

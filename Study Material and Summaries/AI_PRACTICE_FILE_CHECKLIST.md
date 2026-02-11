# AI Practice File Creation Checklist

**PURPOSE:** This checklist MUST be completed and shown to the user BEFORE creating or editing any practice file. No exceptions.

---

## MANDATORY PRE-WORK (Before Creating ANY Practice File)

- [ ] Read STUDY_METHOD.md sections on practice file format
- [ ] Read existing Chapter 8/9 practice files as reference
- [ ] Understand the specific chapter/section requirements

---

## QUESTION WORDING VERIFICATION

For EACH question, verify:

- [ ] **States EVERY method shown in example** (with open, f.write(), shutil.move(), etc.)
- [ ] **If example uses f.write(), question says "use f.write()"** - NEVER "with content"
- [ ] **If example uses shutil.move(), question says "use shutil.move()"** - NEVER "move"
- [ ] **If example uses .mkdir(), question says "use .mkdir()"** - NEVER "create folder"
- [ ] **Variable names are explicit** ("create variable h" not "create a path")
- [ ] **Paths are explicit** (h / 'Desktop' not "Desktop folder")
- [ ] **File names are in quotes** ('test.txt' not test.txt)
- [ ] **WHAT IT DOES line is present** and explains the concept

---

## EXAMPLE VERIFICATION

For EACH example, verify:

- [ ] **Uses DIFFERENT content than question** (spam/bacon not the actual answer)
- [ ] **Shows SAME pattern/syntax as question needs**
- [ ] **Matches the question's method requirements** (if question says f.write(), example shows f.write())
- [ ] **Uses boxed format** with ┌─ EXAMPLE ───────────── header
- [ ] **Is indented with # │ prefix** for each line

---

## STRUCTURE VERIFICATION

- [ ] **Q1 is ALWAYS just imports** (no actual work in Q1)
- [ ] **Q2 is where work begins** (first actual task with the module)
- [ ] **Questions progress logically** (simple → complex)
- [ ] **No "coming back to this later"** - each question is complete
- [ ] **Answer spaces have appropriate blank lines** for student work

---

## FINAL CHECK

- [ ] **Read question out loud** - can you code it without looking at example?
- [ ] **Check against STUDY_METHOD.md rules** one more time
- [ ] **Compare format to Chapter 8/9 reference files** - does it match exactly?

---

## IF ANY CHECKBOX IS UNCHECKED

**STOP. DO NOT CREATE THE FILE.**

Go back and fix the issue. Show the user what you're fixing and why.

---

## AFTER CREATION

- [ ] **Run the file** to verify Exit Code 0
- [ ] **User tests it** - if they struggle, the question wording is WRONG
- [ ] **Document any new patterns** for future reference


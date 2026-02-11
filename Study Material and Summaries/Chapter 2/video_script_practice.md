# Video Script - Practice Only (Internalize, Don't Read!)

## PART 1: Introduction (30 seconds)
"Hi, I'm [your name]. Today I'm going to write a program that converts numeric grades to GPA using an if-elif-else statement, and I'll test it to show you how conditional logic works in Python."

---

## PART 2: Writing the Code (3-4 minutes)

### Getting Input
**[Type: grade = float(input("Enter your numeric grade: "))]**

**Say:** "First, I'm using the input function to get the user's grade. I wrap it in float() to convert the string input into a decimal number, so we can handle grades like 91.2."

---

### The If-Elif-Else Chain
**[Type: if grade >= 93:]**

**Say:** "Now I'm starting my conditional statement with 'if'. This checks if the grade is 93 or higher. If this is true, they get a 4.0 GPA."

**[Type: gpa = 4.0, letter = "A"]**

---

**[Type: elif grade >= 90:]**

**Say:** "The 'elif' means 'else if' - it only runs if the previous condition was false. So if they didn't get 93 or higher, we check if they got at least a 90. This would be an A-minus with a 3.7 GPA."

**[Type: gpa = 3.7, letter = "A-"]**

---

**[Type remaining elif blocks for: 87, 83, 80, 77, 73, 70, 67, 63, 60]**

**Say:** "I'm continuing this pattern for each grade range - B+, B, B-, C+, C, C-, D+, D, D-. Each elif checks the next threshold going down."

---

**[Type: else:]**

**Say:** "Finally, the 'else' catches everything that didn't match - any grade below 60 gets a 0.0, which is failing."

**[Type: gpa = 0.0, letter = "F"]**

---

### Output
**[Type: print(f"Your grade of {grade} is a {letter}, which earns a GPA of {gpa}")]**

**Say:** "I'm using an f-string to display the result, which lets me embed variables directly in the output."

---

## PART 3: Testing (3-4 minutes)

### Test 1: A- Grade
**[Run program, enter: 91.2]**

**Say:** "Let's test this with 91.2. Watch what happens..."

**[Show output: A- with 3.7]**

**Explain:** "Python started at the top. First it checked: is 91.2 greater than or equal to 93? No. So it moved to the next elif: is 91.2 greater than or equal to 90? Yes! So it assigned 3.7 and immediately exited the entire if-elif-else chain. It didn't waste time checking the remaining conditions."

---

### Test 2: B Grade  
**[Run program, enter: 85]**

**Say:** "Now let's test with 85..."

**[Show output: B with 3.0]**

**Explain:** "This time, Python checked the first condition - is 85 >= 93? No. Then 85 >= 90? No. Then 85 >= 87? No. Then 85 >= 83? Yes! So it assigned 3.0 for a B and stopped. The key is that once Python finds a true condition, it executes that block and skips everything else."

---

### Test 3: Failing Grade
**[Run program, enter: 55]**

**Say:** "Finally, let's test a failing grade with 55..."

**[Show output: F with 0.0]**

**Explain:** "Python checked every single if and elif condition, and none of them were true because 55 is less than 60. So it fell through to the else block, which is our catch-all for anything that doesn't match. That's why the else doesn't need a condition - it handles whatever's left."

---

### Optional Test 4: Edge Case
**[Run program, enter: 93]**

**Say:** "Let me show one more - exactly 93..."

**[Show output: A with 4.0]**

**Explain:** "This demonstrates that the >= operator includes the boundary value. 93 is greater than OR equal to 93, so it gets the 4.0."

---

## PART 4: Conclusion (30 seconds)

**Say:** "So that's how if-elif-else statements work in Python. The computer checks each condition in order from top to bottom, executes the first true condition it finds, and then exits the entire chain. This is different from using multiple separate if statements, which would check every condition even after finding a match. Thanks for watching!"

---

## KEY TERMS TO INTERNALIZE:
- **if statement** - checks the first condition
- **elif** - "else if", checks next condition only if previous was false
- **else** - catch-all for anything that didn't match
- **conditional chain** - the entire if-elif-else structure
- **sequential evaluation** - checking from top to bottom
- **exit on first match** - stops after finding true condition
- **float()** - converts input to decimal number
- **f-string** - formatted string with embedded variables
- **>=** operator - greater than or equal to
- **assignment** - storing a value in a variable (gpa = 4.0)

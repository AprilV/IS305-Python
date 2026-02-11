===============================================================================
IS 305 - CHAPTER 1: PYTHON BASICS - COMPLETE STUDY GUIDE
Automate the Boring Stuff with Python, 3rd Edition
===============================================================================

COURSE INFORMATION:
- Class: IS 305 (Information Systems)
- Final Year Bachelor's Degree (Second to Last Term)
- Textbook: Automate the Boring Stuff with Python, 3rd Edition
- Purpose: Study guide and command reference for final project
- Date: January 5, 2026

===============================================================================
CHAPTER OVERVIEW
===============================================================================

Chapter 1 introduces the fundamental concepts of Python programming, covering:
- Using the interactive shell (REPL - Read-Evaluate-Print-Loop)
- Expressions and their evaluation
- Data types (integers, floats, strings)  
- Operators (math and string)
- Variables and assignment statements
- Basic functions for input/output and type conversion
- Writing and running Python programs
- Understanding how computers store data (binary numbers)

===============================================================================
WHAT IS PROGRAMMING?
===============================================================================

Programming = Writing instructions for computers in a language they understand

Basic Programming Instructions:
1. "Do this; then do that" (sequential execution)
2. "If this condition is true, perform this action; otherwise, do that action"
3. "Do this action exactly 27 times" (fixed iteration)
4. "Keep doing that until this condition is true" (conditional iteration)

===============================================================================
WHAT IS PYTHON?
===============================================================================

Python refers to TWO things:
1. Programming Language: Syntax rules for writing valid Python code
2. Interpreter Software: Reads and executes Python source code

Why Python for beginners:
- Gentle learning curve
- Readable syntax  
- Doesn't require complex concepts for simple tasks
- Good first language before learning others

===============================================================================
DATA TYPES
===============================================================================

Python has three primary data types introduced in Chapter 1:

1. INTEGER (int) - Whole numbers
   Examples: -2, -1, 0, 1, 2, 3, 4, 5
   
2. FLOATING-POINT (float) - Numbers with decimal points  
   Examples: -1.25, -1.0, -0.5, 0.0, 0.5, 1.0, 1.25
   
3. STRING (str) - Text values enclosed in single quotes
   Examples: 'a', 'aa', 'Hello!', '11 cats', '5'
   Special case: '' (empty/blank string)

IMPORTANT NOTES:
- Math between int and float always results in float
- Division with / always returns float (even 16/4 = 4.0)
- Strings must be in quotes, integers/floats are not

===============================================================================
OPERATORS
===============================================================================

MATH OPERATORS (Listed by precedence - highest to lowest):

Operator | Operation          | Example    | Result
---------|-------------------|------------|--------
**       | Exponentiation    | 2 ** 3     | 8
%        | Modulus/remainder | 22 % 8     | 6  
//       | Integer division  | 22 // 8    | 2
/        | Division          | 22 / 8     | 2.75
*        | Multiplication    | 3 * 5      | 15
-        | Subtraction       | 5 - 2      | 3
+        | Addition          | 2 + 2      | 4

STRING OPERATORS:

+ (Concatenation): Joins strings together
  Example: 'Alice' + 'Bob' → 'AliceBob'
  
* (Replication): Repeats string multiple times  
  Example: 'Alice' * 5 → 'AliceAliceAliceAliceAlice'
  
OPERATOR PRECEDENCE:
- Use parentheses to override default precedence
- Example: 2 + 3 * 6 = 20, but (2 + 3) * 6 = 30

===============================================================================
VARIABLES AND ASSIGNMENT
===============================================================================

VARIABLES:
- Store single values in computer memory
- Like labeled boxes containing values
- Initialized when first assigned a value
- New assignments overwrite previous values

ASSIGNMENT STATEMENT SYNTAX:
variable_name = value

EXAMPLES:
spam = 42
eggs = 'Hello'  
my_age = 25
spam = spam + 2  # Overwrites previous value

VARIABLE NAMING RULES:
✓ Valid: eggs, my_age, spam, userName
✗ Invalid: 100, 2names (cannot start with number)

===============================================================================
ESSENTIAL FUNCTIONS - COMPLETE REFERENCE
===============================================================================

INPUT/OUTPUT FUNCTIONS:
print(value)          # Displays output to screen
                      # Can display integers, floats, strings, or blank lines
                      # Does not return a value

Examples:
print('Hello, world!')        # Prints: Hello, world!
print(42)                     # Prints: 42
print()                       # Prints blank line

input(prompt)         # Gets keyboard input (always returns string)
                      # Waits for user to type and press ENTER
                      # Returns: String

Examples:
name = input('Enter your name: ')
age = input('>')               # Using > as prompt
data = input()                 # No prompt shown

STRING FUNCTIONS:
len(string)           # Returns number of characters in string
                      # Returns: Integer

Examples:
len('Hello') → 5
len('My very energetic monster just scarfed nachos.') → 46
len('') → 0

TYPE CONVERSION FUNCTIONS:
str(value)            # Converts value to string
                      # Can convert int, float, or other types
                      # Returns: String

Examples:
str(29) → '29'
str(0) → '0'
str(-3.14) → '-3.14'

int(value)            # Converts value to integer  
                      # Rounds down floats, converts s (Windows)
python3               # Start Python interactive shell (macOS/Linux)
exit()               # Exit Python shell  
quit()               # Alternative exit command

Shell Access Methods:
1. Mu Editor: Click New → Save as blank.py → Click Run or F5
2. Command Line (Windows Terminal): Type 'python'
3. Command Line (macOS/Linux Terminal): Type 'python3'

Shell Prompts:
>>> prompt            # Standard Python interactive shell
In [1]: prompt        # Jupyter/IPython style REPL

Shell Features:
- Test expressions immediately
- See results of calculations
- Experiment with functions
- Error messages help debug code
- Great for learning what basic Python instructions do
- Remember things you DO better than things you only READ

Mu Editor Keyboard Shortcuts:
CTRL-S (Windows/Linux)    # Save file
⌘-S (macOS)               # Save file
F5                        # Run program
CTRL-SHIFT-C              # Copy from interactive shell pane
CTRL-C                    # Copy from file editor pan DOWN
int('99.99') → ERROR   # Cannot convert
int('twelve') → ERROR  # Cannot convert

float(value)          # Converts value to floating-point
                      # Returns: Float

Examples:
float('3.14') → 3.14
float(10) → 10.0

type(value)           # Determines data type of a value
                      # Returns: Type information

Examples:
type(42) → <class 'int'>
type(42.0) → <class 'float'>
type('forty two') → <class 'str'>
type(len('test')) → <class 'int'>

MATH FUNCTIONS:
round(number)         # Returns rounded integer
round(number, places) # Returns float rounded to decimal places
                      # Uses banker's rounding (.5 rounds to nearest even)
                      # Returns: Integer or Float

Examples:
round(3.14) → 3
round(7.7) → 8
round(-2.2) → -2
round(3.14, 1) → 3.1
round(7.7777, 3) → 7.778
round(3.5) → 4         # Rounds up
round(2.5) → 2         # Rounds down (banker's rounding)

abs(number)           # Returns absolute value (positive form)
                      # Returns: Same type as input (int or float)

Examples:
abs(25) → 25
abs(-25) → 25
abs(-3.14) → 3.14
abs(0) → 0

===============================================================================
PYTHON INTERACTIVE SHELL COMMANDS
===============================================================================

Starting/Stopping:
python                # Start Python interactive shell
exit()               # Exit Python shell  
quit()               # Alternative exit command

Shell Features:
- Test expressions immediately
- See results of calculations
- Experiment with functions
- Error messages help debug code

===============================================================================
COMMAND REFERENCE - COPY/PASTE EXAMPLES
===============================================================================

VARIABLE ASSIGNMENT:
spam = 42
eggs = 'Hello'
my_name = 'Student'

MATHEMATICAL EXPRESSIONS:
result = (2 + 3) * 4        # Result: 20
power = 2 ** 8              # Result: 256  
remainder = 23 % 7          # Result: 2
division = 22 / 8           # Result: 2.75
int_division = 22 // 8      # Result: 2

STRING OPERATIONS:
greeting = 'Hello' + ' ' + 'World'    # Result: 'Hello World'
repeated = 'Python' * 3               # Result: 'PythonPythonPython'
empty = ''                           # Empty string

TYPE CONVERSIONS:
text_number = str(42)                # Result: '42'
number = int('100')                  # Result: 100
decimal = float('3.14')              # Result: 3.14

STRING LENGTH:
name_length = len('Python')          # Result: 6
message_length = len('Hello World!') # Result: 12

USER INPUT/OUTPUT:
print('Welcome to Python!')
print('Your age is: ' + str(25))
user_name = input('Enter your name: ')
user_age = int(input('Enter your age: '))

COMMON ERROR PREVENTION:
# ✗ WRONG - Cannot concatenate string and number:
# print('I have ' + 99 + ' items')

# ✓ CORRECT - Convert number to string first:
print('I have ' + str(99) + ' items')

===============================================================================
SYNTAX ERROR EXAMPLES
===============================================================================

COMMON MISTAKES TO AVOID:

1. Missing quotes around strings:
   ✗ print(Hello)          # Missing quotes
   ✓ print('Hello')        # Correct

2. Incomplete expressions:
   ✗ 5 +                   # Incomplete
   ✓ 5 + 3                 # Complete

3. Invalid operator combinations:
   ✗ 42 + 5 + * 2          # Invalid syntax
   ✓ 42 + 5 * 2            # Correct

4. String concatenation errors:
   ✗ 'Alice' * 'Bob'       # Cannot multiply strings
   ✗ 'Alice' * 5.0         # Cannot use float for replication
   ✓ 'Alice' * 5           # Correct integer replication

===============================================================================
KEY TAKEAWAYS FOR FINAL PROJECT
===============================================================================

1. EXPRESSIONS: Values + Operators = Single Result
   - All expressions evaluate down to one value
   - Building blocks of all programs

2. DATA TYPES MATTER:
   - Know the difference between 42 (int), 42.0 (float), '42' (string)
   - Type mismatches cause errors

3. VARIABLES ARE STORAGE:
   - Use meaningful names
   - Values can be overwritten
   - Great for storing results of expressions

4. FUNCTIONS ARE TOOLS:
   - print() for output
   - input() for user interaction  
   - len() for string length
   - Type conversion: str(), int(), float()

5. INTERACTIVE SHELL IS YOUR FRIEND:
   - Test code before writing programs
   - Experiment with new concepts
   - Debug and verify expressions

6. ERROR MESSAGES HELP:
   - Read them carefully
   - They point to the problem
   - Professional developers get errors all the time

===============================================================================
STUDY TIPS FOR IS 305 FINAL
===============================================================================

1. Practice in Interactive Shell:
   - Try every example from this summary
   - Experiment with variations
   - Get comfortable with error messages

BINARY NUMBERS & COMPUTER DATA STORAGE
===============================================================================

WHY BINARY?
- Computers use binary (base-2: only 0 and 1) because it's simple
- Hardware can easily represent two states (on/off, current/no current)
- More economical than detecting 10 different voltage levels

BINARY BASICS:
- Binary = Base-2 number system
- Decimal = Base-10 number system
- Binary can represent all the same numbers as decimal

BINARY TO DECIMAL EXAMPLES:
Decimal | Binary  | Decimal | Binary  | Decimal | Binary
--------|---------|---------|---------|---------|--------
0       | 0       | 9       | 1001    | 18      | 10010
1       | 1       | 10      | 1010    | 19      | 10011
2       | 10      | 11      | 1011    | 20      | 10100
3       | 11      | 12      | 1100    | 25      | 11001
4       | 100     | 13      | 1101    | 26      | 11010
5       | 101     | 14      | 1110    | 255     | 11111111
6       | 110     | 15      | 1111    | 256     | 100000000
7       | 111     | 16      | 10000   | 1000    | 1111101000
8       | 1000    | 17      | 10001   | 1024    | 10000000000

BITS AND BYTES:
- Bit: Single binary digit (0 or 1)
- Byte: 8 bits (can represent 2^8 = 256 numbers, from 0-255)
- 1 bit can represent 2 numbers
- 8 bits (1 byte) can represent 256 numbers (0 to 255)

FILE SIZE UNITS (Real vs Advertised):
Unit          | Real Size                | Advertised     | Note
--------------|--------------------------|----------------|------------------
Kilobyte (KB) | 2^10 = 1,024 bytes      | 1,000 bytes    | Manufacturers lie
Megabyte (MB) | 2^20 = 1,048,576 bytes  | 1,000,000      | to make drives
Gigabyte (GB) | 2^30 = 1,073,741,824 B  | 1,000,000,000  | seem bigger
Terabyte (TB) | 2^40 = 1,099,511,627,776| 1,000,000,000,000 | than they are

REAL WORLD FILE SIZES:
- Romeo and Juliet text: ~135 KB
- High-res photo: 2-5 MB
- Movie: 1-50 GB (depends on quality and length)

HOW DATA IS ENCODED AS BINARY:
1. TEXT (UTF-8 encoding):
   - Each character has a unique number
   - 'A' = 65 (01000001 in binary)
   - '?' = 63
   - '7' = 55
   - 'Hello' = 72, 101, 108, 108, 111

2. INTEGERS:
   - 0 to 255: Standard byte (8 bits)
   - -128 to 127: Two's complement system
   
3. FLOATING-POINT:
   - IEEE-754 standard
   - More complex encoding for decimals

4. IMAGES:
   - Pixels in a 2D grid
   - Each pixel: 3 bytes (Red, Green, Blue values 0-255)
   - Example: RGB(255, 0, 255) = purple pixel

5. SOUND:
   - Sound waves graphed over time
   - Graph points converted to binary numbers
   - Speakers reproduce sound from the numbers

6. VIDEO:
   - Combined image data (frames) + audio data

===============================================================================
PRACTICE QUESTIONS & ANSWERS (From Textbook)
===============================================================================

QUESTION 1: Which of the following are operators, and which are values?
*
'hello'
-88.8
-
/
+
5

ANSWER:
Operators: *  -  /  +
Values: 'hello'  -88.8  5

---

QUESTION 2: Which of the following is a variable, and which is a string?
spam
'spam'

ANSWER:
Variable: spam
String: 'spam'

---

QUESTION 3: Name three data types.

ANSWER:
1. Integer (int)
2. Floating-point number (float)
3. String (str)

---

QUESTION 4: What is an expression made up of? What do all expressions do?

ANSWER:
- Made up of: Values and operators
- What they do: All expressions evaluate (reduce) down to a single value

---

QUESTION 5: This chapter introduced assignment statements, like spam = 10. 
What is the difference between an expression and a statement?

ANSWER:
- Expression: Evaluates to a value (example: 2 + 2)
- Statement: Performs an action (example: spam = 10)
- Expressions can be used anywhere you could use a value
- Statements perform actions like assignment

---

QUESTION 6: What does the variable bacon contain after the following code runs?
bacon = 20
bacon + 1

ANSWER:
20
Explanation: The expression bacon + 1 evaluates to 21, but this value is not
assigned back to bacon. The variable still contains 20.

---

QUESTION 7: What should the following two expressions evaluate to?
'spam' + 'spamspam'
'spam' * 3

ANSWER:
'spam' + 'spamspam' → 'spamspamspam'
'spam' * 3 → 'spamspamspam'
Both produce the same result using different operators.

---

QUESTION 8: Why is eggs a valid variable name while 100 is invalid?

ANSWER:
- eggs: Valid because it starts with a letter
- 100: Invalid because variable names cannot begin with a number
Variable names must start with a letter or underscore, not a number.

---

QUESTION 9: What three functions can be used to get the integer, 
floating-point number, or string version of a value?

ANSWER:
1. int() - converts to integer
2. float() - converts to floating-point number
3. str() - converts to string

---

QUESTION 10: Why does this expression cause an error? How can you fix it?
'I eat ' + 99 + ' burritos.'

ANSWER:
Error: TypeError - cannot concatenate str (not "int") to str
Reason: The + operator cannot combine strings and integers

Fix: Convert the integer to a string using str()
'I eat ' + str(99) + ' burritos.'

===============================================================================
EXTRA CREDIT FUNCTIONS (From Textbook)
===============================================================================

bin(number)           # Converts integer to binary string
                      # Returns: String starting with '0b'

Examples:
bin(42) → '0b101010'
bin(255) → '0b11111111'
bin(10) → '0b1010'

hex(number)           # Converts integer to hexadecimal string
                      # Returns: String starting with '0x'

Examples:
hex(42) → '0x2a'
hex(255) → '0xff'
hex(16) → '0x10'

===============================================================================
NEXT STEPS
===============================================================================

Chapter 2 Preview: "Flow Control"
- Boolean values (True/False)
- Comparison operators (==, !=, <, >, <=, >=)  
- Boolean operators (and, or, not)
- if, elif, else statements
- Making programs make decisions

This Chapter 1 foundation is essential for understanding flow control,
loops, functions, and all advanced Python concepts.

===============================================================================
END OF CHAPTER 1 COMPLETE STUDY GUIDE
===============================================================================

Created for: IS 305 - Information Systems Course
Date: January 5, 2026
Purpose: Comprehensive study guide and command reference for final project

This document combines detailed reference material with practical examples
and can be used in VS Code, shared with study groups, and serves as both
a learning tool andolean values (True/False)
- Comparison operators (==, !=, <, >, <=, >=)  
- Boolean operators (and, or, not)
- if, elif, else statements
- Making programs make decisions

This Chapter 1 foundation is essential for understanding flow control,
loops, functions, and all advanced Python concepts.

===============================================================================
END OF CHAPTER 1 SUMMARY
===============================================================================

Created for: IS 305 - Information Systems Course
Student: [Your Name]
Date: January 2026
Purpose: Study guide and command reference for final project preparation

This document can be used in VS Code, shared with study groups, and serves
as a quick reference while coding Python programs.

===============================================================================
IS 305 - CHAPTER 8: STRINGS AND TEXT EDITING - COMPLETE STUDY GUIDE
Automate the Boring Stuff with Python, 3rd Edition
===============================================================================

COURSE INFORMATION:
- Class: IS 305 (Information Systems)
- Final Year Bachelor's Degree (Second to Last Term)  
- Textbook: Automate the Boring Stuff with Python, 3rd Edition
- Purpose: Study guide and command reference for final project
- Date: February 1, 2026

===============================================================================
CHAPTER OVERVIEW
===============================================================================

Chapter 8 covers working with strings and text in Python. Text is one of the most common forms of data that your programs will handle. You need to extract partial strings, add or remove spacing, convert letters to lowercase or uppercase, and check that strings are formatted correctly.

You already know how to concatenate two strings with the + operator, but you can do much more than that. This chapter covers:

- Different ways to write string values (single quotes, double quotes, multiline)
- Escape characters for special characters
- Raw strings that ignore escape characters  
- String indexing and slicing to extract parts of strings
- String methods for validation, transformation, and formatting
- Working with the clipboard using the pyperclip module
- Practical projects for text manipulation

WHY THIS MATTERS:
- Almost every program processes text in some way
- User input is text that needs validation
- Web scraping and data extraction work with text
- File processing often involves text manipulation
- Formatting output for users requires string operations

===============================================================================
STRING LITERALS - WRITING STRINGS IN CODE
===============================================================================

WHAT ARE STRING LITERALS?
A string literal is the actual string value as it appears in your code. It's how you write strings directly in your Python program.

BASIC RULE: Strings can begin and end with either single quotes (') or double quotes (")

WHY TWO OPTIONS?
Having both options allows you to include quote characters inside your strings without problems.

EXAMPLES:

Using single quotes:
spam = 'That is Alice\'s cat.'     # Need to escape the apostrophe with \

Using double quotes:
spam = "That is Alice's cat."      # No escaping needed!

Using single quotes for a sentence with quotes:
speech = "She said, 'Hi!'"         # Double quotes let you use single quotes inside

BOTH ARE VALID:
'Hello'    # Valid string using single quotes  
"Hello"    # Valid string using double quotes

IMPORTANT NOTE:
The quote marks are NOT part of the string value itself - they just tell Python where the string begins and ends. When Python displays the string, it doesn't include the quote marks.

Example:
>>> spam = "Hello"
>>> spam
'Hello'      # Python shows it with single quotes, but that's just representation

CHOOSING WHICH TO USE:
- Use whichever makes your code easier to read
- If your string contains single quotes (apostrophes), use double quotes
- If your string contains double quotes, use single quotes
- Be consistent within your program

===============================================================================
ESCAPE CHARACTERS - SPECIAL CHARACTERS IN STRINGS
===============================================================================

WHAT IS AN ESCAPE CHARACTER?
An escape character lets you use characters that are otherwise impossible to put into a string. It's a way to tell Python "treat this next character specially."

HOW IT WORKS:
An escape character consists of a backslash (\) followed by the character you want to insert.

WHY WE NEED THEM:
Some characters have special meaning in strings or can't be typed directly. Escape characters solve this problem.

COMMON ESCAPE CHARACTERS:

Escape Code | What It Produces           | Example
------------|---------------------------|----------------------------------
\'          | Single quote              | 'Say hi to Bob\'s mother.'
\"          | Double quote              | "She said, \"Hello!\""
\t          | Tab character             | 'Hello\tWorld' → 'Hello    World'
\n          | Newline (line break)      | 'First line\nSecond line'
\\          | Backslash                 | 'C:\\Users\\Al'

DETAILED EXAMPLES:

1. SINGLE QUOTE IN SINGLE-QUOTED STRING:
   spam = 'Say hi to Bob\'s mother.'
   # Without the \, Python would think the string ended at Bob'
   
2. NEWLINE CHARACTER:
   print("Hello there!\nHow are you?\nI'm doing fine.")
   
   Output:
   Hello there!
   How are you!
   I'm doing fine.

3. TAB CHARACTER:
   print('Name:\tAlice\nAge:\t25')
   
   Output:
   Name:    Alice
   Age:     25

4. BACKSLASH IN FILE PATHS:
   path = 'C:\\Users\\Al\\Desktop'
   # Each \\ becomes a single \ in the actual string
   # Without escaping, \U would be interpreted as Unicode escape

IMPORTANT NOTES:
- The escape character is typed in your source code, but it represents a single character in memory
- 'Hello\tWorld' is 11 characters long in memory (not 12)
- len('Hello\tWorld') returns 11

===============================================================================
RAW STRINGS - IGNORING ESCAPE CHARACTERS
===============================================================================

WHAT ARE RAW STRINGS?
Raw strings treat backslashes as literal characters instead of escape characters. They're created by placing an 'r' before the opening quotation mark.

SYNTAX:
r'text with backslashes'

WHY USE RAW STRINGS?
1. Windows file paths: 'C:\Users\Al\Desktop' requires escaping each backslash
   With raw string: r'C:\Users\Al\Desktop' - much easier!

2. Regular expressions (Chapter 9): Regex uses lots of backslashes
   Raw strings make regex patterns more readable

EXAMPLES:

Without raw string (need to escape):
path = 'C:\\Users\\Alice\\Desktop\\file.txt'  # Hard to read, easy to make mistakes

With raw string:
path = r'C:\Users\Alice\Desktop\file.txt'     # Exactly as you see it!

Escape characters are ignored:
print(r'Hello...\n\n...world!')
# Output: Hello...\n\n...world!  (the \n is printed literally, not as newline)

Normal string behavior:
print('Hello...\n\n...world!')
# Output:
# Hello...
#
# ...world!

WHEN NOT TO USE RAW STRINGS:
- When you actually WANT escape characters to work
- In most regular strings where you don't have many backslashes

USE RAW STRINGS FOR:
- File paths (especially on Windows)
- Regular expression patterns
- Any string with lots of backslashes

===============================================================================
MULTILINE STRINGS - TEXT SPANNING MULTIPLE LINES
===============================================================================

WHAT ARE MULTILINE STRINGS?
Multiline strings are strings that span across multiple lines in your source code. They preserve line breaks and formatting exactly as you type them.

SYNTAX:
Begin and end with three single quotes (''') or three double quotes (""")

EXAMPLES:

Using triple quotes:
message = '''Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob'''

print(message)

Output:
Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob

IMPORTANT FEATURES:

1. Quotes inside multiline strings don't need escaping:
   text = '''He said, "I'm going to the store."'''
   # Both single and double quotes work fine inside

2. Line breaks are preserved automatically:
   # No need for \n - just press Enter
   
3. Python's indentation rules DON'T apply inside multiline strings:
   def myfunction():
       text = '''This is indented in the code,
   but this line isn't.
       And this line is indented differently.'''
   # The actual string value contains the indentation as typed

MULTILINE STRINGS AS COMMENTS:
Since multiline strings aren't assigned to a variable, they can act as multiline comments:

"""
This is a multiline comment.
Python ignores this text because it's not assigned to anything.
Useful for:
- Describing what your program does
- Temporary notes
- Disabling multiple lines of code
"""

def function():
    '''
    This is a docstring - a multiline string used to document a function.
    Python has special support for docstrings.
    '''
    pass

WHEN TO USE MULTILINE STRINGS:
- Email templates
- SQL queries  
- HTML/XML content
- Long text messages
- Multi-line error messages
- Function documentation (docstrings)

===============================================================================
STRING INDEXING AND SLICING - EXTRACTING PARTS OF STRINGS
===============================================================================

CONCEPT: Strings behave like lists of characters. Each character has a position (index) that you can use to access it.

STRING INDEXING:

SYNTAX: string[index]

INDEX NUMBERING:
- Positive indexes start from 0 (first character)
- Negative indexes start from -1 (last character)

Example with 'Hello, world!':

Position:   0  1  2  3  4  5  6  7  8  9  10 11 12
Character:  H  e  l  l  o  ,     w  o  r  l  d  !
Negative:  -13-12-11-10 -9 -8 -7 -6 -5 -4 -3 -2 -1

greeting = 'Hello, world!'

Positive indexing:
greeting[0]    → 'H'   (first character)
greeting[4]    → 'o'   (fifth character)
greeting[7]    → 'w'   (space counts as a character!)

Negative indexing:
greeting[-1]   → '!'   (last character)
greeting[-2]   → 'd'   (second to last)
greeting[-13]  → 'H'   (same as index 0)

STRING SLICING:

SYNTAX: string[start:end]

SLICING RULES:
- Includes character at start index
- EXCLUDES character at end index
- Think of it as: start <= index < end

greeting = 'Hello, world!'

greeting[0:5]    → 'Hello'    # Characters 0, 1, 2, 3, 4 (not 5)
greeting[7:12]   → 'world'    # Characters 7, 8, 9, 10, 11 (not 12)

SHORTHAND SLICING:

Omit start (defaults to 0):
greeting[:5]     → 'Hello'    # Same as greeting[0:5]

Omit end (defaults to end of string):
greeting[7:]     → 'world!'   # From index 7 to the end

Omit both (copies entire string):
greeting[:]      → 'Hello, world!'

With negative indexes:
greeting[7:-1]   → 'world'    # From index 7 to second-to-last

IMPORTANT NOTE: Slicing does NOT modify the original string!
greeting = 'Hello, world!'
greeting[7:]     # Returns 'world!' but doesn't change greeting
print(greeting)  # Still 'Hello, world!'

WHY USE SLICING?
- Extract first name from "John Smith"
- Get file extension from "document.pdf"
- Process parts of data
- Validate format of strings

===============================================================================
THE IN AND NOT IN OPERATORS WITH STRINGS
===============================================================================

PURPOSE: Check if one string exists inside another string. Returns True or False (Boolean value).

SYNTAX:
substring in string      # Returns True if substring found
substring not in string  # Returns True if substring NOT found

HOW IT WORKS:
Python searches the entire string to see if the substring appears anywhere inside it.

EXAMPLES:

Basic usage:
'Hello' in 'Hello, World'        → True
'Hello' in 'Hello'               → True
'HELLO' in 'Hello, World'        → False  (case-sensitive!)
'cats' in 'cats and dogs'        → True

Checking if substring is missing:
'cats' not in 'cats and dogs'    → False (cats IS in there)
'mice' not in 'cats and dogs'    → True  (mice is NOT in there)

Empty string:
'' in 'spam'                     → True  (empty string is in everything!)

CASE SENSITIVITY:
The in operator is case-sensitive, meaning it treats uppercase and lowercase as different characters.

'hello' in 'Hello'               → False
'Hello' in 'Hello'               → True

PRACTICAL USES:

1. Validating user input:
   if '@' not in email:
       print('Invalid email address')

2. Checking for keywords:
   if 'error' in log_message.lower():
       send_alert()

3. Filtering data:
   if 'confidential' in document:
       require_authorization()

IMPORTANT NOTES:
- Returns Boolean (True/False), not the position
- Checks for substring anywhere in the string
- Case-sensitive by default
- Empty string is considered to be in all strings
- Exact match of characters (spaces matter!)

COMBINING WITH IF STATEMENTS:
This is very common in real programs:

name = input('Enter your name: ')
if 'Al' in name:
    print('Your name contains Al!')

===============================================================================
F-STRINGS - INSERTING VARIABLES INTO STRINGS
===============================================================================

WHAT ARE F-STRINGS?
F-strings (formatted string literals) are the simplest and most modern way to embed values from variables into strings. They were introduced in Python 3.6.

SYNTAX:
f'text {variable} more text'
f"text {expression} more text"

HOW TO CREATE F-STRINGS:
1. Put the letter 'f' (or 'F') before the opening quotation mark
2. Place variable names or expressions inside curly braces {}
3. Python automatically converts the values to strings and inserts them

BASIC EXAMPLES:

Using variables:
name = 'Al'
age = 4000
f'My name is {name}. I am {age} years old.'
# Result: 'My name is Al. I am 4000 years old.'

Using expressions:
f'In ten years I will be {age + 10}'
# Result: 'In ten years I will be 4010'

Multiple variables:
first = 'Alice'
last = 'Smith'
f'{first} {last}'
# Result: 'Alice Smith'

EXPRESSIONS IN F-STRINGS:
You can put any Python expression inside the curly braces:

Math operations:
price = 19.99
quantity = 3
f'Total cost: ${price * quantity}'
# Result: 'Total cost: $59.97'

Method calls:
name = 'alice'
f'Hello, {name.upper()}!'
# Result: 'Hello, ALICE!'

Conditional expressions:
score = 85
f'You {("passed" if score >= 60 else "failed")}'
# Result: 'You passed'

LITERAL CURLY BRACES:
What if you want actual curly braces in your output, not a variable?
Use double curly braces {{ and }}:

f'{{This will print curly braces}}'
# Result: '{This will print curly braces}'

f'The variable {{name}} is {name}'
# Result: 'The variable {name} is Al'

WHY USE F-STRINGS?
1. More readable than older methods
2. Less typing
3. Faster execution
4. Can use any expression, not just variables
5. Industry standard in modern Python

OLDER ALTERNATIVES (Still valid but less common):

1. % operator (printf-style):
   'My name is %s' % (name)
   'I am %s years old' % (age)

2. .format() method:
   'My name is {}'.format(name)
   'My name is {0} and I am {1} years old'.format(name, age)

WHEN TO USE EACH:
- F-strings: Default choice for Python 3.6+
- .format(): When working with older Python versions
- % operator: Legacy code or when matching C-style formatting

===============================================================================
USEFUL STRING METHODS - COMPLETE REFERENCE
===============================================================================

CONCEPT: String methods are functions that belong to string objects. They perform operations on the string and usually return a new string (the original is never modified because strings are immutable).

SYNTAX: string.method_name(arguments)

---
UPPER() AND LOWER() - CASE CONVERSION
---

PURPOSE: Convert all letters in a string to uppercase or lowercase

SYNTAX:
string.upper()  # Returns new string in UPPERCASE
string.lower()  # Returns new string in lowercase

EXAMPLES:
spam = 'Hello, world!'
spam.upper()  → 'HELLO, WORLD!'
spam.lower()  → 'hello, world!'

IMPORTANT: These return NEW strings - they don't modify the original!
spam = 'Hello, world!'
spam.upper()
print(spam)  # Still prints 'Hello, world!' (unchanged)

To save the result:
spam = spam.upper()  # Now spam contains 'HELLO, WORLD!'

PRACTICAL USE - CASE-INSENSITIVE COMPARISON:
Without lower():
name = input('Enter your name: ')  # User types "ALICE"
if name == 'alice':  # This is False because 'ALICE' != 'alice'
    print('Hello, Alice!')

With lower():
name = input('Enter your name: ')  # User types "ALICE"
if name.lower() == 'alice':  # This is True because 'alice' == 'alice'
    print('Hello, Alice!')

Real-world example:
feeling = input('How do you feel? ')
if feeling.lower() == 'great':
    print('I feel great too.')
# Works whether user types 'great', 'Great', 'GREAT', etc.

---
ISUPPER() AND ISLOWER() - CHECKING CASE
---

PURPOSE: Check if a string is all uppercase or all lowercase

RETURNS: Boolean (True or False)

RULES:
- Returns True only if string has at least one letter AND all letters are the specified case
- Returns False if string has no letters at all

SYNTAX:
string.isupper()  # True if all letters are uppercase
string.islower()  # True if all letters are lowercase

EXAMPLES:

isupper():
'HELLO'.isupper()           → True
'Hello'.isupper()           → False (has lowercase)
'HELLO123'.isupper()        → True (numbers don't count)
'   '.isupper()             → False (no letters)
'ABC_123'.isupper()         → True (underscore and numbers ignored)

islower():
'hello'.islower()           → True
'hello123'.islower()        → True
'Hello123'.islower()        → False (has uppercase H)
'12345'.islower()           → False (no letters at all)
'abc_def'.islower()         → True

NON-LETTER CHARACTERS:
Numbers, spaces, and punctuation are ignored - only letters matter:
'HELLO WORLD 123!'.isupper()  → True
'hello world 123!'.islower()  → True

PRACTICAL USE:
password = input('Enter password: ')
if not password.isupper() and not password.islower():
    print('Good! Mix of uppercase and lowercase.')
else:
    print('Weak password - use mixed case')

---
ISX() STRING METHODS - VALIDATION METHODS
---

These methods check string content and return True or False

METHOD: isalpha()
PURPOSE: Returns True if string consists ONLY of letters and isn't blank
USE CASE: Validate that input contains only letters (no numbers or symbols)

EXAMPLES:
'hello'.isalpha()           → True
'hello123'.isalpha()        → False (has numbers)
'hello world'.isalpha()     → False (has space)
''.isalpha()                → False (blank)

METHOD: isalnum()
PURPOSE: Returns True if string consists ONLY of letters and numbers and isn't blank  
USE CASE: Validate usernames, codes without special characters

EXAMPLES:
'hello123'.isalnum()        → True
'hello'.isalnum()           → True (letters only is OK)
'123'.isalnum()             → True (numbers only is OK)
'hello 123'.isalnum()       → False (has space)
'hello!'.isalnum()          → False (has punctuation)

METHOD: isdecimal()
PURPOSE: Returns True if string consists ONLY of numeric characters (0-9) and isn't blank
USE CASE: Validate that input is a number before converting with int()

EXAMPLES:
'123'.isdecimal()           → True
'123.45'.isdecimal()        → False (decimal point not allowed)
'-123'.isdecimal()          → False (minus sign not allowed)
'   123   '.isdecimal()     → False (spaces not allowed)
''.isdecimal()              → False (blank)

METHOD: isspace()
PURPOSE: Returns True if string consists ONLY of spaces, tabs, newlines and isn't blank
USE CASE: Check if string is only whitespace

EXAMPLES:
'   '.isspace()             → True
' \t\n'.isspace()           → True (space, tab, newline)
''.isspace()                → False (blank string)
'   hello   '.isspace()     → False (has letters)

METHOD: istitle()
PURPOSE: Returns True if string is in title case (each word starts with uppercase, followed by lowercase)
USE CASE: Validate proper name formatting

EXAMPLES:
'This Is Title Case'.istitle()  → True
'This Is title Case'.istitle()  → False ('title' not capitalized)
'THIS IS NOT'.istitle()         → False (all caps)
'this is not'.istitle()         → False (all lowercase)

PRACTICAL VALIDATION EXAMPLE:
while True:
    age = input('Enter your age: ')
    if age.isdecimal():
        break
    print('Please enter a number.')

---
STARTSWITH() AND ENDSWITH() - PATTERN MATCHING
---

PURPOSE: Check if a string begins or ends with a specified substring

RETURNS: Boolean (True or False)

SYNTAX:
string.startswith(substring)
string.endswith(substring)

EXAMPLES:

Basic usage:
'Hello, world!'.startswith('Hello')        → True
'Hello, world!'.startswith('H')            → True
'Hello, world!'.startswith('hello')        → False (case-sensitive!)

'Hello, world!'.endswith('world!')         → True
'Hello, world!'.endswith('!')              → True
'Hello, world!'.endswith('world')          → False (missing !)

Edge case - entire string:
'Hello, world!'.startswith('Hello, world!')  → True
'abc123'.endswith('abc123')                  → True

PRACTICAL USES:

1. File type checking:
   filename = 'document.pdf'
   if filename.endswith('.pdf'):
       print('This is a PDF file')

2. URL validation:
   url = 'https://www.google.com'
   if url.startswith('https://'):
       print('Secure connection')

3. Command processing:
   command = input('> ')
   if command.startswith('/'):
       process_special_command(command)

4. Data filtering:
   if line.startswith('#'):
       continue  # Skip comment lines

Multiple possible endings:
filename = 'photo.jpg'
if filename.endswith('.jpg') or filename.endswith('.png'):
    print('This is an image file')

Better way with tuple:
if filename.endswith(('.jpg', '.png', '.gif')):
    print('This is an image file')

---
JOIN() AND SPLIT() - CONVERTING BETWEEN STRINGS AND LISTS
---

JOIN() - COMBINE LIST INTO STRING

PURPOSE: Join a list of strings into a single string with a separator between each item

SYNTAX: separator.join(list_of_strings)

HOW IT WORKS: The string you call join() on becomes the separator placed between each list item

EXAMPLES:

With comma separator:
', '.join(['cats', 'rats', 'bats'])
# Result: 'cats, rats, bats'

With space separator:
' '.join(['My', 'name', 'is', 'Simon'])
# Result: 'My name is Simon'

With custom separator:
'ABC'.join(['My', 'name', 'is', 'Simon'])
# Result: 'MyABCnameABCisABCSimon'

With empty separator:
''.join(['a', 'b', 'c'])
# Result: 'abc'

With newline separator:
'\n'.join(['First line', 'Second line', 'Third line'])
# Result:
# First line
# Second line
# Third line

PRACTICAL USE - Creating CSV data:
names = ['Alice', 'Bob', 'Carol']
csv_line = ','.join(names)
# Result: 'Alice,Bob,Carol'

SPLIT() - BREAK STRING INTO LIST

PURPOSE: Split a string into a list of strings based on a separator

SYNTAX:
string.split()              # Split on whitespace (default)
string.split(separator)     # Split on specified separator

HOW IT WORKS:
- Finds all occurrences of the separator
- Breaks the string at those points
- Returns a list of the pieces (separator is removed)

EXAMPLES:

Default split (on whitespace):
'My name is Simon'.split()
# Result: ['My', 'name', 'is', 'Simon']

'   My   name   is   Simon   '.split()
# Result: ['My', 'name', 'is', 'Simon']  (extra spaces removed)

Custom separator:
'MyABCnameABCisABCSimon'.split('ABC')
# Result: ['My', 'name', 'is', 'Simon']

Split on newline:
text = 'First line\nSecond line\nThird line'
text.split('\n')
# Result: ['First line', 'Second line', 'Third line']

Split on comma (CSV parsing):
'apple,banana,cherry'.split(',')
# Result: ['apple', 'banana', 'cherry']

PRACTICAL USES:

1. Processing multi-line text:
   text = pyperclip.paste()
   lines = text.split('\n')
   for line in lines:
       process(line)

2. Parsing user input:
   coords = input('Enter x,y: ')  # User types: 10,20
   x, y = coords.split(',')

3. Word counting:
   text = 'Hello world'
   words = text.split()
   print(f'Word count: {len(words)}')  # Word count: 2

JOIN AND SPLIT ARE OPPOSITES:
original = 'cats, rats, bats'
list_version = original.split(', ')  # ['cats', 'rats', 'bats']
back_to_string = ', '.join(list_version)  # 'cats, rats, bats'

---
RJUST(), LJUST(), AND CENTER() - TEXT ALIGNMENT
---

PURPOSE: Add padding spaces to justify or center text within a specified width

SYNTAX:
string.rjust(width)           # Right-justify (pad on left)
string.ljust(width)           # Left-justify (pad on right)
string.center(width)          # Center (pad on both sides)

Optional fill character:
string.rjust(width, fillchar)
string.ljust(width, fillchar)
string.center(width, fillchar)

EXAMPLES:

Right-justify (padding on left):
'Hello'.rjust(10)
# Result: '     Hello' (5 spaces + Hello)

Left-justify (padding on right):
'Hello'.ljust(10)
# Result: 'Hello     ' (Hello + 5 spaces)

Center:
'Hello'.center(20)
# Result: '       Hello        ' (7 spaces + Hello + 8 spaces)

Custom fill character:
'Hello'.rjust(20, '*')
# Result: '***************Hello'

'Hello'.ljust(20, '-')
# Result: 'Hello---------------'

'Hello'.center(20, '=')
# Result: '=======Hello========'

If string is already longer than width:
'Hello'.rjust(3)
# Result: 'Hello' (unchanged - can't make it smaller)

PRACTICAL USE - FORMATTING OUTPUT:

def print_picnic(items_dict, left_width, right_width):
    print('PICNIC ITEMS'.center(left_width + right_width, '-'))
    for k, v in items_dict.items():
        print(k.ljust(left_width, '.') + str(v).rjust(right_width))

picnic_items = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
print_picnic(picnic_items, 12, 5)

Output:
---PICNIC ITEMS---
sandwiches..    4
apples......   12
cups........    4
cookies..... 8000

---
STRIP(), RSTRIP(), AND LSTRIP() - REMOVING WHITESPACE
---

PURPOSE: Remove whitespace characters from the beginning and/or end of a string

SYNTAX:
string.strip()      # Remove from both ends
string.lstrip()     # Remove from left (beginning) only
string.rstrip()     # Remove from right (end) only

Optional - specify characters to remove:
string.strip(chars)
string.lstrip(chars)
string.rstrip(chars)

WHITESPACE CHARACTERS: Spaces, tabs (\t), newlines (\n)

EXAMPLES:

Basic usage:
spam = '    Hello, World    '
spam.strip()   → 'Hello, World'
spam.lstrip()  → 'Hello, World    '
spam.rstrip()  → '    Hello, World'

With tabs and newlines:
'\t  Hello  \n'.strip()   → 'Hello'

IMPORTANT: Only removes from ENDS, not from middle!
'   Hello   World   '.strip()
# Result: 'Hello   World' (middle spaces preserved)

CUSTOM CHARACTERS:
You can specify which characters to remove instead of whitespace

spam = 'SpamSpamBaconSpamEggsSpamSpam'
spam.strip('ampS')
# Result: 'BaconSpamEggs'
# Removes any combination of 'a', 'm', 'p', 'S' from ends

'www.example.com'.strip('cmowz.')
# Result: 'example'
# Useful for cleaning URLs

PRACTICAL USES:

1. Clean user input:
   name = input('Enter your name: ').strip()
   # Removes accidental spaces user might type

2. Process file lines:
   with open('data.txt') as f:
       for line in f:
           line = line.strip()  # Remove newline and spaces
           process(line)

3. Clean CSV data:
   data = '  Alice  ,  Bob  ,  Carol  '
   names = [name.strip() for name in data.split(',')]
   # Result: ['Alice', 'Bob', 'Carol']

COMMON PATTERN:
user_input = input('Enter your email: ').strip().lower()
# 1. Remove accidental spaces
# 2. Convert to lowercase for comparison

---
ORD() AND CHR() - UNICODE CODE POINTS
---

PURPOSE: Convert between characters and their numeric Unicode code points

WHAT IS UNICODE?
Unicode is a standard that assigns a unique number to every character from every writing system in the world.

ORD() - CHARACTER TO NUMBER

SYNTAX: ord(character)
RETURNS: Integer (the Unicode code point)
PARAMETER: Must be a single character string

EXAMPLES:
ord('A')    → 65
ord('a')    → 97
ord('!')    → 33
ord('4')    → 52
ord(' ')    → 32

CHR() - NUMBER TO CHARACTER

SYNTAX: chr(code_point)
RETURNS: String (single character)
PARAMETER: Integer Unicode code point

EXAMPLES:
chr(65)     → 'A'
chr(97)     → 'a'
chr(33)     → '!'
chr(52)     → '4'

THEY'RE OPPOSITES:
chr(ord('A'))   → 'A'
ord(chr(65))    → 65

PRACTICAL USES:

1. Alphabetical comparison:
   ord('A') < ord('B')  → True
   # Used in sorting algorithms

2. Character shifting (like Caesar cipher):
   chr(ord('A') + 1)    → 'B'
   chr(ord('Z') + 1)    → '['  # Goes past Z!

3. Generating character ranges:
   for i in range(ord('A'), ord('Z') + 1):
       print(chr(i), end=' ')
   # Output: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

4. Checking character types:
   def is_uppercase(char):
       return ord('A') <= ord(char) <= ord('Z')

UNICODE FACTS:
- ASCII characters (0-127) are the same in Unicode
- A-Z: 65-90
- a-z: 97-122
- 0-9: 48-57
- Difference between uppercase and lowercase: 32
  ord('a') - ord('A') = 32

===============================================================================
COPYING AND PASTING WITH PYPERCLIP MODULE
===============================================================================

WHAT IS PYPERCLIP?
Pyperclip is a third-party Python module that lets your programs read and write to the computer's clipboard (copy/paste).

INSTALLATION:
Install using pip:
pip install pyperclip

Or in PowerShell:
python -m pip install pyperclip

IMPORTANT: This is NOT part of standard Python - you must install it separately!

AVAILABLE FUNCTIONS:

pyperclip.copy(text)
- Copies the specified text to the clipboard
- Same as pressing Ctrl-C or right-click → Copy
- Parameter: String to copy
- Returns: None

pyperclip.paste()
- Returns the current clipboard content as a string
- Same as pressing Ctrl-V or right-click → Paste
- No parameters
- Returns: String (current clipboard content)

BASIC EXAMPLES:

import pyperclip

# Copy text to clipboard
pyperclip.copy('Hello, world!')

# Get text from clipboard
text = pyperclip.paste()
print(text)  # 'Hello, world!'

PRACTICAL USE - PROCESSING CLIPBOARD TEXT:

# User copies some text manually (Ctrl-C)
# Program processes it and puts result back in clipboard

import pyperclip

text = pyperclip.paste()  # Get what user copied
text = text.upper()       # Process it
pyperclip.copy(text)      # Put result back in clipboard
# User can now paste the uppercase version

WORKFLOW PATTERN:
1. User selects and copies text from anywhere (email, website, document)
2. Runs Python script
3. Script processes clipboard content
4. Script puts result back in clipboard
5. User pastes result wherever they need it

WHY THIS IS POWERFUL:
- No need to save text to a file
- No need to type text into terminal
- Works with text from any source
- Fast workflow for text processing

===============================================================================
PROJECT: ADD BULLETS TO WIKI MARKUP
===============================================================================

PROBLEM:
You have a list of items in your clipboard. You want to add Wikipedia-style bullet points (* ) to the beginning of each line.

INPUT (in clipboard):
Lists of animals
Lists of aquarium life
Lists of biologists by author abbreviation

DESIRED OUTPUT (to clipboard):
* Lists of animals
* Lists of aquarium life
* Lists of biologists by author abbreviation

SOLUTION STRATEGY:
1. Paste text from clipboard
2. Split text into separate lines
3. Add '* ' to beginning of each line
4. Join lines back together
5. Copy result to clipboard

COMPLETE CODE (bulletPointAdder.py):

#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip

text = pyperclip.paste()

# Separate lines and add stars
lines = text.split('\n')
for i in range(len(lines)):  # Loop through all indexes in the lines list
    lines[i] = '* ' + lines[i]  # Add star to each string in lines list

text = '\n'.join(lines)

pyperclip.copy(text)

HOW TO USE:
1. Copy some text to clipboard (Ctrl-C)
2. Run the program: python bulletPointAdder.py
3. Paste result (Ctrl-V) - now has bullets!

STEP-BY-STEP BREAKDOWN:

Step 1: Get clipboard content
text = pyperclip.paste()
# If clipboard contains:
# "Lists of animals\nLists of aquarium life"

Step 2: Split into list
lines = text.split('\n')
# lines = ['Lists of animals', 'Lists of aquarium life']

Step 3: Add bullets
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]
# After loop:
# lines = ['* Lists of animals', '* Lists of aquarium life']

Step 4: Join back together
text = '\n'.join(lines)
# text = '* Lists of animals\n* Lists of aquarium life'

Step 5: Copy to clipboard
pyperclip.copy(text)

ALTERNATIVE APPROACHES:

Using list comprehension (more Pythonic):
lines = ['* ' + line for line in text.split('\n')]
text = '\n'.join(lines)

All in one line (advanced):
text = '\n'.join(['* ' + line for line in pyperclip.paste().split('\n')])
pyperclip.copy(text)

===============================================================================
PRACTICE QUESTIONS
===============================================================================

1. What are escape characters?

ANSWER: Escape characters let you use characters that are otherwise impossible to put in a string. An escape character consists of a backslash (\) followed by the character you want to insert.

2. What do the \n and \t escape characters represent?

ANSWER:
\n = Newline character (line break)
\t = Tab character

3. How can you put a \ backslash character in a string?

ANSWER: Use the \\ escape character. The first backslash escapes the second backslash so it appears as a literal backslash in the string.

4. The string value "Howl's Moving Castle" is a valid string. Why isn't it a problem that the single quote character in the word Howl's isn't escaped?

ANSWER: Because the string uses double quotes on the outside. Single quotes inside double-quoted strings don't need to be escaped. Only if the string used single quotes ('Howl's Moving Castle') would you need to escape: ('Howl\'s Moving Castle')

5. If you don't want to put \n in your string, how can you write a string with newlines in it?

ANSWER: Use a multiline string with triple quotes (''' or """). Press Enter to create actual line breaks in your code, and they'll be preserved in the string.

6. What do the following expressions evaluate to?
   - 'Hello, world!'[1]
   - 'Hello, world!'[0:5]
   - 'Hello, world!'[:5]
   - 'Hello, world!'[3:]

ANSWERS:
- 'Hello, world!'[1]    → 'e'  (character at index 1)
- 'Hello, world!'[0:5]  → 'Hello'  (characters 0-4)
- 'Hello, world!'[:5]   → 'Hello'  (same as [0:5])
- 'Hello, world!'[3:]   → 'lo, world!'  (from index 3 to end)

7. What do the following expressions evaluate to?
   - 'Hello'.upper()
   - 'Hello'.upper().isupper()
   - 'Hello'.upper().lower()

ANSWERS:
- 'Hello'.upper()              → 'HELLO'
- 'Hello'.upper().isupper()    → True  ('HELLO' is all uppercase)
- 'Hello'.upper().lower()      → 'hello'  (converts to upper then to lower)

8. What do the following expressions evaluate to?
   - 'Remember, remember, the fifth of November.'.split()
   - '-'.join('There can be only one.'.split())

ANSWERS:
- 'Remember, remember, the fifth of November.'.split()
  → ['Remember,', 'remember,', 'the', 'fifth', 'of', 'November.']

- '-'.join('There can be only one.'.split())
  → 'There-can-be-only-one.'
  (First splits into words, then joins with - separator)

9. What string methods can you use to right-justify, left-justify, and center a string?

ANSWER:
- rjust() - right-justify (pad left)
- ljust() - left-justify (pad right)
- center() - center (pad both sides)

10. How can you trim whitespace characters from the beginning or end of a string?

ANSWER: Use the strip() family of methods:
- strip() - remove from both ends
- lstrip() - remove from left (beginning)
- rstrip() - remove from right (end)

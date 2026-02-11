===============================================================================
IS 305 - CHAPTER 9: TEXT PATTERN MATCHING WITH REGULAR EXPRESSIONS
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

Regular expressions (called "regexes" for short) allow you to describe patterns for text that you want to match. With regular expressions, you can find text patterns without having to know the exact text you're searching for.

For example, instead of searching for the exact phone number "415-555-1234", you can search for the pattern "three digits, hyphen, three digits, hyphen, four digits" which will match ANY phone number.

This chapter covers:
- Finding text patterns without regular expressions (the hard way)
- Creating and using regular expression patterns
- Grouping parts of patterns with parentheses
- Matching optional patterns and repetitions
- Character classes for matching categories of characters
- The dot character for matching almost anything
- Greedy vs non-greedy matching
- Advanced regex features (anchors, word boundaries, flags)
- String substitution with regex
- Managing complex regex patterns

WHY THIS MATTERS:
- Validate input format (email addresses, phone numbers, zip codes)
- Extract specific data from large amounts of text
- Search log files for errors matching a pattern
- Parse and clean data
- Find and replace text with patterns
- Web scraping and data mining

Without regex, you'd need to write lots of complicated code to check every character. With regex, you can describe patterns in a single line.

===============================================================================
FINDING PATTERNS WITHOUT REGULAR EXPRESSIONS - THE HARD WAY
===============================================================================

PROBLEM: You want to find if a string is a US phone number (format: 415-555-1234)

THE HARD WAY - WITHOUT REGEX:

def isPhoneNumber(text):
    if len(text) != 12:
        return False  # Phone number must be exactly 12 characters
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False  # First 3 characters must be digits
    if text[3] != '-':
        return False  # Character at index 3 must be hyphen
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False  # Next 3 characters must be digits
    if text[7] != '-':
        return False  # Character at index 7 must be hyphen
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False  # Last 4 characters must be digits
    return True

TESTING IT:
print(isPhoneNumber('415-555-4242'))  # True
print(isPhoneNumber('Moshi moshi'))   # False

FINDING PHONE NUMBERS IN LONGER TEXT:
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)

Output:
Phone number found: 415-555-1011
Phone number found: 415-555-9999

PROBLEMS WITH THIS APPROACH:
1. LOTS OF CODE: 17 lines just to validate one simple pattern!
2. HARD TO READ: What pattern is this checking? Not obvious at a glance
3. INFLEXIBLE: Want to handle (415) 555-1234 format? Rewrite everything!
4. TEDIOUS: Want to add extension support? More complex code!
5. ERROR-PRONE: Easy to make off-by-one mistakes with indexes

THIS IS WHY WE NEED REGULAR EXPRESSIONS!

===============================================================================
FINDING PATTERNS WITH REGULAR EXPRESSIONS - THE EASY WAY
===============================================================================

THE SAME TASK WITH REGEX:

import re

phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())

Output:
Phone number found: 415-555-4242

JUST 3 LINES vs 17 LINES!

WHAT DOES r'\d{3}-\d{3}-\d{4}' MEAN?
Breaking it down:
- \d = "any digit" (0-9)
- {3} = "exactly 3 of the preceding pattern"
- - = "a literal hyphen"
- {4} = "exactly 4 of the preceding pattern"

So the pattern means: "3 digits, hyphen, 3 digits, hyphen, 4 digits"

BASIC REGEX WORKFLOW (4 STEPS):

1. Import the re module
   import re

2. Create a Regex object with re.compile()
   phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
   
   WHY THE 'r' PREFIX?
   - Makes it a raw string
   - Prevents Python from interpreting backslashes as escape characters
   - Required because regex patterns use lots of backslashes

3. Pass the string to search into the Regex object's search() method
   mo = phoneNumRegex.search('My number is 415-555-4242.')
   
   RETURNS: A Match object (stored in 'mo')
   - 'mo' is short for "match object" (common convention)
   - Returns None if pattern not found

4. Call the group() method on the Match object to get the matched text
   mo.group()  # Returns: '415-555-4242'

CHECKING IF PATTERN WAS FOUND:

mo = phoneNumRegex.search('Call me tomorrow.')
if mo is None:
    print('Phone number not found.')
else:
    print('Phone number found: ' + mo.group())

===============================================================================
GROUPING WITH PARENTHESES
===============================================================================

CONCEPT: Parentheses create "groups" in your regex pattern. This lets you extract specific parts of the match.

SYNTAX: Use ( ) to create groups

EXAMPLE - SEPARATING AREA CODE FROM REST OF NUMBER:

phoneNumRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo = phoneNumRegex.search('My number is 415-555-4242.')

PATTERN BREAKDOWN:
- (\d{3}) = Group 1: area code (3 digits)
- - = literal hyphen (not in a group)
- (\d{3}-\d{4}) = Group 2: main number (3 digits, hyphen, 4 digits)

ACCESSING GROUPS:

mo.group(1)  # '415' (first group - area code)
mo.group(2)  # '555-4242' (second group - main number)
mo.group(0)  # '415-555-4242' (entire match)
mo.group()   # '415-555-4242' (same as group(0))

GETTING ALL GROUPS AT ONCE:

mo.groups()  # ('415', '555-4242') - returns a tuple

MULTIPLE ASSIGNMENT:
areaCode, mainNumber = mo.groups()
print(areaCode)     # '415'
print(mainNumber)   # '555-4242'

MATCHING LITERAL PARENTHESES:

If you want to match actual parentheses characters, escape them with backslash:

phoneNumRegex = re.compile(r'(\(\d{3}\)) (\d{3}-\d{4})')
mo = phoneNumRegex.search('My phone number is (415) 555-4242.')

mo.group(1)  # '(415)' - includes the parentheses!
mo.group(2)  # '555-4242'

PATTERN BREAKDOWN:
- \( = literal opening parenthesis
- \d{3} = 3 digits
- \) = literal closing parenthesis
- The outer parentheses ( ) create the group
- The \( \) are the literal characters to match

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

MATCHING PART OF A PHRASE:

You can use parentheses to limit which part the | applies to:

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')

This matches:
- Batman
- Batmobile
- Batcopter
- Batbat

But NOT:
- man (must have 'Bat' prefix)
- mobile (must have 'Bat' prefix)

EXAMPLE:
mo = batRegex.search('Batmobile lost a wheel')
mo.group()   # 'Batmobile'
mo.group(1)  # 'mobile' (just the part in parentheses)

PATTERN BREAKDOWN:
- Bat = literal text "Bat"
- (man|mobile|copter|bat) = group that matches one of these four options

===============================================================================
OPTIONAL MATCHING WITH ?
===============================================================================

CONCEPT: The ? character means "match zero or one of the preceding group"
In other words: "this part is optional"

SYNTAX: (pattern)?

EXAMPLE - OPTIONAL "wo" IN BATWOMAN/BATMAN:

batRegex = re.compile(r'Bat(wo)?man')

This matches:
- Batman (wo appears 0 times)
- Batwoman (wo appears 1 time)

Does NOT match:
- Batwowowoman (wo appears more than 1 time)

TESTING:
mo1 = batRegex.search('The Adventures of Batman')
mo1.group()  # 'Batman'

mo2 = batRegex.search('The Adventures of Batwoman')
mo2.group()  # 'Batwoman'

PRACTICAL EXAMPLE - OPTIONAL AREA CODE:

phoneRegex = re.compile(r'(\d{3}-)?\d{3}-\d{4}')

This matches:
- 415-555-1234 (with area code)
- 555-1234 (without area code)

TESTING:
mo1 = phoneRegex.search('My number is 415-555-4242')
mo1.group()  # '415-555-4242'

mo2 = phoneRegex.search('My number is 555-4242')
mo2.group()  # '555-4242'

PATTERN BREAKDOWN:
- (\d{3}-)? = optional group (3 digits and hyphen)
- \d{3}-\d{4} = required (3 digits, hyphen, 4 digits)

IMPORTANT NOTE:
The ? makes the ENTIRE GROUP optional, not just the last character

r'Bat(wo)?man' means: Bat + optional(wo) + man
NOT: Bat + w + optional(o) + man

===============================================================================
MATCHING ZERO OR MORE WITH *
===============================================================================

CONCEPT: The * character means "match zero or more of the preceding group"
Think: "this part can appear any number of times, including not at all"

SYNTAX: (pattern)*

EXAMPLE:

batRegex = re.compile(r'Bat(wo)*man')

This matches:
- Batman (wo appears 0 times)
- Batwoman (wo appears 1 time)  
- Batwowowowoman (wo appears many times)

TESTING:
mo1 = batRegex.search('The Adventures of Batman')
mo1.group()  # 'Batman'

mo2 = batRegex.search('The Adventures of Batwoman')
mo2.group()  # 'Batwoman'

mo3 = batRegex.search('The Adventures of Batwowowowoman')
mo3.group()  # 'Batwowowowoman'

DIFFERENCE BETWEEN ? AND *:

?  = 0 or 1 times (optional, appears at most once)
*  = 0 or more times (optional, can appear many times)

EXAMPLES:

Pattern: r'Bat(wo)?man'
Matches: Batman, Batwoman
Doesn't match: Batwowoman

Pattern: r'Bat(wo)*man'
Matches: Batman, Batwoman, Batwowoman, Batwowowoman

===============================================================================
MATCHING ONE OR MORE WITH +
===============================================================================

CONCEPT: The + character means "match one or more of the preceding group"
Think: "this part must appear at least once, but can appear more"

SYNTAX: (pattern)+

DIFFERENCE FROM *:
* = zero or more (optional)
+ = one or more (required at least once)

EXAMPLE:

batRegex = re.compile(r'Bat(wo)+man')

This matches:
- Batwoman (wo appears 1 time)
- Batwowowowoman (wo appears many times)

Does NOT match:
- Batman (wo must appear at least once!)

TESTING:
mo1 = batRegex.search('The Adventures of Batwoman')
mo1.group()  # 'Batwoman'

mo2 = batRegex.search('The Adventures of Batwowowowoman')
mo2.group()  # 'Batwowowowoman'

mo3 = batRegex.search('The Adventures of Batman')
mo3 == None  # True - no match!

SUMMARY OF ?, *, +:

Symbol | Meaning              | Example    | Matches
-------|---------------------|------------|-------------------------
?      | 0 or 1 time         | r'Bat(wo)?man' | Batman, Batwoman
*      | 0 or more times     | r'Bat(wo)*man' | Batman, Batwoman, Batwowoman...
+      | 1 or more times     | r'Bat(wo)+man' | Batwoman, Batwowoman... (NOT Batman)

PRACTICAL EXAMPLE:

# Match numbers with at least one digit
numberRegex = re.compile(r'\d+')

'I have 42 apples'.match()  # Matches '42'
'I have no apples'.match()  # No match (needs at least one digit)

===============================================================================
MATCHING SPECIFIC REPETITIONS WITH CURLY BRACKETS
===============================================================================

CONCEPT: Curly brackets {} let you specify exactly how many times a pattern should repeat

SYNTAX OPTIONS:

{n}     = Match exactly n times
{n,}    = Match n or more times
{,m}    = Match 0 to m times
{n,m}   = Match at least n and at most m times

EXAMPLES:

EXACTLY 3 TIMES:
haRegex = re.compile(r'(Ha){3}')

Matches:
- HaHaHa (exactly 3 times)

Doesn't match:
- HaHa (only 2 times)
- HaHaHaHa (4 times - too many!)

Testing:
mo1 = haRegex.search('HaHaHa')
mo1.group()  # 'HaHaHa'

mo2 = haRegex.search('Ha')
mo2 == None  # True - not enough Ha's

AT LEAST 3 TIMES:
haRegex = re.compile(r'(Ha){3,}')

Matches:
- HaHaHa (exactly 3)
- HaHaHaHa (4 times)
- HaHaHaHaHa (5 times)
etc.

Doesn't match:
- HaHa (only 2 times)

AT MOST 3 TIMES:
haRegex = re.compile(r'(Ha){,3}')

Matches:
- '' (0 times)
- Ha (1 time)
- HaHa (2 times)
- HaHaHa (3 times)

Doesn't match:
- HaHaHaHa (4 times - too many!)

BETWEEN 3 AND 5 TIMES:
haRegex = re.compile(r'(Ha){3,5}')

Matches:
- HaHaHa (3 times)
- HaHaHaHa (4 times)
- HaHaHaHaHa (5 times)

Doesn't match:
- HaHa (only 2 times)
- HaHaHaHaHaHa (6 times - too many!)

PRACTICAL EXAMPLES:

Phone number (exactly 3 digits, then exactly 3 digits, then exactly 4 digits):
re.compile(r'\d{3}-\d{3}-\d{4}')

Zip code (exactly 5 digits):
re.compile(r'\d{5}')

Zip code with optional +4 extension (5 digits, optionally followed by hyphen and 4 more digits):
re.compile(r'\d{5}(-\d{4})?')

===============================================================================
GREEDY AND NON-GREEDY (LAZY) MATCHING
===============================================================================

CONCEPT: When a pattern can match different amounts of text, Python has to choose how much to match. By default, it's "greedy" - it matches as much as possible. You can make it "non-greedy" (lazy) to match as little as possible.

DEFAULT: GREEDY MATCHING

Greedy means: "Match the LONGEST possible string"

Example:
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo = greedyHaRegex.search('HaHaHaHaHa')
mo.group()  # 'HaHaHaHaHa' - matches all 5 Ha's (the maximum)

Pattern {3,5} means "between 3 and 5 times"
String has 5 Ha's
Greedy matching chooses 5 (the maximum possible)

NON-GREEDY (LAZY) MATCHING: ADD ?

Non-greedy means: "Match the SHORTEST possible string"

Syntax: Add ? after the quantifier

Example:
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')  # Note the ? after {3,5}
mo = nongreedyHaRegex.search('HaHaHaHaHa')
mo.group()  # 'HaHaHa' - matches only 3 Ha's (the minimum)

Pattern {3,5}? means "between 3 and 5 times, but prefer fewer"
String has 5 Ha's
Non-greedy matching chooses 3 (the minimum required)

SUMMARY:

Pattern    | Greedy or Lazy? | Meaning
-----------|----------------|-----------------------------------
{3,5}      | Greedy         | Match 3-5 times, prefer MORE
{3,5}?     | Lazy           | Match 3-5 times, prefer FEWER
+          | Greedy         | Match 1+ times, prefer MORE
+?         | Lazy           | Match 1+ times, prefer FEWER
*          | Greedy         | Match 0+ times, prefer MORE
*?         | Lazy           | Match 0+ times, prefer FEWER
?          | Already lazy   | Match 0-1 times (can't be more greedy!)

PRACTICAL EXAMPLE:

# Matching text in angle brackets
text = '<To serve man> for dinner.>'

greedyRegex = re.compile(r'<.*>')  # Greedy
mo = greedyRegex.search(text)
mo.group()  # '<To serve man> for dinner.>' - matches ALL text between first < and last >

nongreedyRegex = re.compile(r'<.*?>')  # Non-greedy
mo = nongreedyRegex.search(text)
mo.group()  # '<To serve man>' - matches FIRST complete <...> only

WHY THIS MATTERS:
- HTML/XML parsing: You want to match one tag at a time, not everything from first to last tag
- Extracting quoted strings: "hello" and "world" should be two matches, not one "hello" and "world"
- Most of the time, you want non-greedy matching for text extraction!

REMEMBER: The ? has TWO meanings depending on context:
1. After a group: makes the group optional - r'(text)?'
2. After a quantifier: makes matching non-greedy - r'(text)*?' or r'(text)+?' or r'(text){3,5}?'

===============================================================================
THE FINDALL() METHOD
===============================================================================

CONCEPT: search() returns the FIRST match only. findall() returns ALL matches.

search() vs findall():

METHOD: search()
- Returns: Match object (of first match)
- Use: When you want to find one match and extract groups
- Call .group() on the result

METHOD: findall()
- Returns: List of strings (all matches)
- Use: When you want to find all matches
- Already returns strings, no need for .group()

EXAMPLE WITHOUT GROUPS:

phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')

Using search():
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
mo.group()  # '415-555-9999' - only the FIRST match

Using findall():
matches = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
matches  # ['415-555-9999', '212-555-0000'] - ALL matches

EXAMPLE WITH GROUPS:

phoneNumRegex = re.compile(r'(\d{3})-(\d{3})-(\d{4})')

Using search() with groups:
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
mo.group()   # '415-555-9999'
mo.group(1)  # '415'
mo.group(2)  # '555'
mo.group(3)  # '9999'

Using findall() with groups:
matches = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
matches  # [('415', '555', '9999'), ('212', '555', '0000')]
# Returns list of TUPLES, one tuple per match

IMPORTANT DIFFERENCE:

No groups: findall() returns list of strings
['415-555-9999', '212-555-0000']

With groups: findall() returns list of tuples
[('415', '555', '9999'), ('212', '555', '0000')]

PROCESSING FINDALL RESULTS WITH GROUPS:

matches = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
for match in matches:
    areaCode = match[0]
    firstThree = match[1]
    lastFour = match[2]
    print(f'({areaCode}) {firstThree}-{lastFour}')

Output:
(415) 555-9999
(212) 555-0000

CHOOSING WHICH TO USE:

Use search() when:
- You only need the first match
- You want to use .group(1), .group(2), etc. to extract parts
- You need a Match object with more information

Use findall() when:
- You need all matches
- You want a simple list of results
- You're counting how many times a pattern appears

===============================================================================
CHARACTER CLASSES
===============================================================================

CONCEPT: Character classes are shorthand codes that match categories of characters.

COMMON CHARACTER CLASSES:

Code | Matches                                    | Equivalent to
-----|-------------------------------------------|------------------
\d   | Any numeric digit (0-9)                    | [0-9]
\D   | Any character that is NOT a numeric digit  | [^0-9]
\w   | Any letter, digit, or underscore           | [a-zA-Z0-9_]
\W   | Any character that is NOT \w               | [^a-zA-Z0-9_]
\s   | Any whitespace (space, tab, newline)       | [ \t\n\r\f\v]
\S   | Any character that is NOT whitespace       | [^ \t\n\r\f\v]

IMPORTANT: Uppercase versions are the OPPOSITE (negative) of lowercase

EXAMPLES:

\d - Digits:
regex = re.compile(r'\d+')
regex.findall('12 drummers, 11 pipers, 10 lords')
# ['12', '11', '10']

\D - Non-digits:
regex = re.compile(r'\D+')
regex.findall('12 drummers, 11 pipers, 10 lords')
# [' drummers, ', ' pipers, ', ' lords']

\w - Word characters:
regex = re.compile(r'\w+')
regex.findall('Hello_world, how are you?')
# ['Hello_world', 'how', 'are', 'you']

\s - Whitespace:
regex = re.compile(r'\s+')
regex.findall('Hello   world\thow\nare   you')
# ['   ', '\t', '\n', '   ']

COMBINING CHARACTER CLASSES:

Example - Match number followed by space followed by word:
xmasRegex = re.compile(r'\d+\s\w+')
xmasRegex.findall('12 drummers, 11 pipers, 10 lords')
# ['12 drummers', '11 pipers', '10 lords']

Pattern breakdown:
- \d+ = one or more digits
- \s = whitespace character
- \w+ = one or more word characters

CREATING YOUR OWN CHARACTER CLASS:

SYNTAX: Use square brackets [ ]

Examples:

Vowels only:
vowelRegex = re.compile(r'[aeiouAEIOU]')
vowelRegex.findall('RoboCop eats baby food.')
# ['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o']

Consonants (using negative class - note the ^):
consonantRegex = re.compile(r'[^aeiouAEIOU]')
consonantRegex.findall('RoboCop eats baby food.')
# ['R', 'b', 'C', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.']

The ^ inside brackets means "NOT"

Alphanumeric only:
alphanumRegex = re.compile(r'[a-zA-Z0-9]+')

CHARACTER RANGES:

[a-z] = any lowercase letter
[A-Z] = any uppercase letter
[0-9] = any digit (same as \d)
[a-zA-Z] = any letter
[a-zA-Z0-9] = any letter or digit (almost same as \w, but \w includes _)

NEGATIVE CHARACTER CLASS:

[^abc] = anything EXCEPT a, b, or c
[^0-9] = anything EXCEPT digits (same as \D)
[^aeiou] = anything EXCEPT lowercase vowels

IMPORTANT: The ^ only has special meaning at the START of the brackets
[abc^] = matches a, b, c, or the literal ^ character

===============================================================================
THE DOT CHARACTER - MATCHING (ALMOST) ANYTHING
===============================================================================

CONCEPT: The . (dot) character matches any single character except a newline.

SYNTAX: .

EXAMPLES:

Basic usage:
atRegex = re.compile(r'.at')
atRegex.findall('The cat in the hat sat on the flat mat.')
# ['cat', 'hat', 'sat', 'lat', 'mat']
# Note: Matches 'flat' but only returns 'lat' (one character before 'at')

Pattern breakdown:
- . = any single character
- at = literal 'at'
- Together: any character followed by 'at'

Matching whole words:
regex = re.compile(r'.an')
regex.findall('ban can fan man pan ran tan van')
# ['ban', 'can', 'fan', 'man', 'pan', 'ran', 'tan', 'van']

MATCHING EVERYTHING: .*

Combining . and *:
.* = "zero or more of any character" = "match everything"

Example - Extracting name from formatted string:
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
mo.group(1)  # 'Al'
mo.group(2)  # 'Sweigart'

Pattern breakdown:
- First Name: = literal text
- (.*) = group that captures any characters
- Last Name: = literal text
- (.*) = group that captures any characters

GREEDY VS NON-GREEDY WITH .*:

Greedy .* (matches as much as possible):
greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
mo.group()  # '<To serve man> for dinner.>' - from first < to last >

Non-greedy .*? (matches as little as possible):
nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
mo.group()  # '<To serve man>' - from first < to first >

WHAT DOT DOESN'T MATCH: NEWLINES

By default, . matches everything EXCEPT newline (\n)

regex = re.compile(r'.*')
regex.search('Serve the public trust.\nProtect the innocent.').group()
# 'Serve the public trust.' - stops at the newline

To make . match newlines too, use re.DOTALL flag (covered later)

MATCHING A LITERAL DOT:

Use \. to match an actual period:

atRegex = re.compile(r'.at')    # Matches cat, hat, @at, !at
atRegex = re.compile(r'\.at')   # Matches only .at

Example - matching file extensions:
fileRegex = re.compile(r'.*\.txt')
fileRegex.findall('data.txt config.txt readme.md')
# ['data.txt', 'config.txt']

===============================================================================
MATCHING NEWLINES WITH re.DOTALL
===============================================================================

PROBLEM: By default, . matches everything EXCEPT newlines (\n)

SOLUTION: Pass re.DOTALL as second argument to re.compile()

WITHOUT re.DOTALL:

noNewlineRegex = re.compile('.*')
mo = noNewlineRegex.search('Serve the public trust.\nProtect the innocent.')
mo.group()  # 'Serve the public trust.' - stops at \n

WITH re.DOTALL:

newlineRegex = re.compile('.*', re.DOTALL)
mo = newlineRegex.search('Serve the public trust.\nProtect the innocent.')
mo.group()  # 'Serve the public trust.\nProtect the innocent.' - includes everything!

PRACTICAL USE - MATCHING MULTI-LINE TEXT:

# Extract all text between opening and closing tags
htmlRegex = re.compile(r'<div>(.*?)</div>', re.DOTALL)
html = '''<div>
Line 1
Line 2
Line 3
</div>'''
mo = htmlRegex.search(html)
mo.group(1)  # '\nLine 1\nLine 2\nLine 3\n'

Without re.DOTALL, this wouldn't work because . would stop at the first newline!

===============================================================================
ANCHORS: ^ AND $ - MATCHING START AND END
===============================================================================

CONCEPT: Anchors don't match characters - they match positions in the string

^ (caret) = Matches at the BEGINNING of the string
$ (dollar) = Matches at the END of the string

MATCHING AT THE BEGINNING: ^

beginsWithHelloRegex = re.compile(r'^Hello')

beginsWithHelloRegex.search('Hello, world!')  # Match object
beginsWithHelloRegex.search('He said Hello.')  # None - doesn't start with Hello

MATCHING AT THE END: $

endsWithNumberRegex = re.compile(r'\d$')

endsWithNumberRegex.search('Your number is 42')  # Match object
endsWithNumberRegex.search('Your number is forty two.')  # None - doesn't end with digit

MATCHING THE ENTIRE STRING: ^....$

Combining ^ and $ means "the ENTIRE string must match this pattern"

wholeStringIsNumRegex = re.compile(r'^\d+$')

wholeStringIsNumRegex.search('1234567890')  # Match - entire string is digits
wholeStringIsNumRegex.search('12345xyz67890')  # None - has non-digits
wholeStringIsNumRegex.search('x1234567890')  # None - doesn't start with digit

PRACTICAL EXAMPLES:

Validate that entire input is a phone number:
phoneRegex = re.compile(r'^\d{3}-\d{3}-\d{4}$')
phoneRegex.search('415-555-1234')  # Match
phoneRegex.search('My number is 415-555-1234')  # None - has extra text

Validate entire input is a number:
numberRegex = re.compile(r'^\d+$')
numberRegex.search('12345')  # Match
numberRegex.search('12345 ')  # None - has trailing space

IMPORTANT: ^ has DIFFERENT meanings in different contexts:

At start of regex: r'^Hello' = matches beginning of string
Inside brackets: r'[^aeiou]' = negative character class (NOT a vowel)

===============================================================================
WORD BOUNDARIES: \b
===============================================================================

CONCEPT: \b matches at a word boundary - the position between a word character (\w) and a non-word character

WORD CHARACTER: Letters, digits, underscore [a-zA-Z0-9_]
NON-WORD CHARACTER: Everything else (spaces, punctuation, etc.)

USE CASE: Match complete words only, not parts of larger words

EXAMPLE WITHOUT \b:

catRegex = re.compile(r'cat')
catRegex.findall('The cat scattered concatenated cats')
# ['cat', 'cat', 'cat', 'cat'] - matches "cat" everywhere, even inside words!

EXAMPLE WITH \b:

catRegex = re.compile(r'\bcat\b')
catRegex.findall('The cat scattered concatenated cats')
# ['cat'] - only matches the standalone word "cat"

PATTERN BREAKDOWN:
- \b = word boundary
- cat = literal 'cat'
- \b = word boundary

So it matches 'cat' only when it's a complete word

MORE EXAMPLES:

# Match "test" as a complete word
regex = re.compile(r'\btest\b')
regex.search('This is a test')  # Matches
regex.search('This is testing')  # No match - "test" is part of "testing"
regex.search('retest')  # No match - "test" is part of "retest"

# Match words ending in "ing"
regex = re.compile(r'\w+ing\b')
regex.findall('I am running and jumping')  # ['running', 'jumping']

# Match words starting with capital letter
regex = re.compile(r'\b[A-Z]\w+\b')
regex.findall('Alice and Bob went to Paris')  # ['Alice', 'Bob', 'Paris']

IMPORTANT: Word boundaries are "zero-width" - they don't consume characters
They just assert "a boundary exists here"

===============================================================================
CASE-INSENSITIVE MATCHING: re.IGNORECASE
===============================================================================

PROBLEM: By default, regex is case-sensitive

'robocop' != 'RoboCop' != 'ROBOCOP'

SOLUTION: Pass re.IGNORECASE or re.I as second argument to re.compile()

WITHOUT re.IGNORECASE:

regex = re.compile(r'robocop')
regex.search('RoboCop is part man, part machine, all cop.')  # None - doesn't match!

WITH re.IGNORECASE:

robocopRegex = re.compile(r'robocop', re.IGNORECASE)
# OR shorter:
robocopRegex = re.compile(r'robocop', re.I)

robocopRegex.search('RoboCop is part man, part machine, all cop.')  # Match!
robocopRegex.search('ROBOCOP protects the innocent.')  # Match!
robocopRegex.search('Why is Robocop eating baby food?')  # Match!

PRACTICAL USES:

# Accept "yes", "Yes", "YES", etc.
yesRegex = re.compile(r'yes', re.I)
if yesRegex.search(userInput):
    print('User confirmed!')

# Find all occurrences of "python" regardless of case
pythonRegex = re.compile(r'python', re.I)
pythonRegex.findall('Python is great! I love PYTHON. Learn python today.')
# ['Python', 'PYTHON', 'python']

===============================================================================
SUBSTITUTING STRINGS WITH sub()
===============================================================================

CONCEPT: Replace parts of strings that match a pattern

METHOD: regex.sub(replacement, string)

RETURNS: New string with replacements made

BASIC EXAMPLE:

namesRegex = re.compile(r'Agent \w+')
namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
# Result: 'CENSORED gave the secret documents to CENSORED.'

HOW IT WORKS:
1. Finds all matches of the pattern
2. Replaces each match with the replacement string
3. Returns the new string

USING GROUPS IN REPLACEMENT:

You can refer to groups in the replacement string using \1, \2, etc.

agentNamesRegex = re.compile(r'Agent (\w)\w*')
agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew.')
# Result: 'A**** told C**** that E**** knew.'

PATTERN BREAKDOWN:
- Agent = literal text
- (\w) = group 1: first letter of name
- \w* = rest of the name (not in a group, so not captured)

REPLACEMENT BREAKDOWN:
- \1 = first captured group (the first letter)
- **** = literal asterisks

MORE EXAMPLES:

# Redact phone numbers
phoneRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
phoneRegex.sub('XXX-XXX-XXXX', 'Call me at 415-555-1234 or 510-555-9999.')
# 'Call me at XXX-XXX-XXXX or XXX-XXX-XXXX.'

# Swap first and last name
nameRegex = re.compile(r'(\w+) (\w+)')
nameRegex.sub(r'\2, \1', 'Alice Smith')
# 'Smith, Alice'

# Remove all digits
digitRegex = re.compile(r'\d+')
digitRegex.sub('', 'I have 42 apples and 17 oranges.')
# 'I have  apples and  oranges.'

IMPORTANT: sub() doesn't modify the original string - it returns a new one

text = 'Hello World'
newText = re.compile(r'World').sub('Python', text)
print(text)  # 'Hello World' (unchanged)
print(newText)  # 'Hello Python'

===============================================================================
MANAGING COMPLEX REGEXES: re.VERBOSE
===============================================================================

PROBLEM: Complex regex patterns are hard to read

Example:
phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')
# What does this even match?!

SOLUTION: Use re.VERBOSE to write multi-line regex with comments

SYNTAX: Pass re.VERBOSE as second argument, write pattern with line breaks and comments

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)

BENEFITS:
1. Multi-line format is easier to read
2. Comments explain each part
3. Whitespace is ignored (except in character classes)
4. Much easier to maintain and debug!

IMPORTANT NOTES ABOUT re.VERBOSE:

1. Whitespace is ignored (except in character classes):
   r'\d{3} - \d{3}' in verbose mode = r'\d{3}-\d{3}' normally
   
2. Use triple quotes for multi-line strings: '''pattern'''

3. Comments use # (everything after # on that line is ignored)

4. To match actual spaces, use \s or put space in character class [ ]

ANOTHER EXAMPLE:

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+      # username
    @                      # @ symbol
    [a-zA-Z0-9.-]+         # domain name
    (\.[a-zA-Z]{2,4})      # dot-something
    )''', re.VERBOSE)

Much clearer than:
emailRegex = re.compile(r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,4}))')

===============================================================================
COMBINING MULTIPLE FLAGS
===============================================================================

PROBLEM: What if you want re.IGNORECASE AND re.DOTALL AND re.VERBOSE?

SOLUTION: Combine flags using the | (pipe) character

SYNTAX:
re.compile(pattern, flag1 | flag2 | flag3)

EXAMPLES:

Case-insensitive and verbose:
someRegex = re.compile(r'''
    [a-z]+    # one or more letters
    ''', re.IGNORECASE | re.VERBOSE)

All three common flags:
someRegex = re.compile(r'''
    <div>     # opening tag
    .*        # any content (including newlines)
    </div>    # closing tag
    ''', re.IGNORECASE | re.DOTALL | re.VERBOSE)

Case-insensitive and dot-matches-newline:
someRegex = re.compile(r'hello.*world', re.I | re.DOTALL)

COMMON FLAGS SUMMARY:

Flag         | Short | Purpose
-------------|-------|----------------------------------
re.IGNORECASE| re.I  | Case-insensitive matching
re.DOTALL    | re.S  | . matches newlines too
re.VERBOSE   | re.X  | Allow comments and whitespace
re.MULTILINE | re.M  | ^ and $ match line starts/ends

EXAMPLE WITH ALL FLAGS:

complexRegex = re.compile(r'''
    ^           # start of line
    hello       # literal text (case-insensitive)
    .*          # any content (including newlines)
    world       # literal text (case-insensitive)
    $           # end of line
    ''', re.IGNORECASE | re.DOTALL | re.VERBOSE | re.MULTILINE)

===============================================================================
PRACTICE QUESTIONS
===============================================================================

1. What is the function that creates Regex objects?

ANSWER: re.compile()

Example: phoneRegex = re.compile(r'\d{3}-\d{3}-\d{4}')

2. Why are raw strings often used when creating Regex objects?

ANSWER: Raw strings (with r prefix) are used because regex patterns contain many backslashes, and raw strings treat backslashes as literal characters instead of escape characters. Without raw strings, you'd have to escape every backslash: '\\d{3}-\\d{3}-\\d{4}' instead of r'\d{3}-\d{3}-\d{4}'

3. What does the search() method return?

ANSWER: The search() method returns a Match object if the pattern is found, or None if the pattern is not found.

4. How do you get the actual strings that match the pattern from a Match object?

ANSWER: Call the .group() method on the Match object.

Example:
mo = phoneRegex.search('Call me at 415-555-1234')
mo.group()  # Returns '415-555-1234'

5. In the regex created from r'(\d\d\d)-(\d\d\d-\d\d\d\d)', what does group 0 cover? Group 1? Group 2?

ANSWER:
- Group 0: The entire match '415-555-1234'
- Group 1: The first set of parentheses '415'
- Group 2: The second set of parentheses '555-1234'

6. Parentheses and periods have specific meanings in regular expression syntax. How would you specify that you want a regex to match actual parentheses and period characters?

ANSWER: Use backslashes to escape them: \( \) and \.

Example: r'\(\d{3}\) \d{3}-\d{4}' matches (415) 555-1234

7. The findall() method returns a list of strings or a list of tuples of strings. What makes it return one or the other?

ANSWER:
- If the regex has NO groups: returns list of strings
- If the regex has groups: returns list of tuples (one tuple per match)

Example without groups:
re.compile(r'\d{3}-\d{3}-\d{4}').findall('415-555-1234 and 510-555-9999')
Returns: ['415-555-1234', '510-555-9999']

Example with groups:
re.compile(r'(\d{3})-(\d{3}-\d{4})').findall('415-555-1234 and 510-555-9999')
Returns: [('415', '555-1234'), ('510', '555-9999')]

8. What does the | character signify in regular expressions?

ANSWER: The | (pipe) character means "or" - it matches one of multiple alternative patterns.

Example: r'cat|dog' matches either 'cat' or 'dog'
Example: r'Bat(man|mobile|copter)' matches 'Batman', 'Batmobile', or 'Batcopter'

9. What two things does the ? character signify in regular expressions?

ANSWER: The ? has two different meanings:
1. After a group: makes that group optional (match 0 or 1 time)
   Example: r'Bat(wo)?man' matches 'Batman' or 'Batwoman'
   
2. After a quantifier: makes matching non-greedy (match as little as possible)
   Example: r'<.*?>' matches '<To serve>' in '<To serve> for <dinner>' instead of the whole string

10. What is the difference between the + and * characters in regular expressions?

ANSWER:
- + means "one or more" (must appear at least once)
- * means "zero or more" (optional, can appear any number of times)

Example: r'Bat(wo)+man' matches 'Batwoman' but NOT 'Batman'
Example: r'Bat(wo)*man' matches both 'Batman' AND 'Batwoman'

11. What is the difference between {3} and {3,5} in regular expressions?

ANSWER:
- {3} means "exactly 3 times" (no more, no less)
- {3,5} means "between 3 and 5 times" (minimum 3, maximum 5)

Example: r'(Ha){3}' matches 'HaHaHa' only
Example: r'(Ha){3,5}' matches 'HaHaHa', 'HaHaHaHa', or 'HaHaHaHaHa'

12. What do the \d, \w, and \s shorthand character classes signify in regular expressions?

ANSWER:
- \d = any digit (0-9)
- \w = any word character (letter, digit, or underscore) [a-zA-Z0-9_]
- \s = any whitespace character (space, tab, newline)

13. What do the \D, \W, and \S shorthand character classes signify in regular expressions?

ANSWER: Uppercase versions are the OPPOSITE (negative) of lowercase:
- \D = any character that is NOT a digit
- \W = any character that is NOT a word character
- \S = any character that is NOT whitespace

14. What is the difference between .* and .*?  ?

ANSWER:
- .* is greedy - matches as much text as possible
- .*? is non-greedy (lazy) - matches as little text as possible

Example with '<To serve man> for dinner.>':
- .* in r'<.*>' matches '<To serve man> for dinner.>' (everything from first < to last >)
- .*? in r'<.*?>' matches '<To serve man>' (minimum from first < to first >)

15. What is the character class syntax to match all numbers and lowercase letters?

ANSWER: [0-9a-z] or [a-z0-9]

You can also use: [a-z\d] (combining custom class with \d shorthand)

16. How do you make a regular expression case-insensitive?

ANSWER: Pass re.IGNORECASE or re.I as the second argument to re.compile()

Example:
regex = re.compile(r'robocop', re.IGNORECASE)
# or
regex = re.compile(r'robocop', re.I)

17. What does the . character normally match? What does it match if re.DOTALL is passed as the second argument to re.compile()?

ANSWER:
- Normally: . matches any character EXCEPT newline (\n)
- With re.DOTALL: . matches any character INCLUDING newline

18. What is the difference between these two:
    r'(\d\d\d)-(\d\d\d-\d\d\d\d)' and r'\((\d\d\d)\)-(\d\d\d-\d\d\d\d)' ?

ANSWER:
- r'(\d\d\d)-(\d\d\d-\d\d\d\d)' matches: 415-555-1234
- r'\((\d\d\d)\)-(\d\d\d-\d\d\d\d)' matches: (415)-555-1234

The second pattern uses \( and \) to match literal parentheses characters.

19. If numRegex = re.compile(r'\d+'), what will numRegex.sub('X', '12 drummers, 11 pipers, five rings, 3 hens') return?

ANSWER: 'X drummers, X pipers, five rings, X hens'

Explanation: The regex \d+ matches one or more digits. The sub() method replaces each match with 'X'. The numbers 12, 11, and 3 are replaced. "five" is not replaced because it's a word, not digits.

import re

'''
# PIPE OPERATOR - | means "OR"
# Matches first occurrence of Batman OR Tina Fey
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1.group())

mo2 = heroRegex.search('Tina Fey and Batman.')
print(mo2.group())

print()  # blank line

# PIPE WITH GROUPS - () limits where the | applies
# Bat(man|mobile|copter|bat) matches Bat + (man OR mobile OR copter OR bat)
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())    # Full match
print(mo.group(1))   # Just the group part
'''

'''
# OPTIONAL MATCHING - ? means "0 or 1 time"
# (wo)? makes "wo" optional
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

# (\d\d\d-)? makes area code optional
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 415-555-4242')
print(mo1.group())

mo2 = phoneRegex.search('My number is 555-4242')
print(mo2.group())
'''

'''
# ZERO OR MORE - * means "0 or more times"
# (wo)* matches Batman, Batwoman, Batwowowowoman, etc.
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group())
'''

'''
# ONE OR MORE - + means "1 or more times" (NOT zero)
# (wo)+ matches Batwoman, Batwowowowoman, but NOT Batman
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1)  # None - needs at least one "wo"

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())

mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group())
'''

'''
# SPECIFIC REPETITIONS - {n} means "exactly n times"
# {3} matches exactly 3 repetitions
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())

mo2 = haRegex.search('Ha')
print(mo2)

# RANGE REPETITIONS - {min,max} means "between min and max times"
# {3,5} matches 3, 4, or 5 repetitions
haRegex = re.compile(r'(Ha){3,5}')
mo1 = haRegex.search('HaHaHaHaHa')
print(mo1.group())

mo2 = haRegex.search('HaHa')
print(mo2)
'''

'''
# Character classes - shortcuts for common patterns
# \d = any digit (0-9)
# \w = any word character (letters, digits, underscore)
# \s = any whitespace (space, tab, newline)

# \d for digits
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneRegex.search('My number is 415-555-1234.')
print(mo.group())

# \w for word characters (letters, digits, underscore)
nameRegex = re.compile(r'\w+')
mo = nameRegex.search('Hello there!')
print(mo.group())

# \s for whitespace (space, tab, newline)
spaceRegex = re.compile(r'\w+\s\w+')
mo = spaceRegex.search('Hello there!')
print(mo.group())
'''

'''
# NEGATIVE CHARACTER CLASSES (capital letters = NOT)
# \D = NOT a digit (opposite of \d)
# \W = NOT a word character (opposite of \w)
# \S = NOT whitespace (opposite of \s)

notDigitRegex = re.compile(r'\D+')
mo = notDigitRegex.search('123abc456')
print(mo.group())

# CUSTOM CHARACTER CLASSES - [abc] matches a, b, or c
vowelRegex = re.compile(r'[aeiouAEIOU]')
mo = vowelRegex.search('RoboCop eats baby food.')
print(mo.group())

# RANGE - [a-z] matches lowercase letters, [0-5] matches 0 through 5
letterRegex = re.compile(r'[a-zA-Z]+')
mo = letterRegex.search('123abc456DEF')
print(mo.group())
'''

'''
# FINDALL() METHOD - finds ALL matches, not just first
# Returns a list of strings

# .search() returns first match only
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneRegex.search('Cell: 415-555-1234 Work: 212-555-0000')
print(mo.group())

# .findall() returns ALL matches as a list
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
result = phoneRegex.findall('Cell: 415-555-1234 Work: 212-555-0000')
print(result)

# .findall() with groups returns list of tuples
phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
result = phoneRegex.findall('Cell: 415-555-1234 Work: 212-555-0000')
print(result)
'''

'''
# SUB() METHOD - substitute/replace matches with new text
# .sub(replacement, string) finds pattern and replaces it

# Replace names with CENSORED
namesRegex = re.compile(r'Agent \w+')
result = namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
print(result)

# Use groups to keep part of the match
# \1, \2, etc. refer to groups in the pattern
phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
result = phoneRegex.sub(r'(\1) \2', 'My number is 415-555-1234')
print(result)
'''

# GREEDY vs NON-GREEDY MATCHING
# Greedy (default) - matches as much as possible
greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner>')
print(mo.group())

# Non-greedy - add ? after * or + to match as little as possible
nonGreedyRegex = re.compile(r'<.*?>')
mo = nonGreedyRegex.search('<To serve man> for dinner>')
print(mo.group())

# DOT WILDCARD - . matches any character except newline
atRegex = re.compile(r'.at')
result = atRegex.findall('The cat in the hat sat on the flat mat.')
print(result)

# CASE-INSENSITIVE MATCHING - re.IGNORECASE or re.I flag
regex = re.compile(r'robocop', re.IGNORECASE)
mo = regex.search('RoboCop is part man, part machine, all cop.')
print(mo.group())

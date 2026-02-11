# CHAPTER 9 - SECTION 7: FLAGS AND SUB() METHOD

# What: Flags modify regex behavior, sub() substitutes matches
# Why: Case-insensitive matching, replace text with regex
# How: re.IGNORECASE, re.DOTALL, re.VERBOSE, .sub()

import re

# re.IGNORECASE (re.I) - case-insensitive matching
regex = re.compile(r'robocop', re.IGNORECASE)
match1 = regex.search('RoboCop is part man, part machine, all cop.')
print(match1.group())  # RoboCop

match2 = regex.search('ROBOCOP protects the innocent.')
print(match2.group())  # ROBOCOP

# re.DOTALL (re.S) - dot matches newlines too
no_newline_regex = re.compile(r'.*')
match = no_newline_regex.search('Serve.\nProtect.')
print(match.group())  # Serve. (stops at newline)

newline_regex = re.compile(r'.*', re.DOTALL)
match = newline_regex.search('Serve.\nProtect.')
print(match.group())  # Serve.\nProtect. (includes newline)

# re.VERBOSE (re.X) - ignore whitespace and comments in regex
# Makes complex regex readable
phone_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?      # area code (optional)
    (\s|-|\.)?              # separator
    \d{3}                   # first 3 digits
    (\s|-|\.)               # separator
    \d{4}                   # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension (optional)
    )''', re.VERBOSE)

# Combine multiple flags with pipe |
regex = re.compile(r'robocop', re.IGNORECASE | re.DOTALL | re.VERBOSE)

# sub() method - substitute/replace matches
names_regex = re.compile(r'Agent \w+')
result = names_regex.sub('CENSORED', 'Agent Alice gave documents to Agent Bob.')
print(result)  # CENSORED gave documents to CENSORED.

# Use groups in replacement
# \1, \2, etc. refer to groups
agent_regex = re.compile(r'Agent (\w)\w*')
result = agent_regex.sub(r'\1****', 'Agent Alice told Agent Carol')
print(result)  # A**** told C****

# Pass function to sub() for complex replacements
def reverse_name(match):
    return match.group(0)[::-1]

regex = re.compile(r'Agent \w+')
result = regex.sub(reverse_name, 'Agent Alice gave documents to Agent Bob.')
print(result)  # ecilA tnegA gave documents to boB tnegA.

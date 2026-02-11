# CHAPTER 9 - SECTION 4: FINDALL() METHOD

# What: findall() returns ALL matches, not just first one
# Why: search() only finds first match, findall() finds all
# How: Returns list of strings (or tuples if groups)

import re

# search() finds FIRST match only
phone_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
match = phone_regex.search('Cell: 415-555-9999 Work: 212-555-0000')
print(match.group())  # 415-555-9999 (only first)

# findall() finds ALL matches
matches = phone_regex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(matches)  # ['415-555-9999', '212-555-0000']

# Without groups - returns list of strings
regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
result = regex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(result)  # ['415-555-9999', '212-555-0000']

# With groups - returns list of tuples
regex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
result = regex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(result)  # [('415', '555', '9999'), ('212', '555', '0000')]

# search() vs findall()
# search() - returns Match object, use .group() to get text
# findall() - returns list of strings (or tuples), no .group() needed

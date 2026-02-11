# CHAPTER 9 - SECTION 4: FINDALL - Practice

import re

# Q1: Create a regex for phone numbers, use findall() to get ALL phones from 'Call 123-456-7890 or 555-123-4567'
# Example: regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# Example: print(regex.findall('Cell: 415-555-9999 Work: 212-555-0000'))
regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(regex.findall('call: 123-456-7890 or 555-123-4567'))


# Q2: Create a regex with TWO groups: (1) area code (first 3 digits), (2) the rest (3 digits-4 digits)
# Use findall() with the string below to get a list of tuples like [('415', '555-1234'), ('212', '555-5678')]
# Example: regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
print(regex.findall('415-555-1234 and 212-555-5678'))


# Q3: Find all words (one or more letters) in 'The quick brown fox'
# Example: regex = re.compile(r'\w+')
# Example: print(regex.findall('Hello World Python'))
regex = re.compile(r'\w+')
print(regex.findall('The quick brown fox'))


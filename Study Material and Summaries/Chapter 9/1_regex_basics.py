# CHAPTER 9 - SECTION 1: REGEX BASICS

# What: Regular expressions (regex) are patterns used to find text
# Why: More powerful than string methods for complex pattern matching
# How: Use the 're' module

import re

# Without regex - finding phone numbers is tedious
text = "Call me at 415-555-1234 or 415-555-9999"
# Would need complex string methods to find all phone numbers

# With regex - use a pattern
phone_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# Finding one match
match = phone_regex.search('My number is 415-555-4242.')
print(match.group())  # 415-555-4242

# Finding all matches
matches = phone_regex.findall(text)
print(matches)  # ['415-555-1234', '415-555-9999']

# Steps to use regex:
# 1. Import re module
# 2. Create a regex pattern with re.compile()
# 3. Use .search() to find one match or .findall() to find all matches
# 4. Use .group() to get the matched text

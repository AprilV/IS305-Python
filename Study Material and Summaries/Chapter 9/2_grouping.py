# CHAPTER 9 - SECTION 2: GROUPING WITH PARENTHESES

# What: Parentheses () create groups to extract parts of a match
# Why: Extract specific parts like area code vs phone number
# How: Use parentheses in pattern, access with .group(1), .group(2), etc.

import re

# Group 0 is the whole match, groups 1, 2, 3... are parentheses groups
phone_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
match = phone_regex.search('My number is 415-555-4242.')

print(match.group(0))  # 415-555-4242 (entire match)
print(match.group(1))  # 415 (first group - area code)
print(match.group(2))  # 555-4242 (second group - rest)

# Get all groups at once
print(match.groups())  # ('415', '555-4242')

# Can unpack into variables
area_code, main_number = match.groups()
print(f'Area: {area_code}, Number: {main_number}')

# Grouping with pipe | for alternation (OR)
hero_regex = re.compile(r'Batman|Tina Fey')
match1 = hero_regex.search('Batman and Tina Fey.')
print(match1.group())  # Batman (first match found)

match2 = hero_regex.search('Tina Fey and Batman.')
print(match2.group())  # Tina Fey (first match found)

# Group part of pattern
bat_regex = re.compile(r'Bat(man|mobile|copter|bat)')
match = bat_regex.search('Batmobile lost a wheel')
print(match.group())   # Batmobile
print(match.group(1))  # mobile (the part in parentheses)

# CHAPTER 9 - SECTION 2: GROUPING - Practice

import re

# Q1: Create a regex with groups to match phone format (123)- 456-7890, extract area code separately
# Example: regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# Example: match = regex.search('415-555-1234')
# Example: print(match.group(1))  # area code
regex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
match = regex.search('123-456-7890')
print(match.group(1))


# Q2: Create a regex that matches 'Batman' OR 'Superman', test with 'Superman saves the day'
# Example: regex = re.compile(r'cat|dog')
# Example: match = regex.search('I have a dog')
# Example: print(match.group())
regex = re.compile(r'Batman|Superman')
match = regex.search('Superman saves the day')
print(match.group())


# Q3: Create a regex for 'Bat' followed by 'man', 'mobile', or 'copter', test with 'Batcopter'
# Example: regex = re.compile(r'Super(man|woman)')
# Example: match = regex.search('Superwoman')
# Example: print(match.group())
regex = re.compile(r'Bat(man|mobile|copter)')
match = regex.search('Batcopter')
print(match.group())



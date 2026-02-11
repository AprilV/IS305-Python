# CHAPTER 9 - SECTION 7: FLAGS AND SUB - Practice

import re

# Q1: Create a case-insensitive regex to match 'python'. Use re.IGNORECASE flag, then .search() and .group() with 'I love PYTHON'
# Example: regex = re.compile(r'python', re.IGNORECASE)
# Example: print(regex.search('I use JAVA').group())
regex = re.compile(r'python' , re.IGNORECASE)
print(regex.search('I love PYTHON').group())


# Q2: Create a regex for 'cat'. Use .sub() to replace all 'cat' with 'dog' in 'The cat and the cat', then print result
# Example: regex = re.compile(r'fox')
# Example: print(regex.sub('wolf', 'The quick fox'))
regex = re.compile(r'cat')
print(regex.sub('shit' ,'The cat in the hat'))


# Q3: Create a regex with a group to capture first letter after 'Agent '. Use .sub() with \1 backreference to censor 'Agent Alice' to 'Agent A****', then print
# Example: regex = re.compile(r'Name (\w)\w*')
# Example: print(regex.sub(r'Name \1***', 'Name Bob'))
regex = re.compile(r'Agent (\w)\w*')
print(regex.sub(r'Agent \1****', 'Agent Alice'))


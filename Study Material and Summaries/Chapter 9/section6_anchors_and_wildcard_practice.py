# CHAPTER 9 - SECTION 6: ANCHORS AND WILDCARD - Practice

import re

# Q1: Create a regex with ^ to match 'Hello' only at the START of string. Use .search() and .group() with 'Hello world'
# Example: regex = re.compile(r'^Python')
# Example: print(regex.search('Python is great').group())
regex = re.compile(r'^Hello')
print(regex.search('Hello World').group())


# Q2: Create a regex with $ to match 'bye' only at the END of string. Use .search() and .group() with 'Goodbye'
# Example: regex = re.compile(r'world$')
# Example: print(regex.search('Hello world').group())
regex = re.compile(r'bye$')
print(regex.search('Goodbye').group())


# Q3: Create a regex using . (wildcard) to match any 3-letter words ending in 'at'. Use .findall() with 'cat bat rat'
# Example: regex = re.compile(r'.og')
# Example: print(regex.findall('dog fog log'))
regex = re.compile(r'.at')
print(regex.findall('cat bat rat'))


# Q4: Create a regex using .* with groups to capture text between 'start' and 'end'. Use .search() and .group(1) with 'start hello end'
# Example: regex = re.compile(r'begin (.*) finish')
# Example: print(regex.search('begin test finish').group(1))
regex = re.compile(r'start (.*) end')
print(regex.search('start hello end').group(1))


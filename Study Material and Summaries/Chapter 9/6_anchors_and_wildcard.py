# CHAPTER 9 - SECTION 6: ANCHORS (^ $) AND WILDCARD (.)

# What: ^ matches start of string, $ matches end, . matches any character
# Why: Ensure pattern is at specific position or match anything
# How: ^ at start, $ at end, . for any single character

import re

# ^ matches BEGINNING of string
begins_regex = re.compile(r'^Hello')
match1 = begins_regex.search('Hello world')
print(match1.group())  # Hello

match2 = begins_regex.search('Say Hello')
print(match2)  # None (Hello not at start)

# $ matches END of string
ends_regex = re.compile(r'world$')
match1 = ends_regex.search('Hello world')
print(match1.group())  # world

match2 = ends_regex.search('world Hello')
print(match2)  # None (world not at end)

# ^...$ matches ENTIRE string
whole_regex = re.compile(r'^\d+$')
match1 = whole_regex.search('12345')
print(match1.group())  # 12345 (entire string is digits)

match2 = whole_regex.search('12345abc')
print(match2)  # None (has letters too)

# . (dot) matches ANY character except newline
at_regex = re.compile(r'.at')
matches = at_regex.findall('The cat in the hat sat on the flat mat.')
print(matches)  # ['cat', 'hat', 'sat', 'lat', 'mat']

# .* matches EVERYTHING (any character, zero or more times)
name_regex = re.compile(r'First Name: (.*) Last Name: (.*)')
match = name_regex.search('First Name: Al Last Name: Sweigart')
print(match.group(1))  # Al
print(match.group(2))  # Sweigart

# .* is GREEDY (matches as much as possible)
greedy_regex = re.compile(r'<.*>')
match = greedy_regex.search('<To serve man> for dinner.>')
print(match.group())  # <To serve man> for dinner.> (matches too much!)

# .*? is NON-GREEDY (matches as little as possible)
non_greedy_regex = re.compile(r'<.*?>')
match = non_greedy_regex.search('<To serve man> for dinner.>')
print(match.group())  # <To serve man> (stops at first >)

# . matches everything EXCEPT newline
# To match newlines too, use re.DOTALL flag
regex = re.compile(r'.*', re.DOTALL)
match = regex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')
print(match.group())  # Gets everything including newlines

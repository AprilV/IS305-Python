# CHAPTER 9 - SECTION 3: REPETITION (?, *, +, {})

# What: Special characters to match patterns that repeat
# Why: Match varying lengths without writing patterns repeatedly
# How: ?, *, +, {n}, {n,m}

import re

# ? means "zero or one" (optional)
bat_regex = re.compile(r'Bat(wo)?man')
match1 = bat_regex.search('The Adventures of Batman')
print(match1.group())  # Batman

match2 = bat_regex.search('The Adventures of Batwoman')
print(match2.group())  # Batwoman

# * means "zero or more"
bat_regex = re.compile(r'Bat(wo)*man')
match1 = bat_regex.search('The Adventures of Batman')
print(match1.group())  # Batman

match2 = bat_regex.search('The Adventures of Batwowowowoman')
print(match2.group())  # Batwowowowoman

# + means "one or more" (at least one)
bat_regex = re.compile(r'Bat(wo)+man')
# match1 = bat_regex.search('The Adventures of Batman')  # No match! Needs at least one 'wo'

match2 = bat_regex.search('The Adventures of Batwoman')
print(match2.group())  # Batwoman

# {n} means "exactly n times"
ha_regex = re.compile(r'(Ha){3}')
match = ha_regex.search('HaHaHa')
print(match.group())  # HaHaHa

# {n,m} means "between n and m times"
ha_regex = re.compile(r'(Ha){3,5}')
match1 = ha_regex.search('HaHaHa')
print(match1.group())  # HaHaHa

match2 = ha_regex.search('HaHaHaHaHa')
print(match2.group())  # HaHaHaHaHa

# {n,} means "n or more"
# {,m} means "0 to m"

# GREEDY vs NON-GREEDY matching
# Greedy (default) - matches longest possible string
greedy_regex = re.compile(r'(Ha){3,5}')
match = greedy_regex.search('HaHaHaHaHa')
print(match.group())  # HaHaHaHaHa (matches 5, not 3)

# Non-greedy - add ? after repetition to match shortest
non_greedy_regex = re.compile(r'(Ha){3,5}?')
match = non_greedy_regex.search('HaHaHaHaHa')
print(match.group())  # HaHaHa (matches only 3)

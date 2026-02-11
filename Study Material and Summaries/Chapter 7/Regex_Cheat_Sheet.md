# Regular Expressions (Regex) - Quick Reference

## Basic Setup
```python
import re
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  # Create regex object
mo = phoneRegex.search('Call 415-555-1234')         # Search for pattern
print(mo.group())                                    # Get matched string
```

## Key Methods
| Method | What It Does | Returns |
|--------|--------------|---------|
| `re.compile(r'pattern')` | Creates a Regex object | Regex object |
| `.search(string)` | Finds first match | Match object (or None) |
| `.group()` | Gets the matched string | String |
| `.group(1), .group(2)` | Gets specific groups | String |
| `.findall(string)` | Finds all matches | List of strings or tuples |
| `.sub('replacement', string)` | Replace matches | New string |

## Quantifiers (How Many Times)
| Symbol | Meaning | Example | Matches |
|--------|---------|---------|---------|
| `?` | 0 or 1 time (optional) | `(wo)?` | "", "wo" |
| `*` | 0 or more times | `(wo)*` | "", "wo", "wowo", "wowowo" |
| `+` | 1 or more times | `(wo)+` | "wo", "wowo", "wowowo" (NOT "") |
| `{3}` | Exactly 3 times | `(Ha){3}` | "HaHaHa" |
| `{3,5}` | 3 to 5 times | `(Ha){3,5}` | "HaHaHa", "HaHaHaHa", "HaHaHaHaHa" |
| `{3,}` | 3 or more times | `(Ha){3,}` | "HaHaHa", "HaHaHaHa", etc. |

## Character Classes (What to Match)
| Symbol | Meaning | Example |
|--------|---------|---------|
| `\d` | Any digit (0-9) | `\d\d\d` matches "123" |
| `\w` | Any word character (a-z, A-Z, 0-9, _) | `\w+` matches "hello" |
| `\s` | Any whitespace (space, tab, newline) | `\s` matches " " |
| `\D` | NOT a digit | `\D+` matches "abc" |
| `\W` | NOT a word character | `\W+` matches "!!!" |
| `\S` | NOT whitespace | `\S+` matches "word" |
| `.` | Any character (except newline) | `.at` matches "cat", "hat", "bat" |

## Custom Character Classes
| Pattern | Meaning | Example |
|---------|---------|---------|
| `[aeiou]` | Match any vowel | Matches "a", "e", "i", "o", "u" |
| `[a-z]` | Match lowercase letters | Matches "a" through "z" |
| `[A-Z]` | Match uppercase letters | Matches "A" through "Z" |
| `[0-9]` | Match digits | Matches "0" through "9" |
| `[a-zA-Z0-9]` | Match letters and numbers | Matches any alphanumeric |
| `[^aeiou]` | Match anything EXCEPT vowels | Matches consonants, numbers, etc. |

## Special Operators
| Symbol | Meaning | Example |
|--------|---------|---------|
| `\|` | OR (pipe) | `Batman\|Robin` matches "Batman" OR "Robin" |
| `( )` | Group | `(wo)+` treats "wo" as one unit |
| `\` | Escape special chars | `\(` matches literal "(" |

## Greedy vs Non-Greedy
| Pattern | Type | Behavior | Example |
|---------|------|----------|---------|
| `.*` | Greedy | Matches as much as possible | `<.*>` in `<a> <b>` → `<a> <b>` |
| `.*?` | Non-greedy | Matches as little as possible | `<.*?>` in `<a> <b>` → `<a>` |
| `.+` | Greedy | Matches as much as possible | |
| `.+?` | Non-greedy | Matches as little as possible | |

## Groups and Backreferences
```python
# Groups in pattern
phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneRegex.search('415-555-1234')
mo.group(0)  # '415-555-1234' (full match - always group 0)
mo.group(1)  # '415' (first group)
mo.group(2)  # '555-1234' (second group)

# Using groups in replacement
phoneRegex.sub(r'(\1) \2', '415-555-1234')  # '(415) 555-1234'
# \1 = first group, \2 = second group
```

## Special Flags
```python
re.compile(r'pattern', re.IGNORECASE)  # Case-insensitive matching
re.compile(r'pattern', re.I)           # Short version
re.compile(r'pattern', re.DOTALL)      # . matches newlines too
re.compile(r'pattern', re.VERBOSE)     # Allow comments/whitespace in pattern
```

## Common Patterns
```python
# Phone number: 415-555-1234
r'\d\d\d-\d\d\d-\d\d\d\d'
r'(\d{3})-(\d{3})-(\d{4})'

# Email: name@domain.com
r'\w+@\w+\.\w+'

# Match word boundaries
r'\bcat\b'  # Matches "cat" but not "category"

# Start and end of string
r'^Hello'   # Must start with "Hello"
r'world$'   # Must end with "world"
r'^exact$'  # Must be exactly "exact"
```

## Quick Examples
```python
import re

# Basic matching
phoneRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
phoneRegex.search('My number is 415-555-1234').group()  # '415-555-1234'

# Find all matches
phoneRegex.findall('Call 415-555-1234 or 212-555-0000')  # ['415-555-1234', '212-555-0000']

# Replace
namesRegex = re.compile(r'Agent \w+')
namesRegex.sub('CENSORED', 'Agent Alice met Agent Bob.')  # 'CENSORED met CENSORED.'

# Case-insensitive
re.compile(r'robocop', re.I).search('RoboCop').group()  # 'RoboCop'

# Optional parts
batRegex = re.compile(r'Bat(wo)?man')
batRegex.search('Batman').group()    # 'Batman'
batRegex.search('Batwoman').group()  # 'Batwoman'
```

## Remember!
- Always use raw strings: `r'pattern'` (prevents backslash issues)
- `.search()` returns Match object → use `.group()` to get string
- `.findall()` returns list directly
- Group 0 is ALWAYS the full match
- Test your patterns at regex101.com

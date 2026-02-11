# Chapter 6: Manipulating Strings

**Date Completed:** January 26, 2026

## Table of Contents
1. [String Basics](#string-basics)
2. [String Indexing and Slicing](#string-indexing-and-slicing)
3. [String Methods](#string-methods)
4. [Text Alignment](#text-alignment)
5. [String Validation](#string-validation)
6. [Escape Characters](#escape-characters)
7. [Raw Strings](#raw-strings)
8. [Multiline Strings](#multiline-strings)
9. [String Formatting (f-strings)](#string-formatting)

---

## String Basics

### Creating Strings
Strings can be created with single or double quotes - they work identically:
```python
'Hello'    # Single quotes
"Hello"    # Double quotes (same thing)
```

### String Concatenation and Replication
```python
'Alice' + 'Bob'  # 'AliceBob' - concatenation joins strings
'Alice' * 5      # 'AliceAliceAliceAliceAlice' - replication repeats
```

**Important:** String concatenation only works with strings. Can't do `'Hello' + 5` (error).

---

## String Indexing and Slicing

### Indexing (Getting Single Characters)
```python
spam = 'Hello world!'
spam[0]   # 'H' - first character (index starts at 0)
spam[4]   # 'o' - fifth character
spam[-1]  # '!' - last character (negative indices count from end)
spam[-2]  # 'd' - second from last
```

### Slicing (Getting Substrings)
Syntax: `string[start:stop]` - gets characters from `start` up to (but NOT including) `stop`

```python
spam = 'Hello world!'
spam[0:5]   # 'Hello' - characters 0,1,2,3,4
spam[6:11]  # 'world' - characters 6,7,8,9,10
spam[:5]    # 'Hello' - from beginning to index 5
spam[6:]    # 'world!' - from index 6 to end
spam[:]     # 'Hello world!' - entire string
```

**Remember:** The stop index is NOT included in the result.

---

## String Methods

### Case Conversion
```python
spam = 'Hello world!'
spam.upper()   # 'HELLO WORLD!' - all uppercase
spam.lower()   # 'hello world!' - all lowercase
```

**Important:** These methods return a NEW string - they don't change the original:
```python
spam = 'Hello'
spam.upper()  # Returns 'HELLO', but spam is still 'Hello'
spam = spam.upper()  # Need to reassign to keep the change
```

### String Testing Methods (return True/False)
```python
# Starting/Ending
'Hello world'.startswith('Hello')   # True
'Hello world'.startswith('H')       # True
'Hello world'.endswith('world')     # True
'Hello world'.endswith('!')         # False

# Case checking
'HELLO'.isupper()   # True - all uppercase?
'hello'.islower()   # True - all lowercase?
'Hello'.isupper()   # False - mixed case

# Content validation
'hello'.isalpha()      # True - all letters?
'hello123'.isalpha()   # False - has numbers
'123'.isdigit()        # True - all digits?
'hello123'.isalnum()   # True - letters and/or numbers only (no spaces/punctuation)?
'hello 123'.isalnum()  # False - has a space
```

### Split and Join
**split()** - converts string to list (splits on delimiter)
```python
'My name is Simon'.split()       # ['My', 'name', 'is', 'Simon'] - splits on whitespace by default
'My name is Simon'.split('m')    # ['My na', 'e is Si', 'on'] - splits on 'm', removes the 'm'
'1-2-3-4-5'.split('-')          # ['1', '2', '3', '4', '5'] - splits on dashes
```

**join()** - converts list to string (joins with delimiter)
```python
' '.join(['My', 'name', 'is', 'Simon'])    # 'My name is Simon' - joins with space
'--'.join(['My', 'name', 'is', 'Simon'])   # 'My--name--is--Simon' - joins with dashes
''.join(['My', 'name', 'is', 'Simon'])     # 'MynameisSimon' - joins with nothing

# Common pattern: replace characters
'-'.join('There can be only one.'.split())  # 'There-can-be-only-one.' - replaces spaces with dashes
```

**Key concept:** Whatever is BEFORE `.join()` goes BETWEEN each list item.

---

## Text Alignment

### Justification Methods
Add padding to make strings a specific length:

```python
spam = 'Hello'
spam.rjust(10)   # '     Hello' - right justify (adds spaces on left)
spam.ljust(10)   # 'Hello     ' - left justify (adds spaces on right)
spam.center(10)  # '  Hello   ' - center (adds spaces on both sides)
```

**With custom fill character:**
```python
spam.center(10, '*')  # '**Hello***' - fill with asterisks instead of spaces
spam.rjust(10, '-')   # '-----Hello' - fill with dashes
```

### Removing Whitespace
```python
spam = '    Hello World     '
spam.strip()   # 'Hello World' - removes from both sides
spam.lstrip()  # 'Hello World     ' - removes from left (beginning) only
spam.rstrip()  # '    Hello World' - removes from right (end) only
```

**Remember:** 
- `lstrip()` = remove from LEFT
- `rstrip()` = remove from RIGHT
- `strip()` = remove from BOTH

---

## String Validation

Methods that check string content (all return True/False):

```python
'hello'.isalpha()      # True - only letters
'hello123'.isalpha()   # False - has numbers
'123'.isdigit()        # True - only digits
'hello123'.isalnum()   # True - letters and numbers, no spaces or punctuation
'hello 123'.isalnum()  # False - has a space
'HELLO'.isupper()      # True - all uppercase
'hello'.islower()      # True - all lowercase
```

**isalnum() breakdown:**
- **alpha**betic + **num**eric = letters OR numbers (or both)
- NO spaces, NO punctuation allowed
- Think: "Is this a valid variable name without special characters?"

---

## Escape Characters

Special characters that start with backslash `\`:

```python
print('Hello\nWorld')     # Hello
                          # World  (newline)
                          
print('Hello\tWorld')     # Hello    World  (tab)

print('I\'m here')        # I'm here  (escaped single quote)
print("He said \"Hi\"")   # He said "Hi"  (escaped double quotes)
print('C:\\Users\\name')  # C:\Users\name  (escaped backslashes)
```

### Common Escape Characters
| Escape | Meaning |
|--------|---------|
| `\n` | Newline (line break) |
| `\t` | Tab (indentation) |
| `\'` | Single quote |
| `\"` | Double quote |
| `\\` | Backslash |

**Why escape?**
The backslash `\` tells Python "treat the next character specially" - either to create special characters like newlines, or to use normally-special characters (like quotes) as literal text.

---

## Raw Strings

Prefix string with `r` to treat backslashes as literal characters:

```python
print('Hello\nWorld')   # Hello
                        # World  (interprets \n as newline)

print(r'Hello\nWorld')  # Hello\nWorld  (treats \n as literal text)
```

**Main use case: Windows file paths**
```python
path = 'C:\Users\name\folder'    # ERROR - \U and \n are escape sequences
path = r'C:\Users\name\folder'   # CORRECT - backslashes are literal
```

**Other uses:**
- Regular expressions (Chapter 7)
- Any time you need literal backslashes

---

## Multiline Strings

Use triple quotes (`'''` or `"""`) to create strings spanning multiple lines:

```python
print('''Hello
World
Python''')
# Output:
# Hello
# World
# Python
```

**Key points:**
- Must use EXACTLY 3 quotes (not 2, not 5)
- Opening and closing must match: `'''...'` or `"""..."""`
- Indentation inside the string IS PART OF THE STRING (gets printed)

**Comparison to \n:**
```python
# With escape character:
print('Hello\nWorld\nPython')

# With triple quotes (more readable):
print('''Hello
World
Python''')

# Both produce the same output
```

---

## String Formatting

### f-strings (Formatted String Literals)
Modern Python way to insert variables into strings:

```python
name = 'Alice'
age = 25
print(f'My name is {name} and I am {age} years old.')
# Output: My name is Alice and I am 25 years old.
```

**How it works:**
- Put `f` before the opening quote
- Put variable names in `{curly braces}`
- Python replaces `{variable}` with the variable's value
- Numbers are automatically converted to strings

**Comparison to old way (concatenation):**
```python
# Old way (messy):
print('My name is ' + name + ' and I am ' + str(age) + ' years old.')

# New way (clean):
print(f'My name is {name} and I am {age} years old.')
```

**Advantages of f-strings:**
- Cleaner, more readable
- No need for `+` everywhere
- No need to call `str()` on numbers
- Can put expressions inside `{}`

**Examples with expressions:**
```python
x = 10
print(f'Double of {x} is {x * 2}')  # Double of 10 is 20
print(f'Uppercase: {name.upper()}')  # Uppercase: ALICE
```

---

## Key Takeaways

### Strings are Immutable
String methods return NEW strings - they don't change the original:
```python
spam = 'Hello'
spam.upper()       # Returns 'HELLO', but spam is still 'Hello'
spam = spam.upper()  # Need to reassign to keep the change
```

### Quotes: Single vs Double
`'text'` and `"text"` are identical. Use whichever you prefer, or:
- Use double quotes when string contains single quote: `"Howl's Moving Castle"`
- Use single quotes when string contains double quote: `'He said "Hi"'`

### Common Patterns

**Replace characters in a string:**
```python
'-'.join('hello world'.split())  # 'hello-world' (replace spaces with dashes)
```

**Clean up user input:**
```python
user_input = '   hello   '
clean = user_input.strip().lower()  # 'hello' (remove spaces, make lowercase)
```

**Build paths safely:**
```python
path = r'C:\Users\name\Documents'  # Use raw string for Windows paths
```

**Multi-line text:**
```python
message = '''Dear User,
Thank you for your order.
Best regards'''
```

---

## Practice Reminders

1. **String indexing starts at 0**
2. **Slicing [start:stop] does NOT include stop**
3. **Split returns a LIST, join takes a LIST**
4. **isalnum() = letters/numbers only, NO spaces or punctuation**
5. **Strip methods: lstrip = left, rstrip = right, strip = both**
6. **f-strings: put `f` before quote, variables in `{}`**
7. **Raw strings (`r'...'`) for literal backslashes**
8. **Triple quotes (`'''...'''`) for multiline**

---

## Common Mistakes to Avoid

1. ❌ Forgetting string methods return NEW strings
   ```python
   spam = 'Hello'
   spam.upper()  # spam is still 'Hello'!
   ```
   ✅ Reassign to keep the change:
   ```python
   spam = spam.upper()  # Now spam is 'HELLO'
   ```

2. ❌ Confusing slice indices
   ```python
   'Hello'[0:5]  # What does this return?
   ```
   ✅ Remember: stop index NOT included
   ```python
   'Hello'[0:5]  # Returns 'Hello' (indices 0,1,2,3,4)
   ```

3. ❌ Using wrong strip method
   ```python
   '   Hello   '.lstrip()  # Still has spaces on right!
   ```
   ✅ Use correct strip for your needs:
   ```python
   '   Hello   '.strip()  # Removes from both sides
   ```

4. ❌ Forgetting the `f` in f-strings
   ```python
   name = 'Alice'
   print('Hello {name}')  # Prints: Hello {name}
   ```
   ✅ Add `f` before the quote:
   ```python
   print(f'Hello {name}')  # Prints: Hello Alice
   ```

---

## Summary of Methods

| Method | Purpose | Example |
|--------|---------|---------|
| `.upper()` | Convert to uppercase | `'hello'.upper()` → `'HELLO'` |
| `.lower()` | Convert to lowercase | `'HELLO'.lower()` → `'hello'` |
| `.startswith(s)` | Check if starts with s | `'Hello'.startswith('H')` → `True` |
| `.endswith(s)` | Check if ends with s | `'Hello'.endswith('o')` → `True` |
| `.isupper()` | Check if all uppercase | `'HELLO'.isupper()` → `True` |
| `.islower()` | Check if all lowercase | `'hello'.islower()` → `True` |
| `.isalpha()` | Check if all letters | `'hello'.isalpha()` → `True` |
| `.isdigit()` | Check if all digits | `'123'.isdigit()` → `True` |
| `.isalnum()` | Check if letters/digits only | `'hello123'.isalnum()` → `True` |
| `.split()` | Split into list | `'a b c'.split()` → `['a', 'b', 'c']` |
| `.split(x)` | Split on x | `'a-b-c'.split('-')` → `['a', 'b', 'c']` |
| `x.join(list)` | Join list with x | `'-'.join(['a','b'])` → `'a-b'` |
| `.rjust(n)` | Right justify in n chars | `'Hi'.rjust(5)` → `'   Hi'` |
| `.ljust(n)` | Left justify in n chars | `'Hi'.ljust(5)` → `'Hi   '` |
| `.center(n)` | Center in n chars | `'Hi'.center(5)` → `' Hi  '` |
| `.strip()` | Remove whitespace (both) | `' Hi '.strip()` → `'Hi'` |
| `.lstrip()` | Remove whitespace (left) | `' Hi '.lstrip()` → `'Hi '` |
| `.rstrip()` | Remove whitespace (right) | `' Hi '.rstrip()` → `' Hi'` |

---

**Remember:** All these concepts exist to help you. When you need them later, you'll remember "there was a method for that" and can look it up. Focus on understanding the concepts, not memorizing every detail!

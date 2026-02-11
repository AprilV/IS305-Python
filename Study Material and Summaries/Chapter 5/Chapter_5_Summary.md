===================================================================================
IS 305 - CHAPTER 5: DICTIONARIES AND STRUCTURING DATA - STUDY GUIDE
Automate the Boring Stuff with Python, 3rd Edition
===================================================================================

COURSE INFORMATION:
- Class: IS 305 (Information Systems)
- Textbook: Automate the Boring Stuff with Python, 3rd Edition
- Chapter Focus: Dictionaries - Working with key-value pairs
- Date: January 25, 2026

===================================================================================
WHAT IS A DICTIONARY?
===================================================================================

A DICTIONARY is a collection of key-value pairs.

```python
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
```

Key Features:
- Uses curly braces `{}`
- Keys and values separated by colons `:`
- Items separated by commas
- Keys can be strings, integers, floats, or tuples
- Values can be ANY type
- Dictionaries are MUTABLE (can be changed)

===================================================================================
ACCESSING VALUES
===================================================================================

Access values using keys (not numeric indexes):

```python
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
myCat['size']  # 'fat'
myCat['color']  # 'gray'
```

Unlike lists which use numeric indexes (0, 1, 2), dictionaries use descriptive keys.

===================================================================================
DICTIONARIES VS LISTS
===================================================================================

LISTS:
- Ordered collection
- Access by numeric index: `spam[0]`
- Order matters: `[1, 2, 3] != [3, 2, 1]`

DICTIONARIES:
- Unordered collection (before Python 3.7)
- Access by key: `spam['name']`
- Order doesn't matter: `{'a': 1, 'b': 2} == {'b': 2, 'a': 1}`

Example:
```python
spam = ['cats', 'dogs', 'moose']
bacon = ['dogs', 'moose', 'cats']
spam == bacon  # False - different order

eggs = {'name': 'Zophie', 'species': 'cat'}
ham = {'species': 'cat', 'name': 'Zophie'}
eggs == ham  # True - same key-value pairs
```

===================================================================================
ADDING AND CHANGING VALUES
===================================================================================

ADDING NEW KEY-VALUE PAIRS:
```python
spam = {'name': 'Zophie', 'age': 7}
spam['color'] = 'black'
# spam is now {'name': 'Zophie', 'age': 7, 'color': 'black'}
```

CHANGING EXISTING VALUES:
```python
spam['age'] = 8
# spam is now {'name': 'Zophie', 'age': 8, 'color': 'black'}
```

Unlike lists, you can't have duplicate keys. Setting a key that exists overwrites it.

===================================================================================
THE keys(), values(), AND items() METHODS
===================================================================================

THREE DICTIONARY METHODS:

keys() - Returns all keys:
```python
spam = {'color': 'red', 'age': 42}
spam.keys()  # dict_keys(['color', 'age'])
```

values() - Returns all values:
```python
spam.values()  # dict_values(['red', 42])
```

items() - Returns key-value pairs as tuples:
```python
spam.items()  # dict_items([('color', 'red'), ('age', 42)])
```

CONVERTING TO LISTS:
```python
list(spam.keys())    # ['color', 'age']
list(spam.values())  # ['red', 42]
list(spam.items())   # [('color', 'red'), ('age', 42)]
```

LOOPING WITH items():
```python
for key, value in spam.items():
    print(f'{key}: {value}')
# Output:
# color: red
# age: 42
```

===================================================================================
CHECKING IF A KEY OR VALUE EXISTS
===================================================================================

THE in AND not in OPERATORS:

CHECK FOR KEYS:
```python
spam = {'name': 'Zophie', 'age': 7}
'name' in spam        # True
'color' in spam       # False
'color' not in spam   # True
```

CHECK FOR VALUES:
```python
'Zophie' in spam.values()  # True
7 in spam.values()         # True
'black' in spam.values()   # False
```

===================================================================================
THE get() METHOD
===================================================================================

SAFE WAY TO ACCESS VALUES:

```python
picnicItems = {'apples': 5, 'cups': 2}
```

USING BRACKETS (crashes if key doesn't exist):
```python
picnicItems['eggs']  # KeyError: 'eggs'
```

USING get() (returns default if key doesn't exist):
```python
picnicItems.get('eggs', 0)    # 0 (default value)
picnicItems.get('apples', 0)  # 5 (key exists)
```

Format: `dictionary.get(key, defaultValue)`
- If key exists → return its value
- If key doesn't exist → return defaultValue

PRACTICAL EXAMPLE:
```python
numberOfThings = {}

numberOfThings.get('apples', 0) + 1  # Returns 1 (0 + 1)
numberOfThings.get('cups', 0) + 1    # Returns 1 (0 + 1)
```

===================================================================================
THE setdefault() METHOD
===================================================================================

SET A VALUE ONLY IF KEY DOESN'T EXIST:

```python
spam = {'name': 'Pooka', 'age': 5}
spam.setdefault('color', 'black')
# spam is now {'name': 'Pooka', 'age': 5, 'color': 'black'}

spam.setdefault('color', 'white')
# spam is still {'name': 'Pooka', 'age': 5, 'color': 'black'}
# Color already existed, so 'white' was NOT set
```

COMPARING TO MANUAL METHOD:
```python
# Without setdefault:
if 'color' not in spam:
    spam['color'] = 'black'

# With setdefault (same result, one line):
spam.setdefault('color', 'black')
```

PRACTICAL USE - CHARACTER COUNTING:
```python
message = 'It was a bright cold day in April.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
```

===================================================================================
PRETTY PRINTING
===================================================================================

THE pprint MODULE:

```python
import pprint

message = 'It was a bright cold day in April.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)
```

OUTPUT (formatted nicely):
```
{' ': 7,
 'A': 1,
 'I': 1,
 'a': 4,
 'b': 1,
 'c': 1,
 'd': 3,
 'g': 1,
 'h': 1,
 'i': 3,
 'l': 1,
 'n': 1,
 'o': 1,
 'p': 1,
 'r': 2,
 's': 1,
 't': 2,
 'w': 1,
 'y': 1}
```

pprint.pformat() - Returns formatted string instead of printing:
```python
countString = pprint.pformat(count)
print(countString)
```

===================================================================================
NESTED DICTIONARIES AND LISTS
===================================================================================

DICTIONARIES CAN CONTAIN LISTS:
```python
allGuests = {
    'Alice': {'apples': 5, 'pretzels': 12},
    'Bob': {'ham sandwiches': 3, 'apples': 2},
    'Carol': {'cups': 3, 'apple pies': 1}
}
```

ACCESSING NESTED VALUES:
```python
allGuests['Alice']['apples']  # 5
allGuests['Bob']['ham sandwiches']  # 3
```

LOOPING THROUGH NESTED DICTIONARIES:
```python
def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought

print('Number of things being brought:')
print(' - Apples         ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups           ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes          ' + str(totalBrought(allGuests, 'cakes')))
```

===================================================================================
QUICK REFERENCE - COMMON DICTIONARY OPERATIONS
===================================================================================

```python
# Creating dictionaries
spam = {}
spam = {'name': 'Zophie', 'age': 7}

# Accessing values
spam['name']              # 'Zophie'
spam.get('color', 'N/A')  # Safe access with default

# Adding/Changing
spam['color'] = 'black'   # Add or change
spam.setdefault('age', 1) # Set only if doesn't exist

# Checking existence
'name' in spam            # Check for key
'Zophie' in spam.values() # Check for value

# Getting keys, values, items
spam.keys()    # All keys
spam.values()  # All values
spam.items()   # Key-value pairs

# Looping
for key in spam:
    print(key, spam[key])

for key, value in spam.items():
    print(key, value)

# Pretty printing
import pprint
pprint.pprint(spam)
```

===================================================================================
DATA STRUCTURES
===================================================================================

COMBINING LISTS AND DICTIONARIES:

List of dictionaries:
```python
catNames = []
catNames.append({'name': 'Zophie', 'desc': 'chubby'})
catNames.append({'name': 'Pooka', 'desc': 'fluffy'})
```

Dictionary of lists:
```python
catalog = {
    'fruits': ['apple', 'banana'],
    'veggies': ['carrot', 'broccoli']
}
```

===================================================================================
END OF CHAPTER 5 SUMMARY
===================================================================================

===============================================================================
IS 305 - CHAPTER 4: LISTS - ESSENTIAL STUDY GUIDE
Automate the Boring Stuff with Python, 3rd Edition
===============================================================================

COURSE INFORMATION:
- Class: IS 305 (Information Systems)
- Textbook: Automate the Boring Stuff with Python, 3rd Edition
- Chapter Focus: Lists - Working with ordered sequences of values
- Date: January 25, 2026

===============================================================================
WHAT ARE LISTS?
===============================================================================

A LIST is a value that contains multiple values in an ordered sequence.

Example:
```python
spam = ['cat', 'bat', 'rat', 'elephant']
spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]  # Lists can contain other lists
```

Key Points:
- Lists begin with [ and end with ]
- Values inside are separated by commas
- Lists can contain any type of value (strings, integers, floats, other lists)
- Lists are MUTABLE (can be changed after creation)

===============================================================================
ACCESSING VALUES WITH INDEXES
===============================================================================

Index = Integer position of a value in a list (starts at 0)

```python
spam = ['cat', 'bat', 'rat', 'elephant']
spam[0]  # 'cat' - first item
spam[1]  # 'bat' - second item
spam[3]  # 'elephant' - fourth item
```

NEGATIVE INDEXES:
```python
spam[-1]  # 'elephant' - last item
spam[-2]  # 'rat' - second to last
spam[-3]  # 'bat'
```

Index out of range = IndexError

===============================================================================
SUBLISTS WITH SLICES
===============================================================================

SLICE = Getting multiple values from a list

Syntax: list[start:stop] - gets values from start up to (but NOT including) stop

```python
spam = ['cat', 'bat', 'rat', 'elephant']
spam[0:4]   # ['cat', 'bat', 'rat', 'elephant']
spam[1:3]   # ['bat', 'rat']
spam[0:-1]  # ['cat', 'bat', 'rat']
```

SHORTCUTS:
```python
spam[:2]   # ['cat', 'bat'] - leaving out first index starts at 0
spam[1:]   # ['bat', 'rat', 'elephant'] - leaving out second index goes to end
spam[:]    # ['cat', 'bat', 'rat', 'elephant'] - copies entire list
```

===============================================================================
GETTING LENGTH WITH len()
===============================================================================

```python
spam = ['cat', 'dog', 'moose']
len(spam)  # 3
```

===============================================================================
CHANGING VALUES WITH INDEXES
===============================================================================

Lists are MUTABLE - you can change their values

```python
spam = ['cat', 'bat', 'rat', 'elephant']
spam[1] = 'aardvark'
spam  # ['cat', 'aardvark', 'rat', 'elephant']

spam[2] = spam[1]
spam  # ['cat', 'aardvark', 'aardvark', 'elephant']

spam[-1] = 12345
spam  # ['cat', 'aardvark', 'aardvark', 12345]
```

===============================================================================
LIST CONCATENATION AND REPLICATION
===============================================================================

CONCATENATION (joining lists):
```python
[1, 2, 3] + ['A', 'B', 'C']  # [1, 2, 3, 'A', 'B', 'C']
```

REPLICATION (repeating lists):
```python
['X', 'Y', 'Z'] * 3  # ['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z']
spam = [0] * 5       # [0, 0, 0, 0, 0]
```

===============================================================================
REMOVING VALUES WITH del
===============================================================================

```python
spam = ['cat', 'bat', 'rat', 'elephant']
del spam[2]
spam  # ['cat', 'bat', 'elephant']

del spam[0]
spam  # ['bat', 'elephant']
```

===============================================================================
WORKING WITH LISTS
===============================================================================

THE in AND not in OPERATORS:
```python
'howdy' in ['hello', 'hi', 'howdy', 'heyas']  # True
spam = ['hello', 'hi', 'howdy', 'heyas']
'cat' in spam        # False
'howdy' not in spam  # False
'cat' not in spam    # True
```

===============================================================================
MULTIPLE ASSIGNMENT (TUPLE UNPACKING)
===============================================================================

Assign each value in a list to a variable in one line:

```python
cat = ['fat', 'gray', 'loud']
size, color, disposition = cat
# size = 'fat'
# color = 'gray'  
# disposition = 'loud'
```

Number of variables must match number of items!

SWAP VALUES TRICK:
```python
a, b = 'Alice', 'Bob'
a, b = b, a  # Swaps values!
# a = 'Bob'
# b = 'Alice'
```

===============================================================================
USING enumerate() WITH LISTS
===============================================================================

Get both the index AND value in a for loop:

```python
supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for index, item in enumerate(supplies):
    print(f'Index {index} in supplies is: {item}')
```

Output:
```
Index 0 in supplies is: pens
Index 1 in supplies is: staplers
Index 2 in supplies is: flamethrowers
Index 3 in supplies is: binders
```

===============================================================================
USING random.choice() AND random.shuffle()
===============================================================================

```python
import random

pets = ['Dog', 'Cat', 'Moose']
random.choice(pets)  # Randomly selects one item from list

people = ['Alice', 'Bob', 'Carol', 'David']
random.shuffle(people)  # Shuffles list in place (modifies original list)
people  # ['David', 'Carol', 'Alice', 'Bob'] (random order)
```

===============================================================================
AUGMENTED ASSIGNMENT OPERATORS
===============================================================================

Shortcuts for updating variables:

```python
spam = 42
spam += 1    # Same as: spam = spam + 1
spam -= 1    # Same as: spam = spam - 1
spam *= 2    # Same as: spam = spam * 2
spam /= 2    # Same as: spam = spam / 2
spam %= 2    # Same as: spam = spam % 2
```

Works with strings and lists too:
```python
spam = 'Hello'
spam += ' world!'  # 'Hello world!'

bacon = ['Zophie']
bacon *= 3  # ['Zophie', 'Zophie', 'Zophie']
```

===============================================================================
FINDING VALUES WITH index()
===============================================================================

Get the index of a value in a list:

```python
spam = ['hello', 'hi', 'howdy', 'heyas']
spam.index('hello')  # 0
spam.index('heyas')  # 3
spam.index('howdy howdy howdy')  # ValueError: not in list
```

If duplicates exist, returns index of first occurrence:
```python
spam = ['Zophie', 'Pooka', 'Fat-tail', 'Pooka']
spam.index('Pooka')  # 1
```

===============================================================================
ADDING VALUES WITH append() AND insert()
===============================================================================

append() - Adds to the END of list:
```python
spam = ['cat', 'dog', 'bat']
spam.append('moose')
spam  # ['cat', 'dog', 'bat', 'moose']
```

insert() - Adds at specific index:
```python
spam = ['cat', 'dog', 'bat']
spam.insert(1, 'chicken')
spam  # ['cat', 'chicken', 'dog', 'bat']
```

===============================================================================
REMOVING VALUES WITH remove()
===============================================================================

Removes first occurrence of a value:

```python
spam = ['cat', 'bat', 'rat', 'elephant']
spam.remove('bat')
spam  # ['cat', 'rat', 'elephant']
```

If value appears multiple times, only first is removed:
```python
spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
spam.remove('cat')
spam  # ['bat', 'rat', 'cat', 'hat', 'cat']
```

ValueError if value not in list

===============================================================================
SORTING VALUES WITH sort()
===============================================================================

sort() - Sorts list in place (modifies original):

```python
spam = [2, 5, 3.14, 1, -7]
spam.sort()
spam  # [-7, 1, 2, 3.14, 5]

spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
spam.sort()
spam  # ['ants', 'badgers', 'cats', 'dogs', 'elephants']
```

REVERSE ORDER:
```python
spam.sort(reverse=True)
spam  # ['elephants', 'dogs', 'cats', 'badgers', 'ants']
```

IMPORTANT:
- Can't sort lists with mixed types (numbers and strings)
- sort() uses "ASCIIbetical order" - uppercase comes before lowercase
- To sort in regular alphabetical order: spam.sort(key=str.lower)

```python
spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
spam.sort()
spam  # ['Alice', 'Bob', 'Carol', 'ants', 'badgers', 'cats']

spam.sort(key=str.lower)
spam  # ['Alice', 'ants', 'badgers', 'Bob', 'Carol', 'cats']
```

===============================================================================
REVERSING VALUES WITH reverse()
===============================================================================

Reverses order of items in list:

```python
spam = ['cat', 'dog', 'moose']
spam.reverse()
spam  # ['moose', 'dog', 'cat']
```

===============================================================================
EXCEPTIONS TO INDENTATION RULES
===============================================================================

You can split lines for readability:

```python
spam = ['apples',
    'oranges',
    'bananas',
    'cats']

spam = ['apples', 'oranges', 'bananas',
    'cats']
```

===============================================================================
SEQUENCE DATA TYPES
===============================================================================

Lists are a SEQUENCE type (ordered sequence of values)

Other sequence types:
- Strings (sequence of characters)
- Range objects (sequence of numbers from range())

Many things that work with lists also work with sequences:
- Indexing
- Slicing  
- for loops
- len()
- in and not in

MUTABLE vs IMMUTABLE:
- Lists are MUTABLE (can change values)
- Strings and tuples are IMMUTABLE (cannot change values)

```python
name = 'Zophie a cat'
name[7] = 'the'  # ERROR! Strings are immutable

name = 'Zophie a cat'
newName = name[0:7] + 'the' + name[8:12]  # Must create new string
newName  # 'Zophie the cat'
```

===============================================================================
TUPLE DATA TYPE
===============================================================================

TUPLE = Like a list but IMMUTABLE (cannot be changed)

Create with parentheses instead of brackets:
```python
eggs = ('hello', 42, 0.5)
eggs[0]  # 'hello'
eggs[1:3]  # (42, 0.5)
len(eggs)  # 3
```

Can't modify:
```python
eggs[1] = 99  # TypeError: 'tuple' object does not support item assignment
```

WHEN TO USE TUPLES:
1. Code needs data that won't change
2. Tuples can be used as dictionary keys (lists can't)

CONVERTING:
```python
tuple(['cat', 'dog', 5])  # ('cat', 'dog', 5)
list(('cat', 'dog', 5))   # ['cat', 'dog', 5]
list('hello')  # ['h', 'e', 'l', 'l', 'o']
```

===============================================================================
REFERENCES
===============================================================================

IMPORTANT CONCEPT: Variables don't store lists directly - they store REFERENCES to lists

```python
spam = [0, 1, 2, 3, 4, 5]
cheese = spam  # cheese and spam refer to SAME list
cheese[1] = 'Hello!'
spam  # [0, 'Hello!', 2, 3, 4, 5]
cheese  # [0, 'Hello!', 2, 3, 4, 5]
```

Both variables point to same list in memory!

PASSING LISTS TO FUNCTIONS:
```python
def eggs(someParameter):
    someParameter.append('Hello')

spam = [1, 2, 3]
eggs(spam)
print(spam)  # [1, 2, 3, 'Hello']
```

The function modifies the original list!

COPY A LIST:
```python
import copy
spam = ['A', 'B', 'C', 'D']
id(spam)  # 44684232

cheese = copy.copy(spam)  # Creates separate copy
id(cheese)  # 44685832

cheese[1] = 42
spam   # ['A', 'B', 'C', 'D']
cheese # ['A', 42, 'C', 'D']
```

DEEP COPY (for lists of lists):
```python
spam = ['A', 'B', ['C', 'D']]
cheese = copy.deepcopy(spam)  # Copies inner lists too
```

===============================================================================
LINE CONTINUATION CHARACTER
===============================================================================

Use \ to split long lines:

```python
print('Four score and seven ' + \
      'years ago...')
```

===============================================================================
QUICK REFERENCE - COMMON LIST OPERATIONS
===============================================================================

```python
# Creating lists
spam = [1, 2, 3]
spam = ['cat', 'bat', 1, 2]

# Accessing values
spam[0]      # First item
spam[-1]     # Last item
spam[1:3]    # Slice (items 1 and 2)

# Modifying
spam[1] = 'new value'
spam.append('end')
spam.insert(0, 'start')
spam.remove('value')
del spam[0]

# Finding
len(spam)           # Length
'cat' in spam       # Check if in list
spam.index('cat')   # Get index of value

# Sorting/Organizing
spam.sort()
spam.sort(reverse=True)
spam.reverse()

# Loops
for item in spam:
    print(item)

for i, item in enumerate(spam):
    print(i, item)

# Other
random.choice(spam)
random.shuffle(spam)
copy.copy(spam)
```

===============================================================================
END OF CHAPTER 4 SUMMARY
===============================================================================

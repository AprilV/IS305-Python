# Chapter 5 Practice Questions
## From "Automate the Boring Stuff with Python" - End of Chapter Questions

---

## PRACTICE QUESTIONS (From the book)

**1. What does the code for an empty dictionary look like?**

**2. What does a dictionary value with a key `'foo'` and a value `42` look like?**

**3. What is the main difference between a list and a dictionary?**

**4. What happens if you try to access `spam['foo']` if `spam` is `{'bar': 100}`?**

**5. If a dictionary is stored in `spam`, what is the difference between the expressions `'cat' in spam` and `'cat' in spam.values()`?**

**6. If a dictionary is stored in `spam`, what is the difference between the expressions `'cat' in spam` and `'cat' in spam.keys()`?**

**7. What is a shortcut for the following code?**
```python
if 'color' not in spam:
    spam['color'] = 'black'
```

**8. What module and function can be used to "pretty print" dictionary values?**

---

## ANSWER KEY

**1.** `{}`

**2.** `{'foo': 42}`

**3.** Lists are ordered collections accessed by numeric indexes (0, 1, 2...). Dictionaries are unordered collections accessed by keys (which can be strings, numbers, etc.).

**4.** You get a `KeyError: 'foo'` error because the key `'foo'` doesn't exist in the dictionary.

**5.** 
- `'cat' in spam` checks whether there is a `'cat'` **key** in the dictionary.
- `'cat' in spam.values()` checks whether there is a value `'cat'` for one of the keys in `spam`.

**6.** They check the same thing. `'cat' in spam` checks if the string `'cat'` is a key in the dictionary (this is the shortcut). `'cat' in spam.keys()` does the same thing but is more explicit.

**7.** `spam.setdefault('color', 'black')`

**8.** `pprint.pprint()` from the `pprint` module.

---

## HANDS-ON PRACTICE EXERCISES

### Exercise 1: Basic Dictionary Operations
```python
# Create a dictionary for a person with keys: name, age, city
# Print each value
# Add a new key 'job' with a value
# Change the age
# Print the final dictionary
```

### Exercise 2: Using Dictionary Methods
```python
# Create a dictionary: inventory = {'rope': 1, 'torch': 6, 'gold coin': 42}
# Print all the keys
# Print all the values
# Print all key-value pairs
# Check if 'rope' is in the dictionary
# Check if 50 is in the values
```

### Exercise 3: Chess Dictionary Validator
Write a function named `isValidChessBoard()` that takes a dictionary argument and returns `True` or `False` depending on whether the board is valid.

A valid chess board will have:
- Exactly one black king and exactly one white king
- Each player has at most 16 pieces
- All pieces begin with 'w' or 'b' for white/black
- Pieces are: 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'
- All piece names are lowercase (except the first letter for color)
- All keys should be valid positions ('1a' through '8h')

Example board:
```python
board = {
    '1h': 'bking',
    '6c': 'wqueen',
    '2g': 'bbishop',
    '5h': 'bqueen',
    '3e': 'wking'
}
```

### Exercise 4: Fantasy Game Inventory
You are creating a fantasy video game. Write a function `displayInventory()` that takes a dictionary and displays the inventory:

```python
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    # Your code here
    # Print each item and count
    # Print total number of items

displayInventory(stuff)
```

Expected output:
```
Inventory:
12 arrow
42 gold coin
1 rope
6 torch
1 dagger
Total number of items: 62
```

### Exercise 5: List to Dictionary Function for Fantasy Game Inventory
Write a function named `addToInventory(inventory, addedItems)` that:
- Takes a dictionary (current inventory) and a list (loot from a dragon)
- Returns a dictionary that represents the updated inventory

Example:
```python
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
```

Expected output:
```
Inventory:
45 gold coin
1 rope
1 ruby
1 dagger
Total number of items: 48
```

---

## KEY TAKEAWAYS FROM CHAPTER 5

✓ Dictionaries store data as key-value pairs using `{}`  
✓ Access values with keys: `spam['key']`  
✓ Keys must be immutable (strings, numbers, tuples)  
✓ Use `get()` for safe access with default values  
✓ Use `setdefault()` to set a value only if key doesn't exist  
✓ Check existence with `in` operator  
✓ Use `.keys()`, `.values()`, `.items()` to get dictionary data  
✓ Use `pprint.pprint()` to nicely format dictionary output  
✓ Dictionaries are unordered (before Python 3.7) - order doesn't matter for equality  

---

# Chapter 8 - Section 11: join() and split() Reference

# split() - breaks string into list
sentence = 'Hello World Python'
words = sentence.split()  # Split on spaces (default)
print(words)  # ['Hello', 'World', 'Python']

print()

# split() with specific separator
csv_data = 'Alice,25,Boston'
parts = csv_data.split(',')  # Split on commas
print(parts)  # ['Alice', '25', 'Boston']

print()

# split() with newlines
text = 'Line 1\nLine 2\nLine 3'
lines = text.split('\n')
print(lines)  # ['Line 1', 'Line 2', 'Line 3']

print()

# join() - combines list into string
words = ['Python', 'is', 'awesome']
sentence = ' '.join(words)  # Join with spaces
print(sentence)  # Python is awesome

print()

# join() with different separator
items = ['apple', 'banana', 'orange']
csv = ', '.join(items)
print(csv)  # apple, banana, orange

print()

# join() with no separator
letters = ['H', 'e', 'l', 'l', 'o']
word = ''.join(letters)
print(word)  # Hello

print()

# Practical use - processing data
data = 'John,Doe,30,Engineer'
fields = data.split(',')
print(f'First name: {fields[0]}')
print(f'Last name: {fields[1]}')
print(f'Age: {fields[2]}')
print(f'Job: {fields[3]}')

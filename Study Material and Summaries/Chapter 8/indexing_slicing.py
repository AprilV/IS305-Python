# Chapter 8 - Section 5: String Indexing and Slicing Reference

text = 'Hello'

# INDEXING - Get single characters
# Index:  0   1   2   3   4
# String: H   e   l   l   o

print('First character:', text[0])   # 'H'
print('Second character:', text[1])  # 'e'
print('Last character:', text[4])    # 'o'

# Negative indexing - count from the end
print('Last character:', text[-1])   # 'o'
print('Second to last:', text[-2])   # 'l'

print()  # Blank line

# SLICING - Get range of characters
# [start:stop] - gets from start up to (but NOT including) stop

name = 'Python'
#      0 1 2 3 4 5

print('First 3 letters:', name[0:3])   # 'Pyt' (0, 1, 2)
print('Middle letters:', name[2:5])    # 'tho' (2, 3, 4)

# Shortcuts
print('From beginning:', name[:3])     # 'Pyt' (same as [0:3])
print('To the end:', name[2:])         # 'thon' (from 2 to end)
print('Everything:', name[:])          # 'Python' (entire string)

print()  # Blank line

# Common use - get everything except first/last character
message = 'Hello World'
print('Without first:', message[1:])   # 'ello World'
print('Without last:', message[:-1])   # 'Hello Worl'

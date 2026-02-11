# SECTION 13: ORD() AND CHR() FUNCTIONS

# === ORD() - Character to Number ===

# Get numeric code for a character
print(ord('A'))        # 65
print(ord('B'))        # 66
print(ord('a'))        # 97
print(ord('b'))        # 98

# Notice: lowercase is 32 higher than uppercase
print(ord('A'))        # 65
print(ord('a'))        # 97
print(ord('a') - ord('A'))  # 32

# Works with any character
print(ord('!'))        # 33
print(ord('?'))        # 63
print(ord(' '))        # 32 (space character)
print(ord('0'))        # 48 (digit zero)


# === CHR() - Number to Character ===

# Get character from numeric code
print(chr(65))         # 'A'
print(chr(66))         # 'B'
print(chr(97))         # 'a'
print(chr(98))         # 'b'

# Create characters from numbers
print(chr(33))         # '!'
print(chr(63))         # '?'
print(chr(32))         # ' ' (space)


# === PRACTICAL EXAMPLES ===

# Character arithmetic
letter = 'A'
next_letter = chr(ord(letter) + 1)
print(next_letter)     # 'B'

# Convert uppercase to lowercase manually
uppercase = 'A'
lowercase = chr(ord(uppercase) + 32)
print(lowercase)       # 'a'

# Check if character is uppercase (A-Z is 65-90)
char = 'M'
if 65 <= ord(char) <= 90:
    print(f'{char} is uppercase')

# Simple Caesar cipher (shift by 3)
letter = 'A'
shifted = chr(ord(letter) + 3)
print(f'{letter} becomes {shifted}')  # A becomes D

# Generate alphabet
for i in range(26):
    print(chr(65 + i), end=' ')  # A B C D E F G ... Z
print()

for i in range(26):
    print(chr(97 + i), end=' ')  # a b c d e f g ... z
print()

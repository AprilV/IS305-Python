# Chapter 8 - Section 3: Raw Strings Practice

# Normal string - needs double backslashes
print('C:\\Users\\Alice\\Documents')

# Raw string - backslashes work as-is
print(r'C:\Users\Alice\Documents')

# Both print the same thing!

# Raw strings are useful for Windows file paths
path = r'C:\Users\Alice\Desktop\file.txt'
print(path)

# Also useful for regex patterns (you'll see this in Chapter 9)
pattern = r'\d+\.\d+'
print(pattern)

# SECTION 4: READING FILES - Practice

# Q1: Import Path from pathlib module, create variable test_path as Path('test.txt'), use write_text('Hello!'), read and print it
# Example: p = Path('data.txt')
# Example: p.write_text('Test')
# Example: print(p.read_text())


# Q2: Create variable file by opening 'test.txt', read with .read() into variable content, print, close
# Example: file = open('data.txt', encoding='UTF-8')
# Example: content = file.read()
# Example: print(content)
# Example: file.close()
file = open('test.txt')
content = file.read()
print(content)
file.close()




# Q3: Create variable file by opening 'test.txt', read with .readlines() into variable lines, print list, close
# Example: file = open('data.txt', encoding='UTF-8')
# Example: lines = file.readlines()
# Example: print(lines)
# Example: file.close()
file = open('test.txt', encoding='UTF-8')
lines = file.readlines()
print(lines)
file.close()



# Q4: Use with statement to open 'test.txt' as variable file, read into variable content, print content
# Example: with open('data.txt', encoding='UTF-8') as file:
# Example:     content = file.read()
# Example:     print(content)
with open('test.txt', encoding='UTF-8') as file:
    content = file.read()
    print(content)



# Q5: Use with statement to open 'test.txt' as variable file, loop through lines with variable line, print each with .strip()
# Example: with open('data.txt', encoding='UTF-8') as file:
# Example:     for line in file.readlines():
# Example:         print(line.strip())
with open('test.txt') as file:
    for line in file.readlines():
        print(line.strip())



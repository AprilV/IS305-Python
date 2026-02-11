# SECTION 5: WRITING FILES - Practice

# Q1: Import Path from pathlib module, create variable output_path as Path('output.txt'), use write_text() with 'Hello!', read and print
# Example: p = Path('data.txt')
# Example: p.write_text('Test')
# Example: print(p.read_text())




# Q2: Use with statement to open 'output.txt' in write mode as variable file, write 'Line 1\n' and 'Line 2\n'
# Example: with open('data.txt', 'w', encoding='UTF-8') as file:
# Example:     file.write('First\n')
# Example:     file.write('Second\n')
with open('output.txt', 'w', encoding='UTF-8') as file:
    file.write('First\n')
    file.write('Second\n')
          



# Q3: Use with statement to open 'output.txt' in append mode as variable file, write 'Line 3\n'
# Example: with open('data.txt', 'a', encoding='UTF-8') as file:
# Example:     file.write('Third\n')
with open('output.txt', 'a', encoding='UTF-8') as file:
    file.write('Third\n')



# Q4: Use with statement to open 'output.txt' as variable file, read into variable content, print all content
# Example: with open('data.txt', encoding='UTF-8') as file:
# Example:     print(file.read())
with open('output.txt') as file:
    print(file.read())



# Q5: Create demo.txt: use with to open in write mode as variable file, write 'New content\n', then use with to open in append mode as variable file, write 'Added content\n'
# Example: with open('sample.txt', 'w', encoding='UTF-8') as file:
# Example:     file.write('First\n')
# Example: with open('sample.txt', 'a', encoding='UTF-8') as file:
# Example:     file.write('Second\n')
with open('demo.txt', 'w', encoding='UTF-8') as file:
    file.write('New content\n')
with open('demo.txt', 'a', encoding='UTF-8') as file:
    file.write('Added Content\n')






# SECTION 2: PATH PARTS - Practice

# Q1: Import Path from pathlib module, create variable report_path as Path for 'C:/Users/Al/Documents/report.pdf', print filename using .name
# Example: p = Path('C:/Users/Bob/files/data.txt')
# Example: print(p.name)



# Q2: Print stem (filename without extension) of report_path
# Example: print(p.stem)
print(report_path.stem)



# Q3: Print suffix (file extension) of report_path
# Example: print(p.suffix)
print(report_path.suffix)



# Q4: Print parent folder of report_path
# Example: print(p.parent)
print(report_path.parent)



# Q5: Print all parts of report_path as tuple using .parts
# Example: print(p.parts)
print(report_path.parts)



# Q6: Create variable current with current directory, print parent using .parents[0]
# Example: current = Path.cwd()
# Example: print(current.parents[2])
current = Path.cwd()
print(current.parents[0])



# Q7: Print anchor and drive of report_path
# Example: print(p.anchor)
# Example: print(p.drive)
print(report_path.anchor)
print(report_path.drive)



# PowerShell Basics - Compared to Python

---

## Lesson 1: Variables & Data Types

### Python
```python
# Python variables
name = "April"
age = 50
price = 19.99
is_active = True

# Print
print(name)
print(f"Name: {name}, Age: {age}")  # f-string
```

### PowerShell
```powershell
# PowerShell variables - MUST start with $
$name = "April"
$age = 50
$price = 19.99
$isActive = $true  # Note: $true not True

# Print (called Write-Host)
Write-Host $name
Write-Host "Name: $name, Age: $age"  # Direct variable insertion (like f-string)
```

**KEY DIFFERENCES:**
- PowerShell: Variables ALWAYS start with `$`
- Python: `True/False` vs PowerShell: `$true/$false`
- Python: `print()` vs PowerShell: `Write-Host`

---

## Lesson 2: Lists/Arrays

### Python
```python
# Python list
fruits = ["apple", "banana", "orange"]
print(fruits[0])  # "apple"
print(len(fruits))  # 3

# Add item
fruits.append("grape")

# Loop
for fruit in fruits:
    print(fruit)
```

### PowerShell
```powershell
# PowerShell array
$fruits = @("apple", "banana", "orange")
Write-Host $fruits[0]  # "apple"
Write-Host $fruits.Count  # 3

# Add item (arrays are fixed, use += or ArrayList)
$fruits += "grape"

# Loop
foreach ($fruit in $fruits) {
    Write-Host $fruit
}
```

**KEY DIFFERENCES:**
- Python: `[]` vs PowerShell: `@()`
- Python: `.append()` vs PowerShell: `+=`
- Python: `len()` vs PowerShell: `.Count`
- Python: `for...in` vs PowerShell: `foreach...in`

---

## Lesson 3: Dictionaries/Hash Tables

### Python
```python
# Python dictionary
person = {
    "name": "April",
    "age": 50,
    "city": "Unknown"
}

print(person["name"])  # "April"
person["job"] = "PM"  # Add new key
```

### PowerShell
```powershell
# PowerShell hash table
$person = @{
    Name = "April"
    Age = 50
    City = "Unknown"
}

Write-Host $person["Name"]  # "April"
# OR
Write-Host $person.Name  # "April" (dot notation)

$person["Job"] = "PM"  # Add new key
# OR
$person.Job = "PM"
```

**KEY DIFFERENCES:**
- Python: `{}` vs PowerShell: `@{}`
- Python: Must use `["key"]` vs PowerShell: Can use `["key"]` OR `.key`

---

## Lesson 4: If Statements

### Python
```python
# Python comparisons
if age > 18:
    print("Adult")
elif age == 18:
    print("Just turned 18")
else:
    print("Minor")

# Multiple conditions
if age > 18 and is_active:
    print("Active adult")
```

### PowerShell
```powershell
# PowerShell comparisons - DIFFERENT OPERATORS!
if ($age -gt 18) {
    Write-Host "Adult"
}
elseif ($age -eq 18) {
    Write-Host "Just turned 18"
}
else {
    Write-Host "Minor"
}

# Multiple conditions
if (($age -gt 18) -and $isActive) {
    Write-Host "Active adult"
}
```

**CRITICAL DIFFERENCES - Comparison Operators:**
| Python | PowerShell | Meaning |
|--------|------------|---------|
| `==` | `-eq` | Equal |
| `!=` | `-ne` | Not equal |
| `>` | `-gt` | Greater than |
| `>=` | `-ge` | Greater or equal |
| `<` | `-lt` | Less than |
| `<=` | `-le` | Less or equal |
| `and` | `-and` | Logical AND |
| `or` | `-or` | Logical OR |
| `not` | `-not` | Logical NOT |

---

## Lesson 5: Functions

### Python
```python
# Python function
def greet(name):
    return f"Hello, {name}!"

result = greet("April")
print(result)  # "Hello, April!"
```

### PowerShell
```powershell
# PowerShell function
function Greet {
    param(
        [string]$Name
    )
    return "Hello, $Name!"
}

$result = Greet -Name "April"
Write-Host $result  # "Hello, April!"
```

**KEY DIFFERENCES:**
- Python: `def name():` vs PowerShell: `function Name {}`
- PowerShell: Parameters in `param()` block
- PowerShell: Call with `-ParameterName value`

---

## Lesson 6: Reading CSV Files (YOUR PROJECT!)

### Python
```python
import csv

# Read CSV
with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row['ProjectName'])
```

### PowerShell
```powershell
# Read CSV - SO MUCH EASIER!
$data = Import-Csv -Path ".\Data\Construction_Data.csv"

# Each row is an object - access by column name
foreach ($row in $data) {
    Write-Host $row.ProjectName
}

# Or filter with Where-Object (like Python filter)
$openProjects = $data | Where-Object { $_.Status -eq "Open" }
```

**KEY DIFFERENCE:**
- PowerShell: `Import-Csv` is BUILT-IN and creates objects automatically
- Python: Need to import csv module and work with dictionaries
- PowerShell: Use **pipeline** `|` to chain commands (super powerful!)

---

## Quick Reference Card

### Variables
- Python: `name = "value"`
- PowerShell: `$name = "value"`

### Print
- Python: `print()`
- PowerShell: `Write-Host`

### Comparisons
- Python: `==`, `!=`, `>`, `<`, `and`, `or`
- PowerShell: `-eq`, `-ne`, `-gt`, `-lt`, `-and`, `-or`

### Data Structures
- Python: `[]` list, `{}` dict
- PowerShell: `@()` array, `@{}` hash table

### Loops
- Python: `for item in list:`
- PowerShell: `foreach ($item in $list) {}`

---

## What You'll Practice Next

1. **Variables** - Store project name, status, dates
2. **Import CSV** - Read your construction data
3. **Filter data** - Find open projects, projects by PM
4. **Create report** - Write results to file

Sound good?

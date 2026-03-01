################################################################################
# Lesson 1: Write-Host, Variables, and Basic Math
# LEARN: Displaying output, storing data, simple calculations
################################################################################

# ============================================================================
# PART 1: DISPLAYING OUTPUT - Write-Host
# ============================================================================
# Write-Host displays text to the screen (like Python's print())
# 
# SYNTAX: Write-Host "your message here"
#
# CAPITALIZATION RULES:
# - PowerShell is NOT case-sensitive (write-host and Write-Host both work)
# - CONVENTION: Use PascalCase (Write-Host) for readability
# - Commands follow Verb-Noun pattern: Write-Host, Import-Csv, Get-Date
#
# QUOTES RULE:
# - Text MUST be in quotes: "text here" or 'text here'
# ============================================================================

Write-Host "Hello, April!"
Write-Host "This is PowerShell"


# ============================================================================
# COLORS (Optional Parameter)
# ============================================================================
# -ForegroundColor adds color to your text
# Available colors: Red, Green, Yellow, Blue, Cyan, Magenta, White
# This is OPTIONAL - Write-Host works without it

Write-Host "This is green text" -ForegroundColor Green
Write-Host "This is yellow text" -ForegroundColor Yellow
Write-Host "This is cyan text" -ForegroundColor Cyan


# ============================================================================
# SPECIAL CHARACTERS
# ============================================================================
# BACKTICK ` is the "escape character" (like \ in Python)
# Common escape sequences:
#   `n = newline (start a new line)
#   `t = tab

Write-Host "`nThis is after a blank line"
Write-Host "Column1`tColumn2`tColumn3"  # Tab-separated


# ============================================================================
# PART 2: VARIABLES - Storing Data
# ============================================================================
# Variables store data you want to use later
#
# RULES FOR VARIABLES:
# 1. ALWAYS start with $ (REQUIRED - not optional)
# 2. Can contain letters, numbers, underscores
# 3. Case-insensitive ($Name = $name = $NAME all the same)
# 4. Convention: Use camelCase ($firstName) or lowercase ($name)
#
# DATA TYPES (PowerShell figures this out automatically):
# - String = Text (must be in quotes)
# - Integer = Whole number (no quotes)
# - Double = Decimal number (no quotes)
# - Boolean = $true or $false
# ============================================================================


# STRING VARIABLES (text)
$name = "April"
$course = "IS305"

# Display a variable
Write-Host $name

# Put variables INSIDE double quotes
Write-Host "My name is $name"
Write-Host "I am taking $course"

# Combine (concatenate) strings
$greeting = "Hello, " + $name + "!"
Write-Host $greeting


# INTEGER VARIABLES (whole numbers)
$age = 25
$students = 30

Write-Host "Age: $age"
Write-Host "Students in class: $students"


# DECIMAL VARIABLES (numbers with decimal points)
$gpa = 3.75
$price = 19.99

Write-Host "GPA: $gpa"
Write-Host "Price: `$$price"  # `$ prints literal $ symbol


# ============================================================================
# PART 3: MATH OPERATIONS
# ============================================================================
# PowerShell supports standard math operators:
#   +  addition
#   -  subtraction
#   *  multiplication
#   /  division
#   %  modulus (remainder)
# ============================================================================

$x = 10
$y = 3

# Addition
$sum = $x + $y
Write-Host "`n$x + $y = $sum"

# Subtraction
$difference = $x - $y
Write-Host "$x - $y = $difference"

# Multiplication
$product = $x * $y
Write-Host "$x * $y = $product"

# Division
$quotient = $x / $y
Write-Host "$x / $y = $quotient"

# Modulus (remainder)
$remainder = $x % $y
Write-Host "$x % $y = $remainder"


# ============================================================================
# USING VARIABLES IN CALCULATIONS
# ============================================================================

$price = 15.99
$quantity = 5
$total = $price * $quantity

Write-Host "`nItem Price: `$$price"
Write-Host "Quantity: $quantity"
Write-Host "Total Cost: `$$total"


################################################################################
# PRACTICE EXERCISES - Copy to practice.ps1 and complete
################################################################################
#
# Exercise 1: Display Your Info
# - Create variable $myName with your name
# - Create variable $myMajor with your major
# - Display: "My name is [name] and I study [major]"
#
# Exercise 2: Age Calculator
# - Create variable $currentAge with your age
# - Create variable $nextYearAge that adds 1 to currentAge
# - Create variable $tenYearsAge that adds 10 to currentAge
# - Display all three values with labels
#
# Exercise 3: Simple Math
# - Create $num1 = 15
# - Create $num2 = 4
# - Calculate and display: sum, difference, product, quotient, remainder
#
# Exercise 4: Price Calculator
# - Create $itemPrice = 24.99
# - Create $taxRate = 0.07 (7%)
# - Calculate $taxAmount = $itemPrice * $taxRate
# - Calculate $totalPrice = $itemPrice + $taxAmount
# - Display item price, tax amount, and total price
#
################################################################################

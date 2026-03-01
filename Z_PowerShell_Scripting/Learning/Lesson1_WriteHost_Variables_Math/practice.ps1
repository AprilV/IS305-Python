################################################################################
# My Practice - Lesson 1: Write-Host, Variables, and Basic Math
################################################################################

# Q1: Create a variable $myName with your name and display it
#
# Example:
# $firstName = "John"
# Write-Host $firstName
$myName = "April"
Write-Host $myName



# Q2: Create a variable $myMajor and display it in a sentence
#
# Example:
# $subject = "Computer Science"
# Write-Host "I study $subject"
$myMajor = "dick slashing"
Write-Host "I study $myMajor"



# Q3: Create two variables ($myName and $myMajor) and display both in one sentence
#
# Example:
# $firstName = "John"
# $subject = "Computer Science"
# Write-Host "My name is $firstName and I study $subject"
$myName = "bull"
$subject ="InfoServ"
Write-Host "My name is $myName and my major is $subject"



# Q4: Create $currentAge and calculate your age next year
#
# Example:
# $age = 20
# $nextYear = $age + 1
# Write-Host "Current age: $age"
# Write-Host "Next year: $nextYear"
$currentAge = 56 
$nextYear = $currentAge + 1
Write-Host "my age next year will be $nextYear"



# Q5: Calculate your age in 10 years
#
# Example:
# $age = 20
# $future = $age + 10
# Write-Host "In 10 years: $future"
$age = 56
$inTenYears = $age + 10
Write-Host "in ten years i will be $inTenYears"



# Q6: Add two numbers together
# Create $num1 = 15 and $num2 = 4, then calculate their sum
#
# Example:
# $x = 10
# $y = 3
# $sum = $x + $y
# Write-Host "$x + $y = $sum"
$num1 = 15
$num2 = 4
$sum = $num1 + $num2

Write-Host "$num1 + $num2 = $sum"



# Q7: Calculate difference (subtraction)
# Use $num1 = 15 and $num2 = 4
#
# Example:
# $x = 10
# $y = 3
# $difference = $x - $y
# Write-Host "$x - $y = $difference"
$num1 = 15
$num2 = 4
$difference = $num1 - $num2
Write-Host "$num1 - $num2 = $difference"



# Q8: Calculate product (multiplication)
# Use $num1 = 15 and $num2 = 4
#
# Example:
# $x = 10
# $y = 3
# $product = $x * $y
# Write-Host "$x * $y = $product"
$num1 = 15
$num2 = 4
$product = $num1 * $num2
Write-Host "$num1 * $num2 = $product"



# Q9: Price calculator - Create $itemPrice = 24.99 and calculate 7% tax
#
# Example:
# $price = 100
# $taxRate = 0.05
# $tax = $price * $taxRate
# Write-Host "Tax: `$$tax"
$itemPrice = 24.99
$taxRate = 0.07
$tax = $itemPrice * $taxRate
Write-Host "Tax: $tax"



# Q10: Calculate total price (item price + tax)
# Use $itemPrice = 24.99 and $taxRate = 0.07
#
# Example:
# $price = 100
# $tax = $price * 0.05
# $total = $price + $tax
# Write-Host "Total: `$$total"
$itemPrice = 24.99
$taxRate = 0.07
$tax = $itemPrice * $taxRate
$totalPrice = $itemPrice + $tax
Write-Host "Subtotal: $itemPrice Tax: $tax Total Price: $totalPrice"
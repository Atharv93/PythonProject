import math

num1 = int(input("Enter first positive number: "))
num2 = int(input("Enter second positive number: "))
num = int(input("Enter a number to calculate square root: "))
add = num1 + num2
subtract = num1 - num2
product = num1 * num2
div = num1 / num2
print("The addition of two numbers is: ", add)
print("The subtraction of two numbers is: ", subtract)
print("The product of two numbers is: ", product)
print("The division of two numbers is: ", div)

sqrt = math.sqrt(num)
print("Square root of the given number is: ", sqrt)

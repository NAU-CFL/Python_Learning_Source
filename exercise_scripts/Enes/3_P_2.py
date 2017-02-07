# Write a Python program that prompts the user for two floating-point values
# and displays the result of the first number divided by the second,
# with exactly six decimal places displayed

# Author: Enes Kemal Ergin

num1 = float(input("Enter a float point number: "))
num2 = float(input("Enter another float point number: "))
print(format((num1/num2), ".6f"))

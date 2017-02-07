# Write a Python program that prompts the user for two integer
# values and displays the result of the first number divided by
# the second, with exactly two decimal places displayed.

# Author: Enes Kemal Ergin

num1 = int(input("Enter integer 1: "))
num2 = int(input("Enter integer 2: "))
print(format((num1/num2), '.2f'))

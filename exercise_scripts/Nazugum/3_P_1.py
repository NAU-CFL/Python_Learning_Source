# Write a Python program that prompts the user for two integer
# values and displays the result of the first number divided by
# the second, with exactly two decimal places displayed.

# Author: Enes Kemal Ergin


number1 = int(input("Enter the number: "))
number2 = int(input("Enter the divisor: "))
print(format(number1/number2, ".2f"))

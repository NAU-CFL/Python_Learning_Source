# Write a Python program that prompts the user for two integer
# values and displays the result of the first number divided by
# the second, with exactly two decimal places displayed.

# Author: Aliya Kassimova

a=int(input("Enter the value: "))
b=int(input("Enter the value: "))
result=a/b
# print(result)
# print(format(result, '.2f'))
print("The result is", format(result, '.2f'))

# Write a Python program that prompts the user for two floating-point values
#  and displays the result of the first number divided by the second,
#  with exactly six decimal places displayed.


a=float(input("Enter the value: "))
b=float(input("Enter the value: "))
result=a/b
print("The result is", format(result, '.6f'))

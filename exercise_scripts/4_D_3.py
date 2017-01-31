# Develop and test a Python program that determines if an individual qualifies
# for a government First-Time Home Buyer Tax Credit of $8,000. The credit
# was only available to those that;
# (a) bought a house that cost less than $800,000,
# (b) had a combined income of under $225,000 and
# (c) had not owned a primary residence in the last three years.

# Author: Enes Kemal Ergin

print("This program checks if you are qualifier for")
print(" government's first time home buyer tax credit:")

a = input("Have you ever bought a house that cost less than $800,000 (yes/no): ")
b = input("Is your combined income under $225,000? (yes/no):  ")
c = input("Have you owned a primary residence in last 3 years? (yes/no): ")

if a == 'yes' and b == 'yes' and c == 'no':
    print("Congratulations, you are selected for First-Time Home Buyer Tax Credit of $8,000")
else:
    print("We are really sorry to say that your application is not been approved! ")

# Write a Python program in which a student enters the number of college
#  credits earned. If the number of credits is greater than 90, 'Senior Status'
#  is displayed; if greater than 60, 'Junior Status' is displayed; if greater
#  than 30, 'Sophomore Status' is displayed; else, 'Freshman Status' is displayed.

# Author: Enes Kemal Ergin

credit = int(input("Enter your current credit: "))

if  0 < credit < 30:
    print("Freshman")
elif 0 < credit < 60:
    print("Sophomore")
elif 0 < credit < 90:
    print("Junior")
elif 0 < credit <= 120:
    print("Senior")
elif credit > 120:
    print("You should be graduated already!")
else:
    print("You need more education :) ")

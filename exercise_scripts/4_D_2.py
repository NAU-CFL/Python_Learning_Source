## Leap Years to Come

# Develop and test a Python program that displays future leap years,
#  starting with the first occurring leap year from the current year,
#  until a final year entered by the user. (HINT: Module datetime can be used)

# Author: Enes Kemal Ergin

import datetime

valid = True
current_year = datetime.datetime.now().year

while valid:
    user_year = int(input("Enter a future year: "))
    if user_year <= current_year:
        print("I am sorry, you should put a future year")
        valid = False
    else:
        while user_year > current_year:
            if (user_year % 4 == 0) and (not (user_year % 100 == 0) or (user_year % 400 == 0)):
                print(user_year, "is a leap year")
            user_year -= 1
        valid = False

# Write a program that sums a series of (positive) integers entered by the user,
#  excluding all numbers that are greater than 100.

# Author: Enes Kemal Ergin

n = 0
total = 0
while n < 5:
    inp_num = int(input("Enter integer: "))
    n += 1
    if 0 < inp_num <= 100:
        total = total + inp_num
    else:
        continue

print("The total of 5 numbers is: ", inp_num)

# Write a program, in which the user can enter any number of positive and
#  negative integer values, that displays the number of positive values entered,
#  as well as the number of negative values.

# Author: Enes Kemal Ergin

pos_count = 0
neg_count = 0

n = 0
while n < 5:
    n += 1
    num = int(input("Enter an integer number: "))
    if num < 0:
        pos_count += 1
    else:
        neg_count += 1

print("There were ", pos_count, "positive number and ", neg_count, "negative numbers entered")

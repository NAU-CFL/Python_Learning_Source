# Write a Python function named printAsterisks that is passed a positive
#  integer value n, and prints out a line of n asterisks. If n is greater
#  than 75, then only 75 asterisks should be displayed.

# Author: Aliya Kassimova

def printAsterisks(n):
    if n>=0:
        if n>75:
            print("*"*75)
        else:
            print("*"*n)
    else:
        print("Put a positive value")

# Write a Python program in which the user enters either 'A', 'B', or 'C'.
# If 'A' is entered, the program should display the word 'Apple';
# if 'B' is entered, it displays 'Banana'; and if 'C' is entered,
#  it displays 'Coconut'.

# Author: Enes Kemal Ergin

letter = input("Enter one of the following: (A, B, C): ")
temp = True
while temp:
    if letter not in ("A", "B", "C"):
        temp = True
        letter = input("Select from these (A, B, C): ")
    else:
        temp = False

if letter == "A":
    print("Apple")
elif letter == "B":
    print("Banana")
else:
    print("Coconut")

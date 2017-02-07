## Metric Conversations:

# Develop and test a Python program that converts pounds to grams,
#  inches to centimeters, and kilometers to miles. The program should
#  allow conversions both ways.

## Formulas

# 1 lb = 453.59237 g
# cm  x  0.39* = in
# in  x  2.54 = cm
# 1 mil = 1.61 km

# Author: Enes Kemal Ergin
valid = True

while valid:
    print("Which conversation you would like to do:")
    print("\t - Weight: w")
    print("\t - Length: l")
    print("\t - Speed: s")
    choice = input("Enter your selection: ")

    # Control Statements for Weight Calculation
    if choice == 'w':
        print("Please enter (p) for Pounds to Grams and (g) for Grams to Pounds: ")
        choice2 = input()
        if choice2 == 'p':
            inp_number = float(input("Enter the amount in Pounds: "))
            print(inp_number, " pounds equals to ", (inp_number * 453.59237), "grams")
            valid = False
        elif choice2 == 'g':
            inp_number = float(input("Enter the amount in grams: "))
            print(inp_number, " grams equals to ", (inp_number / 453.59237), "pounds")
            valid = False
        else:
            print("I think you did a mistake please follow the instructions:")
            print()

    # Control Statements for Length Calculation
    elif choice == 'l':
        print("Please enter (i) for Inches to Centimeters and (c) for Centimeters to Inches: ")
        choice2 = input()
        if choice2 == 'i':
            inp_number = float(input("Enter the amount in Inches: "))
            print(inp_number, " inches equals to ", (inp_number*2.54), "centimeters")
            valid = False
        elif choice2 == 'c':
            inp_number = float(input("Enter the amount in grams: "))
            print(inp_number, " centimeters equals to ", (inp_number* 0.39), "inches")
            valid = False
        else:
            print("I think you did a mistake please follow the instructions:")
            print()

    # Control Statements for Speed Calculation
    elif choice == 's':
        print("Please enter (m) for Miles to Kilometers and (k) for Kilometers to Miles: ")
        choice2 = input()
        if choice2 == 'm':
            inp_number = float(input("Enter the amount in miles: "))
            print(inp_number, " miles equals to ", (inp_number*1.61), "kilometers")
            valid = False
        elif choice2 == 'k':
            inp_number = float(input("Enter the amount in kilometers: "))
            print(inp_number, " kilometers equals to ", (inp_number/1.61), "miles")
            valid = False
        else:
            print("I think you did a mistake please follow the instructions:")
            print()
    else:
        print("I think you did a mistake please follow the instructions:")
        print()

# Number of Days in Month Program

# Program greeting
print('This program will display the number of days in a given month\n')

# Initialize
valid_input = True

# Get user input
month = int(raw_input('Enter the month (1-12): '))

# determine number of days in month
# Check February

if month == 2:
    year = int(raw_input('Please enter the year (e.g., 2010): '))

    if (year % 4 == 0) and (not (year % 100 == 0) or (year % 400 == 0)):
        num_days = 29
    else:
        num_days = 28

# Jan, Mar, May, Jul, Aug, Oct, Dec
elif month in (1, 3, 5, 7, 8, 10, 12):
    num_days = 31

# Apr, Jun, Sep, Nov
elif month in (4, 6, 9, 11):
    num_days = 30
# Invalid Input
else:
    print('* Invalid Value Entered - ', str(month) + '*')
    valid_input = False

# Output Result
if valid_input:
    print('There are ' + str(num_days) + ' days in the month')

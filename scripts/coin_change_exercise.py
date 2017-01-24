# Coin Change Exercise Program

import random

# Program greeting
print('The purpose of this exercise is to enter a number of coin values that add up to a displayed target value.')
print('Enter coins values as 1-penny, 5-nickel, 10-dime, and 25-quarter.')
print('Hit return/enter after the last entered coin value.')
print('-'*15)

# Initialize
terminate = False
empty_str = ""

# Start the Game
while not terminate:
    amount = random.randint(1,99)
    print("Enter coins that add up to " + str(amount) + " cents, one per line.")
    game_over = False
    total = 0

    while not game_over:
        valid_entry = False

        while not valid_entry:
            if total == 0:
                entry = input('Enter first coin: ')
            else:
                entry = input('Enter next coin: ')

            if entry in (empty_str, '1', '5', '10', '25'):
                valid_entry = True
            else:
                print('Invalid entry')

        if entry == empty_str:
            if total == amount:
                print('Correct!')
            else:
                print('Sorry - you only entered ' + str(total) + ' cents.')

            game_over = True
        else:
            total = total _ int(entry)
            if total > amount:
                print('Sorry - total amount exceeds ' + str(amount) + ' cents.')

    if game_over:
        entry = input('\nTry Again (y/n)?: ')

        if entry  == 'n':
            terminate = True

print('Thanks for playing ... Goodbye!')

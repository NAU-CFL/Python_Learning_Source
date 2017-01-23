# Temperature Conversion Program (Celcius-Fahrenheit / Fahrenheit-Celcius)

# Display program welcome
print('This program will convert temperatures (Fahrenheit/Celcius)')
print('Enter (F) to convert Fahrenheit to Celcius')
print('Enter (C) to convert Celcius to Fahrenheit')

# Get Temperature to convert
which = raw_input('Enter selection: ')
temp = int(raw_input('Enter temperature to convert: '))

# Determine temperature conversion needed and display results
if which == 'F' or which == 'f':
    converted_temp = (temp - 32) * 5.0/9.0
    print(str(temp) + ' degrees Fahrenheit equals ' + str(converted_temp) + ' degrees Celcius')

else:
    converted_temp = (9.0/5.0 * temp) + 32
    print(str(temp) + ' degrees Celcius equals ' + str(converted_temp) + ' degrees Fahrenheit')

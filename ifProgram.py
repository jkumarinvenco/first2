import sys

try:
    x = int(input("Please enter any number: " ))
    if x < 0:
        print("This is negative number")
    elif x == 0:
        print("This is Zero, an awesome number")
    elif x > 0:
        print("This is positive number")
    else:
        print("This is really unknown number...weird")
except ValueError:
    print('Non-numeric data in the file.')
sys.exit()

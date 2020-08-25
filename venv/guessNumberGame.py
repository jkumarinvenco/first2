import random

print("*****this is guess number game*******")
number = random.randrange(1,20)
#numberRange = 1
for numberRange in range(1,7):
    print("Guess the number from 1 to 20")
    guessedNumber = int(input())
    if guessedNumber > number:
        print("Guess is too big, try again")
    elif guessedNumber < number:
        print("Guess is too small, try again")
    else:
        #print("yes, this is the number", +guessedNumber)
        break
if guessedNumber == number:
    print("GOOD JOB, You've guessed it in " +str(numberRange) +" rounds!!")
else:
    print("NOPE, number was " +str(number))


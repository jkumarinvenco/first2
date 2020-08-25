
def collatz(number):
    if number % 2 == 0:
        print(str(number // 2))
        return number // 2
    else:
        print(str(3*number + 1))
        return 3 * number + 1
try:
    print("Enter any number below")
    userNumber = int(input())

    while userNumber != 1:
        userNumber = collatz(userNumber)
except ValueError:
    print("Error: invalid input")


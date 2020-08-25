def devidebyzero(number):

        return 42 /number

try:
    print(devidebyzero(2))
    print(devidebyzero(3))
    print(devidebyzero(0))
except ZeroDivisionError:
    print("ERROR!! Invalid Arg")
# actual Fibonacci series with good handling
nterms = int(input("Please enter number how many number of Fibonacci series:"))
n1 = 0
n2 = 1
count = 0
if nterms <= 0:
    print("Please enter Positive number")
#elif nterms == 1:
#    print("Fibonacci Series: ", nterms, ":")
#    print(n1)
else:
    print("Fibonacci series: ", nterms, ":")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count = count + 1





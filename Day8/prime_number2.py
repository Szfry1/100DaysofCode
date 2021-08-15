def primecheck(number):
    prime = True
    for num in range(2, number):
        if number % num == 0:
            prime = False
    if prime == False:
        print("This is not a prime number")
    else:
        print("This is a prime number.")

number = int(input("What number would you like to check: "))

primecheck(number=number)
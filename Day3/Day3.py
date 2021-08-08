#Day three focuses on control flow and and logical operators
#I will be doing these unguided, since it is pretty beginner level stuff

#The first thing that angela asks for is to determine whether a number is even or odd. I'm going to use a Modulo and a and if statment here

number = int(input("What is your number? "))
if number % 2 == 0:
    print("Your Number is an even number.")
else:
    print("Your Number is an odd number.")

# Angela asks for a ticketing system using a diagram using nested if/else statements
height = int(input("What is your height in CM? "))

if height > 120:
    age = int(input("You can ride. How old are you? "))
    if age < 12 :
        photos = input("Would you like photos - y or n?").lower()
        if photos == "y":
            print("Your cost will be $8.")
        else:
            print("Your cost will be $5")
    elif age >= 12 and age <= 17:
        photos = input("Would you like photos - y or n?").lower()
        if photos == "y":
            print("Your cost will be $10.")
        else:
            print("Your cost will be $7")
    else:
        photos = input("Would you like photos - y or n?").lower()
        if photos == "y":
            print("Your cost will be $15.")
        else:
            print("Your cost will be $12")
else:
    print("Sorry you are not tall enough to ride.")

#
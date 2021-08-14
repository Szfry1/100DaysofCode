#Write your code below this line 👇
def prime_checker(number):
    prime = True
    for num in range(2, number):
        if number % num == 0:
            prime = False

    if prime == True:
        print("This is a prime number")
    elif prime == False:
        print("This is not a prime number")




#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)

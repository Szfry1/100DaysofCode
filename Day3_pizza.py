print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ").lower()
add_pepperoni = input("Do you want pepperoni? Y or N ").lower()
extra_cheese = input("Do you want extra cheese? Y or N ").lower()

if size == "s":
    cost = 15
    if add_pepperoni == "y":
        cost += 2
    if extra_cheese == "y":
        cost += 1
    print (f"Your final bill is ${cost}.")

elif size == "m":
    cost = 20
    if add_pepperoni == "y":
        cost += 3
    if extra_cheese == "y":
        cost += 1
    print (f"Your final bill is ${cost}.")

elif size == "l":
    cost = 25
    if add_pepperoni == "y":
        cost += 3
    if extra_cheese == "y":
        cost += 1
    print (f"Your final bill is ${cost}.")
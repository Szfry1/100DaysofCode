import random
payers = input("Who all is paying? Please seperate with comma ")
payers_list = payers.split(',')
Who_paying = random.randint(0, len(payers_list)-1)
print(payers_list[Who_paying])

#This is the long way around on this. She specifically asked you not to use choice. Here you have to split to put into a list then you do a random int and then put that 
#as the list object number
#A way that i would do this, thats a little easier

print(random.choice(payers_list))
#This is the beginning of day 4. It appears to be a module about randomization 
# Heads or tails 
import random

random_number = random.randint(0,1)

if random_number == 1:
    print("Heads")
else:
    print("Tails")

#with randint you can basically define the range you want to generate a random number from. Here is between 0 and 1
#Another way to do this is to define a list and then do random choice from the list

Heads_tails =  ["Heads" , "Tails"]
print(f"{random.choice(Heads_tails)}")
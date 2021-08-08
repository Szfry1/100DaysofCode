print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

both_names = name1 + name2

t = both_names.count("t")
r = both_names.count("r")
u = both_names.count("u")
e = both_names.count("e")
l = both_names.count("l")
o = both_names.count("o")
v = both_names.count("v")
e1 = both_names.count("e")

Truth = str(t + r + u + e)
Lover = str(l + o + v + e1)

doublenum = int(Truth + Lover)

if doublenum < 10 or doublenum > 90:
    print(f"Your score is {doublenum}, you go together like coke and mentos.")
elif doublenum <= 40 and doublenum >= 50:
    print(f"Your score is {doublenum}, you are alright together.")
else:
    print(f"Your score is {doublenum}.")

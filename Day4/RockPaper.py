import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


allInOne = [rock, paper, scissors]

choice = input("Rock = 1 | Paper = 2 | Scissors =3 ")
ComputerChoice = random.choice(allInOne)

if choice == "1":
    if ComputerChoice == rock:
        print(rock + "vs" + rock)
        print("Draw")
    elif ComputerChoice == paper:
        print(rock + "vs" + paper)
        print("You lose")
    elif ComputerChoice == scissors:
        print(rock + "vs" + scissors)
        print("You win")
elif choice == "2":
    if ComputerChoice == rock:
        print(paper + "vs" + rock)
        print("You win")
    elif ComputerChoice == paper:
        print(paper + "vs" + paper)
        print("Draw")
    elif ComputerChoice == scissors:
        print(paper + "vs" + scissors)
        print("You Lose")
elif choice == "3":
    if ComputerChoice == rock:
        print(scissors + "vs" + rock)
        print("You lose")
    elif ComputerChoice == paper:
        print(scissors + "vs" + paper)
        print("You win")
    elif ComputerChoice == scissors:
        print(scissors + "vs" + scissors)
        print("Draw")

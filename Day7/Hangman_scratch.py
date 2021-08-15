# Going to make Hangman from scratch.
# Basically I just slept on it and moved on to another
# project and I'm just going to make sure all the concepts are stuck in my brain.
import random
list_of_words = ["this", "doggydoor", "music", "giant"]
random_word = random.choice(list_of_words)
len_of_word = int(len(random_word))
lives = 6
display = []
end_of_game = False
for item in range(len_of_word):
    display.append("_")

while end_of_game is False:
    print(display)
    print(f"You have {lives} lives left")
    guess = input("What is your guess? ")

    for position in range(len_of_word):
        if guess == random_word[position]:
            display[position] = guess
    
    if guess not in random_word:
        lives -= 1
        if lives == 0:
            print("You lose!")
            end_of_game = True
    if "_" not in display:
        print(display)
        print("You win")
        end_of_game = True

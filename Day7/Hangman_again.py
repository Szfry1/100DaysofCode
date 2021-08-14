import random
word_list = ["word","list","harmonica"]
random_word =  random.choice(word_list)
word_length = int(len(random_word))
display = []
Lives = 6
end_game = False
for letter in random_word:
    display.append("_")

while end_game == False:
    print(f"You have {Lives} lives left.")
    print(display)
    
    guess = input("What is your guess? ")
    for position in range(word_length):
        if guess in random_word[position]:
            display[position] = guess
    
    if guess not in random_word:
        Lives -=  1
        if Lives == 0:
            print("You Lose")
            end_game = True
    
    if "_" not in display:
        print("".join(display))
        print("You win!")
        end_game = True



    


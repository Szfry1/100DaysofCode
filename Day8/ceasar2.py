# going to write the cesar cipher with no help

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', "'"]


def ceasar(direction, plain_text, shift_number):
    cipher_text = ""
    if direction == "encode":
        shift_number = shift_number
    if direction == "decode":
        shift_number = shift_number * -1
    for spot in plain_text:
        if spot == " ":
            cipher_text += spot
        if spot == "'":
            cipher_text += spot
        else:
            place = alphabet.index(spot)
            rotate = (int(place) + shift_number) % 26
            moved_alpha = alphabet[rotate]
            cipher_text += moved_alpha
    print(cipher_text)
#cipher = True


while True:
    direction = input("Would you like to encode or decode? ").lower()
    plain_text = input("What would you like your message to be? ").lower()
    shift_number = int(input("How many spaces would you like to shift? "))

    ceasar(direction=direction, plain_text=plain_text, shift_number=shift_number)
    again = input("You you like to go again | yes or no? ").lower()
    if again == "yes":
        continue
    else:
        break

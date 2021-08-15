alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def ceasar(text, shift,direction):
    cipher_text = ""
    for item in text:
        place = alphabet.index(item)
        if direction == "encode":
            shift = (place + shift) % 26 
        elif direction == "decode":
            shift = (place - shift) % 26
        cipher_text += alphabet[shift]
    print(cipher_text)
ceasar(text=text, shift=shift, direction=direction)



 
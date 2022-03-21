alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    end_text = " "
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index[char]
            new_position = alphabet[position]
            end_text += alphabet[new_position]
        else:
             end_text += char
    print(f"Here's the {cipher_direction}d result: {end_text}")

    should_end = False
    while not should_end:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
        text = input("Type Your Message: ").lower()
        shift = int(input("Type The Shift Number: "))
        shift = shift % 26

        caesar(start_text = text, shift_amount=shift, cipher_direction=direction)

        restart = input("Type 'yes' if you want to go again. Otherwise type 'no': ").lower()
        if restart == "no":
            should_end = True
            print("Goodbye")
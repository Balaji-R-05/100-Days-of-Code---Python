def caesar(original_text, shift_number, cmd):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'  # Use a string for easier access
    output_text = ""

    # Normalize shift number to ensure it's within range
    shift_number %= 26
    if cmd == "decode":
        shift_number *= -1

    for letter in original_text:
        if letter in alphabets:
            original_position = alphabets.index(letter)
            new_position = (original_position + shift_number) % 26
            output_text += alphabets[new_position]
        else:
            # Keep non-alphabetic characters as they are
            output_text += letter

    print(f"Here is the {cmd}d message: {output_text}")


# User Input
cmd = input("Type 'encode' to encrypt and 'decode' to decrypt: ").lower()
if cmd not in ["encode", "decode"]:
    print("Invalid command. Please type 'encode' or 'decode'.")
else:
    text = input("Type your message: ").lower()
    shift = int(input("Enter shift number: "))

    # Call Caesar cipher function
    caesar(text, shift, cmd)
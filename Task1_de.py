
# Student Name: Jacob Braddock
# Program Name: HTML parser
# Creation Date: March 10th, 2025
# Last Modified Date: March 10th, 2025
# CSCI Course:  452
# Grade Received:  Pending
# Design Comments:This is part of a 3 task assignment in the use of encryption and decryption methods as intruscted among the 3 tasks.
import string

def caesar_decrypt(ciphertext, offset):
    alphabet = string.ascii_lowercase
    decrypted_text = ""
    for char in ciphertext:
        if char.lower() in alphabet:
            new_index = (alphabet.index(char.lower()) - offset) % 26
            new_char = alphabet[new_index]
            decrypted_text += new_char.upper() if char.isupper() else new_char
        else:
            decrypted_text += char
    return decrypted_text

if __name__ == "__main__":
    ciphertext = input("Enter the message to decrypt: ")
    offset = int(input("Enter the offset value: "))
    decrypted_text = caesar_decrypt(ciphertext, offset)
    print("Decrypted message:", decrypted_text)

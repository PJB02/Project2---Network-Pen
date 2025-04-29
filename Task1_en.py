
# Student Name: Jacob Braddock
# Program Name: HTML parser
# Creation Date: March 10th, 2025
# Last Modified Date: March 10th, 2025
# CSCI Course:  452
# Grade Received:  Pending
# Design Comments:This is part of a 3 task assignment in the use of encryption and decryption methods as intruscted among the 3 tasks.

import string

def caesar_encrypt(plaintext, offset):
    alphabet = string.ascii_lowercase
    encrypted_text = ""
    for char in plaintext:
        if char.lower() in alphabet:
            new_index = (alphabet.index(char.lower()) + offset) % 26
            new_char = alphabet[new_index]
            encrypted_text += new_char.upper() if char.isupper() else new_char
        else:
            encrypted_text += char
    return encrypted_text

if __name__ == "__main__":
    plaintext = input("Enter the message to encrypt: ")
    offset = int(input("Enter the offset value: "))
    ciphertext = caesar_encrypt(plaintext, offset)
    print("Encrypted message:", ciphertext)

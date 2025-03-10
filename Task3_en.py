import string
import math

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

def columnar_encrypt(plaintext, num_columns):
    plaintext = plaintext.replace(" ", "")
    num_rows = math.ceil(len(plaintext) / num_columns)
    matrix = [plaintext[i::num_columns] for i in range(num_columns)]
    ciphertext = "".join(matrix)
    return ciphertext

def encrypt(plaintext, caesar_offset, num_columns):
    caesar_encrypted = caesar_encrypt(plaintext, caesar_offset)
    final_encrypted = columnar_encrypt(caesar_encrypted, num_columns)
    return final_encrypted

if __name__ == "__main__":
    plaintext = input("Enter the message to encrypt: ")
    caesar_offset = int(input("Enter the Caesar cipher offset: "))
    num_columns = int(input("Enter the number of columns for Columnar Transposition: "))
    encrypted_message = encrypt(plaintext, caesar_offset, num_columns)
    print("Encrypted message:", encrypted_message)

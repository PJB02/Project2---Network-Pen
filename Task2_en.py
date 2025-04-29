import math


# Student Name: Jacob Braddock
# Program Name: HTML parser
# Creation Date: March 10th, 2025
# Last Modified Date: March 10th, 2025
# CSCI Course:  452
# Grade Received:  Pending
# Design Comments:This is part of a 3 task assignment in the use of encryption and decryption methods as intruscted among the 3 tasks.


def columnar_encrypt(plaintext, num_columns):
    plaintext = plaintext.replace(" ", "")  # Remove spaces
    num_rows = math.ceil(len(plaintext) / num_columns)
    matrix = [plaintext[i::num_columns] for i in range(num_columns)]
    ciphertext = "".join(matrix)
    return ciphertext

if __name__ == "__main__":
    plaintext = input("Enter the message to encrypt: ")
    num_columns = int(input("Enter the number of columns: "))
    ciphertext = columnar_encrypt(plaintext, num_columns)
    print("Encrypted message:", ciphertext)

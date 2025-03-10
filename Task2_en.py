import math

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
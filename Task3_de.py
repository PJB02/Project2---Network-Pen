import string
import math

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

def columnar_decrypt(ciphertext, num_columns):
    num_rows = math.ceil(len(ciphertext) / num_columns)
    num_full_cols = len(ciphertext) % num_columns
    
    matrix = ['' for _ in range(num_rows)]
    
    index = 0
    for col in range(num_columns):
        col_length = num_rows + (1 if col < num_full_cols else 0)
        for row in range(col_length):
            if index < len(ciphertext):
                matrix[row] += ciphertext[index]
                index += 1
    
    plaintext = ''.join(matrix)
    return plaintext

def decrypt(ciphertext, caesar_offset, num_columns):
    columnar_decrypted = columnar_decrypt(ciphertext, num_columns)
    final_decrypted = caesar_decrypt(columnar_decrypted, caesar_offset)
    return final_decrypted

if __name__ == "__main__":
    ciphertext = input("Enter the message to decrypt: ")
    caesar_offset = int(input("Enter the Caesar cipher offset: "))
    num_columns = int(input("Enter the number of columns for Columnar Transposition: "))
    decrypted_message = decrypt(ciphertext, caesar_offset, num_columns)
    print("Decrypted message:", decrypted_message)

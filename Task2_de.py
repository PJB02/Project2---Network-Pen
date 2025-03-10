import math

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

if __name__ == "__main__":
    ciphertext = input("Enter the message to decrypt: ")
    num_columns = int(input("Enter the number of columns: "))
    plaintext = columnar_decrypt(ciphertext, num_columns)
    print("Decrypted message:", plaintext)

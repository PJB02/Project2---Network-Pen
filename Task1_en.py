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
# Cesar cipher

import sys

salt = "raffinato"

# Generate a list with all the alphabet digits
lower_alphabeth = [chr(i) for i in range(97, 123)]
upper_alphabeth = [chr(i) for i in range(65, 91)]
alphabeth = lower_alphabeth + upper_alphabeth

def generate_key(salt: str):
    reversed_alphabeth = list(reversed(alphabeth))

    # The set function is used to create a new string with duplicates removed
    salt = set(salt)
    key = []

    for i in salt:
        key.append(i)
    for i in reversed_alphabeth:
        if i not in key:
            key.append(i)
    return key

def check_encrypt_decrypt(cypher: str):
        if cypher[0] == "#":
            return "decrypt"
        else:
            return "encrypt"

def encrypt(text: str, key: list):
    text = str(text)
    key = list(key)
    buffer = "#"

    for val in text:
        if val in alphabeth:
            buffer += key[alphabeth.index(val)]
        else:
            buffer += val
    return buffer

def decrypt(encrypted_text: str, key: str):
    encrypted_text = str(encrypted_text[1:])
    key = list(key)
    buffer = ""

    for val in encrypted_text:
        if val in alphabeth:
            buffer += alphabeth[key.index(val)]
        else:
            buffer += val
    return buffer

def main():
    try:
        api_file = open(f"{sys.path[0]}\\api_file.txt", "r")
        
        stream = ""

        # Generate the key
        key = generate_key(salt)

        for line in api_file:
            if check_encrypt_decrypt(line) == "encrypt":
                stream += encrypt(line, key)
            elif check_encrypt_decrypt(line) == "decrypt":
                stream += decrypt(line, key)
    finally:
        api_file.close()

    try:
        api_file = open(f"{sys.path[0]}\\api_file.txt", "w")
        api_file.write(stream)
    finally:
        api_file.close() 
    return None

main()
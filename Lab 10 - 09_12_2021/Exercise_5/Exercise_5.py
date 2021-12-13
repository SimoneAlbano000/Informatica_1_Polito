# Cesar cipher

salt = "raffinato"

# Generate a list with all the alphabet digits
alphabeth = [chr(i) for i in range(122, 96 , -1)]

def generate_key(salt: str):
    salt = str(salt)
    key = []

    for i in salt:
        key.append(i)

    for i in alphabeth:
        if i not in key:
            key.append(i)

    return key

def check_encrypt_decrypt(cypher: str):
    for line in api_file:
        if line[0] == "#":
            return "decrypt"
        else:
            return "encrypt"

def encrypt(text: str, key: str):
    text = str(text)
    key = str(key)
    buffer = "#"
    for i in text:
        buffer.join(key[text.index(i)]) 
    return buffer

def decrypt(encrypted_text: str, key: str):
    pass

with open("api_file.txt", "w") as api_file:
    key = generate_key(salt)

    for line in api_file:
        if check_encrypt_decrypt() == "encrypt":
            encrypted_line = encrypt(line, key)
            api_file.write(f"Line \"{line}\" is being encrypted: {encrypted_line}")
        elif check_encrypt_decrypt() == "decrypt":
            decrypted_line = decrypt(line, key)
            api_file.write(f"Line \"{line}\" is being decrypted: {encrypted_line}")
api_file.close()
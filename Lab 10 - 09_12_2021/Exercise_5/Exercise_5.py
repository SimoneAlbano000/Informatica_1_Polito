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
    try:
        api_file = open("api_file.txt", "w")
        for line in api_file:
            if line[0] == "#":
                yield "decrypt"
            else:
                yield "encrypt"
    except:
        print("File error... ")
    finally:
        api_file.close()

def encrypt(text: str):
    pass

def decrypt(encrypted_text: str):
    pass

with open("api_file.txt", "w") as api_file:
    key = generate_key(salt)

    for i, line in enumerate(api_file):
        if check_encrypt_decrypt() == "encrypt":
            encrypted_line = encrypt(line)
            api_file.write(f"Line {i} is being encrypted: #{encrypted_line}")
        elif check_encrypt_decrypt() == "decrypt":
            decrypted_line = decrypt(line)
            api_file.write(f"Line {i} is being decrypted: {encrypted_line}")


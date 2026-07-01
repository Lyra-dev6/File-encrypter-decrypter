import os
from cryptography.fernet import Fernet

def generate_key(key_filename="secret.key"):
    key = Fernet.generate_key()
    with open(key_filename, "wb") as key_file:
        key_file.write(key)
    print(f"New key generated and saved as '{key_filename}'.")

def load_key(key_filename="secret.key"):
    return open(key_filename, "rb").read()

def encrypt_file(file_path, key):
    f = Fernet(key)
    
    with open(file_path, "rb") as file:
        file_data = file.read()
        
    encrypted_data = f.encrypt(file_data)
    
    with open(file_path, "wb") as file:
        file.write(encrypted_data)
    print(f"File '{file_path}' has been encrypted.")

def decrypt_file(file_path, key):
    f = Fernet(key)
    
    with open(file_path, "rb") as file:
        file_data = file.read()
        
    decrypted_data = f.decrypt(file_data)
    
    with open(file_path, "wb") as file:
        file.write(decrypted_data)
    print(f"File '{file_path}' has been decrypted.")

if __name__ == "__main__":
    TARGET_FILE = "my_secret_document.txt"
    KEY_FILE = "encryption.key"

    with open(TARGET_FILE, "w") as f:
        f.write("This is a highly confidential message!")

    generate_key(KEY_FILE)
    encryption_key = load_key(KEY_FILE)

    encrypt_file(TARGET_FILE, encryption_key)
    decrypt_file(TARGET_FILE, encryption_key)

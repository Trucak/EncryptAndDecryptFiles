import os
import cryptography
from cryptography.fernet import Fernet


def encrypt_file(file_path, key):
    """
    This function encrypts a file using the Fernet algorithm from the cryptography library.

    Arguments:
    file_path: string with the path to the file to be encrypted
    key: Fernet object for encryption

    Returns:
    None
    """
    encrypted_file_path = os.path.splitext(file_path)[0] + "_encrypted.txt"

    with open(file_path, "rb") as f:
        file_data = f.read()  # Read data from file.

    encrypted_data = key.encrypt(file_data)  # Encrypt the file data.

    with open(encrypted_file_path, "wb") as f:
        f.write(encrypted_data)  # Write the encrypted data to the file.

    os.remove(file_path)

    return encrypted_file_path

def generate_key():
    """
    This function generates a new Fernet encryption key.

    Arguments:
    None

    Returns:
    key: Fernet object for encryption
    """
    key = Fernet.generate_key()  # Generate a new key.
    write_key_to_file(key)
    return Fernet(key)

def write_key_to_file(key):
    """
    This function writes the key to a file.

    Arguments:
    key: Fernet object for encryption

    Returns:
    None
    """
    i = 1
    filename = f'key{i}.txt'
    while os.path.exists(filename):
        i += 1
        filename = f'key{i}.txt'

    with open(filename, 'wb') as f:
        f.write(key)

if __name__ == "__main__":
    file_path = input("Please enter the path to the file you want to encrypt:")
    key = generate_key()
    encrypted_file_path = encrypt_file(file_path, key)
    print(f"The file at {file_path} was successfully encrypted. The file {encrypted_file_path} was generated with the encrypted file content.")
    print(f"The key was successfully saved to the key.txt file.")

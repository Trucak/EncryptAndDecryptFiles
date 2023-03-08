import os
import cryptography
from cryptography.fernet import Fernet


def decrypt_file(file_path, key):
    """
    This function decrypts a previously encrypted file using the Fernet algorithm from the cryptography library.

    Arguments:
    file_path: string with the path to the file to be decrypted
    key: Fernet object for decryption

    Returns:
    None
    """
    decrypted_file_path = os.path.splitext(file_path)[0] + "_decrypted.txt"

    with open(file_path, "rb") as f:
        encrypted_data = f.read()  # Read the encrypted data from the file.

    decrypted_data = key.decrypt(encrypted_data)  # Decrypt the data from the file.

    with open(decrypted_file_path, "wb") as f:
        f.write(decrypted_data)  # Write the decrypted data to the file.

    os.remove(file_path)  # Remove the encrypted file.

    return decrypted_file_path

def get_key(i):
    """
    This function prompts the user for the decryption key and returns a Fernet object with the provided key.

    Arguments:
    None

    Returns:
    key: Fernet object for decryption
    """
    key_file = f"key{i}.txt"
    with open(key_file, "rb") as f:
        key_string = f.read().strip()  # Read the key from the file.

    key = Fernet(key_string)  # Create a Fernet object with the key.
    return key


if __name__ == "__main__":
    file_path = input("Enter the path to the file you wish to decrypt:")
    i = int(input("Enter the sequential number of the key file used for encryption:"))
    key = get_key(i)
    decrypted_file_path = decrypt_file(file_path, key)
    print(f"The file at {file_path} was decrypted successfully. The file {decrypted_file_path} with the decrypted file content was generated.")
    key_file = f"key{i}.txt"
    os.remove(key_file)
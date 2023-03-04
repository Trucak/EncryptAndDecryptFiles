# File Encryption and Decryption Functions

These Python functions allow you to encrypt and decrypt files using the Fernet encryption algorithm from the cryptography library.


## Installation


To use these functions, you must have Python 3.x and the cryptography library installed on your machine. You can install the library using pip:

```bash
pip3 install cryptography
```
## Usage

#### encrypt_file(file_path, key)

This function encrypts a file using the Fernet encryption algorithm and writes the encrypted data to a new file with the suffix "_encrypted" added to the original file name. The original file is then deleted. The function takes two arguments:
- file_path (str): the path to the file you want to encrypt
- key (Fernet object): the encryption key to use for encryption
To use this function, navigate to the directory containing the encrypt_file.py file and run the following command:

```bash
python3 encrypt_file.py
```

You will be prompted to enter the file path for the file you want to encrypt. Once you enter the path, the file will be encrypted and saved to a new file with the "_encrypted" suffix added to the original file name.
#### generate_key()

This function generates a new Fernet encryption key and saves it to a file called key.txt. The function returns the encryption key as a Fernet object.

#### write_key_to_file(key)

This function writes an existing Fernet encryption key to a file called key.txt. The function takes one argument:

- key (Fernet object): the encryption key to write to the file

#### decrypt_file(file_path, key)

This function decrypts a previously encrypted file using the Fernet encryption algorithm and writes the decrypted data to a new file with the suffix "_decrypted" added to the original file name. The original encrypted file is then deleted. The function takes two arguments:
- file_path (str): the path to the encrypted file you want to decrypt
- key (Fernet object): the encryption key to use for decryption

To use this function, navigate to the directory containing the decrypt_file.py file and run the following command:

```bash
python3 decrypt_file.py
```

You will be prompted to enter the file path for the encrypted file you want to decrypt and the generated key. Once you enter the path, the file will be decrypted and saved to a new file with the "_decrypted" suffix added to the original file name.
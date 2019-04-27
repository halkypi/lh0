import base64
import os, sys
import tkinter as tk
import getpass
from tkinter import filedialog
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

#####################################################
def decrypt_file(input_file, key):

    output_file , _ = os.path.splitext(input_file)
    with open(input_file, 'rb') as f:
        data = f.read()
    fernet = Fernet(key)
    encrypted = fernet.decrypt(data)

    with open(output_file, 'wb') as f:
        f.write(encrypted)

def encrypt_file(input_file, key):

    output_file = input_file + '.encrypted'

    with open(input_file, 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)

    with open(output_file, 'wb') as f:
        f.write(encrypted)

def get_file():
    root = tk.Tk()
    root.withdraw()
    filename = filedialog.askopenfilename()
    return filename

def get_instructions():
    s = input("""Enter 'e' to encrypt or 'd' to decrypt:\n> """)
    if s.lower()[0] == 'e':
        return 'e'
    elif s.lower()[0] == 'd':
        return 'd'
    else:
        main()

def get_key(password_provided):
    password = password_provided.encode() # Convert to type bytes
    salt = b'salt_' # CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password)) # Can only use kdf once
    return key

"""
Tests:
    wrong input file, encrypt
    wrong input file, decrypt
"""

def main():
    instructions = get_instructions()

    if instructions == 'e':
        filename = get_file()
        password = getpass.getpass(prompt='Password:\n> ', stream=None)
        key = get_key(password)
        encrypt_file(filename, key)
        print('File encrypted')

    elif instructions == 'd':
        filename = get_file()
        _ , ext = os.path.splitext(filename)
        if ext != '.encrypted':
            sys.exit('Incorrect file extension')
        else:
            password = getpass.getpass(prompt='Password:\n> ', stream=None)
            key = get_key(password)
            decrypt_file(filename, key)
            print('File decrypted')

if __name__ == '__main__':
    main()

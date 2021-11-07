from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import fileinput
import argparse
import shutil


my_parser = argparse.ArgumentParser("Encrypt, decrypt file")

my_parser.add_argument(
    "Path", metavar="path",
    type=str, help="Enter path to file"
)
my_parser.add_argument(
    "Password",
    type=str, help="Enter password"
)
my_parser.add_argument(
    "Salt",
    type=str, help="Enter salt"
)
my_parser.add_argument(
    "What",
    type=str, help="Enter what you need"
)

args = my_parser.parse_args()
file_name = args.Path
password = args.Password
salt = args.Salt
action = args.What


kdf = PBKDF2HMAC(
    algorithm=hashes.SHA512_224(),
    length=32,
    iterations=10000,
    backend=default_backend(),
    salt=f"{salt}".encode("utf-8")
)

file = f"{file_name}"
my_key = f"{password}".encode("utf-8")
key = base64.urlsafe_b64encode(kdf.derive(my_key))
f = Fernet(key)


# Encrypt
def encrypt_file():
    with fileinput.FileInput(file, inplace=True) as myfile:
        for line in myfile:
            encrypted_line = f.encrypt(line.encode("utf-8"))
            print(encrypted_line.decode(), end="\n")


# Decrypt file
def decrypt_file():
    shutil.copy(file, file + "-backup")
    with fileinput.FileInput(file, inplace=True) as conv_file:
        for line in conv_file:
            convert_line = f.decrypt(line.encode("utf-8"))
            print(convert_line.decode().strip(), end="\n")


if __name__ == '__main__':
    if action == "encrypt":
        encrypt_file()
    elif action == 'decrypt':
        decrypt_file()
    else:
        print(">>>???<<<")

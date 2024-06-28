import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "mod.py" or file == "here_is_the_key.key" or file == "decrypt.py":
        continue

    if os.path.isfile(file):
        files.append(file)

print(files)

key = Fernet.generate_key()

with open("here_is_the_key.key", "rb") as here_is_the_key:
    secretkey = here_is_the_key.read()

for file in files:
    with open(file, "rb") as File:
        contents = File.read()
    content_decrypted = Fernet(secretkey).decrypt(contents)

    with open(file, "wb") as File:
        File.write(content_decrypted)

print("Your files are decrypted now!")

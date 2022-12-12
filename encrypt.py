# Encrypting a file with text in a symmetric block cipher algorithm AES

import pyAesCrypt
password = input("Введите пароль для шифрования файла")  # Asking for a password from a user

# file encryption
pyAesCrypt.encryptFile("txt","txt.aes",password)         # 1 argument - file name, 2 argument - output name, 3 argument - specify password

# file decryption
pyAesCrypt.decryptStream("txt.aes","txt_1",password)     # 1 argument - path of the encrypted file, 2 argument - path to the file where the data will be written, 3 argument - user password


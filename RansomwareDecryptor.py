from cryptography.fernet import Fernet
import os
key = b'insert the key here.'
f = Fernet(key)
for files in os.listdir():
    try:
        with open(files, "r") as file:
            contents = file.readlines()
            file.close()
        decrypted_list = []
        for i in contents:
            e = f.decrypt(i.encode())
            decrypted_list.append(e)
        with open(files, 'w') as file:
            for i in decrypted_list:
                file.writelines(i.decode())
        print(f"Successfully Decrypted File: {files}")
    except:
        pass

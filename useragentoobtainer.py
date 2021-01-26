import threading, os
try:
    from fake_useragent import UserAgent
except:
    os.system('pip install fake_useragent')
filename = input("[+] Enter the name of the file you want to create: ")
if '.txt' not in filename:
    filename += '.txt'
file = open(filename,'w')
def add_agent():
    while True:
        ua = UserAgent()
        print(ua.chrome)
        file.writelines(ua.chrome + '\n')
while True:
   try:
       x = threading.Thread(target=add_agent)
       x.start()
   except:
       pass

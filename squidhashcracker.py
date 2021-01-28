import hashlib, sys
from optparse import OptionParser
def get_args():
    global encoding
    global filename
    global hash
    global onlyencode
    global string
    onlyencode = False
    args = OptionParser()
    args.add_option("-E","--encode",dest="encoding",help="Type of encoding")
    args.add_option("-F","--filename",dest="filename",help="filename of passwords")
    args.add_option('-H','--hash',dest="hash",help="specify hash")
    args.add_option('-S','--string',dest="string")
    arg, opt = args.parse_args()
    if arg.encoding is None:
        encoding = "md5"
    else:
        encoding = arg.encoding
    if arg.string is None:
        pass
    else:
        string = arg.string
        onlyencode = True
    if not onlyencode:
        if arg.filename is None:
            usage()
        else:
            filename = arg.filename
        if arg.hash is None:
            usage()
        else:
            hash = arg.hash
def usage():
    print("""
       _____             _     _ _    _           _      _____                _               ___    ___  
      / ____|           (_)   | | |  | |         | |    / ____|              | |             |__ \  / _ \ 
     | (___   __ _ _   _ _  __| | |__| | __ _ ___| |__ | |     _ __ __ _  ___| | _____ _ __     ) || | | |
      \___ \ / _` | | | | |/ _` |  __  |/ _` / __| '_ \| |    | '__/ _` |/ __| |/ / _ \ '__|   / / | | | |
      ____) | (_| | |_| | | (_| | |  | | (_| \__ \ | | | |____| | | (_| | (__|   <  __/ |     / /_ | |_| |
     |_____/ \__, |\__,_|_|\__,_|_|  |_|\__,_|___/_| |_|\_____|_|  \__,_|\___|_|\_\___|_|    |____(_)___/ 
                | |                                                                                       
                |_|                                                                                                                                                    
    Script By DrSquid
    
    Commands:
    -F, --filename : specifies a filename
    -E, --encoding : Specifies which type of encoding(default is md5)
    -H, --hash : Specify the hash to decode
    -S, --string : Specify a string to encode
    Examples:
    python3 squidhashcracker.py -S hello
    python3 squidhashcracker.py -H 5d41402abc4b2a76b9719d911017c592 -E md5 -F passwords.txt
    """)
    sys.exit()
    quit()
def decode(hash):
    file = open(filename, 'r')
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        if encoding == "md5":
            enc = hashlib.md5(line.encode()).hexdigest()
        elif encoding == "sha256":
            enc = hashlib.sha256(line.encode()).hexdigest()
        elif encoding == "sha1":
            enc = hashlib.sha1(line.encode()).hexdigest()
        elif encoding == "sha224":
            enc = hashlib.sha224(line.encode()).hexdigest()
        elif encoding == "sha384":
            enc = hashlib.sha384(line.encode()).hexdigest()
        elif encoding == "sha512":
            enc = hashlib.sha512(line.encode()).hexdigest()
        else:
            print("[+] Invalid Encoding Arguement!")
            usage()
            sys.exit()
            quit()
        print(f"\n[+] String: {line}")
        print(f"[+] Hashed String: {enc}")
        if enc == hash:
            print(f"[+] Found a match: {line}")
            input("[+] Press enter to exit.")
            sys.exit()
            quit()
        else:
            print(f"[+] {line} was not a match.")
def encode(string, hashtype):
    if encoding == "md5":
        enc = hashlib.md5(string.encode()).hexdigest()
    elif encoding == "sha256":
        enc = hashlib.sha256(string.encode()).hexdigest()
    elif encoding == "sha1":
        enc = hashlib.sha1(string.encode()).hexdigest()
    elif encoding == "sha224":
        enc = hashlib.sha224(string.encode()).hexdigest()
    elif encoding == "sha384":
        enc = hashlib.sha384(string.encode()).hexdigest()
    elif encoding == "sha512":
        enc = hashlib.sha512(string.encode()).hexdigest()
    else:
        print("[+] Invalid Encoding.")
        usage()
    return enc
if __name__ == "__main__":
    get_args()
    if len(sys.argv) < 3:
        usage()
    print("""
         _____             _     _ _    _           _      _____                _               ___    ___  
        / ____|           (_)   | | |  | |         | |    / ____|              | |             |__ \  / _ \ 
       | (___   __ _ _   _ _  __| | |__| | __ _ ___| |__ | |     _ __ __ _  ___| | _____ _ __     ) || | | |
        \___ \ / _` | | | | |/ _` |  __  |/ _` / __| '_ \| |    | '__/ _` |/ __| |/ / _ \ '__|   / / | | | |
        ____) | (_| | |_| | | (_| | |  | | (_| \__ \ | | | |____| | | (_| | (__|   <  __/ |     / /_ | |_| |
       |_____/ \__, |\__,_|_|\__,_|_|  |_|\__,_|___/_| |_|\_____|_|  \__,_|\___|_|\_\___|_|    |____(_)___/ 
                    | |                                                                                       
                    |_|                                                              
        Script By DrSquid\n""")
    if not onlyencode:
        decode(hash)
    else:
        encoded_str = encode(string, encoding)
        print(encoded_str)

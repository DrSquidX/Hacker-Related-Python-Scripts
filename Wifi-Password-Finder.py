#This script can only find wifi passwords stored on your computer.
import subprocess, re
item = subprocess.run(["netsh","wlan","show","profiles"],capture_output=True).stdout.decode()
prof_names = (re.findall("All User Profile     : (.*)\r", item))
passwords = []
check_networks = []
for i in prof_names:
    item = subprocess.run(["netsh", "wlan", "show", "profiles",i], capture_output=True).stdout.decode()
    security_key = False
    security_key_present = (re.findall("Security key           : (.*)\r", item))
    if security_key_present[0] == "Present":
        check_networks.append(i)
    else:
        pass
for i in check_networks:
    item = subprocess.run(["netsh","wlan","show","profiles",i,"key=clear"],capture_output=True).stdout.decode()
    wifi_pass = (re.findall("Key Content            : (.*)\r",item))
    wifi_pass = wifi_pass[0]
    info = {'ssid': i, 'key': wifi_pass}
    passwords.append(info)
for i in passwords:
    print(i)

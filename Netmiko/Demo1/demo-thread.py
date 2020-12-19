from netmiko import ConnectHandler
from threading import Thread
from datetime import datetime

starttime = datetime.now()

threads = []

def chkconn(ip):
    
        device = ConnectHandler(device_type='cisco_xe', ip=ip, username='cisco', password='cisco')
        hostname = device.send_command("show run | in hostname")
        output = hostname.split(" ")
        hostname = output[1]
        print("Hostname for IP %s is : %s" % (ip, hostname))
        device.disconnect()
    
for n in range(2, 4):
    ip = "192.168.122.{0}".format(n)
    t = Thread(target=chkconn, args = (ip,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()


print(datetime.now() - starttime)


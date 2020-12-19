import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

for n in range(1, 5):
    server = "192.168.122.{0}".format(n)
    res = os.system('ping ' + server + ' -c 1')
    if res == 0:
        print("server {0} is reachable".format(server))
    else:
        print("server {0} is unreachable".format(server))
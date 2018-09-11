import socket
import sys

host = ''
port = 6666
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.bind((host, port))
except socket.error as e:
    print(str(e))

sock.listen(5)
print("waiting for a connection...")
conn, addr = sock.accept()
print("Connected to: {} : {}".format(addr[0], addr[1]))

# Client Program
import socket
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
print(host)
port = 9999

mysocket.connect((host, port))
data = mysocket.recv(2048)
print(data)
mysocket.send(b"This is Client")
# mysocket.close()

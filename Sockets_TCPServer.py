# Server Program
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
print(host)
port = 9999
mysock.bind((host, port))
mysock.listen(5)
client, (ip, port) = mysock.accept()
print("clientip: {}, port: {}".format(ip, port))
client.send(b"knock knock knock, I'm Server")
data = client.recv(2048)
print(data)
# mysock.close()


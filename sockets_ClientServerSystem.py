import socket
import sys
import _thread

host = ''
port = 5555
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.bind((host, port))
except socket.error as e:
    print(str(e))

sock.listen(5)
print("waiting for a connection...")


def threaded_client(conne):
    conne.send(str.encode('Welcome.. Type your Info.\r\n'))

    while True:
        reply = ''

        data = conne.recv(2048)
        print("Data received from client: {}".format(data))
        if b"\xff" not in data:
            data = str(data, encoding='ascii').upper()
            # reply = 'Server Output: ' + data.decode('utf-8') + '\r\n'
            reply = 'Server Output: ' + bytes(data, encoding='ascii').decode('ascii') + '\r'
        if not data:
            break
        conne.sendall(str.encode(reply))
    conne.close()


while True:
    conn, addr = sock.accept()
    print("Connected to: {} : {}".format(addr[0], addr[1]))
    _thread.start_new_thread(threaded_client, (conn, ))

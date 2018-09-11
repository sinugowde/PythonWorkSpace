import socket

HOST, PORT = '', 80

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print('Serving HTTP on port {} ...'.format(PORT))

while True:
    client_connection, client_address = listen_socket.accept()
    print("conn: {}: addr: {}".format(client_connection, client_address))
    request = client_connection.recv(1024)
    print(request)
    # print(request)

    # http_response = b"""HTTP/1.1 200 OK \n:) Hello, World!"""
    http_response = b"""HTTP/1.1 200 OOK \r\n Hello, World!"""
    client_connection.sendall(http_response)
    client_connection.close()



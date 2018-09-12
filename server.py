import socket
import _thread

dataFormat = {}


class HTTPServer:

    def __init__(self):
        # self.request = request.decode(encoding='utf-8')
        self.request = ''
        self.methodMapping = {"GET": self.parseGet, "PUT": self.parsePut, "HEAD": self.parseHead,
                              "POST": self.parsePost}

    def set_request(self, request):
        self.request = request.decode(encoding='utf-8')

    def parseGet(self, data):
        requestLine = data['requestLine'].split(" ")
        method = requestLine[0]
        uri = requestLine[1]
        version = requestLine[2]

        if uri == "/":
            uri += "index.html"

        print("method: {}\turi: {}\tversion: {}".format(method, uri, version))
        return self.prepareResponse(data, method, uri, version)

    def prepareResponse(self, data, method, uri, version):
        response = "HTTP/1.1 200 OK\nServer: MKSERVER\n\n<!DOCTYPE html>\n<html><h1><br>Aricent Web Server </br><br>Method: "+method+"\n</br><br>uri: "+uri+"\n</br><br>Version: "+version+"<br></h1></html>"
        method = (data['requestLine'].split(" "))[0]
        uri = (data['requestLine'].split(" "))[1]
        version = (data['requestLine'].split(" "))[2]
        
        filepath = 'webpages' + uri
        res = ''
        with open(filepath, 'r') as f:
            res = f.read()
        res = res.replace("method", (data['requestLine'].split(" "))[0])
        res = res.replace("headerData", data['header'])
        res = "HTTP/1.1 200 OK\n\n" + res
        f.close()
        return response

    def parsePut(self, data):
        print("Received Put request\n")
        pass

    def parseHead(self, data):
        print("Received Head request\n")
        pass

    '''
    Serving HTTP on port 8888 ...
    POST /testpost.html HTTP/1.1

    HOST: localhost:8888

    content-type: text/plain

    content-length: 96

    

    Title = Aricent Certification program

    language = Python

    ProjectName = WebServer Implementation
    '''

    def parsePost(self, postReq):
        print(*"Received Post request\n")
        print(postReq)

        for v in postReq['header'].splitlines():
            if 'content-length' in v:
                conLen = v.split(":")[1]

        if int(conLen) == len(postReq['msgBody']):
           print("full msg body received")

        requestLine = postReq['requestLine'].split(" ")
        uri = requestLine[1]
        filename = 'webpages' + uri
        writeFd = open(filename, 'w')
        writeFd.write(postReq['msgBody'])

    def methodToRun(self, methodToCall, decodeData):
        print("method to run\n")
        return methodToCall(decodeData)

    def parseRequest(self):
        decodedData = self.decodeRequest()

        request_dictionary = {}
        request_line = decodedData['requestLine'].split()
        request_dictionary['method'] = request_line[0]
        request_dictionary['uri'] = request_line[1]
        request_dictionary['http_ver'] = request_line[2]
        decodedData['requestLine'] = request_dictionary

        header_dictionary = {}
        header_data = decodedData['header'].splitlines()
        for line in header_data:
            header_dictionary[(line.split(':', maxsplit=1))[0]] = ((line.split(':', maxsplit=1))[1]).strip()
        decodedData['header'] = header_dictionary

        print("decodedData:\n")
        for key, value in decodedData.items():
            print("{}: {}".format(key, value))
        print('\n')
        responseData = ''
        # method = (decodedData['requestLine'].split(" "))[0]
        # responseData = self.methodToRun(self.methodMapping[method], decodedData)
        return responseData
        
    def decodeRequest(self):
        data = {}

        reqIndex = self.request.find('\r\n')
        data['requestLine'] = self.request[0:reqIndex]

        hdrIndex = self.request.find('\r\n\r\n')
        data['header'] = self.request[reqIndex+2:hdrIndex]

        msgBdyIndex = hdrIndex + 4
        data['msgBody'] = self.request[msgBdyIndex:len(self.request)]

        print("DATA: {}".format(data) + '\n')

        return data


def threaded_client(client_socket, server_instance):

    while True:
        try:
            request = client_connection.recv(1024)
        except ConnectionResetError:
            print("*** Connection Closed ***")
            client_socket.close()
            break
        except:
            print("*** Connection is Broken ***")
            client_socket.close()
            break

        print("Data received from client: {}".format(request))

        if not request:
            print("\n**NO DATA PRESENT**\n")
            print("*** closing the Connection ***")
            client_socket.close()
            break

        server_instance.set_request(request)
        response = server_instance.parseRequest()
        print("Sending Response: ")
        #response = 'HTTP/1.1 200 OK\n'
        client_connection.sendall(response.encode(encoding='utf-8'))
        client_connection.close()


# main function start hear
HOST, PORT = '', 8888

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print('Serving HTTP on port {} ...'.format(PORT))

while True:
    client_connection, client_address = listen_socket.accept()
    print("Connected to: {} : {}".format(client_address[0], client_address[1]))
    server = HTTPServer()
    _thread.start_new_thread(threaded_client, (client_connection, server))


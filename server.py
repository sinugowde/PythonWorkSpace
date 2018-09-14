import socket
import _thread
from wsgiref.handlers import format_date_time
from datetime import datetime
from time import mktime

dataFormat = {}


class HTTPServer:

    def __init__(self):
        # self.request = request.decode(encoding='utf-8')
        self.request = {}
        self.response = {}
        self.methodMapping = {"GET": self.parseGet, "PUT": self.parsePut, "HEAD": self.parseHead,
                              "POST": self.parsePost}

    def set_request(self, request):
        self.request = request.decode(encoding='utf-8')

    def print_request(self):
        print("decodedData:")
        for key, value in self.request.items():
            print("{:<12}: {:<}".format(key, str(value)))
        print('\n')

    def generate_date_time_stamp(self):
        now = datetime.now()
        stamp = mktime(now.timetuple())
        return 'Date: ' + format_date_time(stamp)

    def web_page(self):
        if (self.request['requestLine'])['uri'] == '/':
            content = "<html><head><meta http-equiv=\"Content-Type\" content=\"text/html; " \
                      "charset=utf-8\"></head><body><h1>Aricent Web Server</h1>" \
                      "<h2>Welcome to our Web Page</h2></body></html>"
        return content

    def method_not_implemented(self):
        status_line = (self.request['requestLine'])['http-ver'] + " 501 Not Implemented"
        self.response['status-line'] = status_line
        self.response['message-body'] = "<html><head><meta http-equiv=\"Content-Type\" content=\"text/html; " \
                                        "charset=utf-8\"></head><body><h2>Aricent Web Server</h2><div>501 - " \
                                        "Not Implemented</div></body></html>"
        self.response['general-header'] = 'Date: ' + self.generate_date_time_stamp()
        return self.prepareResponse()

    def parseGet(self):
        print(*"Received GET request\n")
        request_line = self.request['requestLine']

        self.response['status-line'] = request_line['http-ver'] + ' '
        self.response['general-header'] = self.generate_date_time_stamp()

        if request_line['uri'] == "/":
            self.response['status-line'] += '200 OK'
            self.response['message-body'] = self.web_page()

        print("Response: {}".format(self.response) + '\n')

        return self.prepareResponse()

    def prepareResponse(self):
        response_string = ''
        response_format = ['status-line', 'general-header', 'response-header', 'entity-header', 'message-body']
        print("prepare_response: {}".format(self.response))
        self.response['general-header'] += '\r\nConnection: close'
        self.response['general-header'] += '\r\nContent-Type: text/html'

        for item in response_format:
            if item in self.response:
                if response_string == '':
                    response_string = self.response[item] + '\r\n'
                elif item == 'message-body':
                    if (self.request['requestLine'])['method'] is not 'HEAD':
                        response_string = response_string + '\r\n' + self.response[item] + '\r\n'
                else:
                    response_string = response_string + self.response[item] + '\r\n'
        print("response_string: {}".format(response_string))
        return response_string

    def parsePut(self):
        print(*"Received PUT request\n")
        pass

    def parseHead(self):
        print(*"Received HEAD request\n")
        return self.parseGet()

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

    def parsePost(self):
        print(*"Received POST request")

        print(self.request)
        uri = (self.request['requestLine'])['uri']
        print('uri: {}'.format(uri))
        print('replace: {}'.format(uri.replace('http://localhost:8888/', '')))


        # if int(conLen) == len(postReq['msgBody']):
        #    print("full msg body received")
        #
        # requestLine = postReq['requestLine'].split(" ")
        # uri = requestLine[1]
        # filename = 'webpages' + uri
        # writeFd = open(filename, 'w')
        # writeFd.write(postReq['msgBody'])

    def methodToRun(self):
        print("Method to Run: {}".format((self.request['requestLine'])['method']))

        try:
            methodToCall = self.methodMapping[(self.request['requestLine'])['method']]
        except:
            methodToCall = self.method_not_implemented
        return methodToCall()

    def parseRequest(self):
        decodedData = self.decodeRequest()

        request_dictionary = {}
        request_line = decodedData['requestLine'].split()
        request_dictionary['method'] = request_line[0]
        request_dictionary['uri'] = request_line[1]
        request_dictionary['http-ver'] = request_line[2]
        decodedData['requestLine'] = request_dictionary

        header_dictionary = {}
        header_data = decodedData['header'].splitlines()
        for line in header_data:
            header_dictionary[(line.split(':', maxsplit=1))[0]] = ((line.split(':', maxsplit=1))[1]).strip()
        decodedData['header'] = header_dictionary

        self.request = ''
        self.request = decodedData
        self.print_request()

    def decodeRequest(self):
        data = {}

        reqIndex = self.request.find('\r\n')
        data['requestLine'] = self.request[0:reqIndex]

        hdrIndex = self.request.find('\r\n\r\n')
        data['header'] = self.request[reqIndex+2:hdrIndex]

        msgBdyIndex = hdrIndex + 4
        data['msgBody'] = self.request[msgBdyIndex:len(self.request)]

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

        # response = ''
        server_instance.set_request(request)
        server_instance.parseRequest()
        response = server_instance.methodToRun()
        print("Sending Response: \n")
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


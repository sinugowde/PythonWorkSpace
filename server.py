import socket
import os
import _thread
from wsgiref.handlers import format_date_time
from datetime import datetime
from time import mktime
import json
import re

dataFormat = {}


class HTTPServer:

    def __init__(self):
        # self.request = request.decode(encoding='utf-8')
        self.request = {}
        self.response = {}
        self.methodMapping = {"GET": self.parseGet, "PUT": self.parsePut, "HEAD": self.parseHead,
                              "POST": self.parsePost}
        return

    def set_request(self, request):
        self.request = request.decode(encoding='utf-8')
        return

    def print_request(self):
        print("decodedData:")
        for key, value in self.request.items():
            print("{:<12}: {:<}".format(key, str(value)))
        print('\n')
        return

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

    def get_from_index(self, index):
        if os.stat('data.json').st_size == 0:
            json_data = []
        else:
            with open('data.json', 'r') as data_file:
                json_data = json.load(data_file)
        if index == 'all':
            self.response['status-line'] += '200 OK'
            self.response['message-body'] = json.dumps(json_data, indent=4)
        elif len(json_data) >= index:
            self.response['status-line'] += '200 OK'
            self.response['message-body'] = json.dumps(json_data[index - 1], indent=4)
        else:
            self.response['status-line'] += '404 NOT FOUND'
        return

    def parseGet(self):
        print(*"Received GET request\n")
        request_line = self.request['requestLine']

        self.response['status-line'] = request_line['http-ver'] + ' '
        self.response['general-header'] = self.generate_date_time_stamp()

        if request_line['uri'] == "/":
            self.response['status-line'] += '200 OK'
            self.response['message-body'] = self.web_page()
        elif re.findall(r"/post/\d+", request_line['uri']):
            self.get_from_index(int((request_line['uri'].strip('/')).split('/')[1]))
        elif request_line['uri'] == '/post/' or request_line['uri'] == '/post':
            self.get_from_index('all')
        else:
            self.response['status-line'] += '404 NOT FOUND'
        self.response['general-header'] += '\r\nConnection: close'
        self.response['general-header'] += '\r\nContent-Type: text/html'

        print("Response: {}\n".format(self.response) + '\n')

        return self.prepareResponse()

    def prepareResponse(self):
        response_string = ''
        response_format = ['status-line', 'general-header', 'response-header', 'entity-header', 'message-body']
        print("prepare_response: {}\n".format(self.response))

        for item in response_format:
            if item in self.response:
                if response_string == '':
                    response_string = self.response[item] + '\r\n'
                elif item == 'message-body':
                    if (self.request['requestLine'])['method'] != 'HEAD':
                        response_string = response_string + '\r\n' + self.response[item] + '\r\n'
                else:
                    response_string = response_string + self.response[item] + '\r\n'
        print("response_string: {}\n".format(response_string))
        return response_string

    def put_to_index(self, index):
        print("put_to_index: index:: {}\n".format(index))
        if os.stat('data.json').st_size == 0:
            self.response['status-line'] = (self.request['requestLine'])['http-ver'] + ' 404 Not Found'
        else:
            datum = {}
            with open('data.json', 'r') as data_file:
                json_data = json.load(data_file)

            print("put_to_index: len: {}\tjson_data:: {}\n".format(len(json_data),json_data))
            print("put_to_index: json_data_type:: {}\n".format(type(json_data)))

            if (index > 0) and (index <= len(json_data)):
                message_body = self.request['msgBody']
                message_body = re.findall(r'([\w\s]+=[\w\s]+)', message_body)

                for i in range(0, len(message_body), 2):
                    datum[(message_body[i].split('='))[1]] = (message_body[i+1].split('='))[1]

                json_data[index-1] = datum
                print("put_to_index: json_data:: {}\n".format(json_data))

                with open('data.json', 'w') as data_file:
                    if datum:
                        json.dump(json_data, data_file, indent=4)
                self.response['general-header'] += '\r\nLocation: http://localhost:5555/post/'\
                                                   + str(json_data.index(datum) + 1)
                self.response['message-body'] = json.dumps(datum, indent=4)
                self.response['general-header'] += '\r\nContent-Length: ' + str(len(self.response['message-body']))

            else:
                self.response['status-line'] = (self.request['requestLine'])['http-ver'] + ' 404 Not Found'
        return

    def parsePut(self):
        print(*"Received PUT request\n")

        request_line = self.request['requestLine']

        uri = request_line['uri']
        print('uri: {}\n'.format(uri))
        self.response['status-line'] = request_line['http-ver'] + ' '
        self.response['general-header'] = self.generate_date_time_stamp()

        if re.match(r"/post/\d+", request_line['uri']):
            print("parsePut-IF: {}".format(request_line['uri']))
            self.response['status-line'] = (self.request['requestLine'])['http-ver'] + ' 200 OK'
            self.put_to_index(int((request_line['uri'].strip('/')).split('/')[1]))
        else:
            print("parsePut-ELSE: {}".format(request_line['uri']))
            self.response['status-line'] = (self.request['requestLine'])['http-ver'] + ' 404 Not Found'

        self.response['general-header'] += '\r\nContent-Type: application/json; charset=utf-8'
        self.response['general-header'] += '\r\nConnection: keep - alive'
        self.response['general-header'] += '\r\nServer: Aricent Web Server'
        self.response['general-header'] += '\r\nExpires: -1'
        print("post_response: {}\n".format(self.response))

        return self.prepareResponse()

    def parseHead(self):
        print(*"Received HEAD request\n")
        return self.parseGet()

    def prepare_post_data(self):

        if os.stat('data.json').st_size == 0:
            json_data = []
        else:
            with open('data.json', 'r') as data_file:
                json_data = json.load(data_file)

        datum = {}
        header = self.request['header']
        message_body = self.request['msgBody']

        if 'text/csv' in header['Content-Type'] or 'application/x-www-form-urlencoded' in header['Content-Type']:
            message_body = re.findall(r'([\w\s]+=[\w\s]+)', message_body)

            if message_body:
                for i in range(0, len(message_body), 2):
                    datum[(message_body[i].split('='))[1]] = (message_body[i+1].split('='))[1]
            else:
                self.response['status-line'] = (self.request['requestLine'])['http-ver'] + ' 500 Internal Server Error'
        elif 'application/json' in header['Content-Type']:
            try:
                datum = json.loads(message_body)
            except:
                self.response['status-line'] = (self.request['requestLine'])['http-ver'] + ' 500 Internal Server Error'

        if datum not in json_data:
            json_data.append(datum)
            with open('data.json', 'w') as data_file:
                if datum:
                    json.dump(json_data, data_file, indent=4)
        self.response['general-header'] += '\r\nLocation: http://localhost:5555/' + str(json_data.index(datum)+1)

        return datum

    def parsePost(self):

        self.response.clear()
        print(*"Received POST request")
        request_line = self.request['requestLine']

        uri = request_line['uri']
        print('uri: {}\n'.format(uri))
        self.response['status-line'] = request_line['http-ver'] + ' '
        self.response['general-header'] = self.generate_date_time_stamp()

        if uri == '/post':
            self.response['status-line'] += '201 Created'
            self.response['message-body'] = json.dumps(self.prepare_post_data(), indent=4)
        else:
            self.response['status-line'] += '404 Not Found'
            self.response['message-body'] = '{}'

        self.response['general-header'] += '\r\nContent-Type: application/json; charset=utf-8'
        self.response['general-header'] += '\r\nContent-Length: ' + str(len(self.response['message-body']))
        self.response['general-header'] += '\r\nConnection: keep - alive'
        self.response['general-header'] += '\r\nServer: Aricent Web Server'
        self.response['general-header'] += '\r\nExpires: -1'
        print("post_response: {}\n".format(self.response))

        return self.prepareResponse()

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
        return

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
            print("*** Connection Closed ***\n")
            client_socket.close()
            break
        except:
            print("*** Connection is Broken ***\n")
            client_socket.close()
            break

        print("Data received from client: {}\n".format(request))

        if not request:
            print("\n**NO DATA PRESENT**\n")
            print("*** closing the Connection ***\n")
            client_socket.close()
            break

        # response = ''
        server_instance.set_request(request)
        server_instance.parseRequest()
        response = server_instance.methodToRun()
        print("\nSending Response:\n{}\n".format(response))
        client_connection.sendall(response.encode(encoding='utf-8'))
        client_connection.close()


# main function start hear
HOST, PORT = '', 5555

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print('Serving HTTP on port {} ...'.format(PORT))

while True:
    client_connection, client_address = listen_socket.accept()
    print("Connected to: {} : {}\n".format(client_address[0], client_address[1]))
    server = HTTPServer()
    _thread.start_new_thread(threaded_client, (client_connection, server))


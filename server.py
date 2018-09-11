import socket

dataFormat = {}

class HTTPServer:

    def __init__(self,request):
        self.request = request
        self.methodMapping = {"GET":self.parseGet,"PUT":self.parsePut,"HEAD":self.parseHead,"POST":self.parsePost}
        

    def parseGet(self,data):
        requestLine = data['requestLine'].split(" ")
        method = requestLine[0]
        uri = requestLine[1]
        version = requestLine[2]

        if(uri == "/"):
            uri += "index.html"

        print "method: " + method + "\t" + "uri: " + uri + "\t" + "version: " + version
        return self.prepareResponse(data,method,uri,version)

    def prepareResponse(self,data,method,uri,version):
        response = "HTTP/1.1 200 OK\nServer: MKSERVER\n\n<!DOCTYPE html>\n<html><h1><br>Aricent Web Server </br><br>Method: "+method+"\n</br><br>uri: "+uri+"\n</br><br>Version: "+version+"<br></h1></html>"
        method = (data['requestLine'].split(" "))[0]
        uri = (data['requestLine'].split(" "))[1]
        version = (data['requestLine'].split(" "))[2]
        
        filepath = 'webpages' + uri
        res = ''
        with open(filepath,'r') as f:
            res = f.read()
        res = res.replace("method",(data['requestLine'].split(" "))[0])
        res = res.replace("headerData",data['header'])
        res = "HTTP/1.1 200 OK\n\n" + res
        f.close()
        return response

    def parsePut(self,data):
        print "Recieved Put request\n"
        pass

    def parseHead(self,data):
        print "Recieved Head request\n"
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
    def parsePost(self,postReq):
        print "Recieved Post request\n"
        print postReq
        for v in postReq['header'].splitlines():
            if('content-length' in v):
                conLen = v.split(":")[1]
        if(int(conLen) == len(postReq['msgBody'])):
           print "full msg body received"

        requestLine = postReq['requestLine'].split(" ")
        uri = requestLine[1]
        filename = 'webpages'+uri
        writeFd = open(filename,'w')
        writeFd.write(postReq['msgBody'])

    def methodToRun(self,methodToCall,decodeData):
        print "methodtorun\n"
        return methodToCall(decodeData)
        
    def parseRequest(self):
        decodedData = self.decodeRequest()

        responseData = ''
        method = (decodedData['requestLine'].split(" "))[0]
        responseData = self.methodToRun(self.methodMapping[method],decodedData)
        return responseData
        
    def decodeRequest(self):
        data = {}
        
        reqIndex = self.request.find('\r\n')
        data['requestLine'] = self.request[0:reqIndex]
        
        #for i in range(0,idx):
         #   data['requestLine'] += self.request[i]

        hdrIndex = self.request.find('\r\n\r\n')
        data['header'] = self.request[reqIndex+2 : hdrIndex]

        #for i in range(idx+2,idx2):
         #   data['header'] += self.request[i]

        msgBdyIndex = hdrIndex + 4
        data['msgBody'] = self.request[msgBdyIndex : len(self.request)]

        #for i in range(msgBdyIndex,len(self.request)):
         #   data['msgBody'] += self.request[i]

        return data


HOST, PORT = '', 8888

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print 'Serving HTTP on port %s ...' % PORT
while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    print request
    print "\n\n"
    server = HTTPServer(request)
    response = server.parseRequest()
    #print response
    print "sending response"
    #response = 'HTTP/1.1 200 OK\n'
    client_connection.sendall(response)
    client_connection.close()

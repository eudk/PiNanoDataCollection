from socket import *

serverPort = 2023
serverSocket = socket(AF_INET, SOCK_DGRAM)

serverAddress = ('', serverPort)

serverSocket.bind(serverAddress)
print("The server is ready")
while True:
    data, server = serverSocket.recvfrom(1024)
    print(data.decode())
 



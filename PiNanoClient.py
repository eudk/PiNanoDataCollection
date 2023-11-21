#run this on the pi nano to send data to the server

from socket import *
from time import sleep
from sense_hat import SenseHat

serverName = '255.255.255.255'
serverPort = 2023
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)


sense = SenseHat()
while True:
    temp = sense.get_temperature()
    humidity = sense.get_humidity()

    print("Temperature: %s C" % temp)
    print("Humidity: %s %%rH" % humidity)
    clientSocket.sendto(str(temp).encode(), (serverName, serverPort))
    clientSocket.sendto(str(humidity).encode(), (serverName, serverPort))
    sleep(10)



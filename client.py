from pydoc import cli
import socket


#THIS SCRIPT CREATES A CLIENT SIDE CONNECTION USING PYTHON SOCKET LIBRARY

target_host = "10.0.2.15"
target_port = 44445

#CREATE A SOCKET OBJECT
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#CONNECT THE CLIENT TO THE SERVER
client.connect((target_host, target_port))

#SEND SOME DATA TO THE SERVER-SIDE 
client.send("Hello World\nThis is from the Client/Vulnerable Machine!!!".encode('utf-8'))
print(client.recv(1024))


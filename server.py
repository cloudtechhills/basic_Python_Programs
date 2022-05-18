import socket


#THIS SCRIPT CREATES A CLIENT SIDE CONNECTION USING PYTHON SOCKET LIBRARY


host = "localhost"
port = 44445

#CREATE A SOCKET OBJECT
server1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#BIND THE CLIENT TO THE SERVER
server1.bind((host, port))

server1.listen(5)
try:
    print(f"[*] Server Listening on Port [{port}]")
    while True:
        communication_socket, address = server1.accept()
        print(f"[*] Accepted Connection from: {address[0]}:{address[1]}")
        message = communication_socket.recv(1024).decode("utf-8")
        print(f"[*] Message from client is: {message}")
        communication_socket.send(f"[*] Thanks for hitting me up!\nHave a Nice Day!".encode("utf-8"))
        communication_socket.close()
        print(f"[*] Connection with {address} ended!")
except KeyboardInterrupt:
    print("[*] Program Shutting Down! KeyBoard Interrupt...")
    
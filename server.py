import socket, sys

# Create a TCP/IP socket
# AF_INET -> IPv4 
# SOCK_STREAM -> TCP/IP connections
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket connected")

# hosting it on this machine
s.bind(("44.233.151.27", 8080))
print("Server host name ", socket.gethostname())
# queue of 5 clients 
s.listen(5)
print("Socket is listning")

inputs = ""
clientSocket, address = s.accept()
print(f"Connection from {address} has been established")

# what to send to the client
sent = clientSocket.send(bytes("Welcome to the server!", "utf-8"))

while inputs.lower() != "quit":
    recieved = clientSocket.recv(1024)
    if recieved:
        print("Recieved by host name ", socket.gethostbyaddr(address[0])[0])
        print(recieved.decode("utf-8"))

    inputs = input("Enter a message to send: ")
    clientSocket.send(bytes(inputs, "utf-8"))

# close the connection
clientSocket.close()

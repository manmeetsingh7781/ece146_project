import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to public ip like singhrasp.ddnsgeek.com and give port number
s.connect(("192.168.1.210", 8080))
print("Client host name ", socket.gethostname())

inputs = "";

while inputs.lower() != "quit":
    # recieve the message of buffer size 1024
    msg = s.recv(1024)
    if msg:
        # print the message
        print(msg.decode("utf-8"))
   
    inputs = input("Enter a message to send: ")
    s.send(bytes(inputs, "utf-8"))

# close the connection
s.close()
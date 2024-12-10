import socket, threading

hostname, port = ("localhost", 5000)
inputs = ""
def handleClient(clientSocket):
    global inputs;
    # allow multiple messages to send 
    def recieve():
        while True:
            try:
                msg = clientSocket.recv(1024).decode('utf-8')
                if (msg == "quit"):
                    print("Connection closed!")
                    
                    clientSocket.close()    
                    break
                if msg:
                    print("\n===================\n")
                    print(f"Client: {msg}")
                    print("\n===================\n")

                    print("Enter a message to send: " )
            except Exception as e:
                print("Error: ", e)
                break


    def send():
        global inputs;
        while inputs != "quit":
            inputs = input("Enter a message to send: ")
            print(f"You: {inputs}")
            # send the message
            clientSocket.send(bytes(inputs, "utf-8"))
            


    thread_reciever = threading.Thread(target=recieve)
    thread_reciever.start()

    thread_sender = threading.Thread(target=send)
    thread_sender.start()


    thread_reciever.join()
    thread_sender.join()

    # close the connection
    clientSocket.close()


def start_server():
    # Create a TCP/IP socket
    # AF_INET -> IPv4 
    # SOCK_STREAM -> TCP/IP connections
   
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket connected")

    # hosting it on this machine
    s.bind((hostname, port))
    print("Server host name ", socket.gethostname())


    # queue of 5 clients 
    s.listen(5)
    


    clientSocket, address = s.accept()
    print(f"Connection from {address} has been established")

    client_handler = threading.Thread(target=handleClient, args=(clientSocket,))
    client_handler.start()

    # what to send to the client
    clientSocket.send(bytes("Welcome to the server!", "utf-8"))

start_server()
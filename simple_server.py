import socket
import time

HOST = 'localhost'
PORT = 9090

# TCP/IP server with sock stream for internet based devices.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# to allow address reuse if closed unexpectedely.
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))

# start rejecting connections after 5 clients
server.listen(5)

start = time.time()
SERVER_LIFETIME = 100
communication_socket = None
while True:
    elapsed_time = time.time() - start
    print(f"Elapsed time in seconds: {elapsed_time}")
    if elapsed_time> SERVER_LIFETIME:
        break
    
    # To talk to the client, we need to use a communication 
    # socket to talk to the client
    if communication_socket is None:
        communication_socket, address = server.accept()
        print(f"Server is connected to the client at {address}")

    # message passing
    # messages in TCP/IP are byte streams and therefore we need to decode them.
    message = communication_socket.recv(1024).decode(('utf-8'))
    print(f"Message from client is : {message}")
    communication_socket.send("Got your message! Thank you!".encode('utf-8'))

print(f"Closing server after 10 seconds")
communication_socket.close()
server.close()

        



    
import socket
import time 

HOST = "localhost"
PORT = 9090
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)

client.connect((HOST, PORT))

start = time.time()
sentence_list = ['Hello, I am a simple TCP/IP client made using Linux socket API in python.',
                 'I was created at localhost:9090',
                 'I will expand on my properties in future',
                 'The server side may be seeing my messages in ASCII/utf-8, but my native format is byte code to send messages.']

ii = 0
while time.time() - start < 10:
    if ii >= len(sentence_list):
        break

    if sentence_list:
        client.send(f"{sentence_list[ii]}".encode('utf-8'))
    
    message = client.recv(1024).decode("utf-8")
    print(f"Received from server:  {message}")
    ii += 1
    time.sleep(0.1)


message = client.recv(1024).decode("utf-8")
client.close()
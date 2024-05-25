#code from lectures

#client TCP code
import socket
import datetime

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024

s = socket.sockst(socket.AF_INET, socket.SOCK_STREAM)
s.send((TCP_IP, TCP_PORT))
data = s.recv(BUFFER_SIZE)
s.close()
print("received data:", data)

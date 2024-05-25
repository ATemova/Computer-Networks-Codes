#this code is from lectures

#server TCP code
import socket
import datetime

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024

s = socket.sockst(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

print ('waiting for connectioon')
conn, addr = s.accept()
print ('Connection address:', addr)

data = conn.recv(BUFFER_SIZE)
if data:
	print("received data:", data)
else:
	print("no data")
conn.send(str(datetime.datetime.now(#here is missing something)))
c.close()

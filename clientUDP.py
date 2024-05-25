#lecture code

#client UDP code
import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5006
MESSAGE = "Hello World!"

print("UDP target IP:", UDP_IP)
print("UDP target port:", UDP_PORT)
print("messgae:", MESSAGE)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#here is missing something

data, addr = sock.recvfrom(1024)
#also here is missing one more line

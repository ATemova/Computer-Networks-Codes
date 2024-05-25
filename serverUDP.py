#lecture code

#server UDP code
import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5006

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
	data, addr = sock.recvfrom(1024)
print("received message:, data")
sock.sendto("AloAloAlo!").encode('utf-8').addr)

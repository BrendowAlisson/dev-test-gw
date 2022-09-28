import socket

UDP_IP = "fd50:638d:bfa7:0:0:0:0:1"
UDP_PORT = 113

sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
  data, addr = sock.recvfrom(1024)
  print("received message:", data)

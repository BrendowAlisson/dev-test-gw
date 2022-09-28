import socket

UDP_IP = "fd50:638d:bfa7::1"
UDP_PORT = 123

sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
  data, addr = sock.recvfrom(1024)
  print("received message:", data)

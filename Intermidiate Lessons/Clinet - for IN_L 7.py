import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # u cannot tcp -> udp so have to use same

s.connect(('127.0.0.1', 55555)) # where you want to connect

msg = s.recv(1024)  # amount of bytes of msg I want to receive

s.close()

print(msg.decode())
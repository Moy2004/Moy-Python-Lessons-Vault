"""
2023 1/3
1444  جُمَادَىٰ ٱلثَّانِي 10

Sockets and Network Programming
"""
# Network Programming
# Learning about how to send data over network or how to exchange data.
# and how to build connection between clients and server

# Socket
# Just an end point of communication channel - There are two end points
# Basically two client trying to exchange data

# There are lower and higher level, and most of the time we will ue
# lower level such as TCP amd UDP, if you want to access higher we need to use module such as HTTP and more

# TCP and UDP works on transport layer - OSI Model == https://www.imperva.com/learn/application-security/osi-model/

import socket

# have to decide either to use unix socket or internet socket
# TCP = Connection oriented better for any sensible data (Sent-Receive all data ) - slow  == for sending msg
# UDP = Connection less (Sent - Receive data but there is can be some loss + not in order) - fast == for discord call

# now we need to choose which IP we want to host the server

# last question is which port are we going to use - (TCP: (3333) or (2160) and many more)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  # (Type of socket, protocol{tcp or udp})  AF_INET = internet

s.bind(('127.0.0.1',55555)) # IP address and port we want to run
# IP used here is called local host, basically calling itself
# Extra - https://stackoverflow.com/questions/10476987/best-tcp-port-number-range-for-internal-applications

s.listen()  # constantly listening or connecting to possible connection

while True:  # this is server script
    client, address = s.accept()  # accepting the connection
    print(f'connected to {address}')  # prints on server (tells msg is sent)
    client.send('You are connected'.encode())  # prints on client (msg that will be received)
    client.close()

# now we will make client that will connect to server in different python page

"""
Quick 日記
아주 유용했다 본다. 하지만 아직 인터넷이 어떻게
작동하는지 잘은 모르기에 지금 
유튜브에 영상을 보러 갈거다 
OSI Model 중심으로 영상 볼 생각이다 
"""
# TODO before sending disable firewall
"""
2023 1/29 ~ 2023 1/31
1444 رَجَب 7 ~ 1444 رَجَب 9

before start project note:
I want to create the chat room,
where I can send client to my freind,
and he run on his python interperter,
and we can chat in it.

Basic module of TCP chat room
This module is tested and working properly
"""
"""
important
==
This project I realized, 
It is very limited in terms of being creative
and creating my own code.
Most other project I used minimum help from 
outside.
But this one I don't have much option because
There are only few ways to do it. So project
might look very similar to what already exist on 
internet. Because of this problme I wasted 1/30
And now I decided to just do this project. 
But I will do extra project for intermidete 
because I didn't really use my brain nor have fun either
"""
import socket

host = '127.0.0.1'  # changed to local host cause GitHub
port = 45454

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))

s.listen()

while True:
    client, address = s.accept()
    print(f'connected to {address}')
    client.send('hello this is your technical support how may I help you today'.encode())
    client.close()

# https://www.pythonclear.com/errors/connectionrefusederror-errno-111-connection-refused/

"""
import socket

host = '127.0.0.1'
port = 45454

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

msg = s.recv(1024)

print(msg.decode())

s.close()

"""
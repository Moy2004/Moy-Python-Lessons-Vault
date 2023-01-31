"""
2023 1/29 ~ 2023 1/31
1444 رَجَب 7 ~ 1444 رَجَب 9

Server
"""
import socket
import threading

host = '127.0.0.1'
port = 45454

# connecting and finding connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen()

clients = []
ID = []


# Function that send msg to all clients
def send_all(msg):
    for client in clients:
        client.send(msg)


# Send the message from client
def send_msg(client):
    while True:
        try:
            msg = client.recv(1024)
            send_all(msg)
        except:
            index = clients.index(client)  # reads the most recently used index
            clients.remove(client)
            client.close()
            name = ID[index]
            send_all(f'{name} is terminated due to some error'.encode('ascii'))
            ID.remove(name)
            break


# This function will connect and give name to new client
def new():
    while True:
        # connect
        client, address = s.accept()
        print(f'connected to {address}')
        client.send('You are connected to chat room\n'
                    'please click ENTER to join the chat'.encode())

        # name
        name = client.recv(1024).decode('ascii')
        ID.append(name)
        clients.append(client)

        # report to everyone
        send_all(f'{name} has joined the server'.encode('ascii'))

        thread = threading.Thread(target=send_msg, args=(client,))
        thread.start()


new()

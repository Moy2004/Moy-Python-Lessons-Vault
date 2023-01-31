"""
2023 1/29 ~ 2023 1/31
1444 رَجَب 7 ~ 1444 رَجَب 9

Client
"""
import socket
import threading

name = input("Enter your desired name:")

host = '127.0.0.1'
port = 45454

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))


# receiving msg
def receive():
    while True:
        try:
            msg = client.recv(1024).decode('ascii')
            if msg == 'name':
                client.send(name.encode('ascii'))
            else:
                print(msg)
        except:
            print("Error")
            client.close()
            break


# writing msg
def write():
    while True:
        msg = f'{name}: {input("")}'
        client.send(msg.encode('ascii'))


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()

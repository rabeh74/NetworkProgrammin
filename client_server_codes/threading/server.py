from socket import *
from threading import Thread

server = socket(AF_INET , SOCK_STREAM)
addrs = ('localhost' , 9876)
server.bind(addrs)
clients ={}
addresses ={}
def accept_incoming_conn():
    print('waiting connections: ')
    while True:

        client , addr = server.accept()
        msg = 'welcome , enter alias !'
        client.send(msg.encode('utf-8'))
        addresses[client] = addr
        Thread( target= handle_client , args=(client ,addr)).start()

def handle_client(client , addr):
    name = client.recv(1024).decode('utf-8')
    msg =f"weleome {name} if need to close press quit"
    client.send(msg.encode('utf-8'))
    broadcast(f'{name} joined the room')
    clients[client]=name

    while True:
        try:
            msg = client.recv(1024).decode('utf-8')
            if msg != "quit":
                broadcast(msg , name + ':')
            else:
                client.send("quit".encode('utf-8'))
                client.close()
                del clients[client]
                del addresses[client]
                broadcast(f'{name} left the room')
                break
        except:
            break

def broadcast(msg , prefix = ' '):
    for cl in clients.keys():
        cl.send((prefix+msg).encode('utf-8'))
server.listen(5)

print("server start ")
thread_accept = Thread(target=accept_incoming_conn)
thread_accept.start()
thread_accept.join()

server.close()
from socket import *
# from tkinter import *
from threading import Thread



addrs = ('localhost', 1245)
server = socket(AF_INET,SOCK_STREAM)
server.bind(addrs)
server.listen(5)

BUFSIZE = 1024
clients ={}
addresses = {}
def accept_incomin_conn():
    while True:
        try:
            client , addr = server.accept()
            print('{} has connected'.format(addr))
            client.send(bytes('Welcome to the chatroom! Enter your name and press enter!','utf8'))
            addresses[client] = addr
            Thread(target=handle_client,args=(client,)).start()
        except error as e:
            print(e)
            break


def handle_client(client):
    name = client.recv(BUFSIZE).decode('utf8')
    welcome = 'Welcome {}! If you ever want to quit, type quit to exit.'.format(name)
    client.send(bytes(welcome,'utf8'))
    msg = "{} has joined the chat!".format(name)
    broadcast(bytes(msg,'utf8'))
    clients[client] = name
    while True:
        msg = client.recv(BUFSIZE)
        if msg != bytes('{quit}','utf8'):
            broadcast(msg,name+': ')
        else:
            client.send(bytes('{quit}','utf8'))
            client.close()
            del clients[client]
            broadcast(bytes('{} has left the chat.'.format(name),'utf8'))
            break
def broadcast(msg,prefix=''):
    for sock in clients.keys():
        sock.send(bytes(prefix,'utf8')+msg)

if __name__ == '__main__':
    print('Waiting for connection...')
    th = Thread(target= accept_incomin_conn)
    th.start()
    th.join()
    server.close()

from socket import *
from threading import Thread
name = input('enter name please')
client = socket(AF_INET , SOCK_STREAM)
addrs = ('localhost' , 9876)

def recv():

    try:
        while True:
            msg = client.recv(1024)
            if msg.decode('utf-8') == 'welcome , enter alias !':
                client.send(name.encode('utf-8'))
            else:
                print(msg.decode("utf-8"))
    except error as e:
        print('error' , e)

def send():
    try :
        while True:
            msg = input("type :")
            client.send(msg.encode('utf-8'))
    except error as e:
        print('error ocuured' , e)
client.connect(addrs)


Thread(target=recv).start()
Thread(target=send).start()
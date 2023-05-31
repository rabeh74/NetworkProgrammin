from socket import *

server = socket(AF_INET , SOCK_STREAM)
addrs = ('localhost' , 9876)
server.bind(addrs)
server.listen(5)

client , addr = server.accept()
while True:
    try:
        msg = client.recv(1024).decode('utf-8')
        if not msg:
            break
        print('client : ' , msg)
        msg=input("server :")
        client.send(msg.encode('utf-8'))
    except:
        print("error ocuured ")
        break


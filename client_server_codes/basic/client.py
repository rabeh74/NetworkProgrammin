from socket import *

client = socket(AF_INET , SOCK_STREAM)
addrs = ('localhost' , 9876)
client.connect(addrs)
try:
    while True:
        msg = input("enter msg : ")
        if not msg:
            break
        client.send(msg.encode('utf-8'))
        msg = client.recv(1024)
        print("server :" , msg)

    client.close()
except:
    print('error ocuured')


client.close()




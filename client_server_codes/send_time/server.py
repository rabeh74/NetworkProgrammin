import socket
S = socket.socket (socket.AF_INET, socket. SOCK_STREAM)
S.bind((socket.gethostname(), 1025))
S.listen (5)
import datetime
dateAsString = str(datetime.datetime.now())
x=dateAsString.encode()

while True:
    clt, adr = S.accept()
    print (f"Connection to {adr} is established")
    clt.send(x)
# Since bytes is used utf-8 tells what kind of byte is used
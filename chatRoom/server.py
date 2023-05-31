import socket
import threading
from threading import Thread
from datetime import datetime
import tkinter as tk
time = str(datetime.now())
clients={}
addresses={}
BUF = 1024
server = None
HOST_ADDR = 'localhost'
HOST_PORT = 8081

window = tk.Tk()
window.title("Sever")

# Top frame consisting of two buttons widgets (i.e. btnStart, btnStop)
topFrame = tk.Frame(window)
btnStart = tk.Button(topFrame, text="Start", command=lambda: start_server())
btnStart.pack(side=tk.LEFT)
btnStop = tk.Button(
    topFrame, text="Stop", command=lambda: stop_server(), state=tk.DISABLED
)
btnStop.pack(side=tk.LEFT)
topFrame.pack(side=tk.TOP, pady=(5, 0))

# Middle frame consisting of two labels for displaying the host and port info
middleFrame = tk.Frame(window)
lblHost = tk.Label(middleFrame, text="Address:X.X.X.X")
lblHost.pack(side=tk.LEFT)
lblPort = tk.Label(middleFrame, text="Port:xxxx")
lblPort.pack(side=tk.LEFT)
middleFrame.pack(side=tk.TOP, pady=(5, 0))

# The client frame shows the client area
clientFrame = tk.Frame(window)
lblLine = tk.Label(clientFrame, text="**********Client List**********").pack()
scrollBar = tk.Scrollbar(clientFrame)
scrollBar.pack(side=tk.RIGHT, fill=tk.Y)
tkDisplay = tk.Listbox(clientFrame, height=10, width=30 , yscrollcommand=scrollBar.set)
tkDisplay.pack(side=tk.LEFT, fill=tk.BOTH, padx=(5, 0))
tkDisplay.pack()
clientFrame.pack(side=tk.BOTTOM, pady=(5, 10))



def start_server():
    global server, HOST_ADDR, HOST_PORT  # code is fine without this
    btnStart.config(state=tk.DISABLED)
    btnStop.config(state=tk.NORMAL)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(socket.AF_INET)
    print(socket.SOCK_STREAM)

    server.bind((HOST_ADDR, HOST_PORT))
    server.listen(5)  # server is listening for client connection

    threading._start_new_thread(accept_incoming_connections,(server,))

    lblHost.config(text= "Address: " + HOST_ADDR)
    lblPort.config(text= "Port: " + str(HOST_PORT))

def stop_server():
    global server
    print("hi")
    server.close()
    btnStart.config(state=tk.NORMAL)
    btnStop.config(state=tk.DISABLED)

def accept_incoming_connections(server):
    while True:
        try :
            print(" waiting for connections ...")
            client , addrs = server.accept()
            print("%s:%s has connected." % addrs)
            addresses[client] = addrs

            msg = f" greetings , welocome to the chatroom at time {time} \n, please enter your name : "
            client.send(msg.encode('utf-8'))
            Thread(target=handle_client , args=(client,)).start()

        except:
            print("error occured" )
            break

def handle_client(client):
    name = client.recv(BUF).decode('utf-8')
    msg = f"welcome {name} , if you want to quit the chatroom please type {quit} "
    client.send(msg.encode('utf-8'))
    msg = f"{name} has joined the chatroom"
    broadcast(msg.encode('utf-8'))
    clients[client] = name
    update_client_names_display(list(clients.values()))

    while True:
        try :
            msg = client.recv(BUF)
            if msg.decode('utf-8') !='{quit}':
                broadcast(msg , name + ": ")
            else:
                client.send('quit ...'.encode('utf-8'))
                client.close()
                del clients[client]
                del addresses[client]
                update_client_names_display(list(clients.values()))
                broadcast(f"{name} has left the chatroom".encode('utf-8'))
                break

        except Exception as e:
            print(e)
            break
def broadcast(msg , prefix=""):
    for client in clients:
        client.send(prefix.encode('utf-8')+msg)

def update_client_names_display(names):
    # clear the display list
    tkDisplay.delete(0, tk.END)
    for i,name in enumerate(names):
        tkDisplay.insert(tk.END, f"{i+1}-> " + name)

window.mainloop()



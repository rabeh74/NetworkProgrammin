from socket import *
from tkinter import *
from threading import Thread
BUFSIZE = 1024
def recv():
    while True:
        try:
            msg = client.recv(BUFSIZE).decode('utf-8')
            msg_list.insert(END , msg)
        except:
            print("error")
            break
def send(event=None):
    msg = my_msg.get()
    my_msg.set("")
    client.send(bytes(msg , 'utf-8'))
    if msg == "{quit}":
        client.close()
        root.quit()
def in_closing(event=None):
    my_msg.set("{quit}")
    send()

root = Tk()
root.title("chatter")
root.geometry('400x400')

# frame for msg_list
msg_frame = Frame(root)
scrolllbar = Scrollbar(msg_frame)
msg_list = Listbox(msg_frame , height=15 , width=50 , yscrollcommand=scrolllbar.set)

scrolllbar.pack(side=RIGHT , fill=Y)
msg_list.pack(side=LEFT , fill=BOTH)

msg_frame.pack()

# entry name
my_msg = StringVar()
ent_name = Entry(root , textvariable=my_msg)
btn= Button(root , text="Send" , command = send)
ent_name.bind("<Return>" , send)
ent_name.pack()
btn.pack()
root.protocol('WM_DELETE_WINDOW', in_closing)

addr = ('localhost', 1245)
client = socket(AF_INET , SOCK_STREAM)
client.connect(addr)

Thread(target=recv).start()
root.mainloop()
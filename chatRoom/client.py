from tkinter import *
from socket import *
from threading import Thread
BUF = 1024

def recv():
    while True:
        try:
            msg = client.recv(BUF).decode('utf-8')
            msg_box.insert(END , msg)
        except :
            client.close()
            break

def send(event=None):
    msg = my_msg.get()
    my_msg.set("")

    client.send(msg.encode('utf-8'))

    if msg =="{quit}":
        client.close()
        window.quit()

def in_closing(event = None):
    my_msg.set("{quit}")
    send()


# tkinter Root

window = Tk()
window.title("chatter")
window.geometry("400x400")
msg_frame = Frame(window)

# msg Frame

scrollbar = Scrollbar(msg_frame)
msg_box = Listbox(msg_frame , height = 15 , width= 50 , yscrollcommand=scrollbar.set)

scrollbar.pack(side=RIGHT,fill=Y)
msg_box.pack(side=LEFT , fill=BOTH)
msg_frame.pack()
# end frame

# entry and send button
my_msg = StringVar()
my_msg.set('enter msg here !:')
ent_msg = Entry(window , textvariable=my_msg)
ent_msg.bind('<Return>' , send)

btn = Button(window , text='send' , command=send)
ent_msg.pack()
btn.pack()
window.protocol('WM_DELETE_WINDOW' , in_closing)

addr = ('localhost', 8081)
client = socket(AF_INET , SOCK_STREAM)
client.connect(addr)

Thread(target=recv).start()
window.mainloop()







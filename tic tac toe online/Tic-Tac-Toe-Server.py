from tkinter import *
from tkinter import messagebox
from socket import *
from threading import *

#when using astrisk with tkinter messagebox generates an error as it's not included
# we include nessagebox in its own line to solve this problem
#################################window##########################################################
window = Tk()
window.title("Tic Tac Toe Server")
window.geometry("400x300")
################################check############################################################
flag = 1
def check():
    global flag
    #############################button labels########################################################
    bt1 = btn1['text']
    bt2 = btn2['text']
    bt3 = btn3['text']
    bt4 = btn4['text']
    bt5 = btn5['text']
    bt6 = btn6['text']
    bt7 = btn7['text']
    bt8 = btn8['text']
    bt9 = btn9['text']
    #################################################################################################
    flag += 1
    if flag == 10:
        messagebox.showinfo("Draw", "The game result is draw")
        window.destroy()
    if (bt1 == bt2 and bt2 == bt3 and bt1 == 'x') or (bt1 == bt2 and bt2 == bt3 and bt1 == 'o'):
        win(bt1)
    if (bt4 == bt5 and bt5 == bt6 and bt4 == 'x') or (bt4 == bt5 and bt5 == bt6 and bt4 == 'o'):
        win(bt4)
    if (bt7 == bt8 and bt8 == bt9 and bt7 == 'x') or (bt7 == bt8 and bt8 == bt9 and bt7 == 'o'):
        win(bt7)
    if (bt1 == bt4 and bt4 == bt7 and bt1 == 'x') or (bt1 == bt4 and bt4 == bt7 and bt1 == 'o'):
        win(bt1)
    if (bt2 == bt5 and bt5 == bt8 and bt2 == 'x') or (bt2 == bt5 and bt5 == bt8 and bt2 == 'o'):
        win(bt2)
    if (bt3 == bt6 and bt6 == bt9 and bt3 == 'x') or (bt3 == bt6 and bt6 == bt9 and bt3 == 'o'):
        win(bt3)
    if (bt1 == bt5 and bt5 == bt9 and bt1 == 'x') or (bt1 == bt5 and bt5 == bt9 and bt1 == 'o'):
        win(bt1)
    if (bt3 == bt5 and bt5 == bt7 and bt3 == 'x') or (bt3 == bt5 and bt5 == bt7 and bt3 == 'o'):
        win(bt3)
############################win##################################################################
#################################################################################################
def win(player):
    messagebox.showinfo("Congratulation", "the winner is player "+player)
    window.destroy()
############################clicked##############################################################
#################################################################################################
def clicked1():
    if btn1['text'] == " ":
        #global turn
        btn1['text'] = 'x'
        send('a')
        check()
#################################################################################################
def clicked2():
    if btn2['text'] == " ":
        #global turn
        btn2['text'] = 'x'
        send('b')
        check()
#################################################################################################
def clicked3():
    if btn3['text'] == " ":
        #global turn
        btn3['text'] = 'x'
        send('c')
        check()
#################################################################################################
def clicked4():
    if btn4['text'] == " ":
        #global turn
        btn4['text'] = 'x'
        send('d')
        check()
#################################################################################################
def clicked5():
    if btn5['text'] == " ":
        #global turn
        btn5['text'] = 'x'
        send('e')
        check()
#################################################################################################
def clicked6():
    if btn6['text'] == " ":
        #global turn
        btn6['text'] = 'x'
        send('f')
        check()
#################################################################################################
def clicked7():
    if btn7['text'] == " ":
        #global turn
        btn7['text'] = 'x'
        send('g')
        check()
#################################################################################################
def clicked8():
    if btn8['text'] == " ":
        #global turn
        btn8['text'] = 'x'
        send('h')
        check()
#################################################################################################
def clicked9():
    if btn9['text'] == " ":
        #global turn
        btn9['text'] = 'x'
        send('i')
        check()
#############################label###############################################################
lbl1 = Label(window, text="Server: x", font=("Helvetica", "15"))
lbl1.grid(row=0, column=0)

lbl2 = Label(window, text="Clinet: o", font=("Helvetica", "15"))
lbl2.grid(row=1, column=0)
##############################button#############################################################
btn1 = Button(window, text=" ", bg="yellow", fg="black", width=3, height=1, command=clicked1)
btn1.grid(row=0, column=1)

btn2 = Button(window, text=" ", bg="yellow", fg="black", width=3, height=1, command=clicked2)
btn2.grid(row=0, column=2)

btn3 = Button(window, text=" ", bg="yellow", fg="black", width=3, height=1, command=clicked3)
btn3.grid(row=0, column=3)

btn4 = Button(window, text=" ", bg="yellow", fg="black", width=3, height=1, command=clicked4)
btn4.grid(row=1, column=1)

btn5 = Button(window, text=" ", bg="yellow", fg="black", width=3, height=1, command=clicked5)
btn5.grid(row=1, column=2)

btn6 = Button(window, text=" ", bg="yellow", fg="black", width=3, height=1, command=clicked6)
btn6.grid(row=1, column=3)

btn7 = Button(window, text=" ", bg="yellow", fg="black", width=3, height=1, command=clicked7)
btn7.grid(row=2, column=1)

btn8 = Button(window, text=" ", bg="yellow", fg="black", width=3, height=1, command=clicked8)
btn8.grid(row=2, column=2)

btn9 = Button(window, text=" ", bg="yellow", fg="black", width=3, height=1, command=clicked9)
btn9.grid(row=2, column=3)

###########################################################################################################

def handler():
    while True:
        x = conn.recv (2048)
        x = x.decode ('UTF-8')
        if x == 'a':
            btn1['text'] = 'o'
        elif x == 'b':
            btn2['text'] = 'o'
        elif x == 'c':
            btn3['text'] = 'o'
        elif x == 'd':
            btn4['text'] = 'o'
        elif x == 'e':
            btn5['text'] = 'o'
        elif x == 'f':
            btn6['text'] = 'o'
        elif x == 'g':
            btn7['text'] = 'o'
        elif x == 'h':
            btn8['text'] = 'o'
        elif x == 'i':
            btn9['text'] = 'o'


s = socket (AF_INET, SOCK_STREAM)
host = '127.0.0.1'
port = 6000
s.setsockopt (SOL_SOCKET, SO_REUSEADDR, 1) #for port reusability
s.bind ((host, port))
s.listen (5)
conn, add = s.accept ()
cthread = Thread (target=handler)
#cthread.daemon = True
cthread.start()

def send(y):
    conn.send(y.encode('UTF-8'))

window.mainloop()


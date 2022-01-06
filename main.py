from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import socket
import threading
from functools import partial
from pickle import load
ii = 0
connected = False
sendN = False
isHit = False
xy = [0,0]
def tk():
    global map
    global ii
    root = Tk()
    root.title("Battle Ship")
    w = 'a,b,c,d,e,f,g,h,i,j'.split(",")
    h = [x+1 for x in range(len(w))]
    b = []

    map = [
        [0 for x in h],
        [1 for x in h],
        [0 for x in h],
        [0 for x in h],
        [0 for x in h],
        [0 for x in h],
        [0 for x in h],
        [0 for x in h],
        [0 for x in h],
        [0 for x in h]
    ]
    ii = 0
    def press(x,y):
        global ii
        print(f"{x}|{y}")
        if map[x][y] == 1:
            print('hit')
            label = Label(root, text=f'hits = {ii+1}')
            ii+=1
            map[x][y] = 2
            if connected == True:
                sendN = True
                xy = [x,y]
            label.grid(row=len(h)+1, column=5)
            root.update()
        elif map[x][y] == 2:
            messagebox.askokcancel('Opps', 'You seem to have already guessed at that location\nplease try again')
    i = -1
    for x in w:
        i += 1
        for y in h:
            b.append([Button(root, text=f'{x}|{y}', command=partial(press, i,y)), (i,y)])
    for x in b:
        x[0].grid(row=x[1][0], column=x[1][1])
    label = Label(root, text='hits = 0')
    label.grid(row=len(h)+1, column=5)
    stuff = Label(root, text=' ')
    stuff.grid(row=len(h)+2, column=5)
    root.mainloop()
def net():
    host = '192.168.0.103'
    ip = 5050
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind((host,ip))
        s.listen(1)
        con, adr = s.accept()
        d = con.recv(3)
        connected = True
        print(d)
        def send():
            global sendN
            while True:
                if sendN == True:
                    con.send(bytes(f"{xy[0]}|{xy[1]}"),'utf-8')
                    sendN = False
        def recv():
            while True:
                con.recv(3)
        sendt = threading.Thread(target=send)
        recvt = threading.Thread(target=recv)
        sendt.start()
        recvt.start()
    except Exception as e:
        print(e)
        files = [('Battle Ship Map File','*.bsm')]
        filepath = filedialog.askopenfile(mode='rb',filetypes=files)
        a = load(filepath)
        s.connect((host,ip))
        connected = True
        def send():
            global sendN
            while True:
                if sendN == True:
                    s.send(bytes(f"{xy[0]}|{xy[1]}"),'utf-8')
                    sendN = False
        def recv():
            while True:
                s.recv(3)
        sendt = threading.Thread(target=send)
        recvt = threading.Thread(target=recv)
        sendt.start()
        recvt.start()
                
        
    #while True:

        
if __name__ == "__main__":
    nett = threading.Thread(target=net)
    tkt = threading.Thread(target=tk)
    nett.start()
    tkt.start()

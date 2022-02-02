from tkinter import *
from tkinter.ttk import Progressbar
import socket
import math
import time, threading

window = Tk()
window.title("Клієнт")
window.geometry("420x450")
canvas = Canvas(width = 420, height = 450, bg = '#CE7BB0')
canvas.pack()
lbl = Label(window, text = "Параметри", font = ("Arial", 11), bg = '#FFBCD1')
lbl1 = Label(window, text = "a:", font = ("Arial", 11), bg = '#FFBCD1')
lbl2 = Label(window, text= "b:", font = ("Arial", 11), bg = '#FFBCD1')
lbl3 = Label(window, text= "c:", font = ("Arial", 11), bg = '#FFBCD1')
lbl4 = Label(window, text= "Адреса серверу:", font = ("Arial", 11), bg = '#FFBCD1')
lbl5 = Label(window, text= "Порт:", font = ("Arial", 11), bg = '#FFBCD1')
lbl1.place(x=30, y=40)
lbl2.place(x=30, y=70)
lbl3.place(x=30, y=100)
lbl.place(x=30, y=10)
lbl4.place(x=250, y=10)
lbl5.place(x=250, y=70)

txta = Entry(window, width=13, bg = '#FFBCD1')
txta.place(x = 80, y= 42)
txta.insert(0, '5')

txtb = Entry(window, width=13, bg = '#FFBCD1')
txtb.place(x = 80, y= 72)
txtb.insert(0, "2.31")

txtc = Entry(window, width=13, bg = '#FFBCD1')
txtc.place(x = 80, y= 102)
txtc.insert(0, "2.356194")

txt_server = Entry(window, width=13, bg = '#FFBCD1')
txt_server.place(x = 250, y= 40)
txt_server.insert(0, "192.168.0.106")

txt_port = Entry(window, width=13, bg = '#FFBCD1')
txt_port.place(x = 250, y= 100)
txt_port.insert(0, "7000")

frame = Frame(window, width = 395, height = 235, bg = "#FFBCD1", bd = 2, relief = GROOVE)
frame.pack()
frame.place(x= 10, y = 158)


bar = Progressbar(window, length=340, mode = "determinate")
bar['value'] = 0
bar.place(x = 30, y = 400)

def progress():
    for i in range(21):
        bar['value'] += i
        time.sleep(.01)
def clicked():
    threading.Thread(target=progress).start()
    
    Label(window, text = "Підключення до серверу...", font = ("Arial", 11), bg = "#FFBCD1", anchor= NW).place(x=20, y = 163)

    server_address = (txt_server.get(), int(txt_port.get()))

    x = '0.75'
    c = str((5*3.14) / 8)
    print(c)
    y = '0.32'
    print(y)
    a1 = txta.get()
    b1 = txtb.get()
    c1 = txtc.get()
    arr = a1 + ' ' + c1 + ' ' + b1

    print('Підключення до серверу...')

    sc = socket.socket()
    sc.connect(server_address)

    z = 'Підключено до серверу '+ str(server_address[0]) +" "+ str(server_address[1])
    

    Label(window, text = z, font = ("Arial", 11), bg = "#FFBCD1", anchor= NW).place(x=20, y = 183)
    Label(window, text = "Надсилання даних...", font = ("Arial", 11), bg = "#FFBCD1", anchor= NW).place(x=20, y = 203)
    print('Надсилання данних...')

    sc.send(bytearray(arr, 'utf-8'))

    receive_data = sc.recv(1024)
    final_data = float(receive_data.decode('utf-8'))

    print('Результат: ', final_data)
    z1 = 'Результат: ' + str(final_data)
    
    Label(window, text = z1, font = ("Arial", 11), bg = "#FFBCD1", anchor= NW).place(x=20, y = 223)

    print('Підключення завершенно.')
    Label(window, text = "Підключення завершено.", font = ("Arial", 11), bg = "#FFBCD1", anchor= NW).place(x=20, y = 243)
    sc.close()
    
btn = Button(window, text="Підключення до серверу", command = clicked, bg = '#FFBCD1')

btn.pack()
btn.place(x = 136, y= 135)

window.mainloop()


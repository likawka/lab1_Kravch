from tkinter import *
import socket
import math
from tkinter.ttk import Progressbar
import time, threading

window = Tk()
window.title("Сервер")
window.geometry("420x450")
canvas = Canvas(width = 420, height = 450, bg = '#CE7BB0')
canvas.pack()
lbl1 = Label(window, text = "Адреса серверу:", font = ("Arial", 11),  bg = '#FFBCD1')
lbl2 = Label(window, text= "Порт:", font = ("Arial", 11),  bg = '#FFBCD1')
lbl1.place(x=30, y=30)
lbl2.place(x=30, y=60)

txt_server_address = Entry(window, width=13, bg = '#FFBCD1')
txt_server_address.place(x = 150, y= 32)
txt_server_address.insert(0, "192.168.0.106")

txt_port = Entry(window, width=13, bg = '#FFBCD1')
txt_port.place(x = 150, y= 62)
txt_port.insert(0, "7000")

frame = Frame(window, width = 395, height = 273, bg = "#FFBCD1", bd = 2, relief = GROOVE)
frame.pack()
frame.place(x= 10, y = 95)

lbl3 = Label(window, text = "", font = ("Arial", 11), bg = "#FFBCD1")
lbl3.place(x=20, y = 100)

bar = Progressbar(window, length=340, mode="determinate")
bar['value'] = 0
bar.place(x = 30, y = 370)

def update(label, text):
        label['text']= text

def progress():
    for i in range(21):
        bar['value'] += i
        time.sleep(.01)


def clicked():
        
        sa = "Адреса серверу: " + txt_server_address.get()

        update(lbl3, sa)
        
def connect():
        
        threading.Thread(target=progress).start()
        
        server_address = (txt_server_address.get(), int(txt_port.get()))

        sc = socket.socket()
        sc.bind(server_address)
        sc.listen(1)

        print('Сервер підключено ', server_address)
        
        connection, address = sc.accept()

        print('Підключенно пристрій з адресою ', address)

        ca = 'Підключенно пристрій з адресою ' + str(address[0]) +" "+ str(address[1])

        Label(window, text = ca, font = ("Arial", 11), bg = "#FFBCD1", anchor = NW).place(x=20, y = 120)
                
                
        data = None
        data_array = []

        print('Отримання даних...')
        Label(window, text = 'Отримання даних...', font = ("Arial", 11), bg = "#FFBCD1", anchor = NW).place(x=20, y = 140)
                
        while True:
                data = connection.recv(1024)

                if not data:
                        break

                print('Обробка...')

                Label(window, text = 'Обробка...', font = ("Arial", 11), bg = "#FFBCD1", anchor = NW).place(x=20, y = 160)
                        

                # [0: x, 1: c, 2: y]
                args_array = [float(x) for x in data.decode('utf-8').split(' ')]

                summ = 0
                for i in range(1, 30):
                        summ += (((-1)**(i+1)) * ((math.sin(args_array[0])*math.cos(args_array[2]) + math.tan(args_array[1])) / (math.factorial(i+3))))


                print('Надсилання даних до клієнта ', address)
                        
                z1='Надсилання даних до клієнта ' + str(address[0]) +" "+ str(address[1])

                Label(window, text = z1, font = ("Arial", 11), bg = "#FFBCD1", anchor = NW).place(x=20, y = 180)

                connection.send(bytearray(str(summ), 'utf-8'))
                
        connection.close()
        
        Label(window, text = "Підключення завершено.", font = ("Arial", 11), bg = "#FFBCD1", anchor = NW).place(x=20, y = 200)

        


        

btn = Button(window, text="OK", command = clicked, bg = '#EBDCB2')
btn.pack()
btn.place(x = 285, y= 31)

btn2 = Button(window, text="Увімкнути сервер", command = connect, bg = '#EBDCB2')
btn2.pack()
btn2.place(x = 285, y= 64)


  
window.mainloop()
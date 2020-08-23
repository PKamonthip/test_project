#Intro Tkinter 
#Tkinter
from tkinter import *
from tkinter import Tk
from tkinter import ttk


windows = Tk()
windows.title('This is my first GUI')
windows.geometry('500x300+800+200')
#windows.minsize(250, 50)
#windows.minsize(600, 400)

#Label
lbl_hello = Label(text='Hello, Kamonthip').pack(side=TOP)
lbl_tel = Label(text='tel: 0861988899').pack(side=TOP)
lbl_mail = Label(text='sommama@gmail.com').pack(side=TOP)
lbl_username =Label(text='Username: ').place(x=100, y=100)
lbl_password =Label(text='Password: ').place(x=100, y=130)



#Textbox
txt_username =Entry().place(x=180, y=100)
txt_password =Entry().place(x=180, y=130)
#Button
btn_login = ttk.Button(text='LOGIN').place(x=180, y=170)
btn_clear = ttk.Button(text='Claer').place(x=280, y=170)
btn_back = ttk.Button(text='Claer').place(x=380, y=170)


windows.mainloop()



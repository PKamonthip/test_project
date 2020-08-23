#เครื่องคิดเลขแบบง่าย
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sys

# function area
def clear_data():
    str_add.set('')
    str_add2.set('')
    str_sum.set('')


def func_add():
    global str_add
    global str_add2
    global str_sum

    read_add = float(str_add.get())
    read_add2 = float(str_add2.get())

    sum = read_add + read_add2
    str_sum.set(sum)

def func_minus():
    read_add = float(str_add.get())
    read_add2 = float(str_add2.get())

    sum = read_add - read_add2
    str_sum.set(sum)

def func_mul():
    read_add = float(str_add.get())
    read_add2 = float(str_add2.get())

    sum = read_add2*read_add2
    str_sum.set(sum)

def func_div():
    read_add = float(str_add.get())
    read_add2 = float(str_add2.get())

    sum = read_add / read_add2
    str_sum.set(sum)


# create windows
windows = Tk()
windows.title('Easy Calculator')
windows.geometry('360x250+900+100')
windows.resizable(0, 0)


# create label
lbl_sum = Label(windows, text='Calculator by Kamonthip').pack()
lbl_num_1 = Label(windows, text='Number 1').place(x=20, y=30)
lbl_num_2 = Label(windows, text='Number 2').place(x=20, y=60)
lbl_num_total = Label(windows, text='Total Number').place(x=20, y=90)

# textbox
str_add = StringVar()
str_add2 = StringVar()
str_sum = StringVar()
str_div = StringVar()

txt_number1 = Entry(textvariable=str_add).place(x=130, y=30)
txt_number2 = Entry(textvariable=str_add2).place(x=130, y=60)
txt_number_sum = Entry(textvariable=str_sum, state=DISABLED).place(x=130, y=90)

# Button
btn_add = ttk.Button(windows, text='+', command=func_add).place(x=130, y=130)
btn_minus = ttk.Button(windows, text='-', command=func_minus).place(x=130, y=160)
btn_mul = ttk.Button(windows, text='x', command=func_mul).place(x=230, y=130)
btn_div = ttk.Button(windows, text='/', command=func_div).place(x=230, y=160)
btn_clear = ttk.Button(windows, text='Clear', width=17, command=clear_data).place(x=130, y=190)





windows.mainloop()



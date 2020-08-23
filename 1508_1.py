from tkinter import *
from tkinter import messagebox #ข้อความแจ้งเตือน
from tkinter import colorchooser #ตัวเลือกสี
from tkinter import filedialog 
import sys

# function area
def hello():
    print('Hello Kamonthip Phairuen')

def msg_hello(event):
    status = messagebox.askyesno(title='Question', message='ต้องการออกจากระบบใช่มั้ย')
    if status > 0:
        sys.exit()

def choose_color(event):
    my_color = colorchooser.askcolor()
    lbl_c =Label(text=my_color).pack()

def open_file(event):
    my_file = filedialog.askopenfile()
    lbl_file = Label(text=my_file).pack()


# create GUI
windows = Tk()
windows.title('All Widget')
windows.geometry('600x600+900+100')
windows.resizable(0, 0) 

 #Label Area
lbl_name = Label(text='Kamonthip Phairuean', bg="black", fg="red")
lbl_name.pack(side=TOP, padx=5, pady=5)

# button area
btn_hello = Button(text='Hello', command=hello) 
btn_hello.pack(side=TOP, padx=5, pady=5)

btn_msg_hello = Button(text='msg_hello')
btn_msg_hello.bind('<Button-1>', msg_hello)
btn_msg_hello.pack(side=TOP, padx=5, pady=5)

btn_color = Button(text='Choose Color')
btn_color.bind('<Button-1>', choose_color)
btn_color.pack(side=TOP, padx=5, pady=5)

btn_file = Button(text='Choose File')
btn_file.bind('<Button-1>', open_file)
btn_file.pack(side=TOP, padx=5, pady=5)

# Create Menu
menu_file = Menu(windows)
file_menu = Menu(menu_file, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_command(label="Save")
file_menu.add_command(label="Open", command=filedialog.askopenfile)
file_menu.add_command(label="Close",command=sys.exit)
menu_file.add_cascade(label="File", menu=file_menu)
windows.config(menu=menu_file)


edit_menu = Menu(menu_file, tearoff=0)
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Past")
edit_menu.add_command(label="Delete")
menu_file.add_cascade(label="Edit", menu=edit_menu)

# Radio Button
rdo_male = Radiobutton(text='Male', value='male')
rdo_male.pack(side=TOP, padx=5, pady=5)
rdo_female = Radiobutton(text='Female', value='female')
rdo_female.pack(side=TOP, padx=5, pady=5)


# spinbox
spin_box = Spinbox(from_=0, to=10)
spin_box.pack(side=TOP, padx=5, pady=5)

date=['วันจันทร์','วันอังคาร','วันพุธ','วันพฤหัสบดี']
spin_box2 = Spinbox(values=date)
spin_box2.pack(side=TOP, padx=5, pady=5)


# listbox
listbox1 = Listbox()
listbox1.insert(1, "Python")
listbox1.insert(2, "Java")
listbox1.insert(1, "Swift")
listbox1.pack(side=TOP, padx=5, pady=5)


# sidebar
slide1 = Scale(orient=HORIZONTAL, width=20, length=300, from_=0, to=100, tickinterval=10)
slide1.pack(side=TOP, padx=5, pady=5)





windows.mainloop()

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

con = sqlite3.connect('DB_Test.db')
con.cursor()
cur = con.cursor()


def show_data ():
    record = tree.get_children()  # check dataและ clear ตารางก่อน
    for element in record:
        tree.delete(element)

    sql_select = 'SELECT * FROM Tb_Name'
    rows = con.execute(sql_select)
    cpt = 0

    for rows_show in rows:
        tree.insert('','end', text=str(cpt), values=(rows_show[0], rows_show[1],
                    rows_show[2], rows_show[3], rows_show[4]))
        cpt += 1 #ตัวแปรเก็บ rows 
    set_max_id()

def set_max_id():
    sql = 'SELECT MAX(ID) FROM Tb_Name'
    cur.execute(sql)
    rows_max = cur.fetchone()
    set_id = rows_max[0] + 1
    str_id.set(set_id)

def clear_data():
    str_name.set('')
    str_address.set('')
    str_birthday.set('')
    str_tel.set('')
    str_id.set('')
    set_max_id() # clear data และที่มี set_max_id() เพื่อให้ clear ยังคงเก็บการนับ ID ไว้


def select_data(event): #กดข้อลูลในตาราง data ขึ้นมา show ที่ userdata 
    item = tree.selection()
    for i in item:
        str_id.set(tree.item(i, "values")[0])
        str_name.set(tree.item(i, "values")[1])
        str_address.set(tree.item(i, "values")[2])
        str_birthday.set(tree.item(i, "values")[3])
        str_tel.set(tree.item(i, "values")[4])


def insert_data():
    id = str_id.get()
    name = str_name.get()
    address = str_address.get()
    birthday = str_birthday.get()
    tel = str_tel.get()

    if id == '':
        messagebox.showwarning(title='Warning', message='ID is missing. !!!')
    elif name == '':
        messagebox.showwarning(title='Warning', message='Name is missing. !!!')
    elif address == '':
        messagebox.showwarning(title='Warning', message='Address is missing. !!!')
    elif birthday == '':
        messagebox.showwarning(title='Warning', message='Birthday is missing. !!!')
    elif tel == '':
        messagebox.showwarning(title='Warning', message='Tel is missing. !!!')
    else:
        insert = messagebox.askyesno(title='Comfirm insert data', message='Are you want to insert data ?')
        if insert > 0:
            sql_insert = 'INSERT INTO TB_Name VALUES(?,?,?,?,?);'
            data_insert = [id, name, address, birthday, tel]
            con.execute(sql_insert, data_insert)
            con.commit()
            show_data()
            clear_data()


def update_date():
    id = str_id.get()
    name = str_name.get()
    address = str_address.get()
    birthday = str_birthday.get()
    tel = str_tel.get()

    if id == '':
        messagebox.showwarning(title='Warning', message='ID is missing. !!!')
    elif name == '':
        messagebox.showwarning(title='Warning', message='Name is missing. !!!')
    elif address == '':
        messagebox.showwarning(title='Warning', message='Address is missing. !!!')
    elif birthday == '':
        messagebox.showwarning(title='Warning', message='Birthday is missing. !!!')
    elif tel == '':
        messagebox.showwarning(title='Warning', message='Tel is missing. !!!')
    else:
        update = messagebox.askyesno(title='Comfirm update data', message='Are you want to update data ?')
        if update > 0:
            sql_update = 'UPDATE Tb_Name SET Name=?, Address=?, Birthday=?, Tel=? WHERE ID=?;'  # WHERE ID=? หมายถึง id ที่ข้อมูลเราจะแก้
            data_update = [name, address, birthday, tel, id]
            con.execute(sql_update, data_update)
            con.commit()
            show_data()
            clear_data()


def delete_data():
     id = str_id.get()
     if id == '':
        messagebox.showwarning(title='Warning', message='ID is missing. !!!')
     else:
        delete = messagebox.askyesno(title='Comfirm delete data', message='Are you want to delete data ?')
        if delete > 0:
            sql_delete = 'DELETE FROM Tb_Name WHERE ID=?;'  # WHERE ID=? หมายถึง id ที่ข้อมูลเราจะแก้
            data_delete = [id]
            con.execute(sql_delete, data_delete)
            con.commit()
            show_data()
            clear_data()




windows = Tk()
windows.title('User Data')
windows.geometry('700x500+900+100')

str_id =StringVar()
str_name =StringVar()
str_address =StringVar()
str_birthday =StringVar()
str_tel =StringVar()


fm1 = LabelFrame(windows, text='User Data', height=200)
fm1.pack(side=TOP, fill=BOTH, padx=5, pady=5)
lbl_id = Label(fm1, text='ID:')
lbl_id.grid(row=0, column=0, sticky=W, padx=5, pady=5)
text_id = ttk.Entry(fm1, textvariable=str_id, width=40, state=DISABLED)
text_id.grid(row=0, column=1, sticky=W, padx=3, pady=3)


lbl_name = Label(fm1, text='NAME:')
lbl_name.grid(row=1, column=0, sticky=W, padx=3, pady=2)
text_name = ttk.Entry(fm1, textvariable=str_name,width=40)
text_name.grid(row=1, column=1, sticky=W, padx=3, pady=2)


lbl_address = Label(fm1, text='Address:')
lbl_address.grid(row=2, column=0, sticky=W, padx=3, pady=2)
text_address = ttk.Entry(fm1, width=40, textvariable=str_address)
text_address.grid(row=2, column=1, sticky=W, padx=3, pady=2)

lbl_brithday = Label(fm1, text='Brithday:')
lbl_brithday.grid(row=3, column=0, sticky=W, padx=3, pady=2)
text_brithday = ttk.Entry(fm1, textvariable=str_birthday, width=40)
text_brithday.grid(row=3, column=1, sticky=W, padx=3, pady=2)


lbl_tel = Label(fm1, text='Tel:')
lbl_tel.grid(row=4, column=0, sticky=W, padx=3, pady=2)
text_tel = ttk.Entry(fm1, textvariable=str_tel, width=40)
text_tel.grid(row=4, column=1, sticky=W, padx=3, pady=2)




fm2 = LabelFrame(windows, text='Data')
fm2.pack(side=TOP, fill=BOTH, expand=YES, padx=5, pady=5)
tree = ttk.Treeview()
tree['show'] = 'headings'
tree['column'] = ('ID','Name', 'Address', 'Birthday', 'tel')
tree.heading('ID', text='ID')
tree.heading('Name', text='Name')
tree.heading('Address', text='Address')
tree.heading('Birthday', text='Birthday')
tree.heading('tel', text='Tel')
tree.column('ID',width=30)
tree.column('Name',width=150)
tree.column('Address',width=250)
tree.column('Birthday',width=100)
tree.column('tel',width=100)
tree.place(height=250, x=20, y=220)
tree.bind('<ButtonRelease>', select_data)

# Button
btn_insert = ttk.Button(windows, text='Insert', command=insert_data).place(x=480, y=28, width=180)
btn_update = ttk.Button(windows, text='Update', command=update_date).place(x=480, y=58, width=180)
btn_dele = ttk.Button(windows, text='Delete', command=delete_data).place(x=480, y=88, width=180)
btn_clear = ttk.Button(windows, text='Clear', command=clear_data).place(x=480, y=118, width=180)



show_data()
windows.mainloop()

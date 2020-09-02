import sqlite3
from tkinter import *
from tkinter import Tk
from tkinter import ttk
from tkinter import messagebox 

#Tap 1 ข้อมูลสินค้า เพิ่ม, ลบ, แก้ไข ย้ายจากครั้งมาได้

#Tap 2 หน้าทดลองการขายสินค้า, ตัด stock, 


con = sqlite3.connect('DB_Product.db')
con.cursor()
cur = con.cursor()

def show_data ():
    record = tree.get_children()
    for element in record:
        tree.delete(element)

    sql_select = 'SELECT * FROM Tb_Product'
    rows = con.execute(sql_select)
    cpt = 0

    for rows_show in rows:
        tree.insert('','end', text=str(cpt), values=(rows_show[0], rows_show[1],
                    rows_show[2], rows_show[3]))
        cpt += 1
    set_max_id()


def set_max_id():
    sql = 'SELECT MAX(ID) FROM Tb_Product'
    cur.execute(sql)
    rows_max = cur.fetchone()
    set_id = rows_max[0] + 1
    str_id.set(set_id)


def select_data(event):
    item = tree.selection()
    for i in item:
        str_id.set(tree.item(i, "values")[0])
        str_product_name.set(tree.item(i, "values")[1])
        str_product_price.set(tree.item(i, "values")[2])
        str_amount.set(tree.item(i, "values")[3])

def insert_data():
    id = str_id.get()
    product_name = str_product_name.get()
    product_price = str_product_price.get()
  

    if id == '':
        messagebox.showwarning(title='Warning', message='ID is missing. !!!')
    elif product_name == '':
        messagebox.showwarning(title='Warning', message='Product Name is missing. !!!')
    elif product_price == '':
        messagebox.showwarning(title='Warning', message='Product Price is missing. !!!')
    elif amount == '':
        messagebox.showwarning(title='Warning', message='Address is missing. !!!')
    elif product_price.isnumeric() == False: 
        messagebox.showwarning(title='Waring', message='In Put Number')
    elif amount.isnumeric() == False: 
        messagebox.showwarning(title='Waring', message='In Put Number')
    else:
        insert = messagebox.askyesno(title='Conmfirm insert data', message='Are you want to insert data ?')
        if insert > 0:
            sql_insert = 'INSERT INTO TB_Product VALUES(?,?,?,?);'
            data_insert = [id, product_name, product_price, amount]
            con.execute(sql_insert, data_insert)
            con.commit()
            show_data()


def update_date():
    id = str_id.get()
    product_name = str_product_name.get()
    product_price = str_product_price.get()
    amount = str_amount.get()

    if id == '':
        messagebox.showwarning(title='Warning', message='ID is missing. !!!')
    elif product_name == '':
        messagebox.showwarning(title='Warning', message='Name is missing. !!!')
    elif product_price == '':
        messagebox.showwarning(title='Warning', message='Address is missing. !!!')
    elif amount == '':
        messagebox.showwarning(title='Warning', message='Address is missing. !!!')
    elif product_price.isnumeric() == False: 
        messagebox.showwarning(title='Waring', message='In Put Number')
    elif amount.isnumeric() == False: 
        messagebox.showwarning(title='Waring', message='In Put Number')
    else:
        update = messagebox.askyesno(title='Comfirm update data', message='Are you want to update data ?')
        if update > 0:
            sql_update = 'UPDATE Tb_Product SET product_name=?, product_price=?, amount=? WHERE ID=?;'
            data_update = [product_name,product_price,amount, id]
            con.execute(sql_update, data_update)
            con.commit()
            show_data()


def delete_data():
     id = str_id.get()
     if id == '':
        messagebox.showwarning(title='Warning', message='ID is missing. !!!')
     else:
        delete = messagebox.askyesno(title='Comfirm delete data', message='Are you want to delete data ?')
        if delete > 0:
            sql_delete = 'DELETE FROM Tb_Product WHERE ID=?;'
            data_delete = [id]
            con.execute(sql_delete, data_delete)
            con.commit()
            show_data()

def clear_data():
    str_id.set('')
    str_product_name.set('')
    str_product_price.set('')
    str_amount.set('')
    set_max_id()

#windows from area
windows = Tk()
windows.geometry('700x500+700+150')
windows.resizable(0,0)
windows.title('Product Data 1')

#create notebook
notebook = ttk.Notebook(windows, width=660, height=460)
notebook.pack(padx=5, pady=5)

#create frame 
fm_tap1 = Frame(notebook)
fm_tap2 = Frame(notebook)


#add tap
notebook.add(fm_tap1, text='Product Data')
notebook.add(fm_tap2, text='Sale Data')

#tap Product Data
str_id =StringVar()
str_product_name =StringVar()
str_product_price =StringVar()
str_amount =StringVar()

lbl_id = Label(fm_tap1, text='ID:')
lbl_id.grid(row=0, column=0, sticky=W, padx=5, pady=5)
text_id = ttk.Entry(fm_tap1,textvariable=str_id, width=20, state=DISABLED)
text_id.grid(row=0, column=1, sticky=W, padx=3, pady=3)

lbl_name = Label(fm_tap1, text='Product Name:')
lbl_name.grid(row=1, column=0, sticky=W, padx=3, pady=2)
text_name = ttk.Entry(fm_tap1,textvariable=str_product_name, width=40)
text_name.grid(row=1, column=1, sticky=W, padx=3, pady=2)

lbl_price = Label(fm_tap1, text='Product Price:')
lbl_price.grid(row=2, column=0, sticky=W, padx=3, pady=2)
text_price = ttk.Entry(fm_tap1,textvariable=str_product_price, width=40)
text_price.grid(row=2, column=1, sticky=W, padx=3, pady=2)

lbl_amount = Label(fm_tap1, text='Amount:')
lbl_amount.grid(row=3, column=0, sticky=W, padx=3, pady=2)
text_amount = ttk.Entry(fm_tap1,textvariable=str_amount, width=40)
text_amount.grid(row=3, column=1, sticky=W, padx=3, pady=2)


tree = ttk.Treeview(fm_tap1)
tree['show'] = 'headings'
tree['column'] = ('ID','product_name', 'product_price', 'Amount')
tree.heading('ID', text='ID')
tree.heading('product_name', text='Name')
tree.heading('product_price', text='Price')
tree.heading('Amount', text='Amount')
tree.column('ID',width=80)
tree.column('product_name',width=200)
tree.column('product_price',width=150)
tree.column('Amount',width=150)
tree.place(height=250, x=20, y=165)
tree.bind('<ButtonRelease>', select_data)





#tap Sale Data
str_sale_id = StringVar()


lbl_id_tap2 = Label(fm_tap2, text='ID:')
lbl_id_tap2.grid(row=0, column=0, sticky=W, padx=5, pady=5)





#button
photo = PhotoImage(file='add-1-icon.png')
photo1 = PhotoImage(file='Edit-validated-icon.png')
photo2 = PhotoImage(file='delete-icon.png')
photo3 = PhotoImage(file='clear-icon.png')

btn_insert = ttk.Button(windows, text='Insert',command=insert_data, image=photo, compound=LEFT).place(x=40, y=170, width=120)
btn_update = ttk.Button(windows, text='Update',command=update_date, image=photo1, compound=LEFT).place(x=190, y=170, width=120)
btn_dele = ttk.Button(windows, text='Delete',command=delete_data, image=photo2, compound=LEFT).place(x=350, y=170, width=120)
btn_clear = ttk.Button(windows, text='Clear',command=clear_data, image=photo3, compound=LEFT).place(x=500, y=170, width=120)


show_data()
windows.mainloop()
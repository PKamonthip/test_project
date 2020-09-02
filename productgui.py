from tkinter import *
from tkinter import Tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

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
                    rows_show[2]))
        cpt += 1


def select_data(event):
    item = tree.selection()
    for i in item:
        str_id.set(tree.item(i, "values")[0])
        str_product_name.set(tree.item(i, "values")[1])
        str_product_price.set(tree.item(i, "values")[2])



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
    elif product_price.isnumeric() == False: 
        messagebox.showwarning(title='Waring', message='In Put Number')
    else:
        insert = messagebox.askyesno(title='Conmfirm insert data', message='Are you want to insert data ?')
        if insert > 0:
            sql_insert = 'INSERT INTO TB_Product VALUES(?,?,?);'
            data_insert = [id, product_name, product_price]
            con.execute(sql_insert, data_insert)
            con.commit()
            show_data()



def update_date():
    id = str_id.get()
    product_name = str_product_name.get()
    product_price = str_product_price.get()

    if id == '':
        messagebox.showwarning(title='Warning', message='ID is missing. !!!')
    elif product_name == '':
        messagebox.showwarning(title='Warning', message='Name is missing. !!!')
    elif product_price == '':
        messagebox.showwarning(title='Warning', message='Address is missing. !!!')
    elif product_price.isnumeric() == False: 
        messagebox.showwarning(title='Waring', message='In Put Number')
    else:
        update = messagebox.askyesno(title='Comfirm update data', message='Are you want to update data ?')
        if update > 0:
            sql_update = 'UPDATE Tb_Product SET product_name=?, product_price=? WHERE ID=?;'
            data_update = [product_name,product_price, id]
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



windows = Tk()
windows.title('Product Data')
windows.geometry('600x500+800+200')

str_id =StringVar()
str_product_name =StringVar()
str_product_price =StringVar()


fm1 = LabelFrame(windows, text='Proudut Data')
fm1.pack(side=TOP, fill=BOTH, padx=5, pady=10)
lbl_id = Label(fm1, text='ID:')
lbl_id.grid(row=0, column=0, sticky=W, padx=5, pady=5)
text_id = ttk.Entry(fm1,textvariable=str_id, width=20)
text_id.grid(row=0, column=1, sticky=W, padx=3, pady=3)


lbl_name = Label(fm1, text='Product Name:')
lbl_name.grid(row=1, column=0, sticky=W, padx=3, pady=2)
text_name = ttk.Entry(fm1,textvariable=str_product_name, width=40)
text_name.grid(row=1, column=1, sticky=W, padx=3, pady=2)


lbl_price = Label(fm1, text='Product Price:')
lbl_price.grid(row=2, column=0, sticky=W, padx=3, pady=2)
text_price = ttk.Entry(fm1,textvariable=str_product_price, width=40)
text_price.grid(row=2, column=1, sticky=W, padx=3, pady=2)




fm2 = LabelFrame(windows, text='Data',height=300)
fm2.pack(side=TOP, fill=BOTH, expand=YES, padx=5, pady=5)
tree = ttk.Treeview()
tree['show'] = 'headings'
tree['column'] = ('ID','product_name', 'product_price')
tree.heading('ID', text='ID')
tree.heading('product_name', text='Name')
tree.heading('product_price', text='Price')
tree.column('ID',width=80)
tree.column('product_name',width=230)
tree.column('product_price',width=150)
tree.place(height=270, x=20, y=165)
tree.bind('<ButtonRelease>', select_data)






#button
photo = PhotoImage(file='add-1-icon.png')
photo1 = PhotoImage(file='Edit-validated-icon.png')
photo2 = PhotoImage(file='delete-icon.png')

btn_insert = ttk.Button(windows, text='Insert',image=photo, compound=LEFT, command=insert_data).place(x=20, y=450, width=120)
btn_update = ttk.Button(windows, text='Update',image=photo1, compound=LEFT, command=update_date).place(x=190, y=450, width=120)
btn_dele = ttk.Button(windows, text='Delete',image=photo2, compound=LEFT, command=delete_data).place(x=365, y=450, width=120)




show_data()
windows.mainloop()
#OOP = Object Oriented Programming
from tkinter import *
class product:
    def __init__(self,gui):
        self.windows = gui
        self.windows.title('GUI wirh OOP')
        self.windows.geometry('500x600+900+200')
        self.windows.resizable(0, 0)

        #Frame 1 ========
        fm1 = LabelFrame(text='Product')
        fm1.pack(side=TOP, fill=BOTH, expand=YES, padx=10, pady=10)
        self.lbl_product_id = Label(fm1, text='Product_ID')
        self.lbl_product_id.grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.text_product_id = Entry(fm1, width=20)
        self.text_product_id.grid(row=0, column=1, sticky=W, padx=5, pady=5)

        self.lbl_product_name = Label(fm1, text='Product_Name')
        self.lbl_product_name.grid(row=1, column=0, sticky=W, padx=5, pady=5)
        self.text_product_name = Entry(fm1, width=30)
        self.text_product_name.grid(row=1, column=1, sticky=W, padx=5, pady=5)




        fm2 = LabelFrame(self.windows, text='Price',)
        fm2.pack(side=TOP, fill=BOTH, expand=YES, padx=10, pady=10)

    


def update_data():
    
  

    if id == '':
        messagebox.showwarning(title='Warning', message='ID is missing. !!!')
    elif name == '':
        messagebox.showwarning(title='Warning', message='Product Name is missing. !!!')
    elif address == '':
        messagebox.showwarning(title='Warning', message='Product Price is missing. !!!')
    else:
        insert = messagebox.askyesno(title='Comfirm insert data', message='Are you want to insert data ?')
        if insert > 0:
            sql_update = 'INSERT INTO TB_Product VALUES(?,?,?);'
            data_update = [id, product_name, product_price]
            con.execute(sql_insert, data_insert)
            con.commit()
            show_data()
            clear_data()






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
    else:
        update = messagebox.askyesno(title='Comfirm update data', message='Are you want to update data ?')
        if update > 0:
            sql_update = 'UPDATE Tb_Product SET product_namr=?, product_price=?,WHERE ID=?;'
            data_update = [product_price,product_price, id]
            con.execute(sql_update, data_update)
            con.commit()
            show_data()





    

if __name__ == '__main__':
    gui = Tk()
    application = product(gui)
    gui.mainloop()


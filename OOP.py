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

        fm2 = LabelFrame(self.windows, text='Price')
        fm2.pack(side=TOP, fill=BOTH, expand=YES, padx=10, pady=10)
    

if __name__ == '__main__':
    gui = Tk()
    application = product(gui)
    gui.mainloop()


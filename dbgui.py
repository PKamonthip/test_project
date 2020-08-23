from tkinter import *

windows = Tk()
windows.title('User Data')
windows.geometry('700x500+900+100')

fm1 = LabelFrame(windows, text='User Data')
fm1.pack(side=TOP, fill=BOTH, expand=YES, padx=5, pady=5)
lbl_id = Label(fm1, text='ID:')
lbl_id.grid(row=0, column=0, sticky=W, padx=5, pady=5)
text_id = Entry(fm1, width=40)
text_id.grid(row=0, column=1, sticky=W, padx=3, pady=3)


lbl_name = Label(fm1, text='NAME:')
lbl_name.grid(row=1, column=0, sticky=W, padx=3, pady=3)
text_name = Entry(fm1, width=40)
text_name.grid(row=1, column=1, sticky=W, padx=3, pady=3)


lbl_address = Label(fm1, text='Address:')
lbl_address.grid(row=2, column=0, sticky=W, padx=3, pady=3)
text_address = Entry(fm1, width=40)
text_address.grid(row=2, column=1, sticky=W, padx=3, pady=3)

lbl_brithday = Label(fm1, text='Brithday:')
lbl_brithday.grid(row=3, column=0, sticky=W, padx=3, pady=3)
text_brithday = Entry(fm1, width=40)
text_brithday.grid(row=3, column=1, sticky=W, padx=3, pady=3)


lbl_age = Label(fm1, text='AGE:')
lbl_age.grid(row=4, column=0, sticky=W, padx=3, pady=3)
text_age = Entry(fm1, width=40)
text_age.grid(row=4, column=1, sticky=W, padx=3, pady=3)






fm2 = LabelFrame(windows, text='Data')
fm2.pack(side=TOP, fill=BOTH, expand=YES, padx=5, pady=5)



windows.mainloop()

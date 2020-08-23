from tkinter import *
windows = Tk()
windows.title('Teat Label Frame')
windows.geometry('500x300+600+200')
windows.resizable(0, 0)

#frame 1 --------------
fm1 = LabelFrame(windows,tex='ข้อมูลส่วนตัว')
fm1.pack(side=TOP, fill=BOTH, expand=YES, padx=10, pady=10)
lbl_name = Label(fm1, text='ชื่อ - นามสกุล')
lbl_name.grid(row=0, column=0, sticky=W, padx=5, pady=5)
text_name = Entry(fm1, width=30)
text_name.grid(row=0, column=1, sticky=W, padx=5, pady=5)


lbl_addess = Label(fm1, text='ที่อยู่')
lbl_addess.grid(row=1, column=0, sticky=W, padx=5, pady=5)
text_addess = Entry(fm1, width=30)
text_addess.grid(row=1, column=1, sticky=W, padx=5, pady=5)

lbl_education = Label(fm1, text='การศึกษาสูงสุด')
lbl_education.grid(row=2, column=0, sticky=W, padx=5, pady=5)
text_education = Entry(fm1, width=30)
text_education.grid(row=2, column=1, sticky=W, padx=5, pady=5)

lbl_age = Label(fm1, text='อายุ')
lbl_age.grid(row=3, column=0, sticky=W, padx=5, pady=5)
text_age = Entry(fm1, width=15)
text_age.grid(row=3, column=1, sticky=W, padx=5, pady=5)
lbl_age2 = Label(fm1,text='ปี')
lbl_age2.grid(row=3, column=2, sticky=W, padx=2, pady=2)




#frame 2 ---------------
fm2 = LabelFrame(windows, text='ข้อมูลที่ทำงาน')
fm2.pack(side=TOP, fill=BOTH, expand=YES, padx=10, pady=10)

lbl_namework = Label(fm2, text='บริษัท')
lbl_namework.grid(row=0, column=0, sticky=W,padx=5, pady=5)
text_namework = Entry(fm2, width=30)
text_namework.grid(row=0, column=1, sticky=W,padx=5, pady=5)





windows.mainloop()

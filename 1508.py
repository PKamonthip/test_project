#label frame
from tkinter import *
windows = Tk()
windows.title('Test Label Frame')
windows.geometry('500x300+900+200')
windows.resizable(0, 0) #ใช้เมาส์ลากย่อยหรือขยายไม่ได้

#frame 1 --------------
fm1 = LabelFrame(windows,tex='ข้อมูลส่วนตัว')
fm1.pack(side=TOP, fill=BOTH, expand=YES, padx=10, pady=10)
lbl_name = Label(fm1, text='ชื่อ - นามสกุล')
lbl_name.grid(row=0, column=0, sticky=W,padx=5, pady=5)
text_name = Entry(fm1, width=30)
text_name.grid(row=0, column=1, sticky=W,padx=5, pady=5)


lbl_addess = Label(fm1, text='ที่อยู่')
lbl_addess.grid(row=1, column=0, sticky=W,padx=5, pady=5)
text_addess = Entry(fm1, width=30)
text_addess.grid(row=1, column=1, sticky=W,padx=5, pady=5)

lbl_education = Label(fm1, text='การศึกษาสูงสุด')
lbl_education.grid(row=2, column=0, sticky=W,padx=5, pady=5)
text_education = Entry(fm1, width=30)
text_education.grid(row=2, column=1, sticky=W,padx=5, pady=5)

lbl_age = Label(fm1, text='อายุ')
lbl_age.grid(row=3, column=0, sticky=W,padx=5, pady=5)
text_age = Entry(fm1, width=10,
text_age.grid(row=3, column=1, sticky=W,padx=5, pady=5)

#frame 2 ---------------


windows.mainloop()
'''
systax 
while เงื่อนไข :
    คำสั้งต่าง
# check ทำก่อน เงื่อนไข
'''

'''
x = 1
while x <= 10:
    print(x)
    x += 1 # บรรทัดนี้สร้างเงื่อนไงให้หยุด loop 

valid_code = False
while not valid_code: #ถ้าเป็นเท็จวนไปเรื่อยๆ
    code = input('กรุณาใส่รหัสผ่าน: ')
    if code == '1234' :
        valid_code = True  #ถ้า input เข้ามาเป็น '1234' ให้ va เป็น true
print ('รหัสผ่านถูกต้อง')


import random
x = 0
time = 0
# Module random() ค่าจะอยู่ระหว่าง 0 - 1, ถ้าค่าที่ได้น้อยกว่า 0.5 ให้วนไปเรื่อย
while x < 0.5:
    x = random.random()
    time += 1 
print(f'จะต้องสุ่มทั้งหมด {time} ครั้ง เพื่อที่จะได้ค่า x > 0.5')


#สูตรคูรด้วย for_loop 
print('ตารางสูตรคูณ \n ***************') # \n คือการขึ้นบรรทัดใหม่
text = ''
for i in range (1, 6): #loop แนวตั้ง
    for j in range (1,11): # loop แนวนอน
        if j == 1:
            text += '' #ไม่ต้องเว้นช่องว่างเมื่อเริ่มแถวใหม่
        elif (i+j) <= 10:
            text += '  ' #ถ้าเป็นเป็นเลขตัวเดียวให้เว้น 4 ช่อง
        else:
            text += ' ' #ถ้าเป็นเป็นเลขตัว 2 ตัวให้เว้น 2 ช่อง
        text += str(i*j)
    text += '\n'
print (text)

now = datetime.now()
day = date.today() .strftime('%d/%m/%Y')
curtime = datetime.now() .time()
print(now)
print(day)
print(curtime)

now = datetime.now()
day = date.today()
curtime = datetime.now() .time()
print(now)
print(day)
print(curtime)

a = date(2020, 2, 20)
print(a)
t = time(22, 20, 55)
print(t)


### datetime การจัดรูปแบบ
from datetime import datetime
from datetime import date
from datetime import time

thai_date = ['อาทิตย์','จันทร์','อังคาร','พุธ','พฤหัสบดี','ศุกร์','เสาร์']
thai_month =['มกราคม','กุมภาพันธ์','มีนาคม','เมษายน','พฤษภาคม','มิถุนายน',
             'กรกฏาคม','สิงหาคม','กันยายน','ตุลาคม','พฤศจิกายน','ธันวาคม']

dt = datetime.now()
wd = 0 if dt.weekday() == 6 else dt.weekday() + 1
day = dt.day
month = dt.month
year = dt.year + 543
h = dt.hour
m = dt.minute
s = dt.second

print(dt)
print(f'วันเวลาแบบสั้น :{day}/{month}/{year}')
print(f'วันเวลาแบบปกติ :{day}/{thai_month[month - 1]}/{year}')

dmy = f'{thai_date[wd]} ที่ {day} {thai_month[month - 1]} {year}'
time = f'{h}:{m}:{s}'
print(f'วันเวลาแบบเต็ม :{dmy} {time}')


day1 = date(2020, 1, 1)
day2 = date(2020, 7, 28)
delta = day2 - day1
month = delta//30 
#print(month)
#print(f'ห่าง {delta} วันและห่าง {month} เดือน')

day = dalta.day #อ่านจำนวนวันออกมาจาก dalta
num_month = day // 30 #หาจำนวนเดือน
num_day = day % 30 #
 
print(f'วันที่   ห่างกัน {num_month เดือน {num_day} วัน')

###
#วันเกิดเข้ามาผ่าน input แล้วเขียนโปรแกรมคำนวนอายุจากวันเกิด
brithday = date (1990, 2, 1)
today = date.today()
delta2 = today - brithday
day = delta2.days
age = day2 // 365
month = day2 % 30
print((f'อายุ {age} ปี {month} เดือน {day3} วัน'))

#print (brithday)





from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta # หาระยะห่างวันเวลา


thai_date = ['อาทิตย์','จันทร์','อังคาร','พุธ','พฤหัสบดี','ศุกร์','เสาร์']
thai_month =['มกราคม','กุมภาพันธ์','มีนาคม','เมษายน','พฤษภาคม','มิถุนายน',
             'กรกฏาคม','สิงหาคม','กันยายน','ตุลาคม','พฤศจิกายน','ธันวาคม']

dt = date.today()
print(f'วันนี้ตรงกับ: {dt.day} / {dt.month} / {dt.year + 543} ')
app_day = int(input('จำนวนวันที่จะเข้าตรวจครั้งไป : '))
delta = timedelta(days=app_day)
next_dt = dt.__add__(delta)
x = 0
if next_dt.weekday() == 5: # คือเงื่อนไขที่ถ้าไปตกวันหยุดเสาร์  แล้วเลื่อน
    x = 2
elif next_dt.weekday() == 6: # คือเงื่อนไขที่ถ้าไปตกวันหยุดอาทิตย์  แล้วเลือน
    x = 1

delta = timedelta(days=x)
next_dt2 = next_dt.__add__(delta)
d = next_dt2.day
m = next_dt2.month
y = next_dt2.year + 543
w = 0 if next_dt2.weekday() == 6 else next_dt2.weekday() + 1

print(f'นัดคราวต่อไป : วัน {thai_date[w]} ที่ {d} {thai_month[m-1]} {y}')


'''

#การจัดรูปแบบเวลาอย่างง่ายโดยใช้ strftime
from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta # หาระยะห่างวันเวลา

dt = date(2020, 7, 29) 
day = dt.strftime('%d-%B-%Y')
print(day)











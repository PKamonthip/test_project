
def demo1 ():
    i = 1 
    while i <= 10:
        print(i)
        i += 1
    print ('bey')
#demo1()

def demo_for():
    for i in range (1,11):
        print(i)
    print ('bye')
#demo_for()

def sum_input():
    n = int(input('enter: '))
    total = 0
    while n != 0:
        total += n
        n = int(input('enter: '))
    print('total = ', total)

#sum_input()
def sum_input_repeat_unit():
    total = 0
    while True:
        n = int(input('enter: '))
        if n != 0:
            total += n
        else:
            break
    print ('total = ',total)
sum_input_repeat_unit ()

'''''''''''''''


print('ตารางสูตรคูณ \n ***************') # \n คือการขึ้นบรรทัดใหม่
text = ''
for i in range (1, 6): #loop แนวตั้ง
    for j in range (1,11): # loop แนวนอน
        if j == 1:
            text += ' ' #ไม่ต้องเว้นช่องว่างเมื่อเริ่มแถวใหม่
        elif (i+j) <= 10:
            text += ' ' #ถ้าเป็นเป็นเลขตัวเดียวให้เว้น 4 ช่อง
        else:
            text += ' ' #ถ้าเป็นเป็นเลขตัว 2 ตัวให้เว้น 2 ช่อง
        text += str(i*j)
    text += '\n'
print (text)


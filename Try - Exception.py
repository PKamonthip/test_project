'''

try:
    ip = input('กรุณาใส่เลขจำนวนเต็ม: ')
    x = int(ip)
except:
    print('Error ข้อมูลที่ใส่ไม่ใช่จำนวนเต็ม')


try:
    ip = input('กรุณาใส่เลขจำนวนเต็ม: ')
    x = int(ip)
except:
    print('Error ข้อมูลที่ใส่ไม่ใช่จำนวนเต็ม')

print('After try-except')



try:
    f = open('somma.txt', mode='r', encoding='utf-8')
    print(f.read())
    f.seek(0)

except IOError as err:
    print(err)
else:
    f.close()

'''

try:
    with open('somma.txt', mode='w+', encoding='utf-8') as file:
        file.write('รายชื่อสัตว์ \n')
        file.write('เข้ม 1 \n')
        file.write('CAT \n')
        file.write('DOG \n')
#w+ คือเขียนใหม่โดยลบของเก่าแล้วเขียนใหม่

except IOError as err:
    print(err)

else:
    file.close()

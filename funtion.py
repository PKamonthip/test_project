''''
Function แบบไม่ส่งค่ากลับ syntax #คือโปรมแกรมหลัก และโปรแรมย่อย

def ชื่อ function(paramiter):
    คำสั่งต่างๆ 

Function แบบส่งค่ากลับ syntax 
def ชื่อ function(patamiter):
    คำสั่งต่างๆ 
    return ข้อมูลที่ส่งกลับ

def hell0():
    print('Hello Kamonthip')
hell0() # เรียกใช้ function
'''''   

'''
def select_menu():
    print('กรุณาเลือกเมนู')
    menu =input('1: ถอนเงิน, 2: ถามยอด, 3: โอนเงิน, 0: ยกเลิก >> ')
    p = print(mune)
    return p

select_menu()
'''
'''
import random
def rand_num(length):
    result = ''
    for n in range (0, length):
        r = random.randrange(0, 9)
        result += str(r)
    return result 

print(
    'รางวัลที่ 1:', rand_num(6), '\n'
    'รางวัลเลขหน้า 3 ตัว :', rand_num(3), ' ', rand_num(3), '\n'
    'รางวัลเลขท้าย 3 ตัว :', rand_num(3), ' ', rand_num(3), '\n'
    'รางวัลเลขหน้า 2 ตัว :', rand_num(2), '\n'
    )
rand_num()
'''


'''
def random_a_to_z():
    a = ord('a')
    z = ord('z')
    r = random.randint(a, z)
    return chr(r)

print(random_a_to_z()+ random_a_to_z ()+ random_a_to_z()+random_a_to_z())
result = random_a_to_z() + random_a_to_z() + random_a_to_z()+random_a_to_z()
print(result)


def random_3_num():
    a = random.randint(1, 11)
    z = random.randint(1, 11)
    r = random.randint(1, 11)
    c = [a, z, r]
    return c
print(random_3_num())

'''






import random

def random_lottery(a):
    re = ''
    for b in range (0, a):
        y = random.randrange (0, 9)
        re += str (y) 
    return re


    
print('รางวัลที่ 1 : ', random_lottery(6), '\n'
    'รางวัลเลขหน้า 3 ตัว :', random_lottery(3), ' ',random_lottery(3), '\n'
    'รางวัลเลขท้าย 3 ตัว :', random_lottery(3), ' ',random_lottery(3), '\n'
    'รางวัลเลขหน้า 2 ตัว :', random_lottery(2), '\n')


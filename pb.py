import random
balance = random.randint(10000, 50000)
menu = 1
amount = 0
def select_menu():
    global menu 
    print('\n กรุณาเลือกเมนู')
    menu = input('1: ฝาก, 2: ถอน, 3: ถามยอด, 0: ยกเลิก >>>')
    if not menu.isdigit() or int(menu) not in range (1, 4):
        exit(0)
    else:
        menu = int(menu)

    if menu in range(1, 3):
        get_amount()
    elif menu == 3:
        show_balance()

def get_amount():
    global amount
    a = input('จำนวนเงิน >> ')
    if not a.isdigit():
        print('ต้องระบุเป็นตัวเลขจำนวนเต็ม')
        get_amount()
    else:
        amount = int(a)
        if menu == 1:
            desposit()
        elif menu == 2:
            withdraw()

def desposit():
    global balance
    balance += amount
    show_balance()

def withdraw():
    global balance
    if amount <= balance:
        balance -= amount 
        show_balance()
    else:
        print('ยอดเงินไม่เพียงพอ')

def show_balance():
    print('ยอดคงเหลือ : ', format(balance, ','))
    select_menu()

show_balance()
select_menu()















total = 5000
print ('กรุณาเลือกรายการ')
print ('1.เช็คยอดเงิน','\n' '2.ถอน','\n' '3.โอน','\n' '4.ยกเลิก','\n')

option = int(input('รายการที่เลือก: '))
while (option !=0) and (option > 4):
    print('กรุณาเลือกรายการใหม่')
    option = int(input('รายการที่เลือก: '))

if option == 1:
    print(f'จำนวนเงินในบัญชี {total} บาท')

if option == 2:
    withdraw = int(input('กรุณาใส่จำนวนเงิน '))
    if withdraw <= total:
        total2 = (total - withdraw)
        print(f'ยอดเงินคงเหลือ {total2} บาท')
    elif withdraw > total:
        print('ไม่สามารถทำรายการได้')

if option == 3:
    transfer = int(input('กรุณาใส่จำนวนเงิน '))
    if transfer <=total:
        total3 = (total - transfer)
        print(f'ยอดเงินคงเหลือ {total3} บาท')
    elif transfer > total:
        print('ไม่สามารถทำรายการได้')

if option == 4:
    print('ยกเลิกทำรายการ')




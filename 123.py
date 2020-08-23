# from datetime import datetime
from datetime import datetime
print('--ถ้าต้องการยกเลิก กด <enter> โดยไม่ต้องใสข้อมูล')
try: 
    with open('somma.txt', mode='a+', encoding='utf-8') as log_file:
        while True:
            data = input('สิ่งที่เกิดขึ้นในขณะนี้ >> ')
            if data == '':
                break

            dt = datetime.now().replace(microsecond=0)
            log_file.write(str(dt) + ' -- '+ data + '\n')


except IOError as err:
    print(err)

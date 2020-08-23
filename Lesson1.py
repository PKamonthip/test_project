#print('Hello")
print('Som')


#Python Lan
# @ $ 12 ไม่สามารถไปตั้งตัวแปรได้
x = 10
y = 20
x = 30
a = 'Hello'
b = 'Kamonthip'
print (a+b)


# + - * / == >= <= Operation in Python 

input_sarary = int(input('เงินเดือนของคุณ: '))
if input_sarary < 20000:
    print ('คุณไม่สามารถซื้อรถได้')
else:
    print ('คุณสามารถซื้อรถได้')
    car_price = int(input('ราคารถ : '))
    pay_price = int(input('ราคาที่จะต้องผ่อน : '))
    print(f'ราคารถที่ซื้อ {car_price} ราคารถที่จะต้องผ่อน {pay_price}')
    
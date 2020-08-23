'''
Num_keyboardA = int(input('Number: '))
Num_keyboardB = int(input('Number: '))
#Even = int(input('เป็นเลขคู่'))
#Odd = int(input('เป็นเลขคี่'))

if Num_keyboardA % 2 == 0 :
    print (f'จำนวนที่ 1 : {Num_keyboardA}')
    print (f'{Num_keyboardA} : เป็นเลขคู่')
    #print (f'{Num_keyboardA % 2 == 0 :} )
elif Num_keyboardA % 2 != 0:
    print(f'จำนวนที่ 1 : {Num_keyboardA}')
    print(f'{Num_keyboardA } : เป็นเลขคี่')
if Num_keyboardB % 2 == 0 :
    print (f'จำนวนที่ 2 : {Num_keyboardB}')
    print (f'{Num_keyboardB} : เป็นเลขคู่')
elif Num_keyboardB % 2 != 0:
    print(f'จำนวนที่ 2 : {Num_keyboardB}')
    print(f'{Num_keyboardB } : เป็นเลขคี่')

'''





x = int(input(': '))
y = int(input(': '))
z = int(input(': '))

if x>y: 
    if x>z:
        print (f'{x} is max')
    else:
        print (f'{z} is max')
else:
    if y>z:
        print(f'{y} is max')
    else:
        print(f'{z} is max')




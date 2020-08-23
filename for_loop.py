#for check เงื่อนไงก่อน ค่อยทำ
'''
sum = 0
for i in range (1,101):
    num = i
    sum += num
print(sum) 


x = 'apple'
for data in x:
    print (data)


fruit = ['apple', 'mango', 'orang', 'grape']
color = ['red', 'green', 'blue', 'white']

for x in fruit:
    for y in color:
        print(x, y)
   # print (data)
    #if data == 'orang':
        #break

'''


sum = 0
for i in range (1,101):
    if (i %2 == 0) and (i %4 == 0) and (i %5 == 0):
        sum += 1
print (f'จำนวนที่ 2, 4 และ 5 หารลงตัว {sum} จำนวน')



'''
def random_num():
    for i in range (1, 100)
    c = random.randint(i)
    return c

print('num' {random_num})
''''
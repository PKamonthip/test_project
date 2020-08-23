import sqlite3
con = sqlite3.connect('DB_Test.db')
con.cursor()
cur = con.cursor()

sql = 'SELECT * FROM Tb_Name'
cur.execute(sql) #ประมวล DB 
rows = cur.fetchall()
print(rows)

for column in rows:
    print('ID : ', column[0])
    print('Name : ', column[1])
    print('Addres : ', column[2])
    print('Birthday : ', column[3])
    print('tel : ', column[4])
    print('----------------------------')



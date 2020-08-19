import mysql.connector
import csv

mydb = mysql.connector.connect(
    host='localhost',
    username='root',
    password='admin',
    database='metadata'
)
print("database connected successfully")
mycurser = mydb.cursor()
file1 = csv.reader(open('test.csv'))
sql = 'INSERT INTO user(name,email,password,age) VALUES(%s,%s,%s,%s)'
for row in file1:
    mycurser.execute(sql, row)
    print(row)
mydb.commit()
mycurser.close()

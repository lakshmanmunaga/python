import mysql.connector
import csv
# create database
mydb = mysql.connector.connect(
    host='localhost',
    username='root',
    password='admin',
    database='metadata'
)
print("database connected successfully")

mycurser = mydb.cursor()
# read file using csv 
file1 = csv.reader(open('test.csv'))
# insert data into sql
sql = 'INSERT INTO user(name,email,password,age) VALUES(%s,%s,%s,%s)'
for row in file1:
    mycurser.execute(sql, row)
    print(row)
mydb.commit()
#close the curser
mycurser.close()
#close the database
mydb.close()

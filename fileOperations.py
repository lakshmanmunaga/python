import pandas as pd
import mysql.connector

# import csv file

file1 = pd.read_csv('C:/Users/Admin/Desktop/pepples.csv')

# file load into dataframe

data = pd.DataFrame(file1, columns=['name', 'country', 'age'])
print(data)

# connect to server
mydb = mysql.connector.connect(
    host='localhost',
    username='root',
    password='admin',
    database='metadata'
)
mycurser = mydb.cursor()

# create table
mycurser.execute("create table people1(name varchar(25),country varchar(25),age int)")
# insert df into table
for row in data.itertuples():
    mycurser.execute(
        row.name, row.country, row.age)
    mydb.commit()


import mysql.connector

conn = mysql.connector.connect(host='192.168.33.10',user='root', password='root', database='tp6')

cursor = conn.cursor()

cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')

cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'lzc'])

conn.commit()

cursor.close()

cursor = conn.cursor()

cursor.execute('select * from user where id = %s', ('1',))

values = cursor.fetchall()

print(values)

cursor.close()

conn.close()

import sqlite3

conn = sqlite3.connect('test.db')# 一个数据库连接称为connection

cursor = conn.cursor() # 连接到数据库后，需要打开游标，称之为Cursor

#cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')

#cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')

#cursor.rowcount
#conn.commit()
#cursor.close()
#conn.close()

# 查询
cursor.execute('select * from user where id=?', ('1',))

values = cursor.fetchall()
print(values)

cursor.close()
conn.close()
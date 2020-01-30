#Python内置了SQLite3，可以直接使用import导入SQLite3模块
import sqlite3
'''
#连接到数据库文件'mrsoft.db'没有文件会自动创建
conn = sqlite3.connect('mrsoft.db')
#创建一个curosr(游标)
cursor = conn.cursor()
#SQL语句
cursor.execute('CREATE TABLE user (id int(10) primary key, name varchar (20)')
#关闭游标
cursor.close()
conn.close()
#本段代码仅能执行一次，若重复执行则因为user表已经存在而报错



'''

#操控SQLite
#插入数据
conn = sqlite3.connect('mrsoft.db')
cursor = conn.cursor()
cursor.execute('INSERT INTO user (id, name ) values ("1", "MRSOFT") ')
cursor.execute('INSERT INTO user (id, name) values  ("2", "Andy")')

cursor.execute('SELECT * FROM user')
#查询一条数据
result = cursor.fetchone()
#查询多条数据
result1 = cursor.fetchmany(2)
print(result1)
#获取所有记录
result3 = cursor.fetchall()
print(result3)









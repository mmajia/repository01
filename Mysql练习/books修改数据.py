from a创建连接数据库 import db,cursor

cursor.execute("update books set price = {} where id = {}".format(38,1))
cursor.execute("select * from books")
result1 = cursor.fetchall()
print(result1)

cursor.close()
db.close()
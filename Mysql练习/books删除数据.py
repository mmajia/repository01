from a创建连接数据库 import db,cursor
cursor.execute("delete from books where id = {}".format(2))
result = cursor.fetchall()
cursor.close()
db.connect()
db.close()
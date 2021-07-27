from a创建连接数据库 import db,cursor
"""
cursor.execute("select * from books")#查询books表记录
#result1 = cursor.fetchone()#返回的是一个元组，表里的第一条记录
#result1 = cursor.fetchmany(2)#返回的是一个元组,表里的几条记录，括号里不给值默认是1
#result1 = cursor.fetchall()#返回的是一个元组，表里的所有记录
print(result1)
cursor.close()
db.close()
"""
"""
# n = 70
# cursor.execute(f"SELECT * FROM books where price > {n}")

cursor.execute("SELECT * FROM books where price > {}".format(70))
result2 = cursor.fetchall()
print(result2)
cursor.close()
db.close()
"""

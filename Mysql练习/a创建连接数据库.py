import pymysql

db = pymysql.connect(host="localhost",user="root",password="123456",database="abc")
cursor = db.cursor()

#from a创建连接数据库 import cursor,db  要用的时候可以这样直接导入不需要继续输入了，方便